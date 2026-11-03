"""Paid-traffic sign-up page. Short and focused: one message, one action, no menu.
Not for SEO (noindex). Long-form rules do NOT apply here."""
from layout import *


def free_guide():
    root = "../"
    path = "free-guide/"

    def form(n, label="Send me the free guide"):
        return f"""<form data-optin class="lp-form">
      <label for="lp-name-{n}">First name</label>
      <input id="lp-name-{n}" type="text" autocomplete="given-name" placeholder="Your first name">
      <label for="lp-email-{n}">Email address</label>
      <input id="lp-email-{n}" type="email" autocomplete="email" required placeholder="you@example.com">
      <button class="btn" type="submit">{label}</button>
      <p class="small">100% free. We'll email it to you straight away. Unsubscribe any time. <a href="{root}privacy/">Privacy policy</a>.</p>
    </form>"""

    def tile(img, name, kind):
        tag = "Avoid" if kind == "red" else ("Limit" if kind == "amber" else "Choose")
        return f'<div class="lp-tile {kind}"><img src="{root}assets/img/food/{img}.webp" alt="" loading="lazy"><b>{esc(name)}</b><span>{tag}</span></div>'

    main = f"""
<section class="lp-hero">
  <div class="wrap">
    <div class="lp-copy">
      <div class="kicker">Free printable guide</div>
      <h1>Gallbladder pain? Know exactly what to eat, and what to avoid.</h1>
      <p class="lede">Get the free one-page Gallstones Fridge Guide. Stick it on your fridge and stop guessing at every meal.</p>
      <img class="lp-mock" src="{root}assets/img/fridge-guide-mockup.webp" width="900" height="1000" alt="The Gallstones Fridge Guide on a fridge door" fetchpriority="high">
    </div>
    <div class="optin lp-box" id="get-guide">
      <img class="lp-mini" src="{root}assets/img/fridge-guide-preview.webp" width="720" height="1080" alt="The Gallstones Fridge Guide">
      <h2>Where should we send your guide?</h2>
      <ul class="lp-ticks">
        <li>Over 50 everyday foods sorted into <b>choose</b>, <b>limit</b> and <b>avoid</b></li>
        <li>A gentle-foods list for bad days</li>
        <li>Simple portion tips that make the biggest difference</li>
      </ul>
      {form(1)}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap lp-narrow">
    <h2>Does this sound like you?</h2>
    <ul class="lp-pains">
      <li>You've had an attack and now you're scared to eat.</li>
      <li>Your doctor said "cut down on fat" and that was it.</li>
      <li>You're not sure if milk, cheese, eggs or a glass of wine is OK.</li>
      <li>You're waiting for treatment and want fewer bad days.</li>
    </ul>
    <p>You're not alone. Big, fatty meals are the most common trigger for gallbladder pain, but nobody tells you which everyday foods are the problem. This guide does. It's one page, it's simple, and it lives where you need it: on your fridge.</p>
  </div>
</section>

<section class="section lp-peek">
  <div class="wrap">
    <h2>A peek inside the guide</h2>
    <div class="lp-tiles">
      {tile("fried", "Fried food", "red")}
      {tile("cheese", "Full-fat cheese", "red")}
      {tile("fatty-meat", "Bacon and sausages", "red")}
      {tile("healthy-fats", "Avocado and nuts", "amber")}
      {tile("banana", "Bananas", "green")}
      {tile("porridge", "Porridge", "green")}
      {tile("lean-protein", "Chicken breast", "green")}
      {tile("vegetables", "Vegetables", "green")}
    </div>
    <p class="lp-note">Plus dozens more, all on one printable page.</p>
  </div>
</section>

<section class="cta-band">
  <div class="wrap lp-final">
    <div>
      <h2>Get your free Fridge Guide now</h2>
      <p>It takes 10 seconds. We'll email it to you straight away.</p>
    </div>
    <div class="optin">{form(2, "Yes, send me the guide")}</div>
  </div>
</section>

<section class="section">
  <div class="wrap lp-narrow">
    <div class="faq">
      <details><summary>Is it really free?</summary><p>Yes. There's nothing to pay. You'll also get a few short emails with tips on eating well with gallstones, and you can unsubscribe any time.</p></details>
      <details><summary>How do I get it?</summary><p>Pop your email in the box and we'll send it straight to your inbox as a PDF. Print it on A4 and stick it on your fridge.</p></details>
      <details><summary>Is this medical advice?</summary><p>No. It's general guidance on food, based on NHS dietary advice. Always follow what your GP or specialist tells you. If you have severe pain, a high temperature or yellow skin or eyes, call 999 or go to A&amp;E.</p></details>
    </div>
  </div>
</section>
"""
    return page(path, "Free Gallstones Fridge Guide | GallbladderPain.org",
                "Get the free printable Gallstones Fridge Guide: over 50 everyday foods sorted into choose, limit and avoid.",
                main, full_width=True, noindex=True, minimal=True, og_type="website")
