"""Homepage, diet hub and supporting pages."""
from layout import *

NHS_SYMPTOMS = ("NHS: Gallstones symptoms", "https://www.nhs.uk/conditions/gallstones/symptoms/")
NHS_CAUSES = ("NHS: Gallstones causes", "https://www.nhs.uk/conditions/gallstones/prevention/")
CUH_DIET = ("Cambridge University Hospitals NHS Trust: Dietary advice for patients with gallstones", "https://www.cuh.nhs.uk/patient-information/dietary-advice-for-patients-with-gallstones/")
NHS_LABELS = ("NHS: How to read food labels", "https://www.nhs.uk/live-well/eat-well/food-guidelines-and-food-labels/how-to-read-food-labels/")

# Food index for the hub. slug = page exists; None = listed only (becomes a link when the page is written).
FOODS = {
    "green": [
        ("Bananas", "bananas-and-gallstones/"), ("Apples and pears", None), ("Berries", None),
        ("Oats and porridge", None), ("Rice and pasta", None), ("Potatoes (boiled, baked, mashed without butter)", None),
        ("Vegetables, fresh or frozen", None), ("Beans and lentils", None), ("Chicken and turkey breast, no skin", None),
        ("White fish", None), ("Egg whites", "eggs-and-gallstones/"), ("Skimmed or 1% milk", "milk-and-gallstones/"),
        ("Fat-free Greek yoghurt", None), ("Cottage cheese and quark", "cheese-and-gallstones/"), ("Water, herbal tea", None),
    ],
    "amber": [
        ("Whole eggs", "eggs-and-gallstones/"), ("Alcohol", "alcohol-and-gallstones/"), ("Olive oil (1 to 2 tsp)", None),
        ("Avocado (a quarter at a time)", None), ("Nuts and seeds (a small handful)", None), ("Oily fish like salmon", None),
        ("Lean red meat", None), ("Coffee", None), ("Reduced-fat cheese", "cheese-and-gallstones/"), ("Semi-skimmed milk", "milk-and-gallstones/"), ("Dark chocolate", None),
    ],
    "red": [
        ("Fried food and chips", "fried-food-and-gallstones/"), ("Bacon, sausages, salami", None), ("Pastry, pies and sausage rolls", None),
        ("Takeaways and fast food", None), ("Whole milk and milkshakes", "milk-and-gallstones/"), ("Full-fat cheese", "cheese-and-gallstones/"), ("Butter and cream", None), ("Ice cream and cream cakes", None),
        ("Creamy sauces and gravies", None), ("Cream liqueurs", "alcohol-and-gallstones/"), ("Large, heavy meals", None),
    ],
}


def food_cols(root):
    meta = {
        "green": ("Choose more often", "Low in fat and usually easy on the gallbladder."),
        "amber": ("Small amounts", "Fine for many people in sensible portions. Cut back during a flare."),
        "red": ("Limit or avoid", "High in fat. These trigger symptoms for many people."),
    }
    cols = []
    for k in ("green", "amber", "red"):
        h, p = meta[k]
        lis = "".join(
            f'<li><a href="{root}{s}">{esc(n)}</a></li>' if s else f"<li>{esc(n)}</li>" for n, s in FOODS[k]
        )
        pic = {"green": "vegetables", "amber": "healthy-fats", "red": "fried"}[k]
        cols.append(f'<div class="food-col {k}"><img class="col-pic" src="{root}assets/img/food/{pic}.webp" alt="" loading="lazy"><h3>{h}</h3><p>{p}</p><ul>{lis}</ul></div>')
    return '<div class="food-cols">' + "".join(cols) + "</div>"


FOOD_CARDS = [
    ("foods-to-avoid-with-gallstones/", "Foods to avoid with gallstones", "The complete list of common triggers, with easy swaps.", "fatty-meat"),
    ("fried-food-and-gallstones/", "Fried food and gallstones", "The number one trigger, and how to keep the crunch.", "fried"),
    ("milk-and-gallstones/", "Milk and gallstones", "Whole, skimmed or oat? Every milk compared.", "low-fat-dairy"),
    ("cheese-and-gallstones/", "Cheese and gallstones", "Lightest to heaviest, with safe portion sizes.", "cheese"),
    ("eggs-and-gallstones/", "Eggs and gallstones", "Why the white and the yolk get different verdicts.", "lean-protein"),
    ("bananas-and-gallstones/", "Bananas and gallstones", "One of the safest fruits you can eat, even on a bad day.", "banana"),
    ("alcohol-and-gallstones/", "Alcohol and gallstones", "What the research says, drink by drink.", "food/alcohol.svg"),
]


