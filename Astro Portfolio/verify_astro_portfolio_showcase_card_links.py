#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent
DIST_SHOWCASE = ROOT / 'dist' / 'website-development' / 'index.html'
DIST_CSS = ROOT / 'dist' / 'website-development' / 'styles.css'
CHROME_CANDIDATES = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
]

EXPECTED_DEMOS = [
    ('mosaic-content-studio', 'Mosaic Content Studio', 'demos/basic/mosaic-content-studio/'),
    ('verde-lunch-club', 'Verde Lunch Club', 'demos/basic/verde-lunch-club/'),
    ('harbor-legal-translation', 'Harbor Legal Translation', 'demos/basic/harbor-legal-translation/'),
    ('city-lab-pop-up', 'City Lab Pop-Up', 'demos/micro/city-lab-pop-up/'),
    ('mila-yoga-testimonial', 'Mila Yoga Reset', 'demos/micro/mila-yoga-testimonial/'),
]

POINTS = [
    ('preview upper-left', 0.10, 0.16),
    ('card middle', 0.50, 0.48),
    ('lower-right action zone', 0.86, 0.88),
]


def fail(message: str) -> int:
    print(f'VERDICT: FAIL -- {message}')
    return 1


def read_dist() -> tuple[str, str]:
    if not DIST_SHOWCASE.exists():
        raise FileNotFoundError(f'missing {DIST_SHOWCASE}; run npm run build first')
    if not DIST_CSS.exists():
        raise FileNotFoundError(f'missing {DIST_CSS}; run npm run build first')
    return DIST_SHOWCASE.read_text(encoding='utf-8', errors='ignore'), DIST_CSS.read_text(encoding='utf-8', errors='ignore')


def card_block(html: str, slug: str) -> str:
    marker = f'data-demo-slug="{slug}"'
    start = html.find(marker)
    if start < 0:
        raise AssertionError(f'missing selected demo card marker: {slug}')
    article_start = html.rfind('<article', 0, start)
    article_end = html.find('</article>', start)
    if article_start < 0 or article_end < 0:
        raise AssertionError(f'could not isolate article block for {slug}')
    return html[article_start:article_end + len('</article>')]


def structural_check(html: str, css: str) -> None:
    for slug, title, href in EXPECTED_DEMOS:
        block = card_block(html, slug)
        if f'<a class="demo-card__full-link" href="{href}" data-demo-card-link="{slug}"' not in block:
            raise AssertionError(f'{slug} missing full-card overlay anchor with expected href {href!r}')
        if f'aria-label="Open the full {title} Astro demo"' not in block:
            raise AssertionError(f'{slug} overlay anchor missing accessible open-label')
        demo_actions_match = re.search(r'<div class="demo-actions"[^>]*>([\s\S]*?)</div>', block)
        if not demo_actions_match:
            raise AssertionError(f'{slug} missing visual demo-actions label')
        if '<a ' in demo_actions_match.group(1).lower():
            raise AssertionError(f'{slug} still has a nested/secondary CTA anchor inside the demo card')
        if '<span class="demo-action-label">Open full Astro demo</span>' not in demo_actions_match.group(1):
            raise AssertionError(f'{slug} visual CTA was not converted to a non-anchor label')
    for token in [
        '.demo-card__full-link',
        'inset: -1px;',
        'z-index: 4;',
        '.demo-card__full-link:focus-visible',
        '.demo-action-label',
    ]:
        if token not in css:
            raise AssertionError(f'showcase CSS missing full-card click token: {token}')


def chrome_path() -> str | None:
    for candidate in CHROME_CANDIDATES:
        if Path(candidate).exists():
            return candidate
    return None


def server_ready(base_url: str) -> None:
    with urlopen(base_url.rstrip('/') + '/website-development/', timeout=5) as resp:
        if resp.status != 200:
            raise RuntimeError(f'HTTP {resp.status} from /website-development/')


