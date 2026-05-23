#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from html import unescape
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
CHROME_CANDIDATES = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
]

SHOWCASE_BACK_TARGET = '../projects.html#video1'


@dataclass(frozen=True)
class ExpectedVideo:
    section_id: str
    title: str
    youtube_id: str
    href: str


EXPECTED_VIDEOS = [
    ExpectedVideo('festa2025', 'Italian National Day 2025', 'hz1xPkvdhcI', 'https://www.youtube.com/watch?v=hz1xPkvdhcI'),
    ExpectedVideo('festa2024', 'Italian National Day 2024', 'T7MQqKLdZvc', 'https://www.youtube.com/watch?v=T7MQqKLdZvc'),
    ExpectedVideo('video1', 'Perché ci siamo noi', 'yUjjPUTrvt0', 'https://www.youtube.com/watch?v=yUjjPUTrvt0&t=110s'),
]

ATTR_RE = re.compile(r'''([:\w-]+)=(['"])(.*?)\2''', re.S)


def fail(message: str) -> int:
    print(f'VERDICT: FAIL -- {message}')
    return 1


def read_dist(rel: str) -> str:
    path = DIST / rel
    if not path.exists():
        raise FileNotFoundError(f'missing {path}; run npm run build first')
    return path.read_text(encoding='utf-8', errors='ignore')


def attrs(opening_tag: str) -> dict[str, str]:
    return {name: unescape(value) for name, _, value in ATTR_RE.findall(opening_tag)}


def section_block(html: str, section_id: str) -> str:
    match = re.search(r'<section\s+id="' + re.escape(section_id) + r'"[\s\S]*?</section>', html)
    if not match:
        raise AssertionError(f'missing section #{section_id}')
    return match.group(0)


def first_anchor_with_video_id(block: str, youtube_id: str) -> tuple[str, dict[str, str]]:
    pattern = re.compile(
        r'<a\b(?=[^>]*\bproject-video-link\b)(?=[^>]*\bdata-video-id="' + re.escape(youtube_id) + r'")[^>]*>',
        re.S,
    )
    match = pattern.search(block)
    if not match:
        raise AssertionError(f'missing project-video-link anchor for video id {youtube_id}')
    opening = match.group(0)
    return opening, attrs(opening)


def structural_check() -> None:
    projects = read_dist('projects.html')
    showcase = read_dist('website-development/index.html')

    if showcase.count(f'href="{SHOWCASE_BACK_TARGET}"') != 1:
        raise AssertionError(f'expected 1 Website Development return link to {SHOWCASE_BACK_TARGET}')
    if 'href="../projects.html#other-projects"' in showcase:
        raise AssertionError('Website Development page still links back to #other-projects')
    if 'Back to portfolio projects' in showcase:
        raise AssertionError('Website Development page still renders the purged scope-boundary back-link copy')

    total_video_links = len(re.findall(r'<a\b[^>]*\bproject-video-link\b', projects))
    if total_video_links != len(EXPECTED_VIDEOS):
        raise AssertionError(f'project video-link anchor count {total_video_links}, expected {len(EXPECTED_VIDEOS)}')
    if re.search(r'<div\b[^>]*\bproject-video-loop\b[^>]*\bdata-video-loop-card\b', projects):
        raise AssertionError('at least one project video loop is still a div instead of a clickable anchor')

    for expected in EXPECTED_VIDEOS:
        block = section_block(projects, expected.section_id)
        opening, attr = first_anchor_with_video_id(block, expected.youtube_id)
        if attr.get('href') != expected.href:
            raise AssertionError(f'{expected.title} href mismatch: expected {expected.href}, got {attr.get("href")}')
        if attr.get('target') != '_blank':
            raise AssertionError(f'{expected.title} must open in a new tab with target="_blank"')
        rel_tokens = set(attr.get('rel', '').split())
        if not {'noopener', 'noreferrer'}.issubset(rel_tokens):
            raise AssertionError(f'{expected.title} rel must include noopener noreferrer')
        if 'aria-label' not in attr or 'YouTube' not in attr['aria-label']:
            raise AssertionError(f'{expected.title} anchor needs a YouTube aria-label')
        if 'project-video-frame' not in block or 'project-video-poster' not in block:
            raise AssertionError(f'{expected.title} missing local video/poster preview inside anchor')
        if opening.count('<a') != 1:
            raise AssertionError(f'{expected.title} malformed opening anchor')

    css = read_dist('styles.css')
    for token in ['.project-video-link', 'cursor: pointer', 'Open on YouTube', 'pointer-events: none']:
        if token not in css:
            raise AssertionError(f'project video-link CSS missing token: {token}')


