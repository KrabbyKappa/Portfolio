#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from PIL import Image
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
PUBLIC = ROOT / 'public'
SRC = ROOT / 'src'

REQUIRED_ROUTES = [
    'index.html',
    'projects.html',
    'articles.html',
    'references.html',
    'website-development/index.html',
    'website-development/demos/micro/city-lab-pop-up/index.html',
    'website-development/demos/micro/lumo-desk-lamp-teaser/index.html',
    'website-development/demos/micro/mila-yoga-testimonial/index.html',
    'website-development/demos/micro/northstar-notary-proof/index.html',
    'website-development/demos/micro/riverside-bike-rescue/index.html',
    'website-development/demos/basic/harbor-legal-translation/index.html',
    'website-development/demos/basic/verde-lunch-club/index.html',
    'website-development/demos/basic/mosaic-content-studio/index.html',
    'website-development/demos/basic/clearpath-commute-analytics/index.html',
    'website-development/demos/basic/atlas-family-foundation/index.html',
]

DEMO_SLUGS = [
    'city-lab-pop-up',
    'lumo-desk-lamp-teaser',
    'mila-yoga-testimonial',
    'northstar-notary-proof',
    'riverside-bike-rescue',
    'harbor-legal-translation',
    'verde-lunch-club',
    'mosaic-content-studio',
    'clearpath-commute-analytics',
    'atlas-family-foundation',
]

SHOWCASE_SELECTED_SLUGS = [
    'mosaic-content-studio',
    'verde-lunch-club',
    'harbor-legal-translation',
    'city-lab-pop-up',
    'mila-yoga-testimonial',
]

SHOWCASE_SELECTED_HREFS = {
    'mosaic-content-studio': 'demos/basic/mosaic-content-studio/',
    'verde-lunch-club': 'demos/basic/verde-lunch-club/',
    'harbor-legal-translation': 'demos/basic/harbor-legal-translation/',
    'city-lab-pop-up': 'demos/micro/city-lab-pop-up/',
    'mila-yoga-testimonial': 'demos/micro/mila-yoga-testimonial/',
}

ORBIT_PREVIEW_SLUGS = [
    'mosaic-content-studio',
    'verde-lunch-club',
    'harbor-legal-translation',
    'city-lab-pop-up',
    'mila-yoga-testimonial',
]

SHOWCASE_CANONICAL_SHOTS = [
    'assets/site-previews/bizwholistic.jpg',
    *[f'assets/site-previews/{slug}.jpg' for slug in SHOWCASE_SELECTED_SLUGS],
]

PREVIEW_PARITY_SHOTS = [
    'website-development/assets/site-previews/bizwholistic.jpg',
    *[f'website-development/assets/site-previews/{slug}.jpg' for slug in ORBIT_PREVIEW_SLUGS],
]

PREVIEW_NON_SELECTED_SHOTS = [
    'website-development/assets/site-previews/atlas-family-foundation.jpg',
]

EDUCATION_LOGOS = [
    'media/education-logos/dalarna-university-symbol.png',
    'media/education-logos/unistranieri-perugia-symbol.png',
    'media/education-logos/university-trento-symbol.png',
]

AMBIENT_PRIMITIVE_RE = re.compile(r'<(?:polygon|circle|line|polyline|path|rect|ellipse)\b[^>]*>', re.I)
AMBIENT_SHAPE_MARKER_RE = re.compile(r'\bdata-ambient-shape=(["\'])(.*?)\1', re.I)
AMBIENT_HEAVY_RE = re.compile(r'<(?:path|image|use|foreignObject|canvas|video|iframe|text)\b', re.I)

LOCAL_ATTR_RE = re.compile(r'''\b(?:href|src)=(['"])(.*?)\1''', re.I)
ID_RE = re.compile(r'''\bid=(['"])(.*?)\1''', re.I)
H1_RE = re.compile(r'<h1\b', re.I)
HEADING_RE = re.compile(r'<h[1-6]\b[^>]*>(.*?)</h[1-6]>', re.I | re.S)


def fail(msg: str, failures: list[str]) -> None:
    failures.append(msg)


def read(rel: str) -> str:
    return (DIST / rel).read_text(encoding='utf-8', errors='ignore')


