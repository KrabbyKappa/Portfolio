#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC_PAGES = [ROOT / 'src/pages/index.astro', ROOT / 'src/pages/projects.astro']
DIST_PAGES = {
    'home': ROOT / 'dist/index.html',
    'projects': ROOT / 'dist/projects.html',
}
DIST_CSS = ROOT / 'dist/styles.css'

PAGE_EXPECTED = {
    'home': {
        'min_width': 1280,
        'min_height': 720,
        'label': 'lightweight 720p home preview',
        'videos': {
            'hz1xPkvdhcI': {
                'start': '0',
                'end': '15',
                'title_token': 'Italian National Day 2025',
                'video': 'media/project-previews/italian-national-day-2025-preview-720.mp4',
                'poster': 'media/project-previews/italian-national-day-2025-poster.jpg',
                'duration_min': 14.5,
                'duration_max': 15.6,
                'min_size': 1_000_000,
                'max_size': 4_500_000,
            },
            'yUjjPUTrvt0': {
                'start': '110',
                'end': '133',
                'title_token': 'Perché ci siamo noi',
                'video': 'media/project-previews/perche-ci-siamo-noi-110-133-preview-720.mp4',
                'poster': 'media/project-previews/perche-ci-siamo-noi-110-133-poster.jpg',
                'duration_min': 22.4,
                'duration_max': 23.8,
                'min_size': 1_000_000,
                'max_size': 3_500_000,
            },
        },
    },
    'projects': {
        'min_width': 1920,
        'min_height': 1080,
        'label': 'full-size 1080p project detail preview',
        'videos': {
            'hz1xPkvdhcI': {
                'start': '0',
                'end': '15',
                'title_token': 'Italian National Day 2025',
                'video': 'media/project-previews/italian-national-day-2025-loop-1080.mp4',
                'poster': 'media/project-previews/italian-national-day-2025-poster.jpg',
                'duration_min': 14.5,
                'duration_max': 15.6,
                'min_size': 4_000_000,
                'max_size': 12_000_000,
            },
            'yUjjPUTrvt0': {
                'start': '110',
                'end': '133',
                'title_token': 'Perché ci siamo noi',
                'video': 'media/project-previews/perche-ci-siamo-noi-110-133-loop-1080.mp4',
                'poster': 'media/project-previews/perche-ci-siamo-noi-110-133-poster.jpg',
                'duration_min': 22.4,
                'duration_max': 23.8,
                'min_size': 4_000_000,
                'max_size': 8_000_000,
            },
            'T7MQqKLdZvc': {
                'start': '0',
                'end': '15',
                'title_token': 'Festa della Repubblica 2024',
                'video': 'media/project-previews/italian-national-day-2024-loop-1080.mp4',
                'poster': 'media/project-previews/italian-national-day-2024-poster.jpg',
                'duration_min': 14.5,
                'duration_max': 15.7,
                'min_size': 4_000_000,
                'max_size': 12_000_000,
            },
        },
    },
}

VIDEO_RE = re.compile(r'<video\b(?P<attrs>[^>]*)>(?P<body>[\s\S]*?)</video>', re.I)
ATTR_RE = re.compile(r'''\b([\w:-]+)=(['"])(.*?)\2''', re.I | re.S)
SOURCE_RE = re.compile(r'<source\b(?P<attrs>[^>]*)>', re.I | re.S)
CROP_RE = re.compile(r'crop=(\d+):(\d+):(\d+):(\d+)')


def attrs(block: str) -> dict[str, str]:
    return {name.lower(): value for name, _, value in ATTR_RE.findall(block)}


def fail(msg: str, failures: list[str]) -> None:
    failures.append(msg)