def cards(root, items):
    out = []
    for it in items:
        p, t, d = it[:3]
        img = it[3] if len(it) > 3 else None
        pic = (f'<img src="{root}assets/img/{img}" alt="" loading="lazy">' if img and "." in img else f'<img src="{root}assets/img/food/{img}.webp" alt="" loading="lazy">') if img else '<span class="card-nopic" aria-hidden="true"></span>'
        out.append(f'<a class="card"><span class="card-pic">{pic}</span><strong>{esc(t)}</strong><span>{esc(d)}</span></a>'.replace('<a class="card">', f'<a class="card" href="{root}{p}">'))
    return '<div class="cards">' + "".join(out) + "</div>"


# ---------------------------------------------------------------- HOME
def home():
    from pages_foods import avoid_grid
    root = ""
    main = f"""
<section class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <div class="kicker">Gallbladder pain and gallstones</div>
      <h1>The foods that trigger gallbladder pain, and what to eat instead</h1>
      <p class="lede">Most people with gallstones leave the doctor's with one line of advice: "cut down on fatty food". Then the next attack comes, and they're left wondering whether it was the milk, the cheese or the chips they had last night.</p>
      <p>We answer those questions food by food, in plain English, checked against NHS advice. Start with the usual suspects:</p>
      <div class="suspects">
        <a href="{root}fried-food-and-gallstones/">{food_img(root, "fried", "Chips", "suspect-pic")}<span>Fried food</span></a>
        <a href="{root}milk-and-gallstones/">{food_img(root, "low-fat-dairy", "A glass of milk", "suspect-pic")}<span>Whole milk</span></a>
        <a href="{root}cheese-and-gallstones/">{food_img(root, "cheese", "Cheese", "suspect-pic")}<span>Cheese</span></a>
        <a href="{root}foods-to-avoid-with-gallstones/">{food_img(root, "fatty-meat", "Bacon and steak", "suspect-pic")}<span>Fatty meat</span></a>
      </div>
    </div>
    {optin(root, "hero", "Get the free printable Fridge Guide", anchor=True)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Foods to avoid with gallstones</h2>
      <p>These eight are behind most gallbladder attacks. Each one has a simple swap, so you can still enjoy your meals.</p>
    </div>
    {avoid_grid(root)}
    <p class="more"><a href="{root}foods-to-avoid-with-gallstones/">See the complete list of foods to avoid, with swaps &rarr;</a></p>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <img src="{root}assets/img/fridge-guide-mockup.webp" width="900" height="1000" alt="The Gallstones Fridge Guide on a fridge door" loading="lazy">
    <div>
      <h2>Stop guessing at every meal</h2>
      <p>The free Gallstones Fridge Guide puts every food on one page: what to choose, what to limit and what to eat on a bad day. Print it, stick it on the fridge, and everyone who cooks for you knows what's safe.</p>
      <ul>
        <li>Over 50 everyday foods sorted into green, amber and red</li>
        <li>A gentle-foods list for flare-up days</li>
        <li>Portion tips that make the biggest difference</li>
      </ul>
      <a class="btn" href="#get-guide">Send me the free guide</a>
    </div>
  </div>
</section>

<section class="section pain-band">
  <div class="wrap">
    <div>
      <h2>Is it your gallbladder?</h2>
      <p>Gallbladder pain usually starts under the ribs on the right or in the middle of the upper tummy, and can spread to the back and right shoulder blade. A typical attack is severe and steady, often comes after a fatty meal or at night, and eases over a few hours.</p>
      <p>Our guides explain what an attack feels like, what causes it, and the warning signs that mean you need help straight away.</p>
      <ul class="link-list">
        <li><a href="{root}gallbladder-pain/">Gallbladder pain: where it hurts and when to get help</a></li>
        <li><a href="{root}gallbladder-symptoms/">Gallbladder symptoms: 10 signs of a problem</a></li>
        <li><a href="{root}gallbladder-attack/">Gallbladder attack: what to do</a></li>
        <li><a href="{root}where-is-gallbladder-pain-felt/">Where is gallbladder pain felt?</a></li>
        <li><a href="{root}gallbladder-pain-relief/">Gallbladder pain relief: what helps</a></li>
        <li><a href="{root}gallstones-treatment/">Gallstones treatment: every option explained</a></li>
        <li><a href="{root}gallstones-symptoms-in-women/">Gallstones symptoms in women</a></li>
        <li><a href="{root}inflamed-gallbladder/">Inflamed or infected gallbladder</a></li>
      </ul>
    </div>
    <img src="{root}assets/img/pain-map.svg" width="640" height="380" alt="Diagram showing where gallbladder pain is felt, front and back" loading="lazy">
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Guides</h2></div>
    {cards(root, [("gallbladder-pain/", "Gallbladder pain", "Where it hurts, what triggers it and when to get help.", "pain-map.svg"), ("gallstones-diet/", "The gallstones diet", "What to eat, what to limit, and a gentle menu for flare-ups.", "vegetables")] + FOOD_CARDS[1:])}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>The three rules that matter most</h2>
    <ol class="steps">
      <li><b>Keep meals small and regular</b>Skipping meals and fasting make the gallbladder empty less often. Big meals ask it to squeeze hard all at once.</li>
      <li><b>Watch the fat in each sitting</b>Large, high-fat meals are the most common trigger. You don't need zero fat, just less at once.</li>
      <li><b>Fill up on fibre</b>Vegetables, fruit, oats, beans and wholegrains are the backbone of a gallbladder-friendly plate.</li>
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap" style="max-width:860px">
    <h2>How we write our guides</h2>
    <p>Every page checks its advice against NHS guidance and published research, and lists its sources at the bottom. Where the evidence is thin, we say so. We won't tell you a juice, cleanse or single food will dissolve your gallstones, because nothing has been shown to do that. What food <em>can</em> do is make attacks less likely and everyday eating far less stressful.</p>
    {red_flags()}
  </div>
</section>
"""
    schema = [
        {"@type": "WebSite", "name": SITE_NAME, "url": SITE_URL + "/", "inLanguage": "en-GB"},
        {"@type": "Organization", "name": SITE_NAME, "url": SITE_URL + "/", "logo": SITE_URL + "/favicon.svg"},
    ]
    return page("", "Gallbladder Pain & Gallstones: Foods to Avoid and What to Eat",
                "The foods that trigger gallbladder pain, what an attack feels like and when to get help. Plain-English guides checked against NHS advice, plus a free printable Gallstones Fridge Guide.",
                main, full_width=True, schema=schema, og_type="website")