def css_balanced(path: Path) -> bool:
    text = path.read_text(encoding='utf-8', errors='ignore')
    depth = 0
    for ch in text:
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def local_target_exists(page_rel: str, url: str, ids_by_page: dict[str, set[str]]) -> tuple[bool, str]:
    if not url or url.startswith(('#', 'mailto:', 'tel:', 'javascript:', 'data:')):
        return True, ''
    parsed = urlparse(url)
    if parsed.scheme in {'http', 'https', '//'} or url.startswith('//'):
        return True, ''

    path = unquote(parsed.path)
    fragment = parsed.fragment
    if ':~:' in fragment:
        # Chrome text-fragment directives may follow a normal id fragment, e.g.
        # #other-projects:~:text=Festa%20della%20Repubblica%202025.
        # Link-target validation should verify only the actual element id.
        fragment = fragment.split(':~:', 1)[0]
    current_file = DIST / page_rel
    base_dir = current_file.parent

    if path.startswith('/'):
        target = DIST / path.lstrip('/')
    elif path:
        target = (base_dir / path).resolve()
        try:
            target.relative_to(DIST.resolve())
        except ValueError:
            return False, f'{page_rel}: local URL escapes dist: {url}'
    else:
        target = current_file

    candidates = []
    if target.exists():
        candidates.append(target)
    if target.suffix == '':
        candidates.extend([target / 'index.html', Path(str(target) + '.html')])
    elif target.name.endswith('.html') and not target.exists():
        candidates.append(target / 'index.html')

    existing = next((c for c in candidates if c.exists()), None)
    if existing is None:
        return False, f'{page_rel}: missing local target {url}'

    if fragment:
        rel = str(existing.relative_to(DIST)).replace('\\', '/')
        if fragment not in ids_by_page.get(rel, set()):
            return False, f'{page_rel}: missing fragment #{fragment} in {rel} for {url}'

    return True, ''