def chrome_path() -> str | None:
    for candidate in CHROME_CANDIDATES:
        if Path(candidate).exists():
            return candidate
    return None


def server_ready(base_url: str) -> None:
    with urlopen(base_url.rstrip('/') + '/projects.html', timeout=5) as resp:
        if resp.status != 200:
            raise RuntimeError(f'HTTP {resp.status} from /projects.html')


def browser_click_check(base_url: str) -> None:
    from playwright.sync_api import sync_playwright

    base = base_url.rstrip('/') + '/'
    server_ready(base)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path=chrome_path())
        try:
            context = browser.new_context(viewport={'width': 1280, 'height': 900}, device_scale_factor=1)
            context.route('https://www.youtube.com/**', lambda route: route.fulfill(status=200, content_type='text/html', body='<title>YouTube stub</title>'))
            page = context.new_page()
            try:
                response = page.goto(base + 'website-development/', wait_until='load', timeout=30000)
                if not response or response.status != 200:
                    raise AssertionError(f'website-development load failed: {response.status if response else "no response"}')
                page.locator('a.identity').click(timeout=10000)
                page.wait_for_url(base + 'projects.html#video1', timeout=10000)

                response = page.goto(base + 'website-development/', wait_until='load', timeout=30000)
                if not response or response.status != 200:
                    raise AssertionError(f'website-development reload failed: {response.status if response else "no response"}')
                if page.locator('a.text-link[href="../projects.html#video1"]').count() != 0:
                    raise AssertionError('purged scope-boundary text-link still exists on website-development page')

                response = page.goto(base + 'projects.html', wait_until='load', timeout=30000)
                if not response or response.status != 200:
                    raise AssertionError(f'projects load failed: {response.status if response else "no response"}')
                for expected in EXPECTED_VIDEOS:
                    link = page.locator(f'#{expected.section_id} a.project-video-link').first
                    if link.count() != 1:
                        raise AssertionError(f'could not locate video link for {expected.title}')
                    link.scroll_into_view_if_needed(timeout=10000)
                    with page.expect_popup(timeout=10000) as popup_info:
                        link.click(timeout=10000)
                    popup = popup_info.value
                    popup.wait_for_load_state('domcontentloaded', timeout=10000)
                    if popup.url != expected.href:
                        raise AssertionError(f'{expected.title} popup URL mismatch: expected {expected.href}, got {popup.url}')
                    popup.close()
            finally:
                context.close()
        finally:
            browser.close()


def main() -> int:
    parser = argparse.ArgumentParser(description='Verify Astro Portfolio Projects page video click-through links')
    parser.add_argument('--base-url', help='Optional local server rooted at Astro Portfolio/dist for browser click verification')
    args = parser.parse_args()
    try:
        structural_check()
        if args.base_url:
            browser_click_check(args.base_url)
    except Exception as exc:
        return fail(str(exc))
    mode = 'structural + browser click' if args.base_url else 'structural'
    print(f'VERDICT: PASS -- {mode} check confirmed Website Development identity link lands on projects.html#video1, the purged scope-boundary back link is absent, and all 3 project videos open YouTube in new tabs')
    return 0


if __name__ == '__main__':
    sys.exit(main())