# ---------------------------------------------------------------- HUB
HUB_FAQ = [
    ("Can diet get rid of gallstones?",
     "No food or diet has been shown to dissolve gallstones that are already there. What diet can do is lower the chance of painful attacks and support your general health while you wait for treatment or decide on next steps with your doctor."),
    ("Do I need to cut out fat completely?",
     "No. NHS dietitians say a strict low-fat diet isn't needed for everyone. Small amounts of healthy fats are part of a balanced diet. If fatty food triggers your symptoms, cut back on it, and keep portions of fat small at each meal."),
    ("What can I eat during a gallbladder flare-up?",
     "Stick to gentle, low-fat foods in small portions: broth-based soups, porridge, rice, toast, bananas, plain potatoes, steamed vegetables, chicken breast and white fish. If pain lasts longer than 30 minutes, get urgent medical advice."),
    ("Should I lose weight if I have gallstones?",
     "If you're carrying extra weight, losing some can help, but do it gradually. Losing more than about 1kg (2lb) a week, or crash and yo-yo dieting, can make gallstones more likely."),
    ("Do I need a special diet after gallbladder removal?",
     "Usually not. Most people can return to a normal, balanced diet. Some find large fatty meals cause loose stools for a while. Speak to your doctor if diarrhoea doesn't settle."),
    ("Is coffee OK with gallstones?",
     "Black coffee has almost no fat, so the coffee itself is unlikely to be the problem. Watch what comes with it: whole milk, cream, syrups and pastries add up quickly."),
]