def media_info(path: Path) -> dict[str, object] | None:
    try:
        res = subprocess.run(
            [
                'ffprobe', '-v', 'error', '-select_streams', 'v:0',
                '-show_entries', 'stream=width,height,sample_aspect_ratio,display_aspect_ratio',
                '-show_entries', 'format=duration,size,bit_rate',
                '-of', 'json', str(path),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
            timeout=20,
        )
        data = json.loads(res.stdout)
        stream = data.get('streams', [{}])[0]
        fmt = data.get('format', {})
        return {
            'width': int(stream.get('width', 0) or 0),
            'height': int(stream.get('height', 0) or 0),
            'sar': stream.get('sample_aspect_ratio'),
            'dar': stream.get('display_aspect_ratio'),
            'duration': float(fmt.get('duration', 0) or 0),
            'size': int(fmt.get('size', 0) or 0),
            'bit_rate': int(fmt.get('bit_rate', 0) or 0),
        }
    except Exception:
        return None


def cropdetect_last(path: Path) -> tuple[int, int, int, int] | None:
    try:
        proc = subprocess.run(
            [
                'ffmpeg', '-v', 'info', '-ss', '2', '-i', str(path),
                '-frames:v', '60', '-vf', 'cropdetect=24:16:0', '-f', 'null', '-',
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60,
        )
        matches = CROP_RE.findall(proc.stderr)
        if not matches:
            return None
        return tuple(int(part) for part in matches[-1])
    except Exception:
        return None


def extract_videos(html: str) -> list[tuple[str, dict[str, str], dict[str, str]]]:
    videos = []
    for match in VIDEO_RE.finditer(html):
        raw_video_attrs = match.group('attrs')
        video_attrs = attrs(raw_video_attrs)
        if 'preview-video-frame' not in video_attrs.get('class', ''):
            continue
        source_match = SOURCE_RE.search(match.group('body'))
        source_attrs = attrs(source_match.group('attrs')) if source_match else {}
        videos.append((raw_video_attrs, video_attrs, source_attrs))
    return videos


def check_page(page_name: str, html: str, failures: list[str]) -> None:
    spec = PAGE_EXPECTED[page_name]
    for forbidden in [
        'preview-loop-badge',
        'www.youtube-nocookie.com/embed/hz1xPkvdhcI',
        'www.youtube-nocookie.com/embed/yUjjPUTrvt0',
        'www.youtube.com/embed/T7MQqKLdZvc',
        'https://www.youtube.com/embed/T7MQqKLdZvc',
        'https://www.youtube.com/iframe_api',
    ]:
        if forbidden in html:
            fail(f'{page_name}: forbidden visible/external video-preview token present: {forbidden}', failures)

    # Route isolation: home should not carry full project 1080 assets; project page should not carry the home-only previews.
    other_page = 'projects' if page_name == 'home' else 'home'
    for other in PAGE_EXPECTED[other_page]['videos'].values():
        if str(other['video']) in html:
            fail(f'{page_name}: leaked {other_page}-only video asset {other["video"]}', failures)

    expected_count = len(spec['videos'])
    card_count = len(re.findall(r'<div\b[^>]*\bdata-video-loop-card\b', html))
    if card_count != expected_count:
        fail(f'{page_name}: has {card_count} local video loop cards, expected {expected_count}', failures)

    videos = extract_videos(html)
    if len(videos) != expected_count:
        fail(f'{page_name}: has {len(videos)} preview video elements, expected {expected_count}', failures)

    for video_id, video_spec in spec['videos'].items():
        if video_spec['title_token'] not in html:
            fail(f'{page_name}: missing title token for video {video_id}: {video_spec["title_token"]}', failures)
        data_marker = f'data-video-id="{video_id}" data-source-start="{video_spec["start"]}" data-source-end="{video_spec["end"]}"'
        if data_marker not in html:
            fail(f'{page_name}: missing data source start/end marker for video {video_id}', failures)
        for rel_key in ['video', 'poster']:
            rel = str(video_spec[rel_key])
            if rel not in html:
                fail(f'{page_name}: missing {rel_key} reference for {video_id}: {rel}', failures)
            media_path = ROOT / 'dist' / rel
            if not media_path.exists():
                fail(f'missing built {rel_key} asset for {video_id}: {rel}', failures)
            elif media_path.stat().st_size <= 1024:
                fail(f'built {rel_key} asset too small for {video_id}: {rel}', failures)
        matching = [item for item in videos if item[2].get('src') == video_spec['video']]
        if len(matching) != 1:
            fail(f'{page_name}: expected exactly one local video source for {video_id}, found {len(matching)}', failures)
            continue
        raw_video_attrs, video_attrs, source_attrs = matching[0]
        if source_attrs.get('type') != 'video/mp4':
            fail(f'{page_name}/{video_id}: source type is {source_attrs.get("type")!r}, expected video/mp4', failures)
        for attr in ['muted', 'playsinline']:
            if not re.search(rf'\b{attr}\b', raw_video_attrs, re.I):
                fail(f'{page_name}/{video_id}: video missing {attr} attribute', failures)
        if re.search(r'\bautoplay\b', raw_video_attrs, re.I):
            fail(f'{page_name}/{video_id}: video should not carry autoplay; IntersectionObserver should start playback only when visible', failures)
        if video_attrs.get('preload') != 'metadata':
            fail(f'{page_name}/{video_id}: preload should be metadata', failures)
        if video_attrs.get('poster') != video_spec['poster']:
            fail(f'{page_name}/{video_id}: video poster {video_attrs.get("poster")!r}, expected {video_spec["poster"]!r}', failures)


def check_media(page_name: str, video_id: str, video_spec: dict[str, object], failures: list[str]) -> None:
    page_spec = PAGE_EXPECTED[page_name]
    media_path = ROOT / 'dist' / str(video_spec['video'])
    info = media_info(media_path)
    if info is None:
        fail(f'{page_name}/{video_id}: ffprobe could not read built video geometry', failures)
        return
    width = int(info['width'])
    height = int(info['height'])
    duration = float(info['duration'])
    size = int(info['size'])
    if width < int(page_spec['min_width']) or height < int(page_spec['min_height']):
        fail(f'{page_name}/{video_id}: video geometry is {width}x{height}, expected at least {page_spec["min_width"]}x{page_spec["min_height"]}', failures)
    if info['sar'] != '1:1' or info['dar'] != '16:9':
        fail(f'{page_name}/{video_id}: aspect metadata sar={info["sar"]} dar={info["dar"]}, expected sar=1:1 dar=16:9', failures)
    if not (float(video_spec['duration_min']) <= duration <= float(video_spec['duration_max'])):
        fail(f'{page_name}/{video_id}: duration {duration:.2f}s outside expected range {video_spec["duration_min"]}-{video_spec["duration_max"]}', failures)
    if size < int(video_spec['min_size']):
        fail(f'{page_name}/{video_id}: video file size {size} is below local preview quality floor {video_spec["min_size"]}', failures)
    if size > int(video_spec['max_size']):
        fail(f'{page_name}/{video_id}: video file size {size} exceeds route performance ceiling {video_spec["max_size"]}', failures)
    crop = cropdetect_last(media_path)
    if crop is None:
        fail(f'{page_name}/{video_id}: cropdetect could not verify absence of letterbox bands', failures)
    else:
        crop_w, crop_h, crop_x, crop_y = crop
        min_crop_w = int(page_spec['min_width']) - 40
        min_crop_h = int(page_spec['min_height']) - 40
        if crop_w < min_crop_w or crop_h < min_crop_h:
            fail(f'{page_name}/{video_id}: cropdetect still sees likely letterbox crop={crop_w}:{crop_h}:{crop_x}:{crop_y}', failures)


def main() -> int:
    failures: list[str] = []
    for src in SRC_PAGES:
        if not src.exists():
            fail(f'missing source page: {src.relative_to(ROOT)}', failures)
    for page in DIST_PAGES.values():
        if not page.exists():
            fail(f'missing built page: {page.relative_to(ROOT)}', failures)
    if not DIST_CSS.exists():
        fail('dist/styles.css missing; run npm run build first', failures)

    source = '\n'.join(src.read_text(encoding='utf-8', errors='ignore') for src in SRC_PAGES if src.exists())
    css = DIST_CSS.read_text(encoding='utf-8', errors='ignore') if DIST_CSS.exists() else ''

    for forbidden in [
        'preview-loop-badge',
        'www.youtube-nocookie.com/embed/hz1xPkvdhcI',
        'www.youtube-nocookie.com/embed/yUjjPUTrvt0',
        'www.youtube.com/embed/T7MQqKLdZvc',
        'https://www.youtube.com/embed/T7MQqKLdZvc',
        'https://www.youtube.com/iframe_api',
    ]:
        if forbidden in source or forbidden in css:
            fail(f'forbidden visible/external video-preview token present: {forbidden}', failures)

    for token in [
        'data-video-loop-card',
        'video.preview-video-frame',
        'loadedmetadata',
        'timeupdate',
        'video.duration - video.currentTime <= fadeWindow',
        "card.classList.add('is-fading')",
        'video.currentTime = 0',
        'IntersectionObserver',
        "rootMargin: '160px 0px'",
        'prefers-reduced-motion: reduce',
    ]:
        if token not in source:
            fail(f'source missing local loop-controller token: {token}', failures)

    for token in [
        '.preview-card--video',
        '.preview-video',
        '.preview-video-frame',
        '.preview-video.is-fading .preview-video-frame',
        '.project-video-loop',
        '.project-video-loop.is-fading .project-video-frame',
        'object-fit: cover',
        'transform: scale(1.42)',
        'pointer-events: none',
    ]:
        if token not in css:
            fail(f'CSS missing local video-preview token: {token}', failures)

    for page_name, page in DIST_PAGES.items():
        if page.exists():
            check_page(page_name, page.read_text(encoding='utf-8', errors='ignore'), failures)

    seen_assets: set[str] = set()
    for page_name, page_spec in PAGE_EXPECTED.items():
        for video_id, video_spec in page_spec['videos'].items():
            asset = str(video_spec['video'])
            if asset not in seen_assets:
                check_media(page_name, video_id, video_spec, failures)
                seen_assets.add(asset)

    if failures:
        print('VERDICT: FAIL — Astro Portfolio project video-loop verifier found issues')
        for item in failures:
            print('-', item)
        return 1

    print('VERDICT: PASS — Astro Portfolio video loops are route-split: 720p lightweight home cards, 1080p projects page loops including Festa della Repubblica 2024, muted, badge-free, letterbox-cropped, cover-framed, and visibility-gated')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