def browser_click_check(base_url: str) -> None:
    from playwright.sync_api import sync_playwright

    root = base_url.rstrip('/') + '/'
    showcase_url = urljoin(root, 'website-development/')
    server_ready(root)
    viewports = [
        ('desktop', {'width': 1280, 'height': 900}),
        ('mobile', {'width': 390, 'height': 820}),
    ]
    launch_kwargs = {'headless': True}
    executable = chrome_path()
    if executable:
        launch_kwargs['executable_path'] = executable
    with sync_playwright() as p:
        browser = p.chromium.launch(**launch_kwargs)
        try:
            for viewport_name, viewport in viewports:
                for slug, title, href in EXPECTED_DEMOS:
                    expected_url = urljoin(showcase_url, href)
                    for label, frac_x, frac_y in POINTS:
                        page = browser.new_page(viewport=viewport, device_scale_factor=1)
                        try:
                            response = page.goto(showcase_url, wait_until='load', timeout=30000)
                            if not response or response.status != 200:
                                raise AssertionError(f'{viewport_name} showcase load failed for {slug}: {response.status if response else "no response"}')
                            card = page.locator(f'[data-demo-slug="{slug}"]').first
                            if card.count() != 1:
                                raise AssertionError(f'{viewport_name}: could not locate demo card {slug}')
                            card.evaluate("el => el.scrollIntoView({ block: 'center', inline: 'nearest', behavior: 'instant' })")
                            page.wait_for_timeout(180)
                            overlay = card.locator(f'a.demo-card__full-link[data-demo-card-link="{slug}"]').first
                            if overlay.count() != 1:
                                raise AssertionError(f'{viewport_name}: missing overlay link for {slug}')
                            page.evaluate(
                                """
                                ([slug, fracY]) => {
                                  const card = document.querySelector(`[data-demo-slug="${slug}"]`);
                                  if (!card) return;
                                  const r = card.getBoundingClientRect();
                                  const absoluteTargetY = window.scrollY + r.top + (r.height * fracY);
                                  const desiredViewportY = Math.min(Math.max(window.innerHeight * 0.52, 132), window.innerHeight - 120);
                                  window.scrollTo({ top: Math.max(0, absoluteTargetY - desiredViewportY), behavior: 'instant' });
                                }
                                """,
                                [slug, frac_y],
                            )
                            page.wait_for_timeout(80)
                            boxes = page.evaluate(
                                """
                                (slug) => {
                                  const card = document.querySelector(`[data-demo-slug="${slug}"]`);
                                  const overlay = card?.querySelector(`a.demo-card__full-link[data-demo-card-link="${slug}"]`);
                                  const rect = (el) => {
                                    if (!el) return null;
                                    const r = el.getBoundingClientRect();
                                    return { x: r.x, y: r.y, width: r.width, height: r.height };
                                  };
                                  return { card: rect(card), overlay: rect(overlay) };
                                }
                                """,
                                slug,
                            )
                            card_box = boxes.get('card')
                            overlay_box = boxes.get('overlay')
                            if not card_box or not overlay_box:
                                raise AssertionError(f'{viewport_name}: missing card/overlay box for {slug}')
                            covers_card = (
                                overlay_box['x'] <= card_box['x'] + 1.5
                                and overlay_box['y'] <= card_box['y'] + 1.5
                                and overlay_box['x'] + overlay_box['width'] >= card_box['x'] + card_box['width'] - 1.5
                                and overlay_box['y'] + overlay_box['height'] >= card_box['y'] + card_box['height'] - 1.5
                            )
                            if not covers_card:
                                raise AssertionError(
                                    f'{viewport_name}: overlay does not cover full card for {slug}; '
                                    f'card={card_box} overlay={overlay_box}'
                                )
                            x = card_box['x'] + max(8, min(card_box['width'] - 8, card_box['width'] * frac_x))
                            y = card_box['y'] + max(8, min(card_box['height'] - 8, card_box['height'] * frac_y))
                            topmost = page.evaluate(
                                """
                                ([x, y]) => {
                                  const el = document.elementFromPoint(x, y);
                                  const link = el && el.closest && el.closest('a[data-demo-card-link]');
                                  return {
                                    tag: el ? el.tagName : null,
                                    className: el ? String(el.className || '') : null,
                                    slug: link ? link.getAttribute('data-demo-card-link') : null,
                                    href: link ? link.getAttribute('href') : null,
                                  };
                                }
                                """,
                                [x, y],
                            )
                            if topmost.get('slug') != slug or topmost.get('href') != href:
                                raise AssertionError(f'{viewport_name}: {slug} {label} is not covered by the demo link; topmost={topmost}')
                            page.mouse.click(x, y)
                            page.wait_for_load_state('load', timeout=30000)
                            page.wait_for_timeout(150)
                            got_url = page.url
                            if got_url != expected_url:
                                raise AssertionError(f'{viewport_name}: {slug} {label} click URL mismatch: expected {expected_url!r}, got {got_url!r}')
                        finally:
                            page.close()
        finally:
            browser.close()


def main() -> int:
    parser = argparse.ArgumentParser(description='Verify that Website Development showcase demo cards are fully clickable')
    parser.add_argument('--base-url', help='Optional local server rooted at Astro Portfolio/dist or Astro dev output for browser click verification')
    args = parser.parse_args()
    try:
        html, css = read_dist()
        structural_check(html, css)
        if args.base_url:
            browser_click_check(args.base_url)
    except Exception as exc:
        return fail(str(exc))
    mode = 'structural + rendered full-card click' if args.base_url else 'structural'
    print(f'VERDICT: PASS -- {mode} check confirmed all {len(EXPECTED_DEMOS)} Website Development demo cards open from preview, middle, and lower-right card surfaces on desktop/mobile')
    return 0


if __name__ == '__main__':
    sys.exit(main())