def hub():
    from pages_foods import avoid_grid
    root = "../"
    path = "gallstones-diet/"
    h1 = "Gallstones Diet: What to Eat, What to Limit and What to Avoid"
    desc = "A complete, practical diet for gallstones: foods to choose, foods to limit, a gentle flare-up menu and how to read food labels. Checked against NHS advice."
    main = f"""
<h1>{h1}</h1>
{byline()}
<p class="lede">The right diet for gallstones isn't about giving up everything you enjoy. It comes down to smaller meals, less fat at any one sitting, and plenty of fibre. This guide shows you what that looks like on your plate.</p>

<div class="callout">
  <h3>The short version</h3>
  <ul>
    <li><b>Eat little and often.</b> Three regular meals, plus small snacks if you need them. Don't skip breakfast.</li>
    <li><b>Spread your fat out.</b> One large, fatty meal is the most common trigger for an attack.</li>
    <li><b>Grill, steam, boil, poach or microwave</b> instead of frying or roasting in oil.</li>
    <li><b>Aim for at least five portions of fruit and vegetables a day</b> and choose wholegrains.</li>
    <li><b>Drink 6 to 8 glasses of fluid a day,</b> mostly water.</li>
    <li><b>If you need to lose weight, go slowly,</b> no faster than about 1kg (2lb) a week.</li>
  </ul>
</div>

{optin(root, "inline", anchor=True)}

<h2>Start with the foods to avoid</h2>
<p>The quickest win is cutting back on the foods behind most attacks. Tap any of them for the full guide.</p>
{avoid_grid(root)}

<h2>Do you really need a low-fat diet?</h2>
<p>This surprises most people. NHS dietitians say a strict low-fat diet isn't needed for everyone with gallstones, and there's little evidence that cutting fat to the bone helps. Fat is part of a balanced diet, and small amounts of healthy fats like olive oil, nuts and avocado are good for you.</p>
<p>So why does everyone say "avoid fat"? When you eat a fatty meal, your gallbladder squeezes to push bile into your gut to help digest it. If a gallstone is in the way, that squeeze can bring on pain. The bigger and fattier the meal, the harder the squeeze.</p>
<p>That gives you a simple, workable rule: <b>it's the amount of fat in one sitting that matters most.</b> A teaspoon of olive oil on your salad is a very different thing from a full English breakfast. If you notice fatty food triggers your symptoms, cut back further. Everyone's tolerance is different.</p>

<h2>Gallstones food list: green, amber and red</h2>
<p>Here's how common foods sort out for most people with gallstones. Tap any linked food for the full guide, including portion sizes and better ways to cook it.</p>
{food_cols(root)}
<p>This list matches the printable Fridge Guide, so you can check it at a glance while you cook.</p>

<h2>How to spot hidden fat on food labels</h2>
<p>UK food packs use traffic-light colours, and they're one of the easiest tools you have. Look at the <b>fat</b> figure per 100g:</p>
<div class="table-wrap"><table>
  <thead><tr><th>Label colour</th><th>Fat per 100g</th><th>What it means for you</th></tr></thead>
  <tbody>
    <tr><td><span class="tag green">Green</span></td><td class="num">3g or less</td><td>Low fat. A good everyday choice.</td></tr>
    <tr><td><span class="tag amber">Amber</span></td><td class="num">3g to 17.5g</td><td>Medium. Fine in sensible portions; check how much you're eating.</td></tr>
    <tr><td><span class="tag red">Red</span></td><td class="num">over 17.5g</td><td>High fat. Keep portions small or save it for occasional treats.</td></tr>
  </tbody>
</table></div>
<p>Watch for foods that sound healthy but aren't: granola, shop-bought smoothies with nut butter, "light" ready meals with creamy sauces and coleslaw can all carry more fat than you'd expect.</p>

<h2>When you eat matters as much as what you eat</h2>
<p>Your gallbladder stores bile between meals and empties when you eat. Long gaps without food let bile sit and concentrate, and regular meals keep it moving. That's why the NHS advice is to eat regular meals, have breakfast soon after you get up, and avoid fasting or skipping meals.</p>
<p>If big meals leave you uncomfortable, switch to smaller portions more often: three modest meals and two light snacks works well for many people.</p>
<p>The same logic applies to weight loss. Losing weight is a good idea if you're carrying extra, but crash diets and rapid weight loss make gallstones <em>more</em> likely. Aim for no more than about 1kg (2lb) a week.</p>

{ad_slot()}

<h2>A gentle day of eating during a flare-up</h2>
<p>When your gallbladder is grumbling, keep things simple, low in fat and small. This is the sort of day that suits most people:</p>
<div class="table-wrap"><table>
  <thead><tr><th>Meal</th><th>What to eat</th></tr></thead>
  <tbody>
    <tr><td>Breakfast</td><td>Porridge made with water or skimmed milk, topped with a sliced banana</td></tr>
    <tr><td>Mid-morning</td><td>Dry toast or a couple of rice cakes, and a cup of herbal tea</td></tr>
    <tr><td>Lunch</td><td>Broth-based vegetable soup (no cream) with a slice of bread, no butter</td></tr>
    <tr><td>Afternoon</td><td>Apple sauce or a pot of fat-free yoghurt</td></tr>
    <tr><td>Dinner</td><td>Poached white fish or skinless chicken breast with plain boiled potatoes and steamed vegetables</td></tr>
    <tr><td>Through the day</td><td>Water, sipped regularly</td></tr>
  </tbody>
</table></div>
<p>As you feel better, bring back a wider range of foods from the green and amber lists, one at a time, so you can tell what suits you.</p>

<h2>Cooking swaps that make the biggest difference</h2>
<div class="table-wrap"><table>
  <thead><tr><th>Instead of</th><th>Try</th></tr></thead>
  <tbody>
    <tr><td>Fried eggs</td><td>Poached or boiled eggs, or an egg-white omelette</td></tr>
    <tr><td>Chips or roast potatoes</td><td>Baked potato or new potatoes with herbs</td></tr>
    <tr><td>Bacon sandwich</td><td>Lean ham or turkey with tomato in wholemeal bread</td></tr>
    <tr><td>Creamy pasta sauce</td><td>Tomato-based sauce with vegetables</td></tr>
    <tr><td>Butter on everything</td><td>A thin scrape, or none on toast that's topped with something else</td></tr>
    <tr><td>Ice cream</td><td>Fat-free Greek yoghurt with berries</td></tr>
    <tr><td>Crisps</td><td>Plain popcorn, rice cakes or fruit</td></tr>
  </tbody>
</table></div>

<h2>Food-by-food guides</h2>
<p>Our detailed guides explain how each food affects your gallbladder, how much is sensible and the best way to prepare it.</p>
{cards(root, FOOD_CARDS)}

{red_flags()}

{faq(HUB_FAQ)}

{optin(root, "inline", "Want this whole list on your fridge?")}

{author_box(root)}
{sources([CUH_DIET, NHS_SYMPTOMS, NHS_CAUSES, NHS_LABELS])}
"""
    return page(path, "Gallstones Diet: Foods to Eat, Limit and Avoid (UK Guide)", desc, main,
                crumbs=[("Home", ""), ("Gallstones diet", path)],
                schema=[article_schema(path, h1, desc), faq_schema(HUB_FAQ)], nav_current=path)


