"""Builds the GallbladderPain.org site into the folder above this one.
Usage:  python3 _build/build.py
Add a new page: write a function in pages_foods.py, then add it to PAGES below."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from layout import SITE_URL, PUBLISHED
import pages_core as c
import pages_foods as f
import pages_pain as pn
import pages_symptoms as sy
import pages_landing as lp
import pages_seo as seo

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (output path, builder, include in sitemap, priority)
PAGES = [
    ("", c.home, True, "1.0"),
    ("gallbladder-pain/", pn.gallbladder_pain, True, "0.9"),
    ("gallbladder-symptoms/", sy.symptoms, True, "0.9"),
    ("gallbladder-attack/", sy.attack, True, "0.9"),
    ("where-is-gallbladder-pain-felt/", seo.where_pain, True, "0.9"),
    ("gallstones-treatment/", seo.treatment, True, "0.9"),
    ("gallbladder-pain-relief/", seo.pain_relief, True, "0.9"),
    ("gallstones-symptoms-in-women/", sy.women, True, "0.9"),
    ("inflamed-gallbladder/", sy.inflamed, True, "0.8"),
    ("gallstones-diet/", c.hub, True, "0.9"),
    ("foods-to-avoid-with-gallstones/", f.foods_to_avoid, True, "0.9"),
    ("fried-food-and-gallstones/", f.fried_food, True, "0.8"),
    ("milk-and-gallstones/", f.milk, True, "0.8"),
    ("cheese-and-gallstones/", f.cheese, True, "0.8"),
    ("bananas-and-gallstones/", f.bananas, True, "0.8"),
    ("alcohol-and-gallstones/", f.alcohol, True, "0.8"),
    ("eggs-and-gallstones/", f.eggs, True, "0.8"),
    ("about/", c.about, True, "0.3"),
    ("medical-disclaimer/", c.disclaimer, True, "0.2"),
    ("privacy/", c.privacy, True, "0.1"),
    ("free-guide/", lp.free_guide, False, None),
    ("thank-you/", c.thank_you, False, None),
    ("404.html", c.not_found, False, None),
]

urls = []
for path, fn, in_map, prio in PAGES:
    target = os.path.join(OUT, path, "index.html") if not path.endswith(".html") else os.path.join(OUT, path)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(fn())
    if in_map:
        urls.append(f"  <url><loc>{SITE_URL}/{path}</loc><lastmod>{PUBLISHED}</lastmod><priority>{prio}</priority></url>")
    print("built", path or "index")

with open(os.path.join(OUT, "sitemap.xml"), "w") as fh:
    fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w") as fh:
    fh.write(f"User-agent: *\nDisallow: /thank-you/\n\nSitemap: {SITE_URL}/sitemap.xml\n")
with open(os.path.join(OUT, "favicon.svg"), "w") as fh:
    fh.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="#163a6b"/><path d="M16 4c5.5 4.6 10 9.2 10 14.7a10 10 0 0 1-20 0C6 13.2 10.5 8.6 16 4z" fill="#66bb6a"/><circle cx="13.2" cy="19" r="2.4" fill="#ffd54f"/><circle cx="18.8" cy="20.8" r="2" fill="#ffd54f"/><circle cx="16" cy="15" r="1.8" fill="#ffd54f"/></svg>\n')
print("done")
