"""Shared page layout for GallbladderPain.org. Run build.py to regenerate the site."""
import json, html

SITE_NAME = "GallbladderPain.org"
SITE_URL = "https://gallbladderpain.org"   # change if you use www. or a different domain
PUBLISHED = "2026-11-03"
PUBLISHED_HUMAN = "3 November 2026"
AUTHOR = "The GallbladderPain.org editorial team"   # replace with a real named author when you have one

_form_counter = [0]


def esc(s):
    return html.escape(s, quote=True)


def optin(root, variant="rail", heading=None, anchor=False):
    """The Fridge Guide sign-up box. variant: rail | inline | hero"""
    _form_counter[0] += 1
    n = _form_counter[0]
    heading = heading or "Get the free Gallstones Fridge Guide"
    img = f'<img src="{root}assets/img/fridge-guide-preview.webp" width="720" height="1080" alt="Preview of the printable Gallstones Fridge Guide: foods to choose, limit and avoid" loading="lazy">'
    bullets = """<ul>
      <li>Every food sorted into <b>choose</b>, <b>limit</b> and <b>flare-day</b> lists</li>
      <li>A gentle-foods list for bad days</li>
      <li>One page, made to print and stick on your fridge</li>
    </ul>"""
    form = f"""<form data-optin>
      <label for="name-{n}">First name</label>
      <input id="name-{n}" type="text" autocomplete="given-name" placeholder="Your first name">
      <label for="email-{n}">Email address</label>
      <input id="email-{n}" type="email" autocomplete="email" required placeholder="you@example.com">
      <button class="btn" type="submit">Send me the free guide</button>
      <p class="small">Free. No spam. Unsubscribe any time. See our <a href="{root}privacy/">privacy policy</a>.</p>
    </form>"""
    mock = f'<img src="{root}assets/img/fridge-guide-mockup.webp" width="900" height="1000" alt="The printable Gallstones Fridge Guide held on a fridge door with magnets" loading="lazy">'
    aid = ' id="get-guide"' if anchor else ""
    if variant == "inline":
        return f"""<aside class="optin optin-inline"{aid} aria-label="Free fridge guide">
  {mock}
  <div style="display:grid;gap:.8rem">
    <h3>{esc(heading)}</h3>
    <p>Stop guessing at every meal. Print it, stick it on the fridge, and the whole household knows what's safe.</p>
    {form}
  </div>
</aside>"""
    if variant == "hero":
        return f"""<div class="optin"{aid}>
  <div class="hero-guide">
    {mock.replace('loading="lazy"', 'fetchpriority="high"')}
    <div style="display:grid;gap:.6rem"><h2 style="font-size:var(--step-1)">{esc(heading)}</h2>{bullets}</div>
  </div>
  {form}
</div>"""
    return f"""<aside class="optin" aria-label="Free fridge guide">
  <h3>{esc(heading)}</h3>
  {img}
  {bullets}
  {form}
</aside>"""


def guide_strip(root, text="Want the full list of foods to avoid on one printable page?"):
    """Slim call-to-action that jumps to the sign-up box. Used near the top of pages."""
    return f"""<a class="guide-strip" href="#get-guide">
  <img src="{root}assets/img/fridge-guide-preview.webp" width="720" height="1080" alt="" loading="lazy">
  <span><b>{esc(text)}</b> Get the free Gallstones Fridge Guide &rarr;</span>
</a>"""


def food_img(root, name, alt, cls="food-pic"):
    return f'<img class="{cls}" src="{root}assets/img/food/{name}.webp" alt="{esc(alt)}" loading="lazy">'


def ad_slot():
    return '<div class="ad-slot" data-ad></div>'


def red_flags():
    return """<div class="callout warn" role="note">
  <h3>When to get help straight away</h3>
  <p>Get urgent advice from your GP or NHS 111 if tummy pain lasts longer than 30 minutes. Call 999 or go to A&amp;E if you have:</p>
  <ul>
    <li>sudden, severe tummy pain</li>
    <li>pain spreading to your back, with vomiting</li>
    <li>a very high temperature, or you feel hot, cold or shivery</li>
    <li>yellow skin or yellowing in the whites of your eyes</li>
  </ul>
  <p>Don't drive yourself. No food or drink on this site replaces medical care.</p>
</div>"""


def faq(items):
    blocks = "\n".join(
        f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in items
    )
    return f'<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">Questions people ask</h2>{blocks}</section>'


def faq_schema(items):
    import re
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
            for q, a in items
        ],
    }


def sources(items):
    lis = "\n".join(f'<li><a href="{u}" rel="noopener" target="_blank">{esc(t)}</a></li>' for t, u in items)
    return f'<section class="sources" aria-labelledby="src-h"><h2 id="src-h" style="font-size:var(--step-1)">Sources</h2><ol>{lis}</ol></section>'


def author_box(root, reviewed=None):
    return f"""<div class="author-box">
  <b>About this guide.</b> Written by {esc(AUTHOR)} and checked against NHS guidance and published research (listed in the sources).
  We update pages when the evidence changes. <a href="{root}about/">How we write our guides</a>.
  This page is general information, not medical advice. <a href="{root}medical-disclaimer/">Read our medical disclaimer</a>.
</div>"""


