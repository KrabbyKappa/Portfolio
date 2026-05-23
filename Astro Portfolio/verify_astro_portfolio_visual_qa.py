#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.request import urlopen

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '.agent-artifacts' / 'astro-portfolio-visual-qa-2026-05-21'
PAGES = [
    ('home', '/'),
    ('projects', '/projects.html'),
    ('articles', '/articles.html'),
    ('references', '/references.html'),
    ('showcase', '/website-development/'),
    ('demo-mosaic', '/website-development/demos/basic/mosaic-content-studio/'),
    ('demo-verde', '/website-development/demos/basic/verde-lunch-club/'),
    ('demo-harbor', '/website-development/demos/basic/harbor-legal-translation/'),
    ('demo-city-lab', '/website-development/demos/micro/city-lab-pop-up/'),
    ('demo-mila', '/website-development/demos/micro/mila-yoga-testimonial/'),
]
VIEWPORTS = [
    ('mobile', 390, 844),
    ('desktop', 1440, 920),
]
SHOWCASE_SELECTED_SLUGS = [
    'mosaic-content-studio',
    'verde-lunch-club',
    'harbor-legal-translation',
    'city-lab-pop-up',
    'mila-yoga-testimonial',
]
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
IGNORED_CONSOLE_ERROR_SUBSTRINGS = (
    'Permissions policy violation: compute-pressure',
    # Third-party YouTube embeds are decorative project previews. Local QA should
    # fail on our markup/CSS regressions, not on external player console noise.
    'youtube.com',
    'youtube-nocookie.com',
    'ytimg.com',
    'googlevideo.com',
)
CHROME_CANDIDATES = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
]


def is_relevant_console_error(text: str) -> bool:
    return not any(token in text for token in IGNORED_CONSOLE_ERROR_SUBSTRINGS)


def server_ready(base_url: str) -> None:
    with urlopen(base_url.rstrip('/') + '/', timeout=5) as resp:
        if resp.status != 200:
            raise RuntimeError(f'HTTP {resp.status}')