# ---------------------------------------------------------------- SUPPORT PAGES
def about():
    root = "../"
    main = f"""
<h1>About GallbladderPain.org</h1>
<p class="lede">GallbladderPain.org helps people living with gallstones understand their gallbladder pain and eat in a way that makes attacks less likely.</p>
<p>Gallstones are very common in the UK, and many people wait months between diagnosis and treatment. In that time, the advice they get about food is often a single line: "avoid fatty food". This site fills in the detail: what the pain means, when to get help, and what to eat, one food at a time.</p>
<h2>How we write our guides</h2>
<ul>
  <li><b>We check against trusted sources.</b> Our main references are NHS guidance, NHS hospital dietetic advice and published research. Every guide lists its sources.</li>
  <li><b>We say when evidence is weak.</b> If something is based on small or old studies, we tell you.</li>
  <li><b>We don't promise cures.</b> No food, juice or cleanse has been shown to dissolve gallstones, and we won't pretend otherwise.</li>
  <li><b>We keep pages up to date.</b> Each page shows when it was last updated.</li>
</ul>
<!-- TODO: add the real author name, photo and short bio here, and a named medical reviewer when you have one. -->
<h2>How the site is funded</h2>
<p>GallbladderPain.org is free to read. We pay for it through advertising and affiliate links, which are clearly labelled. Advertisers have no say over what we write. <a href="{root}medical-disclaimer/#affiliate">Read more about advertising on this site</a>.</p>
<h2>Contact</h2>
<p>Spotted a mistake or have a question? Email us at <b>hello@gallbladderpain.org</b>.</p>
<!-- TODO: set up this email address, or replace it with your own. -->
"""
    return page("about/", "About GallbladderPain.org", "Who we are, how we write our gallbladder pain and gallstones diet guides, and how the site is funded.",
                main, rail=False, crumbs=[("Home", ""), ("About", "about/")], nav_current="about/")