def page(path, title, description, main, *, h1=None, crumbs=None, rail=True, schema=None,
         noindex=False, og_type="article", nav_current=None, full_width=False, root=None, minimal=False):
    """path: '' for home, 'gallstones-diet/' for a section. Returns full HTML."""
    depth = path.count("/")
    root = ("../" * depth) if root is None else root
    url = SITE_URL + "/" + path
    nav = [("gallbladder-pain/", "Gallbladder pain"), ("gallstones-diet/", "Gallstones diet"), ("foods-to-avoid-with-gallstones/", "Foods to avoid"), ("about/", "About")]
    nav_html = "".join(
        f'<a href="{root}{p}"{" aria-current=\"page\"" if p == nav_current else ""}>{t}</a>' for p, t in nav
    )
    graph = []
    if crumbs:
        graph.append({
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE_URL + "/" + p}
                for i, (n, p) in enumerate(crumbs)
            ],
        })
    if schema:
        graph.extend(schema if isinstance(schema, list) else [schema])
    ld = ""
    if graph:
        ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False) + "</script>"
    crumbs_html = ""
    if crumbs:
        parts = [f'<a href="{root}{p}">{esc(n)}</a>' for n, p in crumbs[:-1]] + [esc(crumbs[-1][0])]
        crumbs_html = '<nav class="crumbs" aria-label="Breadcrumb">' + " &rsaquo; ".join(parts) + "</nav>"
    if full_width:
        body = main
    else:
        rail_html = f'<aside class="rail">{optin(root)}{ad_slot()}</aside>' if rail else ""
        body = f'<div class="wrap page{"" if rail else " single"}"><article class="article">{crumbs_html}{main}</article>{rail_html}</div>'
    robots = '<meta name="robots" content="noindex, follow">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'
    html_out = f"""<!doctype html>
<html lang="en-GB" data-root="{root}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
{robots}
<link rel="canonical" href="{url}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}/assets/img/og-image.jpg">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Bitter:wght@700;800&display=swap">
<link rel="stylesheet" href="{root}assets/css/style.css">
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="{root}"{' tabindex="-1"' if minimal else ''} aria-label="GallbladderPain.org home">
      <svg width="30" height="30" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3c6 5 11 10 11 16a11 11 0 0 1-22 0C5 13 10 8 16 3z" fill="#66bb6a"/><circle cx="13" cy="19" r="2.6" fill="#ffd54f"/><circle cx="19" cy="21" r="2.2" fill="#ffd54f"/><circle cx="16" cy="15" r="1.9" fill="#ffd54f"/></svg>Gallbladder<span>Pain</span><small>.org</small>
    </a>
    {"" if minimal else f'<nav class="nav" aria-label="Main">{nav_html}<a class="nav-cta" href="{root}#get-guide">Free fridge guide</a></nav>'}
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-links">
      {"" if not minimal else f'<a href="{root}privacy/">Privacy</a><a href="{root}medical-disclaimer/">Medical disclaimer</a><a href="{root}about/">About us</a></div><p>GallbladderPain.org gives general information, not medical advice. If you have severe pain, a fever or yellow skin or eyes, call 999 or go to A&amp;E.</p><p>&copy; 2026 GallbladderPain.org</p></div></footer><script src="{root}assets/js/site.js" defer></script></body></html>'}
      <a href="{root}">Home</a>
      <a href="{root}gallbladder-pain/">Gallbladder pain</a>
      <a href="{root}gallstones-diet/">Gallstones diet</a>
      <a href="{root}foods-to-avoid-with-gallstones/">Foods to avoid</a>
      <a href="{root}about/">About us</a>
      <a href="{root}medical-disclaimer/">Medical disclaimer</a>
      <a href="{root}privacy/">Privacy</a>
    </div>
    <p>GallbladderPain.org gives general information about gallbladder pain, gallstones and eating well. It is not a substitute for advice from your GP, pharmacist or specialist. If you have severe pain, a fever or yellow skin or eyes, call 999 or go to A&amp;E.</p>
    <p>Some links on this site are advertisements or affiliate links. If you buy through them we may earn a commission, at no extra cost to you. This never changes what we say about food or health. <a href="{root}medical-disclaimer/#affiliate">More about how we fund the site</a>.</p>
    <p>&copy; 2026 GallbladderPain.org</p>
  </div>
</footer>
<a class="sticky-cta" href="#get-guide">Get the free Fridge Guide</a>
<script src="{root}assets/js/site.js" defer></script>
</body>
</html>
"""
    if minimal:
        html_out = html_out[: html_out.index("</html>") + len("</html>")] + "\n"
    return html_out


def article_schema(path, headline, description):
    return {
        "@type": "Article",
        "headline": headline,
        "description": description,
        "mainEntityOfPage": SITE_URL + "/" + path,
        "datePublished": PUBLISHED,
        "dateModified": PUBLISHED,
        "inLanguage": "en-GB",
        "image": SITE_URL + "/assets/img/og-image.jpg",
        "author": {"@type": "Organization", "name": AUTHOR},
        "publisher": {"@type": "Organization", "name": SITE_NAME, "url": SITE_URL},
    }


def byline():
    return f'<div class="byline"><span>By {esc(AUTHOR)}</span><span>Updated {PUBLISHED_HUMAN}</span></div>'