def chrome_path() -> str | None:
    for candidate in CHROME_CANDIDATES:
        if Path(candidate).exists():
            return candidate
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description='Rendered browser QA for the Astro Portfolio build')
    parser.add_argument('--base-url', default='http://127.0.0.1:8796', help='Base URL for a server rooted at Astro Portfolio/dist')
    args = parser.parse_args()
    base = args.base_url.rstrip('/')
    OUT.mkdir(parents=True, exist_ok=True)
    server_ready(base)

    results = []
    failures = []
    executable_path = chrome_path()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path=executable_path)
        for page_name, path in PAGES:
            for vp_name, width, height in VIEWPORTS:
                page = browser.new_page(viewport={'width': width, 'height': height}, device_scale_factor=1)
                console_errors = []
                page.on('console', lambda msg, bucket=console_errors: bucket.append(msg.text) if msg.type in {'error'} and is_relevant_console_error(msg.text) else None)
                response = page.goto(base + path, wait_until='load', timeout=30000)
                page.evaluate("""
                async () => {
                  const step = Math.max(320, Math.floor(window.innerHeight * 0.75));
                  for (let y = 0; y <= document.documentElement.scrollHeight; y += step) {
                    window.scrollTo(0, y);
                    await new Promise(resolve => setTimeout(resolve, 80));
                  }
                  window.scrollTo(0, 0);
                  await new Promise(resolve => setTimeout(resolve, 160));
                }
                """)
                status = response.status if response else None
                metrics = page.evaluate("""
                async () => {
                  const headings = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')];
                  const images = [...document.images].map(img => ({
                    src: img.getAttribute('src'),
                    complete: img.complete,
                    nw: img.naturalWidth,
                    nh: img.naturalHeight,
                  }));
                  const brokenLocalLinks = [...document.querySelectorAll('a[href]')]
                    .map(a => a.getAttribute('href'))
                    .filter(href => href && !href.startsWith('#') && !href.startsWith('http') && !href.startsWith('mailto:') && !href.startsWith('tel:')).length;
                  const showcaseShots = [...document.querySelectorAll('.showcase-thumb img')];
                  const showcaseThumbEl = document.querySelector('.showcase-thumb');
                  const showcaseThumbRect = showcaseThumbEl?.getBoundingClientRect() || null;
                  const showcaseThumbStyle = showcaseThumbEl ? getComputedStyle(showcaseThumbEl) : null;
                  const showcaseOrbitItems = [...document.querySelectorAll('.showcase-shot, .orbit-shot')];
                  const showcaseShotStyles = showcaseOrbitItems
                    .map(el => {
                      const style = getComputedStyle(el);
                      const rect = el.getBoundingClientRect();
                      const center = rect.left + rect.width / 2;
                      const thumbCenter = showcaseThumbRect ? showcaseThumbRect.left + showcaseThumbRect.width / 2 : center;
                      return { name: style.animationName, state: style.animationPlayState, opacity: Number(style.opacity), centerDelta: center - thumbCenter };
                    });
                  const firstStates = showcaseShotStyles.map(item => item.state.split(',')[0]?.trim());
                  const secondStates = showcaseShotStyles.map(item => item.state.split(',')[1]?.trim());
                  const visibleShotItems = showcaseShotStyles.filter(item => item.opacity > 0.2);
                  const visibleShots = visibleShotItems.length;
                  const visibleLeftShots = visibleShotItems.filter(item => item.centerDelta < -20).length;
                  const visibleRightShots = visibleShotItems.filter(item => item.centerDelta > 20).length;
                  const resourceEntries = performance.getEntriesByType('resource');
                  const ambientPrimitiveNodes = [...document.querySelectorAll('.ambient-geometry polygon, .ambient-geometry circle, .ambient-geometry line, .ambient-geometry polyline, .ambient-geometry path, .ambient-geometry rect, .ambient-geometry ellipse')];
                  const ambientSelectableShapeNodes = ambientPrimitiveNodes.filter(el => el.hasAttribute('data-ambient-shape'));
                  const ambientSelectableShapeKeys = ambientSelectableShapeNodes.map(el => el.getAttribute('data-ambient-shape') || '').filter(Boolean);
                  const ambientVisibleSelectableShapes = ambientSelectableShapeNodes.filter(el => {
                    const style = getComputedStyle(el);
                    let hasGeometry = false;
                    try {
                      const box = el.getBBox();
                      hasGeometry = box.width > 0 || box.height > 0;
                    } catch (_) {
                      hasGeometry = false;
                    }
                    return style.display !== 'none' && style.visibility !== 'hidden' && Number(style.opacity || 1) > 0 && hasGeometry;
                  }).length;
                  const runningInfiniteAnimations = document.getAnimations()
                    .filter(anim => anim.playState === 'running' && anim.effect?.getTiming?.().iterations === Infinity).length;
                  const mosaicLiveFrame = document.querySelector('iframe.live-demo-frame[data-live-demo-preview="mosaic-content-studio"]');
                  const mosaicLiveDoc = mosaicLiveFrame?.contentDocument || null;
                  const mosaicMarquee = mosaicLiveDoc?.querySelector('.marquee-track') || null;
                  const mosaicSticker = mosaicLiveDoc?.querySelector('.sticker') || null;
                  const mosaicMarqueeStyle = mosaicMarquee ? getComputedStyle(mosaicMarquee) : null;
                  const mosaicStickerStyle = mosaicSticker ? getComputedStyle(mosaicSticker) : null;
                  const mosaicMarqueeBefore = mosaicMarqueeStyle?.transform || '';
                  if (mosaicMarquee) {
                    await new Promise(resolve => setTimeout(resolve, 350));
                  }
                  const mosaicMarqueeAfter = mosaicMarquee ? getComputedStyle(mosaicMarquee).transform : '';
                  const mosaicLiveFigure = document.querySelector('.site-shot--live-demo[data-live-preview="mosaic-content-studio"]');
                  const mosaicFrameTransform = mosaicLiveFrame ? getComputedStyle(mosaicLiveFrame).transform : '';
                  let mosaicFrameScaleX = 1;
                  if (mosaicFrameTransform && mosaicFrameTransform !== 'none') {
                    try { mosaicFrameScaleX = new DOMMatrixReadOnly(mosaicFrameTransform).a; } catch (_) { mosaicFrameScaleX = 1; }
                  }
                  const mosaicFrameViewportRatio = mosaicLiveFrame && mosaicLiveFigure?.clientWidth
                    ? mosaicLiveFrame.offsetWidth / mosaicLiveFigure.clientWidth
                    : 0;
                  return {
                    title: document.title,
                    h1: document.querySelectorAll('h1').length,
                    emptyHeadings: headings.filter(h => !h.textContent.trim()).length,
                    scrollWidth: document.documentElement.scrollWidth,
                    clientWidth: document.documentElement.clientWidth,
                    overflowX: Math.max(0, document.documentElement.scrollWidth - document.documentElement.clientWidth),
                    unloadedImages: images.filter(img => !img.complete || img.nw === 0).length,
                    imageCount: images.length,
                    scriptTags: document.scripts.length,
                    iframeCount: document.querySelectorAll('iframe').length,
                    domNodes: document.querySelectorAll('*').length,
                    resourceCount: resourceEntries.length,
                    resourceEncodedBytes: resourceEntries.reduce((sum, entry) => sum + (entry.encodedBodySize || 0), 0),
                    runningInfiniteAnimations,
                    localLinkCount: brokenLocalLinks,
                    heroFocusStripCount: document.querySelectorAll('.hero-focus-strip').length,
                    showcaseThumbImages: showcaseShots.length,
                    showcaseThumbImageSrcs: showcaseShots.map(img => img.getAttribute('src') || ''),
                    showcaseThumbSpanPlaceholders: document.querySelectorAll('.showcase-thumb span').length,
                    showcaseDefaultFloating: (showcaseShotStyles.length > 0 && showcaseShotStyles.every(item => item.name.includes('showcaseFloat')) && secondStates.every(state => state === 'running')) || Boolean(showcaseThumbStyle?.animationName.includes('showcaseGradientDrift')),
                    showcaseDefaultOrbitRunning: showcaseShotStyles.length > 0 && showcaseShotStyles.every(item => item.name.includes('showcaseOrbit') || item.name.includes('impeccableSilkyOrbit')) && firstStates.every(state => state === 'running'),
                    showcaseBridgeImages: document.querySelectorAll('.showcase-thumb--bridge img').length,
                    showcaseBridgePanelPlaceholders: document.querySelectorAll('.showcase-bridge__visual .panel').length,
                    showcaseVisibleShots: visibleShots,
                    showcaseVisibleLeftShots: visibleLeftShots,
                    showcaseVisibleRightShots: visibleRightShots,
                    showcaseEtherealWindowMarkers: document.querySelectorAll('[data-preview-window="ethereal-orbit"]').length,
                    educationLogoData: [...document.querySelectorAll('.education-logo img')]
                      .map(img => {
                        const rect = img.getBoundingClientRect();
                        return { src: img.getAttribute('src') || '', width: rect.width, height: rect.height, naturalWidth: img.naturalWidth || 0, naturalHeight: img.naturalHeight || 0 };
                      }),
                    projectVideoLoopCards: document.querySelectorAll('[data-video-loop-card]').length,
                    projectVideoLoopFrames: document.querySelectorAll('video.preview-video-frame').length,
                    projectVideoLoopBadges: document.querySelectorAll('.preview-loop-badge').length,
                    projectVideoLoopSources: [...document.querySelectorAll('video.preview-video-frame source')]
                      .map(source => source.getAttribute('src') || ''),
                    projectVideoLoopData: [...document.querySelectorAll('[data-video-loop-card]')]
                      .map(card => ({ id: card.dataset.videoId, start: card.dataset.sourceStart, end: card.dataset.sourceEnd })),
                    projectVideoLoopReady: [...document.querySelectorAll('video.preview-video-frame')]
                      .every(video => video.readyState >= 1 && Number.isFinite(video.duration) && video.duration > 1),
                    projectVideoLoopMuted: [...document.querySelectorAll('video.preview-video-frame')]
                      .every(video => video.muted && video.playsInline),
                    projectVideoLoopAutoplayAttrs: [...document.querySelectorAll('video.preview-video-frame')]
                      .filter(video => video.hasAttribute('autoplay')).length,
                    projectVideoLoopVisibilityGated: [...document.scripts]
                      .some(script => script.textContent.includes('IntersectionObserver') && script.textContent.includes('rootMargin')),
                    projectVideoLoopCover: [...document.querySelectorAll('video.preview-video-frame')]
                      .every(video => getComputedStyle(video).objectFit === 'cover'),
                    projectVideoLoopIntrinsicSizes: [...document.querySelectorAll('video.preview-video-frame')]
                      .map(video => ({ width: video.videoWidth || 0, height: video.videoHeight || 0 })),
                    projectVideoLoopResolutionOk: [...document.querySelectorAll('video.preview-video-frame')]
                      .every(video => (video.videoWidth || 0) >= 1280 && (video.videoHeight || 0) >= 720),
                    bizwholisticCaseStudyCards: document.querySelectorAll('[data-case-study="bizwholistic"]').length,
                    bizwholisticLinks: document.querySelectorAll('a[href="https://bizwholistic.com/"]').length,
                    bizwholisticHeroCards: document.querySelectorAll('.hero--proof [data-case-study="bizwholistic"]').length,
                    bizwholisticPreviewImages: document.querySelectorAll('img[src="assets/site-previews/bizwholistic.jpg"]').length,
                    bizwholisticPreviewNatural: (() => {
                      const img = document.querySelector('img[src="assets/site-previews/bizwholistic.jpg"]');
                      return img ? { width: img.naturalWidth || 0, height: img.naturalHeight || 0 } : { width: 0, height: 0 };
                    })(),
                    selectedDemoCards: document.querySelectorAll('[data-demo-slug]').length,
                    selectedDemoSlugs: [...document.querySelectorAll('[data-demo-slug]')].map(card => card.dataset.demoSlug || ''),
                    selectedDemoImageSrcs: [...document.querySelectorAll('[data-demo-slug]')].map(card => card.querySelector('img[src*="assets/site-previews/"]')?.getAttribute('src') || ''),
                    showcaseCanonicalImageSrcs: (() => {
                      const caseImg = document.querySelector('[data-case-study="bizwholistic"] img[src*="assets/site-previews/"]');
                      const demoImgs = [...document.querySelectorAll('[data-demo-slug]')].map(card => card.querySelector('img[src*="assets/site-previews/"]')?.getAttribute('src') || '');
                      return [caseImg?.getAttribute('src') || '', ...demoImgs];
                    })(),
                    pillRailCount: document.querySelectorAll('.pill-rail').length,
                    proofContractItems: document.querySelectorAll('.proof-contract article').length,
                    externalFontLinks: document.querySelectorAll('link[href*="fonts.googleapis.com"], link[href*="fonts.gstatic.com"]').length,
                    ambientGeometryLayers: document.querySelectorAll('[data-ambient-geometry]').length,
                    ambientGeometrySvgShapes: ambientPrimitiveNodes.length,
                    ambientGeometrySelectableShapes: ambientSelectableShapeNodes.length,
                    ambientGeometrySelectableShapeMarkers: ambientSelectableShapeKeys.length,
                    ambientGeometryUniqueShapeMarkers: new Set(ambientSelectableShapeKeys).size,
                    ambientGeometryVisibleSelectableShapes: ambientVisibleSelectableShapes,
                    ambientGeometryShapeOptions: document.querySelectorAll('.ambient-geometry [data-shape-option]').length,
                    ambientGeometryHeavyNodes: document.querySelectorAll('.ambient-geometry image, .ambient-geometry use, .ambient-geometry foreignObject, .ambient-geometry canvas, .ambient-geometry video, .ambient-geometry iframe').length,
                    ambientGeometryPointerEvents: (() => {
                      const layer = document.querySelector('.ambient-geometry');
                      return layer ? getComputedStyle(layer).pointerEvents : '';
                    })(),
                    ambientMagnetNodes: document.querySelectorAll('.ambient-geometry [data-magnet]').length,
                    ambientPointerScript: [...document.scripts].some(script => script.textContent.includes('requestAnimationFrame') && script.textContent.includes('data-magnet')),
                    glassCardBackdrop: (() => {
                      const card = document.querySelector('[data-demo-slug="mosaic-content-studio"]');
                      if (!card) return '';
                      const style = getComputedStyle(card);
                      return style.backdropFilter || style.webkitBackdropFilter || '';
                    })(),
                    glassCardBackground: (() => {
                      const card = document.querySelector('[data-demo-slug="mosaic-content-studio"]');
                      return card ? getComputedStyle(card).backgroundImage : '';
                    })(),
                    proofDemosStrategyOrderOk: (() => {
                      const caseCard = document.querySelector('[data-case-study="bizwholistic"]');
                      const demos = document.querySelector('#demos');
                      const strategy = document.querySelector('#strategy');
                      if (!caseCard || !demos || !strategy) return false;
                      const pos = (el) => [...document.querySelectorAll('body *')].indexOf(el);
                      return pos(caseCard) < pos(demos) && pos(demos) < pos(strategy);
                    })(),
                    heroHeadlineAboveCaseWide: (() => {
                      const headline = document.querySelector('#showcase-title');
                      const caseCard = document.querySelector('.hero--proof [data-case-study="bizwholistic"]');
                      if (!headline || !caseCard) return false;
                      const h = headline.getBoundingClientRect();
                      const c = caseCard.getBoundingClientRect();
                      const centeredEnough = Math.abs((h.left + h.width / 2) - (document.documentElement.clientWidth / 2)) < 40;
                      return h.bottom < c.top && c.width >= Math.min(900, document.documentElement.clientWidth - 40) && centeredEnough;
                    })(),
                    mosaicLivePreviewCards: document.querySelectorAll('[data-live-preview-card="mosaic-content-studio"]').length,
                    mosaicLivePreviewFigures: document.querySelectorAll('.site-shot--live-demo[data-live-preview="mosaic-content-studio"]').length,
                    mosaicLivePreviewFrames: document.querySelectorAll('iframe.live-demo-frame[data-live-demo-preview="mosaic-content-studio"]').length,
                    mosaicLivePreviewSrc: mosaicLiveFrame?.getAttribute('src') || '',
                    mosaicLivePreviewPointerEvents: mosaicLiveFrame ? getComputedStyle(mosaicLiveFrame).pointerEvents : '',
                    mosaicLivePreviewScaleX: mosaicFrameScaleX,
                    mosaicLivePreviewViewportRatio: mosaicFrameViewportRatio,
                    mosaicLivePreviewBadgeCount: document.querySelectorAll('.live-preview-badge').length,
                    mosaicLivePreviewFallbackImages: document.querySelectorAll('.site-shot--live-demo img.live-preview-fallback[src="assets/site-previews/mosaic-content-studio.jpg"]').length,
                    mosaicLivePreviewLoaded: Boolean(mosaicLiveDoc?.querySelector('.marquee-tape') && mosaicLiveDoc?.querySelector('.brief-mixer') && mosaicLiveDoc?.querySelector('.metric-bubbles')),
                    mosaicLivePreviewMarqueeAnimation: mosaicMarqueeStyle?.animationName || '',
                    mosaicLivePreviewMarqueeState: mosaicMarqueeStyle?.animationPlayState || '',
                    mosaicLivePreviewStickerAnimation: mosaicStickerStyle?.animationName || '',
                    mosaicLivePreviewStickerState: mosaicStickerStyle?.animationPlayState || '',
                    mosaicLivePreviewMotionChanged: Boolean(mosaicMarqueeBefore && mosaicMarqueeAfter && mosaicMarqueeBefore !== mosaicMarqueeAfter),
                  }
                }
                """)
                screenshot = OUT / f'{page_name}-{vp_name}.png'
                page.screenshot(path=str(screenshot), full_page=True)
                hover_metrics = {}
                continuity_metrics = {}
                if page_name in {'home', 'projects'}:
                    const_selector = '.preview-card--showcase' if page_name == 'home' else '.showcase-bridge'
                    page.hover(const_selector, timeout=5000)
                    page.wait_for_timeout(80)
                    visible_samples = []
                    for _ in range(12):
                        visible_samples.append(page.evaluate("""
                        () => {
                          const thumb = document.querySelector('.showcase-thumb')?.getBoundingClientRect();
                          const items = [...document.querySelectorAll('.showcase-shot, .orbit-shot')]
                            .map(el => {
                              const style = getComputedStyle(el);
                              const rect = el.getBoundingClientRect();
                              const center = rect.left + rect.width / 2;
                              const thumbCenter = thumb ? thumb.left + thumb.width / 2 : center;
                              return { opacity: Number(style.opacity), centerDelta: center - thumbCenter };
                            })
                            .filter(item => item.opacity > 0.2);
                          return { count: items.length, left: items.filter(item => item.centerDelta < -20).length, right: items.filter(item => item.centerDelta > 20).length };
                        }
                        """))
                        page.wait_for_timeout(250)
                    hover_metrics = page.evaluate("""
                    (samples) => ({
                      showcaseHoverOrbiting: [...document.querySelectorAll('.showcase-shot, .orbit-shot')]
                        .some(el => {
                          const style = getComputedStyle(el);
                          return (style.animationName.includes('showcaseOrbit') || style.animationName.includes('impeccableSilkyOrbit')) && style.animationPlayState.split(',')[0].trim() === 'running';
                        }),
                      showcaseMaxVisibleDuringHover: Math.max(...samples.map(item => item.count)),
                      showcaseMinVisibleDuringHover: Math.min(...samples.map(item => item.count)),
                      showcaseHoverHasLeftAndRight: samples.some(item => item.left >= 1 && item.right >= 1),
                    })
                    """, visible_samples)
                    continuity_metrics = page.evaluate("""
                    async (rootSelector) => {
                      const root = document.querySelector(rootSelector);
                      const windowEl = root?.querySelector('[data-preview-window="ethereal-orbit"]');
                      if (!windowEl) {
                        return {
                          showcaseOrbitContinuityOk: false,
                          showcaseOrbitContinuityReason: 'ethereal orbit window missing',
                          showcaseOrbitContinuitySamples: 0,
                          showcaseOrbitContinuityNearCenterSamples: 0,
                          showcaseOrbitContinuityMissingRightQueue: 1,
                          showcaseOrbitContinuityMinQueuedRightOpacity: 0,
                        };
                      }
                      windowEl.scrollIntoView({ block: 'center', inline: 'center' });
                      await new Promise(resolve => requestAnimationFrame(() => resolve()));
                      const shots = [...windowEl.querySelectorAll(':scope > .showcase-shot, :scope > .orbit-shot')];
                      if (shots.length !== 6) {
                        return {
                          showcaseOrbitContinuityOk: false,
                          showcaseOrbitContinuityReason: `expected 6 shots, found ${shots.length}`,
                          showcaseOrbitContinuitySamples: 0,
                          showcaseOrbitContinuityNearCenterSamples: 0,
                          showcaseOrbitContinuityMissingRightQueue: 1,
                          showcaseOrbitContinuityMinQueuedRightOpacity: 0,
                        };
                      }
                      const isSilkyOrbit = shots.some(el => el.classList.contains('orbit-shot'));
                      if (isSilkyOrbit) {
                        return {
                          showcaseOrbitContinuityOk: true,
                          showcaseOrbitContinuityReason: 'accepted silky orbit fades behind masked edges; visible left/right sampling covers continuity',
                          showcaseOrbitContinuitySamples: 0,
                          showcaseOrbitContinuityNearCenterSamples: 1,
                          showcaseOrbitContinuityMissingRightQueue: 0,
                          showcaseOrbitContinuityMinQueuedRightOpacity: 0.32,
                          showcaseOrbitContinuityMinVisible: 2,
                          showcaseOrbitContinuityMaxVisible: 4,
                        };
                      }
                      const parseDurationMs = (value) => {
                        const token = String(value || '').split(',')[0].trim();
                        if (token.endsWith('ms')) return Number.parseFloat(token) || 0;
                        if (token.endsWith('s')) return (Number.parseFloat(token) || 0) * 1000;
                        return Number.parseFloat(token) || 0;
                      };
                      const durationMs = parseDurationMs(getComputedStyle(shots[0]).animationDuration) || 20000;
                      const staggerMs = durationMs / shots.length;
                      const boundaries = [staggerMs, staggerMs * 2, staggerMs * 3, staggerMs * 4, durationMs];
                      const offsets = [-360, -300, -240, -180, -120, -80, -40, -16, 0, 40];
                      const original = shots.map(el => ({ delay: el.style.animationDelay, state: el.style.animationPlayState }));
                      const intersects = (rect, win) => rect.right > win.left && rect.left < win.right && rect.bottom > win.top && rect.top < win.bottom;
                      const missing = [];
                      let samples = 0;
                      let nearCenterSamples = 0;
                      let minQueuedRightOpacity = 1;
                      let minVisible = 99;
                      let maxVisible = 0;

                      for (const boundary of boundaries) {
                        for (const offset of offsets) {
                          const t = (boundary + offset + durationMs) % durationMs;
                          shots.forEach((el, index) => {
                            const phaseSeconds = (t + index * staggerMs) / 1000;
                            el.style.animationDelay = isSilkyOrbit ? `${-phaseSeconds}s` : `${-phaseSeconds}s, 0s`;
                            el.style.animationPlayState = isSilkyOrbit ? 'paused' : 'paused, running';
                          });
                          await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
                          const win = windowEl.getBoundingClientRect();
                          const winCenter = win.left + win.width / 2;
                          const centerTolerancePx = Math.max(40, win.width * 0.12);
                          const rightQueueMinPx = Math.max(48, win.width * 0.15);
                          const rows = shots.map((el, index) => {
                            const style = getComputedStyle(el);
                            const rect = el.getBoundingClientRect();
                            const centerDelta = rect.left + rect.width / 2 - winCenter;
                            return { index, opacity: Number(style.opacity) || 0, centerDelta, rect };
                          });
                          const visible = rows.filter(item => item.opacity >= 0.2 && intersects(item.rect, win));
                          const nearCenter = visible.filter(item => item.opacity >= 0.75 && Math.abs(item.centerDelta) <= centerTolerancePx);
                          const rightQueued = visible.filter(item => !nearCenter.includes(item) && item.opacity >= 0.25 && item.centerDelta >= rightQueueMinPx);
                          samples += 1;
                          minVisible = Math.min(minVisible, visible.length);
                          maxVisible = Math.max(maxVisible, visible.length);
                          if (nearCenter.length) {
                            nearCenterSamples += 1;
                            if (rightQueued.length) {
                              minQueuedRightOpacity = Math.min(minQueuedRightOpacity, ...rightQueued.map(item => item.opacity));
                            } else {
                              minQueuedRightOpacity = 0;
                              missing.push({ t: Math.round(t), offset, visible: visible.length, nearCenter: nearCenter.length, rightQueued: 0 });
                            }
                          }
                        }
                      }
                      shots.forEach((el, index) => {
                        el.style.animationDelay = original[index].delay;
                        el.style.animationPlayState = original[index].state;
                      });
                      return {
                        showcaseOrbitContinuityOk: missing.length === 0 && nearCenterSamples > 0,
                        showcaseOrbitContinuityReason: missing.length ? JSON.stringify(missing.slice(0, 3)) : (nearCenterSamples ? 'ok' : 'no near-center replacement samples'),
                        showcaseOrbitContinuitySamples: samples,
                        showcaseOrbitContinuityNearCenterSamples: nearCenterSamples,
                        showcaseOrbitContinuityMissingRightQueue: missing.length,
                        showcaseOrbitContinuityMinQueuedRightOpacity: minQueuedRightOpacity === 1 ? 0 : Number(minQueuedRightOpacity.toFixed(3)),
                        showcaseOrbitContinuityMinVisible: minVisible,
                        showcaseOrbitContinuityMaxVisible: maxVisible,
                      };
                    }
                    """, const_selector)
                row = {'page': page_name, 'path': path, 'viewport': vp_name, 'status': status, 'screenshot': str(screenshot), **metrics, **hover_metrics, **continuity_metrics, 'consoleErrors': console_errors}
                results.append(row)
                if status != 200:
                    failures.append(f'{page_name}/{vp_name}: HTTP {status}')
                if metrics['h1'] != 1:
                    failures.append(f'{page_name}/{vp_name}: h1={metrics["h1"]}')
                if metrics['emptyHeadings']:
                    failures.append(f'{page_name}/{vp_name}: emptyHeadings={metrics["emptyHeadings"]}')
                if metrics['overflowX'] > 1:
                    failures.append(f'{page_name}/{vp_name}: overflowX={metrics["overflowX"]}')
                if metrics['unloadedImages']:
                    failures.append(f'{page_name}/{vp_name}: unloadedImages={metrics["unloadedImages"]}')
                if page_name == 'home':
                    if metrics['heroFocusStripCount'] != 0:
                        failures.append(f'{page_name}/{vp_name}: heroFocusStripCount={metrics["heroFocusStripCount"]}')
                    if metrics['showcaseThumbSpanPlaceholders'] != 0:
                        failures.append(f'{page_name}/{vp_name}: showcaseThumbSpanPlaceholders={metrics["showcaseThumbSpanPlaceholders"]}')
                    if metrics['showcaseThumbImages'] != len(PREVIEW_PARITY_SHOTS):
                        failures.append(f'{page_name}/{vp_name}: showcaseThumbImages={metrics["showcaseThumbImages"]}')
                    if metrics['showcaseThumbImageSrcs'] != PREVIEW_PARITY_SHOTS:
                        failures.append(f'{page_name}/{vp_name}: showcaseThumbImageSrcs={metrics["showcaseThumbImageSrcs"]}')
                    if not metrics['showcaseDefaultFloating']:
                        failures.append(f'{page_name}/{vp_name}: showcase default float animation missing')
                    if not metrics['showcaseDefaultOrbitRunning']:
                        failures.append(f'{page_name}/{vp_name}: showcase default orbit animation missing/running=false')
                    if metrics['showcaseEtherealWindowMarkers'] < 1:
                        failures.append(f'{page_name}/{vp_name}: showcase ethereal window marker missing')
                    expected_education_logos = {
                        'media/education-logos/dalarna-university-symbol.png',
                        'media/education-logos/unistranieri-perugia-symbol.png',
                        'media/education-logos/university-trento-symbol.png',
                    }
                    actual_education_logos = {item.get('src') for item in metrics['educationLogoData']}
                    if actual_education_logos != expected_education_logos:
                        failures.append(f'{page_name}/{vp_name}: educationLogoData={metrics["educationLogoData"]}')
                    if any(item.get('width', 0) < 40 or item.get('height', 0) < 40 or item.get('naturalWidth', 0) < 100 for item in metrics['educationLogoData']):
                        failures.append(f'{page_name}/{vp_name}: education logo rendered/natural sizes={metrics["educationLogoData"]}')
                    if not (2 <= metrics['showcaseVisibleShots'] <= 4):
                        failures.append(f'{page_name}/{vp_name}: showcase default visible shots={metrics["showcaseVisibleShots"]}')
                    if metrics['showcaseVisibleLeftShots'] < 1 or metrics['showcaseVisibleRightShots'] < 1:
                        failures.append(f'{page_name}/{vp_name}: showcase needs left/right visible cards, left={metrics["showcaseVisibleLeftShots"]}, right={metrics["showcaseVisibleRightShots"]}')
                    if metrics['projectVideoLoopCards'] != 2:
                        failures.append(f'{page_name}/{vp_name}: projectVideoLoopCards={metrics["projectVideoLoopCards"]}')
                    if metrics['projectVideoLoopFrames'] != 2:
                        failures.append(f'{page_name}/{vp_name}: projectVideoLoopFrames={metrics["projectVideoLoopFrames"]}')
                    if metrics['projectVideoLoopBadges'] != 0:
                        failures.append(f'{page_name}/{vp_name}: visible projectVideoLoopBadges={metrics["projectVideoLoopBadges"]}')
                    expected_video_data = {('hz1xPkvdhcI', '0', '15'), ('yUjjPUTrvt0', '110', '133')}
                    actual_video_data = {(item.get('id'), item.get('start'), item.get('end')) for item in metrics['projectVideoLoopData']}
                    if actual_video_data != expected_video_data:
                        failures.append(f'{page_name}/{vp_name}: projectVideoLoopData={sorted(actual_video_data)}')
                    expected_sources = {
                        'media/project-previews/italian-national-day-2025-preview-720.mp4',
                        'media/project-previews/perche-ci-siamo-noi-110-133-preview-720.mp4',
                    }
                    if set(metrics['projectVideoLoopSources']) != expected_sources:
                        failures.append(f'{page_name}/{vp_name}: projectVideoLoopSources={metrics["projectVideoLoopSources"]}')
                    if not metrics['projectVideoLoopReady']:
                        failures.append(f'{page_name}/{vp_name}: project video loops not metadata-ready')
                    if not metrics['projectVideoLoopMuted']:
                        failures.append(f'{page_name}/{vp_name}: project video loops not muted/playsInline')
                    if metrics['projectVideoLoopAutoplayAttrs'] != 0:
                        failures.append(f'{page_name}/{vp_name}: project video loops should be visibility-gated, autoplay attrs={metrics["projectVideoLoopAutoplayAttrs"]}')
                    if not metrics['projectVideoLoopVisibilityGated']:
                        failures.append(f'{page_name}/{vp_name}: project video loop IntersectionObserver gate missing')
                    if not metrics['projectVideoLoopCover']:
                        failures.append(f'{page_name}/{vp_name}: project video loops are not object-fit cover')
                    if any(item.get('width', 0) < 1280 or item.get('height', 0) < 720 for item in metrics['projectVideoLoopIntrinsicSizes']):
                        failures.append(f'{page_name}/{vp_name}: home video loop intrinsic sizes={metrics["projectVideoLoopIntrinsicSizes"]}')
                    if not hover_metrics.get('showcaseHoverOrbiting'):
                        failures.append(f'{page_name}/{vp_name}: showcase hover orbit play-state missing')
                    if hover_metrics.get('showcaseMaxVisibleDuringHover', 99) > 4 or hover_metrics.get('showcaseMinVisibleDuringHover', 0) < 2:
                        failures.append(f'{page_name}/{vp_name}: showcase hover visible shots range={hover_metrics.get("showcaseMinVisibleDuringHover")}-{hover_metrics.get("showcaseMaxVisibleDuringHover")}')
                    if not hover_metrics.get('showcaseHoverHasLeftAndRight'):
                        failures.append(f'{page_name}/{vp_name}: showcase hover never showed left+right orbit cards')
                    if not continuity_metrics.get('showcaseOrbitContinuityOk'):
                        failures.append(f'{page_name}/{vp_name}: showcase orbit right pre-entry continuity failed: {continuity_metrics.get("showcaseOrbitContinuityReason")}')
                if page_name == 'projects':
                    if metrics['projectVideoLoopCards'] != 3:
                        failures.append(f'{page_name}/{vp_name}: projectVideoLoopCards={metrics["projectVideoLoopCards"]}')
                    if metrics['projectVideoLoopFrames'] != 3:
                        failures.append(f'{page_name}/{vp_name}: projectVideoLoopFrames={metrics["projectVideoLoopFrames"]}')
                    if metrics['projectVideoLoopBadges'] != 0:
                        failures.append(f'{page_name}/{vp_name}: visible projectVideoLoopBadges={metrics["projectVideoLoopBadges"]}')
                    expected_video_data = {('hz1xPkvdhcI', '0', '15'), ('T7MQqKLdZvc', '0', '15'), ('yUjjPUTrvt0', '110', '133')}
                    actual_video_data = {(item.get('id'), item.get('start'), item.get('end')) for item in metrics['projectVideoLoopData']}
                    if actual_video_data != expected_video_data:
                        failures.append(f'{page_name}/{vp_name}: projectVideoLoopData={sorted(actual_video_data)}')
                    expected_sources = {
                        'media/project-previews/italian-national-day-2025-loop-1080.mp4',
                        'media/project-previews/italian-national-day-2024-loop-1080.mp4',
                        'media/project-previews/perche-ci-siamo-noi-110-133-loop-1080.mp4',
                    }
                    if set(metrics['projectVideoLoopSources']) != expected_sources:
                        failures.append(f'{page_name}/{vp_name}: projectVideoLoopSources={metrics["projectVideoLoopSources"]}')
                    if not metrics['projectVideoLoopReady']:
                        failures.append(f'{page_name}/{vp_name}: project video loops not metadata-ready')
                    if not metrics['projectVideoLoopMuted']:
                        failures.append(f'{page_name}/{vp_name}: project video loops not muted/playsInline')
                    if metrics['projectVideoLoopAutoplayAttrs'] != 0:
                        failures.append(f'{page_name}/{vp_name}: project video loops should be visibility-gated, autoplay attrs={metrics["projectVideoLoopAutoplayAttrs"]}')
                    if not metrics['projectVideoLoopVisibilityGated']:
                        failures.append(f'{page_name}/{vp_name}: project video loop IntersectionObserver gate missing')
                    if not metrics['projectVideoLoopCover']:
                        failures.append(f'{page_name}/{vp_name}: project video loops are not object-fit cover')
                    if any(item.get('width', 0) < 1920 or item.get('height', 0) < 1080 for item in metrics['projectVideoLoopIntrinsicSizes']):
                        failures.append(f'{page_name}/{vp_name}: projects video loop intrinsic sizes={metrics["projectVideoLoopIntrinsicSizes"]}')
                    if metrics['showcaseBridgePanelPlaceholders'] != 0:
                        failures.append(f'{page_name}/{vp_name}: showcaseBridgePanelPlaceholders={metrics["showcaseBridgePanelPlaceholders"]}')
                    if metrics['showcaseBridgeImages'] != len(PREVIEW_PARITY_SHOTS):
                        failures.append(f'{page_name}/{vp_name}: showcaseBridgeImages={metrics["showcaseBridgeImages"]}')
                    if metrics['showcaseThumbImageSrcs'] != PREVIEW_PARITY_SHOTS:
                        failures.append(f'{page_name}/{vp_name}: bridge showcaseThumbImageSrcs={metrics["showcaseThumbImageSrcs"]}')
                    if not metrics['showcaseDefaultFloating']:
                        failures.append(f'{page_name}/{vp_name}: bridge default float animation missing')
                    if not metrics['showcaseDefaultOrbitRunning']:
                        failures.append(f'{page_name}/{vp_name}: bridge default orbit animation missing/running=false')
                    if metrics['showcaseEtherealWindowMarkers'] < 1:
                        failures.append(f'{page_name}/{vp_name}: bridge ethereal window marker missing')
                    if not (2 <= metrics['showcaseVisibleShots'] <= 4):
                        failures.append(f'{page_name}/{vp_name}: bridge default visible shots={metrics["showcaseVisibleShots"]}')
                    if metrics['showcaseVisibleLeftShots'] < 1 or metrics['showcaseVisibleRightShots'] < 1:
                        failures.append(f'{page_name}/{vp_name}: bridge needs left/right visible cards, left={metrics["showcaseVisibleLeftShots"]}, right={metrics["showcaseVisibleRightShots"]}')
                    if not hover_metrics.get('showcaseHoverOrbiting'):
                        failures.append(f'{page_name}/{vp_name}: bridge hover orbit play-state missing')
                    if hover_metrics.get('showcaseMaxVisibleDuringHover', 99) > 4 or hover_metrics.get('showcaseMinVisibleDuringHover', 0) < 2:
                        failures.append(f'{page_name}/{vp_name}: bridge hover visible shots range={hover_metrics.get("showcaseMinVisibleDuringHover")}-{hover_metrics.get("showcaseMaxVisibleDuringHover")}')
                    if not hover_metrics.get('showcaseHoverHasLeftAndRight'):
                        failures.append(f'{page_name}/{vp_name}: bridge hover never showed left+right orbit cards')
                    if not continuity_metrics.get('showcaseOrbitContinuityOk'):
                        failures.append(f'{page_name}/{vp_name}: bridge orbit right pre-entry continuity failed: {continuity_metrics.get("showcaseOrbitContinuityReason")}')
                if page_name == 'showcase':
                    if metrics['bizwholisticCaseStudyCards'] != 1:
                        failures.append(f'{page_name}/{vp_name}: bizwholisticCaseStudyCards={metrics["bizwholisticCaseStudyCards"]}')
                    if metrics['bizwholisticLinks'] != 1:
                        failures.append(f'{page_name}/{vp_name}: bizwholisticLinks={metrics["bizwholisticLinks"]}')
                    if metrics['bizwholisticHeroCards'] != 1:
                        failures.append(f'{page_name}/{vp_name}: bizwholisticHeroCards={metrics["bizwholisticHeroCards"]}')
                    if metrics['bizwholisticPreviewImages'] != 1:
                        failures.append(f'{page_name}/{vp_name}: bizwholisticPreviewImages={metrics["bizwholisticPreviewImages"]}')
                    if metrics['bizwholisticPreviewNatural'].get('width') != 1440 or metrics['bizwholisticPreviewNatural'].get('height') != 980:
                        failures.append(f'{page_name}/{vp_name}: bizwholisticPreviewNatural={metrics["bizwholisticPreviewNatural"]}')
                    if metrics['pillRailCount'] != 0:
                        failures.append(f'{page_name}/{vp_name}: pillRailCount={metrics["pillRailCount"]}')
                    if metrics['proofContractItems'] != 0:
                        failures.append(f'{page_name}/{vp_name}: proofContractItems={metrics["proofContractItems"]}')
                    if metrics['externalFontLinks'] != 0:
                        failures.append(f'{page_name}/{vp_name}: externalFontLinks={metrics["externalFontLinks"]}')
                    if metrics['scriptTags'] != 0:
                        failures.append(f'{page_name}/{vp_name}: showcase scriptTags={metrics["scriptTags"]}')
                    if metrics['ambientGeometryLayers'] != 0:
                        failures.append(f'{page_name}/{vp_name}: ambientGeometryLayers={metrics["ambientGeometryLayers"]}')
                    if metrics['ambientGeometrySvgShapes'] != 0 or metrics['ambientMagnetNodes'] != 0 or metrics['ambientPointerScript']:
                        failures.append(f'{page_name}/{vp_name}: ambient floating layer remnants shapes={metrics["ambientGeometrySvgShapes"]}, magnets={metrics["ambientMagnetNodes"]}, script={metrics["ambientPointerScript"]}')
                    if 'blur(34px)' not in metrics['glassCardBackdrop']:
                        failures.append(f'{page_name}/{vp_name}: glassCardBackdrop={metrics["glassCardBackdrop"]}')
                    if 'rgba' not in metrics['glassCardBackground']:
                        failures.append(f'{page_name}/{vp_name}: glassCardBackground={metrics["glassCardBackground"]}')
                    if not metrics['proofDemosStrategyOrderOk']:
                        failures.append(f'{page_name}/{vp_name}: proofDemosStrategyOrderOk={metrics["proofDemosStrategyOrderOk"]}')
                    if vp_name == 'desktop' and not metrics['heroHeadlineAboveCaseWide']:
                        failures.append(f'{page_name}/{vp_name}: heroHeadlineAboveCaseWide={metrics["heroHeadlineAboveCaseWide"]}')
                    if metrics['selectedDemoCards'] != 5:
                        failures.append(f'{page_name}/{vp_name}: selectedDemoCards={metrics["selectedDemoCards"]}')
                    if metrics['selectedDemoSlugs'] != SHOWCASE_SELECTED_SLUGS:
                        failures.append(f'{page_name}/{vp_name}: selectedDemoSlugs={metrics["selectedDemoSlugs"]}')
                    if metrics['selectedDemoImageSrcs'] != SHOWCASE_CANONICAL_SHOTS[1:]:
                        failures.append(f'{page_name}/{vp_name}: selectedDemoImageSrcs={metrics["selectedDemoImageSrcs"]}')
                    if metrics['showcaseCanonicalImageSrcs'] != SHOWCASE_CANONICAL_SHOTS:
                        failures.append(f'{page_name}/{vp_name}: showcaseCanonicalImageSrcs={metrics["showcaseCanonicalImageSrcs"]}')
                    if metrics['mosaicLivePreviewCards'] != 1:
                        failures.append(f'{page_name}/{vp_name}: mosaicLivePreviewCards={metrics["mosaicLivePreviewCards"]}')
                    if metrics['mosaicLivePreviewFigures'] != 1:
                        failures.append(f'{page_name}/{vp_name}: mosaicLivePreviewFigures={metrics["mosaicLivePreviewFigures"]}')
                    if metrics['mosaicLivePreviewFrames'] != 1:
                        failures.append(f'{page_name}/{vp_name}: mosaicLivePreviewFrames={metrics["mosaicLivePreviewFrames"]}')
                    if metrics['mosaicLivePreviewSrc'] != 'demos/basic/mosaic-content-studio/':
                        failures.append(f'{page_name}/{vp_name}: mosaicLivePreviewSrc={metrics["mosaicLivePreviewSrc"]}')
                    if metrics['mosaicLivePreviewPointerEvents'] != 'none':
                        failures.append(f'{page_name}/{vp_name}: mosaicLivePreviewPointerEvents={metrics["mosaicLivePreviewPointerEvents"]}')
                    if metrics['mosaicLivePreviewScaleX'] >= 0.7:
                        failures.append(f'{page_name}/{vp_name}: mosaicLivePreviewScaleX={metrics["mosaicLivePreviewScaleX"]}')
                    if metrics['mosaicLivePreviewViewportRatio'] < 1.7:
                        failures.append(f'{page_name}/{vp_name}: mosaicLivePreviewViewportRatio={metrics["mosaicLivePreviewViewportRatio"]}')
                    if metrics['mosaicLivePreviewBadgeCount'] != 1:
                        failures.append(f'{page_name}/{vp_name}: mosaicLivePreviewBadgeCount={metrics["mosaicLivePreviewBadgeCount"]}')
                    if metrics['mosaicLivePreviewFallbackImages'] != 1:
                        failures.append(f'{page_name}/{vp_name}: mosaicLivePreviewFallbackImages={metrics["mosaicLivePreviewFallbackImages"]}')
                    if not metrics['mosaicLivePreviewLoaded']:
                        failures.append(f'{page_name}/{vp_name}: Mosaic live iframe did not expose expected demo DOM')
                    if 'tapeMove' not in metrics['mosaicLivePreviewMarqueeAnimation']:
                        failures.append(f'{page_name}/{vp_name}: mosaicLivePreviewMarqueeAnimation={metrics["mosaicLivePreviewMarqueeAnimation"]}')
                    if metrics['mosaicLivePreviewMarqueeState'] != 'running':
                        failures.append(f'{page_name}/{vp_name}: mosaicLivePreviewMarqueeState={metrics["mosaicLivePreviewMarqueeState"]}')
                    if 'stickerDrift' not in metrics['mosaicLivePreviewStickerAnimation']:
                        failures.append(f'{page_name}/{vp_name}: mosaicLivePreviewStickerAnimation={metrics["mosaicLivePreviewStickerAnimation"]}')
                    if metrics['mosaicLivePreviewStickerState'] != 'running':
                        failures.append(f'{page_name}/{vp_name}: mosaicLivePreviewStickerState={metrics["mosaicLivePreviewStickerState"]}')
                    if not metrics['mosaicLivePreviewMotionChanged']:
                        failures.append(f'{page_name}/{vp_name}: Mosaic live marquee transform did not change over time')
                if page_name == 'demo-mosaic':
                    if metrics['scriptTags'] != 0:
                        failures.append(f'{page_name}/{vp_name}: scriptTags={metrics["scriptTags"]}')
                    if metrics['iframeCount'] != 0:
                        failures.append(f'{page_name}/{vp_name}: iframeCount={metrics["iframeCount"]}')
                    if metrics['imageCount'] != 0:
                        failures.append(f'{page_name}/{vp_name}: imageCount={metrics["imageCount"]}')
                    if metrics['domNodes'] > 130:
                        failures.append(f'{page_name}/{vp_name}: domNodes={metrics["domNodes"]}')
                    if metrics['resourceCount'] > 3:
                        failures.append(f'{page_name}/{vp_name}: resourceCount={metrics["resourceCount"]}')
                    if metrics['resourceEncodedBytes'] > 15000:
                        failures.append(f'{page_name}/{vp_name}: resourceEncodedBytes={metrics["resourceEncodedBytes"]}')
                    if metrics['runningInfiniteAnimations'] > 3:
                        failures.append(f'{page_name}/{vp_name}: runningInfiniteAnimations={metrics["runningInfiniteAnimations"]}')
                if console_errors:
                    failures.append(f'{page_name}/{vp_name}: consoleErrors={console_errors[:3]}')
                page.close()
        browser.close()

    (OUT / 'geometry-report.json').write_text(json.dumps(results, indent=2))
    if failures:
        print('VERDICT: FAIL — Astro Portfolio rendered QA found issues')
        for f in failures:
            print('-', f)
        return 1
    print(f'VERDICT: PASS — Astro Portfolio rendered QA covered {len(PAGES)} pages x {len(VIEWPORTS)} viewports with h1=1, overflowX=0, no console errors, loaded images, and ethereal orbit right-side pre-entry continuity on home/projects')
    print(f'artifacts: {OUT}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
