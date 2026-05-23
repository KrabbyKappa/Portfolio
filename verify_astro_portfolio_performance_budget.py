#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'

# GitHub Pages documented ceilings as of the 2026-05-21 check:
# published site <= 1 GB; soft bandwidth limit 100 GB/month. This verifier keeps the
# portfolio far below those limits so the free GitHub Pages setup remains viable.
DIST_SIZE_WARN = 200 * 1024 * 1024
DIST_SIZE_HARD = 900 * 1024 * 1024
PROJECT_PREVIEW_VIDEO_HARD = 30 * 1024 * 1024

PAGE_FILES = {
    'home': DIST / 'index.html',
    'projects': DIST / 'projects.html',
    'website-development': DIST / 'website-development/index.html',
}

VIDEO_BUDGETS = {
    'media/project-previews/italian-national-day-2025-preview-720.mp4': (1_000_000, 4_500_000),
    'media/project-previews/perche-ci-siamo-noi-110-133-preview-720.mp4': (1_000_000, 3_500_000),
    'media/project-previews/italian-national-day-2025-loop-1080.mp4': (4_000_000, 12_000_000),
    'media/project-previews/italian-national-day-2024-loop-1080.mp4': (4_000_000, 12_000_000),
    'media/project-previews/perche-ci-siamo-noi-110-133-loop-1080.mp4': (4_000_000, 8_000_000),
}

HOME_ONLY = {
    'media/project-previews/italian-national-day-2025-preview-720.mp4',
    'media/project-previews/perche-ci-siamo-noi-110-133-preview-720.mp4',
}
PROJECTS_ONLY = {
    'media/project-previews/italian-national-day-2025-loop-1080.mp4',
    'media/project-previews/italian-national-day-2024-loop-1080.mp4',
    'media/project-previews/perche-ci-siamo-noi-110-133-loop-1080.mp4',
}


def fail(failures: list[str], message: str) -> None:
    failures.append(message)


def file_size(path: Path) -> int:
    return path.stat().st_size if path.exists() else 0


def tree_size(path: Path) -> int:
    return sum(p.stat().st_size for p in path.rglob('*') if p.is_file())


def rel_assets(html: str, attr: str) -> list[str]:
    return re.findall(rf'\b{attr}=["\']([^"\']+)["\']', html)


def check_html_routes(failures: list[str]) -> None:
    pages = {}
    for name, path in PAGE_FILES.items():
        if not path.exists():
            fail(failures, f'missing built page: {path.relative_to(ROOT)}')
            continue
        pages[name] = path.read_text(encoding='utf-8', errors='ignore')

    home = pages.get('home', '')
    projects = pages.get('projects', '')
    showcase = pages.get('website-development', '')

    if '/website-development/styles.css' in home:
        fail(failures, 'home page loads website-development stylesheet; routes should remain separate')
    if re.search(r'<link\b[^>]+href=["\']/styles\.css["\']', showcase):
        fail(failures, 'website-development page loads portfolio stylesheet; routes should remain separate')
    if 'media/project-previews/' in showcase:
        fail(failures, 'website-development page carries project preview video assets')

    for forbidden_embed in ['youtube.com/embed/', 'youtube-nocookie.com/embed/', 'https://www.youtube.com/iframe_api']:
        for page_name, html in pages.items():
            if forbidden_embed in html:
                fail(failures, f'{page_name}: external YouTube embed/API leaked into the built page')

    for token in PROJECTS_ONLY:
        if token in home:
            fail(failures, f'home page leaked projects-only 1080p video: {token}')
    for token in HOME_ONLY:
        if token in projects:
            fail(failures, f'projects page leaked home-only 720p video: {token}')

    for page_name, html in pages.items():
        if re.search(r'<link\b[^>]+rel=["\'](?:preload|prefetch)["\'][^>]+(?:\.mp4|website-development/demos)', html, re.I):
            fail(failures, f'{page_name}: preloads/prefetches heavy video or demo-route assets')
        if re.search(r'<video\b[^>]*\bautoplay\b', html, re.I):
            fail(failures, f'{page_name}: video has autoplay attribute instead of visibility-gated playback')
        if 'IntersectionObserver' not in html and page_name in {'home', 'projects'}:
            fail(failures, f'{page_name}: missing IntersectionObserver video gate')
        if 'prefers-reduced-motion: reduce' not in html and page_name in {'home', 'projects'}:
            fail(failures, f'{page_name}: missing reduced-motion video guard')

    # The home can show a small screenshot carousel for the showcase, but it should not
    # embed per-demo HTML/CSS bundles or hidden demo pages before the user opens them.
    for demo_token in [
        '/website-development/demos/basic/mosaic-content-studio/styles.css',
        '/website-development/demos/basic/verde-lunch-club/styles.css',
        '/website-development/demos/basic/harbor-legal-translation/styles.css',
        '/website-development/demos/micro/city-lab-pop-up/styles.css',
    ]:
        if demo_token in home:
            fail(failures, f'home page preloads demo CSS bundle: {demo_token}')


def check_asset_budgets(failures: list[str]) -> dict[str, int]:
    sizes: dict[str, int] = {}
    for rel, (min_size, max_size) in VIDEO_BUDGETS.items():
        path = DIST / rel
        if not path.exists():
            fail(failures, f'missing video asset: {rel}')
            continue
        size = file_size(path)
        sizes[rel] = size
        if size < min_size:
            fail(failures, f'{rel}: {size} bytes below quality floor {min_size}')
        if size > max_size:
            fail(failures, f'{rel}: {size} bytes exceeds budget {max_size}')

    preview_dir = DIST / 'media/project-previews'
    total_preview_video = sum(p.stat().st_size for p in preview_dir.glob('*.mp4')) if preview_dir.exists() else 0
    sizes['total_project_preview_mp4'] = total_preview_video
    if total_preview_video > PROJECT_PREVIEW_VIDEO_HARD:
        fail(failures, f'project preview videos total {total_preview_video} bytes exceeds budget {PROJECT_PREVIEW_VIDEO_HARD}')

    dist_total = tree_size(DIST) if DIST.exists() else 0
    sizes['dist_total'] = dist_total
    if dist_total > DIST_SIZE_HARD:
        fail(failures, f'dist total {dist_total} bytes approaches/exceeds GitHub Pages published-site ceiling')
    if dist_total > DIST_SIZE_WARN:
        fail(failures, f'dist total {dist_total} bytes exceeds conservative portfolio warning budget {DIST_SIZE_WARN}')
    return sizes


def main() -> int:
    failures: list[str] = []
    if not DIST.exists():
        fail(failures, 'dist missing; run npm run build first')
    check_html_routes(failures)
    sizes = check_asset_budgets(failures)

    if failures:
        print('VERDICT: FAIL — Astro Portfolio performance budget found issues')
        for item in failures:
            print('-', item)
        return 1

    print('VERDICT: PASS — Astro Portfolio performance budget keeps routes isolated and GitHub Pages/free-hosting payloads bounded')
    for key, value in sizes.items():
        print(f'{key}: {value} bytes')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