def main() -> int:
    failures: list[str] = []

    if not DIST.exists():
        fail('dist/ missing; run npm run build first', failures)
    else:
        for rel in REQUIRED_ROUTES:
            if not (DIST / rel).exists():
                fail(f'missing built route: {rel}', failures)

    # Astro source must own HTML routes; public must not contain old route HTML.
    expected_sources = [
        SRC / 'pages/index.astro',
        SRC / 'pages/projects.astro',
        SRC / 'pages/articles.astro',
        SRC / 'pages/references.astro',
        SRC / 'pages/website-development/index.astro',
    ]
    for path in expected_sources:
        if not path.exists():
            fail(f'missing Astro route source: {path.relative_to(ROOT)}', failures)

    forbidden_public_html = [p for p in PUBLIC.rglob('*.html')]
    if forbidden_public_html:
        fail('old HTML route files found in public/: ' + ', '.join(str(p.relative_to(ROOT)) for p in forbidden_public_html[:10]), failures)

    # Static asset passthrough.
    if (DIST / 'CNAME').read_text(encoding='utf-8', errors='ignore').strip() != 'lucakosowski.com':
        fail('dist/CNAME missing or wrong custom domain', failures)
    for rel in ['.nojekyll', 'profile.jpg', 'Luca_Kosowski_CV.pdf', 'Reference_Letter_English.pdf', 'Reference_Letter_Italian.pdf', 'styles.css', 'website-development/styles.css']:
        if not (DIST / rel).exists():
            fail(f'missing built asset: {rel}', failures)
    for rel in EDUCATION_LOGOS:
        asset = DIST / rel
        if not asset.exists():
            fail(f'missing education logo asset: {rel}', failures)
        else:
            try:
                with Image.open(asset) as image:
                    if image.size != (320, 320):
                        fail(f'education logo asset {rel} has dimensions {image.size}, expected (320, 320)', failures)
                    if image.getbbox() is None:
                        fail(f'education logo asset {rel} is blank', failures)
            except Exception as exc:
                fail(f'education logo asset {rel} is not readable: {exc}', failures)

    # Required content parity.
    if (DIST / 'index.html').exists():
        home = read('index.html')
        for token in ['Digital and Marketing Services', 'Bizwholistic Ltd.', 'Jan 2026 - Present', 'Luca_Kosowski_CV.pdf']:
            if token not in home:
                fail(f'home missing token: {token}', failures)
        for rel in EDUCATION_LOGOS:
            if rel not in home:
                fail(f'home missing education logo reference: {rel}', failures)
        badge_count = home.count('class="education-logo"')
        if badge_count != 3:
            fail(f'home education logo badge count is {badge_count}, expected 3', failures)
        if 'hero-focus-strip' in home:
            fail('home still contains removed hero focus strip', failures)
        thumb_match = re.search(r'<div[^>]+class="[^"]*\bshowcase-thumb\b[^"]*"[\s\S]*?</div>', home)
        if not thumb_match:
            fail('home showcase preview block missing', failures)
        elif '<span' in thumb_match.group(0):
            fail('home showcase preview still uses empty span placeholders', failures)
        if 'data-preview-window="ethereal-orbit"' not in home:
            fail('home showcase preview missing ethereal orbit window marker', failures)
        if thumb_match:
            home_preview_shots = re.findall(r'src="(website-development/assets/site-previews/[^"]+\.jpg)"', thumb_match.group(0))
            if home_preview_shots != PREVIEW_PARITY_SHOTS:
                fail(f'home showcase preview screenshot sequence {home_preview_shots}, expected {PREVIEW_PARITY_SHOTS}', failures)
            for img in PREVIEW_NON_SELECTED_SHOTS:
                if img in thumb_match.group(0):
                    fail(f'home showcase preview still includes non-selected screenshot: {img}', failures)
    if (DIST / 'projects.html').exists():
        projects = read('projects.html')
        for token in ['Other Projects', 'Website Development Showcase', 'website-development/']:
            if token not in projects:
                fail(f'projects missing token: {token}', failures)
        if 'panel--left' in projects or 'panel--center' in projects or 'panel--right' in projects:
            fail('projects showcase bridge still uses abstract panel placeholders', failures)
        if 'showcase-thumb--bridge' not in projects:
            fail('projects showcase bridge missing real screenshot animation block', failures)
        if 'data-preview-window="ethereal-orbit"' not in projects:
            fail('projects showcase bridge missing ethereal orbit window marker', failures)
        bridge_match = re.search(r'<div[^>]+class="[^"]*\bshowcase-thumb--bridge\b[^"]*"[\s\S]*?</div>', projects)
        if not bridge_match:
            fail('projects showcase bridge preview block missing', failures)
        else:
            project_preview_shots = re.findall(r'src="(website-development/assets/site-previews/[^"]+\.jpg)"', bridge_match.group(0))
            if project_preview_shots != PREVIEW_PARITY_SHOTS:
                fail(f'projects showcase bridge screenshot sequence {project_preview_shots}, expected {PREVIEW_PARITY_SHOTS}', failures)
            for img in PREVIEW_NON_SELECTED_SHOTS:
                if img in bridge_match.group(0):
                    fail(f'projects showcase bridge still includes non-selected screenshot: {img}', failures)
    if (DIST / 'website-development/index.html').exists():
        showcase = read('website-development/index.html')
        biz_img = 'assets/site-previews/bizwholistic.jpg'
        if biz_img not in showcase:
            fail(f'showcase does not reference Bizwholistic screenshot: {biz_img}', failures)
        biz_asset = DIST / 'website-development' / biz_img
        if not biz_asset.exists():
            fail(f'missing Bizwholistic screenshot asset: website-development/{biz_img}', failures)
        else:
            try:
                with Image.open(biz_asset) as image:
                    if image.size != (1440, 980):
                        fail(f'Bizwholistic screenshot dimensions {image.size}, expected (1440, 980)', failures)
            except Exception as exc:
                fail(f'Bizwholistic screenshot is not a readable image: {exc}', failures)
            if biz_asset.stat().st_size < 50_000:
                fail(f'Bizwholistic screenshot asset is suspiciously small ({biz_asset.stat().st_size} bytes); likely not the live site preview', failures)
        for token in ['data-case-study="bizwholistic"', 'https://bizwholistic.com/', 'Bizwholistic']:
            if token not in showcase:
                fail(f'showcase missing Bizwholistic case-study token: {token}', failures)
        for token in ['id="proof"', 'class="hero hero--proof"', 'class="hero-layout"', 'Your ideal website, shaped around your ambition.', 'Selected package websites for the portfolio page.', 'Display strategy']:
            if token not in showcase:
                fail(f'showcase missing professional proof-object layout token: {token}', failures)
        if 'href="#contact"' in showcase:
            fail('showcase Contact nav still points to a removed local #contact section', failures)
        thick_glass_tab_count = showcase.count('data-thick-glass-tab')
        if thick_glass_tab_count != 14:
            fail(f'showcase thick-glass tab markers count is {thick_glass_tab_count}, expected 14', failures)
        for forbidden_token in ['data-ambient-geometry', 'class="ambient-geometry"', '__ambientPhysics', 'data-magnet', 'data-physics-field="inter-shape"']:
            if forbidden_token in showcase:
                fail(f'showcase still contains removed ambient floating layer token: {forbidden_token}', failures)
        for forbidden in ['pill-rail', 'Astro routes</span>', 'Mirrored assets</span>', 'Screenshot proof</span>', 'Premium website directions', 'Live Astro case study / company services', 'Clicking the card sends visitors', 'Portfolio proof-object contract', 'For now this route shows the four demos Luca requested', 'Demo businesses are fictional package examples']:
            if forbidden in showcase:
                fail(f'showcase still contains removed pill/category rail token: {forbidden}', failures)
        if 'fonts.googleapis.com' in showcase or 'fonts.gstatic.com' in showcase:
            fail('showcase still loads external Google font resources; keep this route lightweight', failures)
        case_pos = showcase.find('data-case-study="bizwholistic"')
        demos_pos = showcase.find('id="demos"')
        strategy_pos = showcase.find('id="strategy"')
        if not (0 <= case_pos < demos_pos < strategy_pos):
            fail('showcase section order must be Bizwholistic proof card, selected demos, then Display strategy', failures)
        for purged in ['scope-boundary', 'scope-marker', 'scope-heading', 'Real work and demo concepts stay visibly separate.', 'Showcase labeling key', 'Back to portfolio projects', 'id="contact"', 'Contact information']:
            if purged in showcase:
                fail(f'showcase still contains purged scope-boundary/local-contact token: {purged}', failures)
        selected_demo_slugs = re.findall(r'data-demo-slug="([^"]+)"', showcase)
        if selected_demo_slugs != SHOWCASE_SELECTED_SLUGS:
            fail(f'showcase selected demo slug sequence {selected_demo_slugs}, expected {SHOWCASE_SELECTED_SLUGS}', failures)
        showcase_preview_images = re.findall(r'src="(assets/site-previews/[^"]+\.jpg)"', showcase)
        if showcase_preview_images != SHOWCASE_CANONICAL_SHOTS:
            fail(f'showcase canonical preview image sequence {showcase_preview_images}, expected {SHOWCASE_CANONICAL_SHOTS}', failures)
        for slug in SHOWCASE_SELECTED_SLUGS:
            img = f'assets/site-previews/{slug}.jpg'
            if img not in showcase:
                fail(f'showcase does not reference selected screenshot: {img}', failures)
            if not (DIST / 'website-development' / img).exists():
                fail(f'missing selected screenshot asset: website-development/{img}', failures)
            if f'data-demo-slug="{slug}"' not in showcase:
                fail(f'showcase missing selected demo card marker: {slug}', failures)
            href = SHOWCASE_SELECTED_HREFS[slug]
            article_match = re.search(r'<article[^>]+data-demo-slug="' + re.escape(slug) + r'"[\s\S]*?</article>', showcase)
            if not article_match:
                fail(f'showcase missing selected demo article block: {slug}', failures)
                continue
            article = article_match.group(0)
            if not re.search(r'<a[^>]+class="demo-card__full-link"[^>]+href="' + re.escape(href) + r'"[^>]+data-demo-card-link="' + re.escape(slug) + r'"', article):
                fail(f'showcase missing full-card demo overlay link for {slug}', failures)
            if img not in article:
                fail(f'showcase selected demo article {slug} does not contain its screenshot {img}', failures)
        action_label_count = len(re.findall(r'<div class="demo-actions"[^>]*>\s*<span class="demo-action-label">\s*Open full Astro demo\s*</span>\s*</div>', showcase, re.S))
        if action_label_count != len(SHOWCASE_SELECTED_SLUGS):
            fail(f'showcase demo action labels count is {action_label_count}, expected {len(SHOWCASE_SELECTED_SLUGS)} non-anchor labels because the full card owns navigation', failures)
        if re.search(r'<div class="demo-actions"[^>]*>\s*<a\b', showcase):
            fail('showcase still contains an inner demo-actions anchor instead of full-card navigation', failures)
        for slug in sorted(set(DEMO_SLUGS) - set(SHOWCASE_SELECTED_SLUGS)):
            if f'data-demo-slug="{slug}"' in showcase:
                fail(f'showcase unexpectedly displays non-selected demo card: {slug}', failures)
        mosaic_live_tokens = [
            'data-live-preview-card="mosaic-content-studio"',
            'data-live-preview="mosaic-content-studio"',
            'class="live-demo-frame"',
            'data-live-demo-preview="mosaic-content-studio"',
            'src="demos/basic/mosaic-content-studio/"',
            'sandbox="allow-same-origin"',
            'Live animated preview',
            'class="live-preview-fallback"',
        ]
        for token in mosaic_live_tokens:
            if token not in showcase:
                fail(f'showcase missing Mosaic live-preview token: {token}', failures)

    for rel in ['styles.css', 'website-development/styles.css']:
        path = DIST / rel
        if path.exists() and not css_balanced(path):
            fail(f'CSS braces are not balanced: {rel}', failures)
    main_css = DIST / 'styles.css'
    if main_css.exists():
        css = main_css.read_text(encoding='utf-8', errors='ignore')
        for token in ['showcaseFloat', 'showcaseOrbit', 'showcaseGradientDrift', 'showcaseBandMorph', '.preview-card--showcase:hover .showcase-shot', '.showcase-bridge:hover .showcase-shot', 'animation-play-state: running, running', '.showcase-thumb--bridge', 'linear-gradient(180deg, #01050d 0%, #061023 46%, #030815 100%)', 'radial-gradient(ellipse at center, rgba(116, 188, 247, 0.8)', 'animation: impeccableSilkyOrbit 22s', '-webkit-mask-image: none', 'width: min(62%, 224px)', 'height: 70%', 'opacity: 0.56', 'opacity: 1;', 'translate(-6%, -50%)', 'translate(-94%, -50%)', 'translate(30%, -50%)', 'translate(4%, -50%)', '96%', 'rotateY(-24deg)', 'rotateY(24deg)', 'rotateY(-34deg)']:
            if token not in css:
                fail(f'main CSS missing showcase preview ethereal orbit token: {token}', failures)
        for forbidden_showcase_bg in ['showcaseWindowMist', 'background-size: 100% 100%, 42px 42px, 58px 58px', 'rgba(125, 211, 252, 0.30)', '#0b63ce 122%', '-webkit-mask-image: linear-gradient(90deg, transparent 0%, #000 14%, #000 86%, transparent 100%)']:
            if forbidden_showcase_bg in css:
                fail(f'main CSS still contains space-like showcase background token: {forbidden_showcase_bg}', failures)
        if 'showcaseRotate' in css or 'animation-play-state: paused, running' in css:
            fail('main CSS still contains old paused one-card showcase rotation system', failures)
        if 'hero-focus-strip' in css:
            fail('main CSS still contains removed hero focus strip styling', failures)
    showcase_css = DIST / 'website-development/styles.css'
    if showcase_css.exists():
        css = showcase_css.read_text(encoding='utf-8', errors='ignore')
        for placeholder in ['.stage-card::after', '.demo-card::after']:
            if placeholder in css:
                fail(f'abstract placeholder selector returned: {placeholder}', failures)
        for forbidden in ['.pill-rail', 'pill-rail span']:
            if forbidden in css:
                fail(f'showcase CSS still contains removed pill rail styling: {forbidden}', failures)
        for token in ['.hero-layout', '.hero--proof', 'backdrop-filter: blur(34px) saturate(1.55)', 'overscroll-behavior: none', 'grid-template-columns: 1fr', 'width: min(100%, 1080px)', 'min-height: min(860px, calc(100svh - 72px))', '--tab-refract', '.showcase-topbar nav a::after', '--tab-depth', 'transform-style: preserve-3d', 'saturate(330%) contrast(1.15) blur(4px)', '.showcase-topbar nav a::before', '.demo-card__full-link', '.demo-card__full-link:focus-visible', '.demo-action-label']:
            if token not in css:
                fail(f'showcase CSS missing professional/lightweight layout token: {token}', failures)
        for forbidden_css in ['.ambient-geometry', '.geo-node', 'geoFloat', 'ambientCanvasWrap']:
            if forbidden_css in css:
                fail(f'showcase CSS still contains removed ambient floating layer styling: {forbidden_css}', failures)
        if '--bg: #f7f3ec' not in css:
            fail('showcase CSS must use the light theme background token --bg: #f7f3ec', failures)
        for token in ['.site-shot--live-demo', '.live-preview-shell', '.live-demo-frame', 'width: 192%', 'height: 192%', 'transform: scale(0.52)', 'transform-origin: top left', 'pointer-events: none', '.live-preview-fallback', 'display: none !important', '.live-preview-badge']:
            if token not in css:
                fail(f'showcase CSS missing Mosaic live-preview token: {token}', failures)

    mosaic_rel = 'website-development/demos/basic/mosaic-content-studio/index.html'
    mosaic_css_rel = 'website-development/demos/basic/mosaic-content-studio/styles.css'
    if (DIST / mosaic_rel).exists():
        mosaic_html = read(mosaic_rel)
        mosaic_css_path = DIST / mosaic_css_rel
        mosaic_css = mosaic_css_path.read_text(encoding='utf-8', errors='ignore') if mosaic_css_path.exists() else ''
        for token in [
            'data-interaction-style="css-only-floating-collage"',
            'marquee-tape',
            'brief-mixer',
            'data-interactive="radio-brief-mixer"',
            'type="radio"',
            '<details',
            'tabindex="0"',
        ]:
            if token not in mosaic_html:
                fail(f'Mosaic interactive route missing HTML token: {token}', failures)
        for token in ['float-field', 'float-chip', 'float-dot']:
            if token in mosaic_html:
                fail(f'Mosaic removed background element still present in HTML: {token}', failures)
        for token in [
            '@keyframes tapeMove',
            '@keyframes stickerDrift',
            'content-visibility:auto',
            'contain-intrinsic-size:360px',
            'will-change:transform',
            '.mixer-radio',
            '.case-strip article:hover',
            '.sticker:hover',
            'prefers-reduced-motion',
        ]:
            if token not in mosaic_css:
                fail(f'Mosaic interactive route missing CSS token: {token}', failures)
        for token in ['.float-field', '.float-chip', '.float-dot', '@keyframes dotOrbit', '@keyframes floatLoose', 'bubbleBob', 'spotlightWander', 'mix-blend-mode']:
            if token in mosaic_css:
                fail(f'Mosaic removed background CSS still present: {token}', failures)
        marquee_match = re.search(r"\.marquee-tape\{([^}]*)\}", mosaic_css)
        if not marquee_match:
            fail('Mosaic marquee tape CSS block missing', failures)
        elif 'rotate(' in marquee_match.group(1):
            fail('Mosaic marquee tape must be horizontal; rotate() found', failures)
        bubble_match = re.search(r"\.metric-bubbles li\{([^}]*)\}", mosaic_css)
        if not bubble_match:
            fail('Mosaic metric bubble CSS block missing', failures)
        else:
            bubble_block = bubble_match.group(1).replace(' ', '')
            for centering_token in ['display:flex', 'flex-direction:column', 'align-items:center', 'justify-content:center', 'aspect-ratio:1']:
                if centering_token not in bubble_block:
                    fail(f'Mosaic metric bubbles missing centering token: {centering_token}', failures)

    ids_by_page: dict[str, set[str]] = {}
    for rel in REQUIRED_ROUTES:
        path = DIST / rel
        if not path.exists():
            continue
        html = path.read_text(encoding='utf-8', errors='ignore')
        ids = [m.group(2) for m in ID_RE.finditer(html)]
        ids_by_page[rel] = set(ids)
        dupes = sorted({x for x in ids if ids.count(x) > 1})
        if dupes:
            fail(f'{rel}: duplicate ids {dupes}', failures)
        h1_count = len(H1_RE.findall(html))
        if h1_count != 1:
            fail(f'{rel}: h1 count {h1_count}, expected 1', failures)
        empty_headings = [re.sub(r'<[^>]+>', '', m.group(1)).strip() for m in HEADING_RE.finditer(html)]
        if any(not h for h in empty_headings):
            fail(f'{rel}: empty heading detected', failures)

    for rel in REQUIRED_ROUTES:
        path = DIST / rel
        if not path.exists():
            continue
        html = path.read_text(encoding='utf-8', errors='ignore')
        for _, url in LOCAL_ATTR_RE.findall(html):
            ok, reason = local_target_exists(rel, url, ids_by_page)
            if not ok:
                fail(reason, failures)

    if failures:
        print('VERDICT: FAIL — Astro Portfolio structural verifier found issues')
        for item in failures:
            print('-', item)
        return 1

    print('VERDICT: PASS — Astro Portfolio build has route, content, asset, screenshot, link, heading, CSS, and Astro-source parity')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