def disclaimer():
    main = """
<h1>Medical disclaimer</h1>
<p class="lede">The information on GallbladderPain.org is for general information only. It is not medical advice.</p>
<p>Our guides are written to help you understand how food choices may affect gallstone symptoms. They can't take account of your personal medical history, other conditions or medicines. Always follow the advice of your GP, specialist, dietitian or pharmacist, and speak to them before making big changes to your diet or taking supplements.</p>
<p>If you have severe tummy pain, pain spreading to your back with vomiting, a high temperature, or yellow skin or eyes, call 999 or go to A&amp;E. For pain lasting longer than 30 minutes, get urgent advice from your GP or NHS 111.</p>
<h2 id="affiliate">Advertising and affiliate links</h2>
<p>Some pages show advertisements, and some links are affiliate links. If you click one and buy something, we may earn a commission, at no extra cost to you. Adverts are labelled "Advertisement".</p>
<p>Products advertised on this site are not a treatment or cure for gallstones, and nothing we say about food should be read as a recommendation for a particular product. Advertisers have no influence over our food guides.</p>
"""
    return page("medical-disclaimer/", "Medical Disclaimer | GallbladderPain.org", "GallbladderPain.org provides general information, not medical advice. Read how we handle advertising and affiliate links.",
                main, rail=False, crumbs=[("Home", ""), ("Medical disclaimer", "medical-disclaimer/")])


def privacy():
    main = """
<h1>Privacy policy</h1>
<p class="lede">This page explains what personal information we collect and how we use it.</p>
<!-- TODO: review this with your own details before launch: business name, address, email provider and analytics tool. -->
<h2>Who we are</h2>
<p>GallbladderPain.org (gallbladderpain.org) is run by [YOUR NAME OR BUSINESS NAME], [ADDRESS]. Contact: hello@gallbladderpain.org.</p>
<h2>What we collect</h2>
<ul>
  <li><b>Your name and email address</b>, when you ask for the Fridge Guide. We use them to send you the guide and our emails about eating well with gallstones, which may include offers. Our legal basis is your consent.</li>
  <li><b>Anonymous usage data</b> through our analytics tool, such as which pages are visited, to help us improve the site.</li>
</ul>
<h2>Who we share it with</h2>
<p>Your email address is stored by our email provider, [MailerLite / Kit], which processes it on our behalf. We never sell your details.</p>
<h2>Your rights</h2>
<p>You can unsubscribe at any time using the link at the bottom of every email. You can also ask us to see, correct or delete the information we hold about you by emailing hello@gallbladderpain.org. If you're unhappy with how we handle your data, you can complain to the Information Commissioner's Office (ico.org.uk).</p>
<h2>Cookies</h2>
<p>We use only the cookies needed for the site and analytics to work. [Update this section to match the analytics tool you install.]</p>
<p>Last updated: 3 November 2026.</p>
"""
    return page("privacy/", "Privacy Policy | GallbladderPain.org", "How GallbladderPain.org collects, uses and protects your personal information.",
                main, rail=False, crumbs=[("Home", ""), ("Privacy", "privacy/")])


def thank_you():
    root = "../"
    main = f"""
<h1>Check your inbox: your Fridge Guide is on its way</h1>
<p class="lede">We've just emailed you the printable Gallstones Fridge Guide. It usually arrives within a couple of minutes.</p>
<div class="callout">
  <h3>Can't see it?</h3>
  <ul>
    <li>Check your spam, junk or "Promotions" folder.</li>
    <li>Mark the email as "not spam" so you get our future guides.</li>
    <li>Still nothing after 10 minutes? Email hello@gallbladderpain.org.</li>
  </ul>
</div>
<h2>While you wait</h2>
<p>These are the guides our readers find most useful:</p>
{cards(root, [("gallstones-diet/", "The complete gallstones diet", "What to eat, what to limit, and a gentle flare-up menu.", "vegetables")] + FOOD_CARDS)}
{ad_slot()}
"""
    return page("thank-you/", "Thank You | GallbladderPain.org", "Your Gallstones Fridge Guide is on its way.", main,
                rail=False, noindex=True)


def not_found():
    main = """
<h1>Sorry, we can't find that page</h1>
<p class="lede">It may have moved. Try the complete gallstones diet guide or head back to the homepage.</p>
<p><a href="/gallstones-diet/">Gallstones diet guide</a> &middot; <a href="/">Homepage</a></p>
"""
    return page("404.html", "Page not found | GallbladderPain.org", "Page not found.", main, rail=False, noindex=True, root="/")
