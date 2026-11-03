"""Food-by-food guides. Each follows: verdict -> why -> how much -> how to eat it -> swaps -> red flags -> FAQ -> sources."""
from layout import *
from pages_core import CUH_DIET, NHS_SYMPTOMS, FOOD_CARDS, cards

USDA = ("USDA FoodData Central (nutrition values)", "https://fdc.nal.usda.gov/")
NHS_PANCREATITIS = ("NHS: Acute pancreatitis causes", "https://www.nhs.uk/conditions/acute-pancreatitis/causes/")
NHS_UNITS = ("NHS: Alcohol units and low-risk drinking guidelines", "https://www.nhs.uk/live-well/alcohol-advice/calculating-alcohol-units/")
BAI_2022 = ("Bai Y et al. Addictive behavior and incident gallstone disease: a dose-response meta-analysis and Mendelian randomization study. Frontiers in Nutrition, 2022", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9589252/")


def verdict(colour, label, text, facts, img=None, alt=""):
    f = "".join(f"<span>{k} <b>{v}</b></span>" for k, v in facts)
    pic = f'<img class="verdict-pic" src="../assets/img/food/{img}.webp" alt="{alt}">' if img else ""
    return f"""<div class="verdict {colour}{' has-pic' if img else ''}">
  <div class="light" aria-hidden="true"><i></i><i></i><i></i></div>
  <div><div class="verdict-label">{label}</div><div class="verdict-text">{text}</div><div class="verdict-facts">{f}</div></div>
  {pic}
</div>"""


def related(root, current):
    return "<h2>More food guides</h2>" + cards(root, [c for c in FOOD_CARDS if c[0] != current] +
        [("gallstones-diet/", "The complete gallstones diet", "Every food sorted into choose, limit and avoid.", "vegetables"), ("gallbladder-pain/", "Gallbladder pain", "Where it hurts, what triggers it and when to get help.", "pain-map.svg")])


def food_page(path, title, h1, desc, body, faq_items, src, strip="Not sure what else is safe? Get every food sorted on one printable page."):
    root = "../"
    ad = ad_slot()
    # the first sign-up box goes where the in-article ad was; the ad moves further down
    body = body.replace(ad, optin(root, "inline", "Get the printable list of what to eat and avoid", anchor=True), 1)
    body = body.replace("<h2>", guide_strip(root, strip) + "\n<h2>", 1)
    body = body.replace("<h2>The bottom line</h2>", ad + "\n<h2>The bottom line</h2>", 1)
    main = f"""<h1>{h1}</h1>
{byline()}
{body}
{red_flags()}
{faq(faq_items)}
{optin(root, "inline", "Get every food sorted for you, free")}
{related(root, path)}
{author_box(root)}
{sources(src)}"""
    name = h1.split(":")[0].split("?")[0]
    return page(path, title, desc, main,
                crumbs=[("Home", ""), ("Gallstones diet", "gallstones-diet/"), (name, path)],
                schema=[article_schema(path, h1, desc), faq_schema(faq_items)])


# ---------------------------------------------------------------- BANANAS
BANANA_FAQ = [
    ("Can I eat bananas during a gallbladder attack?",
     "During an attack many people can't face food at all, and that's fine for a short while. When you're ready to eat again, a ripe banana is one of the gentlest foods to start with. If pain lasts longer than 30 minutes, get urgent medical advice."),
    ("How many bananas a day can I eat with gallstones?",
     "One or two a day is a sensible amount for most people. They're very low in fat, so the limit is about keeping your diet varied and your sugar intake reasonable, not about your gallbladder."),
    ("Are banana smoothies good for gallstones?",
     "Yes, if you make them yourself with skimmed milk or fat-free yoghurt. Shop-bought smoothies and smoothie-bar drinks often add nut butter, full-fat yoghurt or ice cream, which can push the fat up a lot."),
    ("Can bananas dissolve gallstones?",
     "No. Bananas are a great food for people with gallstones, but no food has been shown to dissolve stones. Be wary of anyone who says otherwise."),
    ("Are bananas good after gallbladder removal?",
     "Yes. Bananas are easy to digest and their soluble fibre can help firm up loose stools, which some people get after surgery."),
    ("Is banana bread OK with gallstones?",
     "Usually not as an everyday food. Most banana bread recipes use a lot of butter or oil, so a thick slice can carry more fat than you'd guess. Try a reduced-fat recipe, or have a small slice occasionally."),
]


def bananas():
    path = "bananas-and-gallstones/"
    h1 = "Bananas and Gallstones: Are Bananas Good for Your Gallbladder?"
    desc = "Yes, bananas are one of the best fruits for gallstones: almost no fat, gentle fibre and easy to digest. How many to eat, the best ways to have them, and what to avoid."
    body = f"""
<p class="lede">If you have gallstones and want a snack you never need to worry about, reach for a banana. They're one of the safest foods on the whole list, and they're on our gentle "flare-day" list too.</p>
{verdict("green", "Green: choose often", "Yes, bananas are one of the safest fruits you can eat with gallstones.",
         [("Fat per medium banana:", "about 0.4g"), ("Fibre:", "about 3g"), ("Good on flare days:", "yes")], "banana", "Two ripe bananas")}

<h2>Why bananas are so gallbladder-friendly</h2>
<p>The main thing that sets off gallstone pain is a large, fatty meal. When fat reaches your gut, your gallbladder squeezes out bile to help digest it, and if a stone is in the way, that squeeze hurts. A medium banana has well under half a gram of fat, so it asks almost nothing of your gallbladder.</p>
<p>Bananas bring three other things to the table:</p>
<ul>
  <li><b>Gentle fibre.</b> About 3g per banana, much of it soluble fibre, which is kind to a sensitive gut. A high-fibre diet is part of the standard NHS advice for gallstones.</li>
  <li><b>Easy digestion.</b> A ripe banana is soft, mild and filling. That's why it's a staple of bland diets for upset stomachs.</li>
  <li><b>Potassium.</b> Useful if you've been sick and need to top up what you've lost.</li>
</ul>

{ad_slot()}

<h2>Ripe or green: does it matter?</h2>
<p>For most people, a ripe banana (yellow, with a few brown freckles) is the better choice when your gallbladder is playing up. As a banana ripens, its starch turns to natural sugar and it gets softer and easier to digest.</p>
<p>Greener bananas contain more resistant starch. That's good for gut bacteria, but it can cause wind and bloating in some people. If you're already uncomfortable, that's the last thing you need. Save green bananas for good days.</p>

<h2>The best ways to eat bananas with gallstones</h2>
<ul>
  <li><b>On its own,</b> as a snack between meals. Eating little and often keeps your gallbladder emptying gently.</li>
  <li><b>Sliced on porridge</b> made with water or skimmed milk. This is one of the best breakfasts you can have on a bad day.</li>
  <li><b>With fat-free Greek yoghurt</b> and a sprinkle of oats.</li>
  <li><b>In a homemade smoothie</b> with skimmed milk and a handful of berries.</li>
  <li><b>Frozen and blended</b> into "nice cream": a creamy dessert with none of the fat of real ice cream.</li>
  <li><b>Mashed on toast</b> instead of butter.</li>
</ul>

<h2>Banana foods to be careful with</h2>
<p>The banana is never the problem. What gets added to it can be.</p>
<div class="table-wrap"><table>
  <thead><tr><th>Food</th><th>Verdict</th><th>Why</th></tr></thead>
  <tbody>
    <tr><td>Fresh banana</td><td><span class="tag green">Green</span></td><td>Almost no fat</td></tr>
    <tr><td>Homemade banana smoothie (skimmed milk)</td><td><span class="tag green">Green</span></td><td>Low fat, filling</td></tr>
    <tr><td>Banana with a small spoon of peanut butter</td><td><span class="tag amber">Amber</span></td><td>Peanut butter is about half fat; keep it to a teaspoon or two</td></tr>
    <tr><td>Dried banana chips</td><td><span class="tag amber">Amber</span></td><td>Usually fried in coconut or palm oil, so much higher in fat than fresh banana</td></tr>
    <tr><td>Banana bread or muffins</td><td><span class="tag amber">Amber</span></td><td>Often made with lots of butter or oil</td></tr>
    <tr><td>Banoffee pie, banana fritters, banana split</td><td><span class="tag red">Red</span></td><td>Cream, toffee, batter, frying or ice cream</td></tr>
  </tbody>
</table></div>

<h2>What about bananas and blood sugar?</h2>
<p>Bananas contain natural sugar, so if you have diabetes (which is more common in people with gallstones), pair your banana with some protein, such as fat-free yoghurt, or choose a smaller, less ripe one. One a day fits comfortably into most diets. Ask your diabetes team if you're unsure.</p>

<h2>The bottom line</h2>
<p>Bananas are cheap, easy and about as gallbladder-friendly as food gets. Keep a bunch in the fruit bowl, and when you're not sure what's safe to eat, a banana is always a good answer.</p>
"""
    return food_page(path, "Bananas and Gallstones: Are Bananas Good for Your Gallbladder?", h1, desc, body, BANANA_FAQ,
                     [CUH_DIET, NHS_SYMPTOMS, USDA])


# ---------------------------------------------------------------- ALCOHOL
ALCOHOL_FAQ = [
    ("Can I drink alcohol with gallstones?",
     "Many people with gallstones can have a small amount of alcohol without problems, especially spirits or wine with a low-fat meal. Avoid it during a flare-up, if you've ever had pancreatitis, or if your doctor has told you not to drink."),
    ("Does alcohol cause gallstones?",
     "Not in the usual sense. Studies of large groups have actually linked moderate drinking with fewer gallstones, but genetic research suggests ordinary drinking doesn't cause or prevent them. Heavy drinking is harmful in many other ways, including to your liver and pancreas."),
    ("Can alcohol trigger a gallbladder attack?",
     "The drink itself is rarely the main trigger. The fatty food that often comes with it (a takeaway, pub food or a fry-up the next morning) is far more likely to cause an attack. Creamy drinks like cream liqueurs are an exception."),
    ("Is red wine good for gallstones?",
     "There's no good evidence that red wine helps gallstones. It contains no fat, so a small glass with a light meal is fine for many people, but don't start drinking for health reasons."),
    ("Is beer bad for gallstones?",
     "Beer and lager contain no fat. The problems are the volume, which can leave you bloated, and the snacks that go with it. A single drink is usually fine; several pints with crisps and a kebab is a different story."),
    ("Can I drink alcohol while waiting for gallbladder surgery?",
     "Ask your surgical team. Many advise cutting down or stopping in the weeks before an operation. If you've had pancreatitis caused by gallstones, you'll usually be told to avoid alcohol completely."),
]


def alcohol():
    path = "alcohol-and-gallstones/"
    h1 = "Alcohol and Gallstones: Can You Drink with Gallstones?"
    desc = "Can you drink alcohol with gallstones? What the research really says, which drinks are safest, which to avoid, and when to stop drinking completely."
    body = f"""
<p class="lede">It's one of the first things people ask after a gallstones diagnosis, usually with a weekend, a wedding or Christmas in mind. The honest answer is more reassuring than you might expect, with some important exceptions.</p>
{verdict("amber", "Amber: small amounts, with care", "A small drink is fine for many people. Avoid alcohol during flare-ups or if you've had pancreatitis.",
         [("Fat in wine, beer and spirits:", "none"), ("UK low-risk limit:", "14 units a week"), ("Flare days:", "avoid")])}

<h2>What the research says</h2>
<p>This is where it gets interesting. A 2022 review that pooled studies from around the world found that people who drink moderately are <em>less</em> likely to develop gallstones than people who don't drink. The pattern held for beer, wine and spirits.</p>
<p>Before you pour a celebratory glass, there's a catch. The same researchers then used genetic data, a method that's better at telling cause from coincidence, and found no sign that ordinary drinking actually protects against gallstones. Problem drinking, on the other hand, was linked with slightly <em>more</em> gallstones.</p>
<p>So the fair summary is this: moderate drinking doesn't seem to cause gallstones, but it doesn't treat or prevent them either. Nobody should start drinking because of their gallbladder.</p>

<h2>The real risk: alcohol, gallstones and your pancreas</h2>
<p>This is the part most websites skip. According to the NHS, gallstones and alcohol are the two main causes of acute pancreatitis, a painful and sometimes serious inflammation of the pancreas. A stone that slips out of the gallbladder can block the duct the pancreas shares, and heavy drinking puts extra strain on the pancreas too.</p>
<p>If you have gallstones, you already have one of the two big risk factors. That's a good reason to keep drinking well within the UK low-risk guideline of no more than 14 units a week, spread over three or more days. And if you've ever had pancreatitis, you'll normally be advised not to drink at all.</p>

{ad_slot()}

<h2>Which drinks are best and worst with gallstones?</h2>
<p>Most alcoholic drinks contain no fat at all, so they don't directly ask your gallbladder to work. The differences come from cream, coconut, sugar and sheer volume.</p>
<div class="table-wrap"><table>
  <thead><tr><th>Drink</th><th>Verdict</th><th>What to know</th></tr></thead>
  <tbody>
    <tr><td>Spirits with a slimline or diet mixer</td><td><span class="tag amber">Amber</span></td><td>No fat, small volume. Keep measures single.</td></tr>
    <tr><td>Dry white, red or rosé wine</td><td><span class="tag amber">Amber</span></td><td>No fat. A small (125ml) glass is about 1.5 units.</td></tr>
    <tr><td>Beer, lager and cider</td><td><span class="tag amber">Amber</span></td><td>No fat, but large volumes can leave you bloated and uncomfortable.</td></tr>
    <tr><td>Prosecco and sparkling wine</td><td><span class="tag amber">Amber</span></td><td>No fat, though the bubbles bother some people.</td></tr>
    <tr><td>Cream liqueurs (Irish cream and similar)</td><td><span class="tag red">Red</span></td><td>Made with real cream, so they're high in fat.</td></tr>
    <tr><td>Creamy cocktails (piña colada, White Russian, eggnog)</td><td><span class="tag red">Red</span></td><td>Coconut cream, cream or egg yolk push the fat right up.</td></tr>
  </tbody>
</table></div>

<h2>It's usually the food, not the drink</h2>
<p>Think about what normally goes with a night out: crisps and nuts at the bar, a takeaway on the way home, a full English the next morning. Those are exactly the large, fatty meals most likely to set off a gallbladder attack.</p>
<p>If you're going to drink, a few simple habits make a big difference:</p>
<ul>
  <li><b>Eat a light, low-fat meal first,</b> such as grilled chicken with rice or a jacket potato with beans.</li>
  <li><b>Alternate every drink with a glass of water.</b></li>
  <li><b>Plan the late-night food.</b> Skip the kebab and chips; have toast or a bowl of cereal with skimmed milk at home.</li>
  <li><b>Choose a lighter breakfast</b> the next day: poached eggs on toast instead of a fry-up.</li>
  <li><b>Check your medicines.</b> Some painkillers used for gallstone pain, such as codeine, shouldn't be mixed with alcohol. Ask your pharmacist.</li>
</ul>

<h2>When to avoid alcohol completely</h2>
<ul>
  <li>During a flare-up or while you're still sore from a recent attack</li>
  <li>If you've ever had pancreatitis</li>
  <li>If you have yellowing of the skin or eyes, or any liver problem</li>
  <li>In the run-up to surgery, if your team has advised it</li>
  <li>If your medicines say not to drink</li>
</ul>

<h2>The bottom line</h2>
<p>You don't have to become teetotal because you have gallstones. A single drink with a light meal is fine for many people. Keep within 14 units a week, skip the creamy drinks, and be strict about the food that comes with drinking. If you've had pancreatitis, alcohol is off the table.</p>
"""
    return food_page(path, "Alcohol and Gallstones: Can You Drink with Gallstones? (UK Guide)", h1, desc, body, ALCOHOL_FAQ,
                     [BAI_2022, NHS_PANCREATITIS, NHS_UNITS, NHS_SYMPTOMS])


# ---------------------------------------------------------------- EGGS
EGG_FAQ = [
    ("Are eggs bad for gallstones?",
     "Not usually. Egg whites are almost fat-free and are a great protein for people with gallstones. Whole eggs are fine for many people in sensible amounts, cooked without extra fat. The yolk holds nearly all the fat, so it's the part that may bother some people."),
    ("How many eggs can I eat a day with gallstones?",
     "Most people do well with one whole egg at a time, or one whole egg plus extra whites if you want a bigger portion. Avoid big plates of eggs, and keep fried eggs for occasional treats."),
    ("Can I eat eggs during a gallbladder flare-up?",
     "Stick to egg whites during a flare-up, or skip eggs until you feel better. When you bring whole eggs back, start with one boiled or poached egg and see how you feel."),
    ("Are boiled eggs OK with gallstones?",
     "Yes. Boiling and poaching add no extra fat, so they're the best ways to cook eggs. Fried eggs, scrambled eggs made with butter or cream, and quiche are higher in fat."),
    ("Does cholesterol in eggs cause gallstones?",
     "Most gallstones are made mainly of cholesterol, so it's a fair question. But most of the cholesterol in your bile is made by your own liver, and the evidence linking egg-eating to new gallstones is mixed. Overall weight, fibre intake and meal pattern matter more."),
    ("Is mayonnaise OK with gallstones?",
     "Regular mayonnaise is mostly oil and egg yolk, so it's high in fat. Use light mayonnaise sparingly, or swap in fat-free yoghurt with a squeeze of lemon."),
]


def eggs():
    path = "eggs-and-gallstones/"
    h1 = "Eggs and Gallstones: Can You Eat Eggs with Gallstones?"
    desc = "Can you eat eggs with gallstones? Why egg whites are a green-light food, how many whole eggs are sensible, and the best and worst ways to cook them."
    body = f"""
<p class="lede">Eggs get mixed reviews in gallstone circles. Some people eat them every day without a twinge; others swear a fried egg sets them off. Both can be true, and the reason comes down to one part of the egg.</p>
{verdict("amber", "Amber: whole eggs · Green: egg whites", "Yes, most people can eat eggs. Egg whites are almost fat-free; keep whole eggs to one at a time.",
         [("Fat in a large egg:", "about 5g"), ("Fat in the white:", "almost none"), ("Flare days:", "whites only")])}

<h2>It's all about the yolk</h2>
<p>A large egg has about 5 grams of fat, and almost every bit of it is in the yolk. The white is nearly pure protein with practically no fat at all.</p>
<p>That matters because fat is what makes your gallbladder squeeze. One yolk on its own is a modest amount of fat. Two or three fried eggs, with butter on the toast and a sausage on the side, is a big fatty meal, and that's when trouble starts.</p>
<div class="table-wrap"><table>
  <thead><tr><th>Part of the egg (large)</th><th>Fat</th><th>Protein</th><th>Verdict</th></tr></thead>
  <tbody>
    <tr><td>Whole egg</td><td class="num">about 5g</td><td class="num">about 6g</td><td><span class="tag amber">Amber</span></td></tr>
    <tr><td>Yolk only</td><td class="num">about 4.5g</td><td class="num">about 2.7g</td><td><span class="tag amber">Amber</span></td></tr>
    <tr><td>White only</td><td class="num">under 0.1g</td><td class="num">about 3.6g</td><td><span class="tag green">Green</span></td></tr>
  </tbody>
</table></div>
<p>Eggs are also on the protein list in NHS hospital dietary advice for gallstones. They're cheap, filling and quick to cook, so it's worth finding the version that suits you rather than cutting them out.</p>

{ad_slot()}

<h2>How you cook them changes everything</h2>
<p>The same egg can be a light meal or a heavy one depending on the pan.</p>
<div class="table-wrap"><table>
  <thead><tr><th>Egg dish</th><th>Verdict</th><th>Why</th></tr></thead>
  <tbody>
    <tr><td>Egg-white omelette with vegetables</td><td><span class="tag green">Green</span></td><td>High protein, almost no fat</td></tr>
    <tr><td>Poached or boiled egg</td><td><span class="tag amber">Amber</span></td><td>No added fat; just the yolk's own</td></tr>
    <tr><td>Scrambled egg, cooked in a non-stick pan with skimmed milk</td><td><span class="tag amber">Amber</span></td><td>Fine in small portions</td></tr>
    <tr><td>Fried egg</td><td><span class="tag red">Red</span></td><td>Soaks up oil or butter on top of the yolk's fat</td></tr>
    <tr><td>Scrambled egg with butter or cream</td><td><span class="tag red">Red</span></td><td>Adds a lot of dairy fat</td></tr>
    <tr><td>Quiche, Scotch eggs, egg mayonnaise</td><td><span class="tag red">Red</span></td><td>Pastry, sausage meat, frying or mayonnaise</td></tr>
  </tbody>
</table></div>

<h2>Easy egg swaps</h2>
<ul>
  <li><b>Two-and-one omelette:</b> one whole egg plus two whites gives you a big, satisfying omelette with the fat of a single egg.</li>
  <li><b>Cartons of liquid egg white</b> from the supermarket chiller make egg-white omelettes and scrambles quick.</li>
  <li><b>Poached eggs on wholemeal toast,</b> with no butter, instead of a fry-up.</li>
  <li><b>Egg-white "mayo" sandwiches:</b> chopped boiled egg white mixed with fat-free yoghurt, chives and black pepper.</li>
  <li><b>Use a non-stick pan</b> or a few sprays of oil, rather than a knob of butter.</li>
</ul>

<h2>What about cholesterol?</h2>
<p>Most gallstones in the UK are made mainly of cholesterol, so it's natural to wonder whether cholesterol-rich egg yolks are a problem. The picture is less simple than it sounds. Your liver makes most of the cholesterol in your bile, and studies looking at egg-eating and new gallstones haven't given a clear answer. Things like your weight, how much fibre you eat and your meal pattern have a stronger effect.</p>
<p>The practical advice stays the same: enjoy eggs in modest amounts, and lean on the whites when you want more protein.</p>

<h2>Are eggs a common trigger?</h2>
<p>Some people find that eggs, especially fried eggs or rich yolks, bring on discomfort, even when other fatty foods don't. Everyone's tolerance is different. If you suspect eggs, try a week of egg whites only, then bring back one boiled whole egg and see how you feel. A simple food diary makes the pattern much easier to spot.</p>

<h2>The bottom line</h2>
<p>You don't need to give up eggs. Egg whites are a green-light food you can eat freely. Whole eggs are fine for most people one at a time, boiled or poached. Save fried eggs and creamy scrambled eggs for occasional treats, and stick to whites on bad days.</p>
"""
    return food_page(path, "Eggs and Gallstones: Can You Eat Eggs with Gallstones?", h1, desc, body, EGG_FAQ,
                     [CUH_DIET, NHS_SYMPTOMS, USDA])


# ---------------------------------------------------------------- FOODS TO AVOID (pillar)
AVOID_FAQ = [
    ("What foods trigger gallbladder attacks?",
     "The most common triggers are large meals that are high in fat: fried food, takeaways, fatty and processed meat, full-fat dairy such as cheese, cream and butter, pastries and creamy sauces. Everyone's triggers are a little different, so a food diary helps you find yours."),
    ("Do I have to avoid fat completely with gallstones?",
     "No. NHS dietitians say a strict low-fat diet isn't needed for everyone. Small amounts of healthy fats, such as a teaspoon of olive oil or a small handful of nuts, are part of a balanced diet. It's large amounts of fat in one meal that cause most problems."),
    ("Is milk bad for gallstones?",
     "Whole milk is a higher-fat food, so it's best limited. Skimmed and 1% milk are low in fat and are fine for most people. See our full guide to milk and gallstones."),
    ("Can I eat cheese with gallstones?",
     "Most hard cheeses are around a third fat, so keep portions small. Cottage cheese, quark and reduced-fat cheeses are much lighter options. See our full guide to cheese and gallstones."),
    ("Are eggs on the list of foods to avoid?",
     "Not for most people. Egg whites are almost fat-free. Whole eggs are fine one at a time, boiled or poached. Fried eggs are the version to limit."),
    ("Should I avoid spicy food with gallstones?",
     "Spicy food isn't a direct gallstone trigger, but it can upset a sensitive stomach and is often served in rich, oily dishes like curries. Choose tomato-based dishes over creamy ones and see how you get on."),
    ("Is chocolate bad for gallstones?",
     "Most chocolate is around 30% fat, so a whole bar counts as a fatty snack. A couple of squares of dark chocolate is usually fine. Chocolate cake, cream-filled bars and chocolate mousse are better kept as rare treats."),
]

AVOID_ITEMS = [
    ("fried", "Fried food", "Chips, fried chicken, battered fish, onion rings, doughnuts.", "fried-food-and-gallstones/"),
    ("low-fat-dairy", "Whole milk", "Full-fat milk in tea, cereal, milkshakes and lattes adds up.", "milk-and-gallstones/"),
    ("cheese", "Full-fat cheese", "Cheddar, brie and halloumi are around a third fat.", "cheese-and-gallstones/"),
    ("fatty-meat", "Fatty and processed meat", "Bacon, sausages, salami, pepperoni, ribs, fatty mince.", None),
    ("full-fat-dairy", "Cream, butter and ice cream", "Some of the most concentrated fat in the kitchen.", None),
    ("fast-food", "Takeaways and fast food", "Burgers, pizza, kebabs, curries with creamy sauces.", None),
    ("sugary", "Pastries, cakes and biscuits", "Butter and sugar together: croissants, pies, muffins.", None),
    ("plate", "Big, heavy meals", "Even healthy food in a huge portion can trigger pain.", None),
]


def avoid_grid(root, items=AVOID_ITEMS, link=True):
    out = []
    for img, name, text, href in items:
        inner = f'{food_img(root, img, name, "avoid-pic")}<div><strong>{esc(name)}</strong><span>{esc(text)}</span></div>'
        if href and link:
            out.append(f'<a class="avoid-card" href="{root}{href}">{inner}<em>Read the guide &rarr;</em></a>')
        else:
            cls = "avoid-card portion" if img == "plate" else "avoid-card"
            out.append(f'<div class="{cls}">{inner}</div>')
    return '<div class="avoid-grid">' + "".join(out) + "</div>"


def foods_to_avoid():
    root = "../"
    path = "foods-to-avoid-with-gallstones/"
    h1 = "Foods to Avoid with Gallstones: The Complete List"
    desc = "The foods most likely to trigger gallstone pain, from fried food and fatty meat to whole milk and cheese, why they cause problems, and what to eat instead."
    body = f"""
<p class="lede">If you've just been told you have gallstones, this is the list to start with. These are the foods most likely to bring on pain, and for every one of them there's an easy swap that lets you keep enjoying your meals.</p>

<h2>The foods to avoid at a glance</h2>
<p>All of these have one thing in common: a lot of fat in one go. Tap a food for its full guide.</p>
{avoid_grid(root)}

{ad_slot()}

<h2>Why these foods cause gallstone pain</h2>
<p>Your gallbladder is a small pouch under your liver that stores bile, a fluid that helps you digest fat. When fat arrives in your gut, your body releases a hormone called cholecystokinin (CCK), which tells the gallbladder to squeeze bile out.</p>
<p>If a gallstone is sitting near the exit, that squeeze can press the stone against the opening or push it into the duct. That's what causes the sudden, severe pain in the upper right or middle of your tummy, known as biliary colic. The more fat in a meal, the stronger the squeeze. That's why a fry-up or a takeaway is far more likely to cause an attack than a bowl of porridge.</p>

<h2>1. Fried food</h2>
{food_img(root, "fried", "Chips in a red carton", "inline-pic")}
<p>Frying soaks food in oil. A plain boiled potato has almost no fat; the same potato as chip-shop chips can carry a meal's worth. Battered fish, fried chicken, onion rings, spring rolls, samosas and doughnuts all fall into this group.</p>
<p><b>Swap it:</b> oven-baked or air-fried chips with a teaspoon of oil, grilled fish, breadcrumbed chicken baked in the oven. <a href="{root}fried-food-and-gallstones/">Read the full guide to fried food and gallstones</a>.</p>

<h2>2. Whole milk and full-fat dairy</h2>
{food_img(root, "full-fat-dairy", "Cheese and an ice cream sundae", "inline-pic")}
<p>Dairy fat is one of the most common hidden triggers because it turns up in so many everyday things: milk in tea and coffee, cheese in sandwiches, butter on toast, cream in sauces. Whole milk, cream, butter, ice cream and most hard and soft cheeses are all high in fat.</p>
<p><b>Swap it:</b> skimmed or 1% milk, fat-free Greek yoghurt, cottage cheese or quark, and a thin scrape of spread instead of butter. See our guides to <a href="{root}milk-and-gallstones/">milk</a> and <a href="{root}cheese-and-gallstones/">cheese</a>.</p>

<h2>3. Fatty and processed meat</h2>
{food_img(root, "fatty-meat", "Bacon and a steak", "inline-pic")}
<p>Bacon, sausages, burgers, salami, pepperoni, chorizo, pork pies, ribs, lamb chops and fatty mince are all high in saturated fat. Processed meats are often fried as well, which doubles up the problem.</p>
<p><b>Swap it:</b> skinless chicken or turkey, lean ham, 5%-fat mince, white fish, beans and lentils. Trim any visible fat before cooking.</p>

<h2>4. Takeaways and fast food</h2>
{food_img(root, "fast-food", "A burger and a slice of pizza", "inline-pic")}
<p>A burger and fries, a large pizza, a kebab or a creamy curry with pilau rice and naan can each carry more fat than you'd normally eat in a whole day. Takeaways are one of the most common triggers people report, often late in the evening.</p>
<p><b>Swap it:</b> a tomato-based curry with boiled rice, a thin-crust pizza with vegetable toppings and half the cheese, a grilled chicken wrap, or sushi.</p>

<h2>5. Pastries, cakes and biscuits</h2>
{food_img(root, "sugary", "A doughnut and a muffin", "inline-pic")}
<p>Croissants, pain au chocolat, sausage rolls, pies, cream cakes, muffins and many biscuits are made with lots of butter or other fat. Because they're sweet or snack-sized, it's easy to forget how rich they are.</p>
<p><b>Swap it:</b> a toasted teacake or crumpet with jam, malt loaf, a meringue with berries, or fruit with fat-free yoghurt.</p>

<h2>6. Creamy sauces, gravies and soups</h2>
<p>Carbonara, korma, cheese sauce, hollandaise, creamy mushroom soup and meat gravy made from the roasting fat can turn a light meal into a heavy one.</p>
<p><b>Swap it:</b> tomato-based pasta sauces, stock-based gravy, broth-based soups and a squeeze of lemon or herbs for flavour.</p>

<h2>7. Big, heavy meals</h2>
{food_img(root, "plate", "A balanced plate with chicken and vegetables", "inline-pic")}
<p>Portion size matters as much as the food itself. A huge Sunday roast or an all-you-can-eat buffet asks your gallbladder to work hard all at once, even if each item is fairly healthy.</p>
<p><b>Swap it:</b> eat smaller meals more often. Three modest meals and one or two light snacks suit most people well.</p>

<h2>Foods that sound healthy but can catch you out</h2>
<div class="table-wrap"><table>
  <thead><tr><th>Food</th><th>Why it catches people out</th></tr></thead>
  <tbody>
    <tr><td>Granola</td><td>Often baked with oil and nuts; can be much higher in fat than plain oats</td></tr>
    <tr><td>Coleslaw and potato salad</td><td>Mostly mayonnaise</td></tr>
    <tr><td>Avocado</td><td>Healthy fat, but a whole one is a lot; stick to a quarter</td></tr>
    <tr><td>Nuts and nut butter</td><td>Good for you in small amounts, but about half fat</td></tr>
    <tr><td>Coffee-shop lattes</td><td>A large one made with whole milk adds more fat than you'd guess</td></tr>
    <tr><td>Ready meals labelled "light"</td><td>Still check the fat per 100g on the label</td></tr>
  </tbody>
</table></div>

<h2>What you can still eat</h2>
<p>Plenty. Fruit, vegetables, oats, rice, pasta, potatoes (not fried), bread, beans and lentils, skinless chicken and turkey, white fish, egg whites, and skimmed or 1% milk are all gallbladder-friendly. Our <a href="{root}gallstones-diet/">complete gallstones diet guide</a> has the full green, amber and red list, and a gentle menu for flare-up days.</p>

<h2>The bottom line</h2>
<p>You don't need to give up fat completely. Avoid the big hitters (fried food, fatty meat, takeaways, cream, butter and full-fat cheese), keep portions modest, and spread what fat you do eat across the day. Most people find their attacks become much less frequent once they do.</p>
"""
    return food_page(path, "Foods to Avoid with Gallstones: The Complete UK List", h1, desc, body, AVOID_FAQ,
                     [CUH_DIET, NHS_SYMPTOMS, ("NHS: Gallstones causes", "https://www.nhs.uk/conditions/gallstones/prevention/")],
                     strip="Want this whole list on your fridge door, with the safe swaps?")


# ---------------------------------------------------------------- FRIED FOOD
FRIED_FAQ = [
    ("Why does fried food cause gallbladder pain?",
     "Fried food is soaked in oil, so it's very high in fat. Fat tells your gallbladder to squeeze out bile, and if a gallstone is in the way, that squeeze can cause pain. The more fat in one meal, the stronger the squeeze."),
    ("Is air-fried food OK with gallstones?",
     "Usually, yes. An air fryer uses a teaspoon of oil or none at all, so air-fried chips or chicken have a fraction of the fat of deep-fried versions. Watch out for frozen foods that are already coated in oil or batter."),
    ("Can I eat fish and chips with gallstones?",
     "A full portion from the chip shop is one of the most common triggers. If you really fancy it, share a portion, choose a smaller size, or make a home version with oven-baked breadcrumbed fish and oven chips."),
    ("Are oven chips better than chip-shop chips?",
     "Yes. Oven chips are usually much lower in fat than chips deep-fried in a chip shop or takeaway. Check the pack and choose thicker, straight-cut chips, which absorb less oil than thin fries or crinkle cuts."),
    ("Is stir-frying OK?",
     "A stir-fry made with a teaspoon or two of oil is fine for most people, and it's a great way to eat more vegetables. It's deep-frying and shallow-frying in a lot of oil that cause problems."),
    ("How long after eating fried food does gallbladder pain start?",
     "Pain often begins within an hour or so of a fatty meal, and sometimes later in the evening or at night. If pain lasts longer than 30 minutes, get urgent advice from your GP or NHS 111."),
]


def fried_food():
    root = "../"
    path = "fried-food-and-gallstones/"
    h1 = "Fried Food and Gallstones: Why It Triggers Pain and What to Eat Instead"
    desc = "Fried food is the number one trigger for gallstone pain. Why it causes attacks, which fried foods are worst, and easy swaps like air frying and oven baking."
    body = f"""
<p class="lede">Ask anyone with gallstones what set off their first attack, and fried food comes up again and again. It's the single most common trigger, and the good news is that it's also one of the easiest to work around.</p>
{verdict("red", "Red: limit or avoid", "Fried food is the most common trigger for gallstone pain. Bake, grill or air-fry instead.",
         [("Deep-fried:", "avoid"), ("Air-fried or oven-baked:", "usually fine"), ("Flare days:", "avoid")], "fried", "Chips in a red carton")}

<h2>Why fried food is so hard on your gallbladder</h2>
<p>When food is fried, it soaks up oil. Batter and breadcrumbs soak up even more. A plain boiled potato has almost no fat at all, but turn it into chip-shop chips and it can carry as much fat as a whole meal should.</p>
<p>When that fat reaches your gut, your body releases a hormone called cholecystokinin (CCK). It tells your gallbladder to squeeze hard and push out bile to break the fat down. If a stone is sitting near the exit, that squeeze can press it against the opening or into the duct, and that's when the pain starts. More fat means a harder squeeze, which is why a fried meal is so much more likely to cause an attack than a lighter one.</p>

{ad_slot()}

<h2>The worst fried foods for gallstones</h2>
<div class="table-wrap"><table>
  <thead><tr><th>Food</th><th>Verdict</th><th>Why</th></tr></thead>
  <tbody>
    <tr><td>Fish and chips from the chip shop</td><td><span class="tag red">Red</span></td><td>Battered fish and deep-fried chips together</td></tr>
    <tr><td>Fried chicken and chicken nuggets</td><td><span class="tag red">Red</span></td><td>Skin plus coating, deep-fried</td></tr>
    <tr><td>Full English breakfast (fried)</td><td><span class="tag red">Red</span></td><td>Fried eggs, bacon, sausages and fried bread in one sitting</td></tr>
    <tr><td>Onion rings, spring rolls, samosas, bhajis</td><td><span class="tag red">Red</span></td><td>Batter or pastry, deep-fried</td></tr>
    <tr><td>Doughnuts</td><td><span class="tag red">Red</span></td><td>Deep-fried dough, often filled with cream</td></tr>
    <tr><td>Crisps</td><td><span class="tag amber">Amber</span></td><td>Fried, but a small bag is a modest amount. Baked crisps are lighter.</td></tr>
    <tr><td>Stir-fry with a teaspoon of oil</td><td><span class="tag green">Green</span></td><td>Very little oil, lots of vegetables</td></tr>
  </tbody>
</table></div>

<h2>Swaps that keep the crunch</h2>
<p>You don't need to give up the foods you love. Changing how you cook them makes the biggest difference.</p>
<div class="swap-grid">
  <div class="swap">{food_img(root, "fried", "Chips", "swap-pic")}<div><b>Chip-shop chips</b><span>&rarr; Oven chips or air-fried potato wedges with a teaspoon of oil</span></div></div>
  <div class="swap">{food_img(root, "white-fish", "White fish", "swap-pic")}<div><b>Battered fish</b><span>&rarr; Oven-baked fish with a breadcrumb and lemon crust</span></div></div>
  <div class="swap">{food_img(root, "lean-protein", "Grilled chicken breast", "swap-pic")}<div><b>Fried chicken</b><span>&rarr; Skinless chicken in seasoned breadcrumbs, baked or air-fried</span></div></div>
  <div class="swap">{food_img(root, "toast", "Toast", "swap-pic")}<div><b>Fried breakfast</b><span>&rarr; Poached egg, grilled tomatoes, mushrooms and wholemeal toast</span></div></div>
</div>

<h2>Is an air fryer worth it with gallstones?</h2>
<p>For a lot of people, yes. An air fryer is a small fan oven: it crisps food with hot air instead of a pan of oil. Most things need a light spray or a teaspoon of oil, and some need none at all. Chips, potato wedges, breaded chicken, fish fillets and roasted vegetables all come out crisp with a fraction of the fat.</p>
<p>One thing to watch: frozen chips, nuggets and fish fingers are often part-fried before they're frozen. Check the fat per 100g on the pack, and choose the products with green or amber labels.</p>

<h2>Better ways to cook</h2>
<ul>
  <li><b>Grill</b> meat and fish on a rack so the fat drips away.</li>
  <li><b>Bake or roast</b> on baking paper with a few sprays of oil instead of a pool of it.</li>
  <li><b>Poach or steam</b> fish, chicken and eggs.</li>
  <li><b>Stir-fry</b> in a non-stick pan or wok with a teaspoon of oil and a splash of water or stock.</li>
  <li><b>Microwave</b> vegetables and fish; it's quick and needs no fat at all.</li>
</ul>

<h2>Eating out</h2>
<p>Restaurants and takeaways fry far more than most people realise. A few questions help: ask for food grilled instead of fried, choose boiled rice or a jacket potato instead of chips, have sauces on the side, and look for words like "grilled", "steamed", "baked" or "tandoori" on the menu. Avoid "crispy", "battered", "tempura", "golden" and "pan-fried".</p>

<h2>The bottom line</h2>
<p>Fried food is the trigger most worth cutting back on. You don't have to give up chips, chicken or fish; just cook them in the oven, under the grill or in an air fryer. It's one change that makes a real difference for most people with gallstones.</p>
"""
    return food_page(path, "Fried Food and Gallstones: Why It Triggers Pain (and Easy Swaps)", h1, desc, body, FRIED_FAQ,
                     [CUH_DIET, NHS_SYMPTOMS], strip="Get the printable list of fried foods to avoid, and the safe swaps.")


# ---------------------------------------------------------------- MILK
MILK_FAQ = [
    ("Is milk bad for gallstones?",
     "Whole milk is higher in fat, so it's best limited, especially in large amounts. Skimmed and 1% milk are low in fat and suit most people with gallstones well."),
    ("Which milk is best for gallstones?",
     "Skimmed milk has the least fat, with almost none per glass. 1% milk is a good middle ground if you find skimmed too thin. Unsweetened plant milks such as almond, oat or soya are also low in fat."),
    ("Can I have milk in my tea and coffee?",
     "Yes. A splash of semi-skimmed in a cup of tea is a very small amount of fat. It's large milky drinks made with whole milk, like a big latte or hot chocolate, that add up."),
    ("Is milk OK during a gallbladder flare-up?",
     "Skimmed milk is usually fine in small amounts, for example on porridge. Avoid whole milk, milkshakes and creamy drinks until you feel better."),
    ("Is lactose a problem with gallstones?",
     "Lactose doesn't affect gallstones. But lactose intolerance can cause bloating and tummy pain, which can be confused with gallbladder symptoms. If you notice symptoms with all milk, including skimmed, mention it to your GP."),
    ("Is coconut milk OK with gallstones?",
     "It depends which kind. The coconut milk drink sold in cartons next to other plant milks is low in fat. Tinned coconut milk used in cooking is very high in fat, so swap it for reduced-fat coconut milk or a tomato-based sauce."),
]


def milk():
    root = "../"
    path = "milk-and-gallstones/"
    h1 = "Milk and Gallstones: Which Milk Is Best for Your Gallbladder?"
    desc = "Is milk bad for gallstones? Whole vs semi-skimmed vs skimmed vs plant milks compared, how much is fine in tea and coffee, and the milky drinks to watch."
    body = f"""
<p class="lede">Milk is in almost everything: your morning tea, your cereal, your coffee, your sauces. If you have gallstones, the type of milk you buy can quietly make a big difference to how much fat you eat every day.</p>
{verdict("amber", "Whole milk: limit · Skimmed and 1%: choose", "Switch to skimmed or 1% milk. Keep whole milk, cream and milkshakes for rare treats.",
         [("Whole milk, 200ml glass:", "about 7g fat"), ("Skimmed, 200ml glass:", "under 0.5g fat"), ("Flare days:", "skimmed only")], "low-fat-dairy", "A glass of milk")}

<h2>How much fat is in your milk?</h2>
<p>The difference between milks is bigger than most people think. A glass of whole milk has around twenty times the fat of the same glass of skimmed.</p>
<div class="table-wrap"><table>
  <thead><tr><th>Milk (UK)</th><th>Fat per 100ml</th><th>Fat per 200ml glass</th><th>Verdict</th></tr></thead>
  <tbody>
    <tr><td>Whole (blue top)</td><td class="num">about 3.6g</td><td class="num">about 7g</td><td><span class="tag red">Red</span></td></tr>
    <tr><td>Semi-skimmed (green top)</td><td class="num">about 1.7g</td><td class="num">about 3.5g</td><td><span class="tag amber">Amber</span></td></tr>
    <tr><td>1% (orange top)</td><td class="num">about 1g</td><td class="num">about 2g</td><td><span class="tag green">Green</span></td></tr>
    <tr><td>Skimmed (red top)</td><td class="num">about 0.1 to 0.3g</td><td class="num">under 0.5g</td><td><span class="tag green">Green</span></td></tr>
  </tbody>
</table></div>
<p>Check the label on your own brand, as figures vary a little.</p>

<h2>Why the type of milk matters</h2>
<p>Fat is what makes your gallbladder squeeze, and the squeeze is what causes pain when a stone is in the way. One splash of whole milk in your tea won't do much. But milk is something most of us have several times a day, so the fat adds up: two milky coffees, a bowl of cereal and a white sauce at dinner, all made with whole milk, is a fair amount of dairy fat before you've counted anything else.</p>
<p>Switching to skimmed or 1% is one of the easiest changes you can make. You keep the protein and calcium, and lose almost all the fat.</p>

{ad_slot()}

<h2>Milky drinks to watch</h2>
<div class="table-wrap"><table>
  <thead><tr><th>Drink</th><th>Verdict</th><th>Better choice</th></tr></thead>
  <tbody>
    <tr><td>Tea or coffee with a splash of milk</td><td><span class="tag green">Green</span></td><td>Fine with any milk; skimmed is lightest</td></tr>
    <tr><td>Large latte or cappuccino with whole milk</td><td><span class="tag amber">Amber</span></td><td>Ask for skimmed milk, or have a small size</td></tr>
    <tr><td>Hot chocolate with whipped cream</td><td><span class="tag red">Red</span></td><td>Skimmed milk, no cream</td></tr>
    <tr><td>Milkshakes</td><td><span class="tag red">Red</span></td><td>Homemade with skimmed milk, banana and berries</td></tr>
    <tr><td>Frappés and iced coffee-shop drinks</td><td><span class="tag red">Red</span></td><td>Iced americano or an iced latte with skimmed milk</td></tr>
  </tbody>
</table></div>

<h2>What about plant milks?</h2>
<p>Most unsweetened plant milks in cartons are low in fat, and many are fortified with calcium. Here's how they compare:</p>
<ul>
  <li><b>Almond milk (unsweetened):</b> about 1g of fat per 100ml. A light option.</li>
  <li><b>Oat milk:</b> about 1.5g per 100ml for standard versions. "Barista" versions often have added oil and can be closer to 3g, so check the label.</li>
  <li><b>Soya milk (unsweetened):</b> about 2g per 100ml, with more protein than other plant milks.</li>
  <li><b>Coconut milk drink (carton):</b> about 1g per 100ml. Very different from tinned coconut milk, which is high in fat.</li>
</ul>
<p>Choose versions with added calcium, and avoid sweetened or "creamy" versions if you're watching fat.</p>

<h2>Is milk OK during a flare-up?</h2>
<p>Many people tolerate skimmed milk well on bad days, for example on porridge or in a cup of tea. Avoid whole milk, cream, milkshakes and hot chocolate until you feel better. If milk seems to upset you even when it's skimmed, it may be worth asking your GP about lactose intolerance, which can cause similar bloating and tummy pain.</p>

<h2>The bottom line</h2>
<p>You don't need to give up milk. Swap whole milk for skimmed or 1%, ask for skimmed in coffee shops, and keep milkshakes and creamy hot chocolates as rare treats. It's one of the simplest changes you can make, and you'll barely notice it after a week or two.</p>
"""
    return food_page(path, "Milk and Gallstones: Is Milk Bad for Gallstones? (UK Guide)", h1, desc, body, MILK_FAQ,
                     [CUH_DIET, NHS_SYMPTOMS, USDA], strip="Get the printable list of dairy to choose and dairy to avoid.")


# ---------------------------------------------------------------- CHEESE
CHEESE_FAQ = [
    ("Can I eat cheese with gallstones?",
     "Yes, in small amounts. Most hard cheeses are about a third fat, so keep portions to around 30g, about the size of a small matchbox. Cottage cheese, quark and reduced-fat cheeses are much lighter choices."),
    ("What is the best cheese for gallstones?",
     "Quark and low-fat cottage cheese are the lightest options, with very little fat. Reduced-fat cheddar, half-fat mozzarella and light soft cheese are good middle-ground choices."),
    ("Is cottage cheese good for gallstones?",
     "Yes. Cottage cheese is high in protein and much lower in fat than other cheeses, especially the low-fat versions. It's a good swap for cheddar in sandwiches and on jacket potatoes."),
    ("Is cheese on toast OK with gallstones?",
     "A thin slice of reduced-fat cheese on toast, with no butter underneath, is fine for many people. A thick layer of full-fat cheddar on buttered toast is a much heavier snack."),
    ("Can I eat pizza with gallstones?",
     "Pizza is often a trigger because of the amount of cheese and fatty toppings like pepperoni. A thin-crust pizza with vegetable toppings and half the usual cheese is a lighter choice."),
    ("Is halloumi OK with gallstones?",
     "Halloumi is about a quarter fat, and it's usually fried, which adds more. Grill a small portion instead, or swap it for grilled tofu or chicken."),
]


def cheese():
    root = "../"
    path = "cheese-and-gallstones/"
    h1 = "Cheese and Gallstones: Which Cheeses Are Safe to Eat?"
    desc = "Can you eat cheese with gallstones? Fat in cheddar, brie, mozzarella, feta, cottage cheese and more compared, safe portion sizes, and the best lighter swaps."
    body = f"""
<p class="lede">Cheese is one of the foods people miss most after a gallstones diagnosis. You don't have to give it up, but it helps to know which cheeses are light, which are heavy, and how much is sensible.</p>
{verdict("amber", "Full-fat cheese: small amounts · Cottage cheese and quark: choose", "Keep full-fat cheese to a matchbox-sized portion. Choose cottage cheese, quark and reduced-fat cheeses more often.",
         [("Cheddar, 30g:", "about 10g fat"), ("Cottage cheese, 30g:", "about 1g fat"), ("Flare days:", "avoid most cheese")], "cheese", "A wedge of cheese")}

<h2>Why cheese can trigger gallstone pain</h2>
<p>Most hard cheeses are about one-third fat. That means a generous chunk of cheddar, a cheese sandwich made with thick slices, or a plate of cheesy pasta can deliver a lot of fat in one go. Fat is what makes your gallbladder squeeze, and if a stone is in the way, that squeeze can be painful.</p>
<p>The fix isn't cutting out cheese completely. It's choosing lighter cheeses most of the time and keeping full-fat cheese to small portions. A 30g portion of hard cheese, about the size of a small matchbox, is the standard serving size used in UK healthy-eating advice.</p>

{ad_slot()}

<h2>Cheese fat chart: lightest to heaviest</h2>
<div class="table-wrap"><table>
  <thead><tr><th>Cheese</th><th>Fat per 100g</th><th>Fat per 30g</th><th>Verdict</th></tr></thead>
  <tbody>
    <tr><td>Quark</td><td class="num">under 0.5g</td><td class="num">almost none</td><td><span class="tag green">Green</span></td></tr>
    <tr><td>Cottage cheese, low-fat</td><td class="num">about 1.5g</td><td class="num">under 0.5g</td><td><span class="tag green">Green</span></td></tr>
    <tr><td>Cottage cheese, standard</td><td class="num">about 4g</td><td class="num">about 1g</td><td><span class="tag green">Green</span></td></tr>
    <tr><td>Mozzarella, half-fat</td><td class="num">about 10g</td><td class="num">about 3g</td><td><span class="tag amber">Amber</span></td></tr>
    <tr><td>Feta</td><td class="num">about 20g</td><td class="num">about 6g</td><td><span class="tag amber">Amber</span></td></tr>
    <tr><td>Mozzarella, standard</td><td class="num">about 20g</td><td class="num">about 6g</td><td><span class="tag amber">Amber</span></td></tr>
    <tr><td>Reduced-fat cheddar</td><td class="num">about 22g</td><td class="num">about 6.5g</td><td><span class="tag amber">Amber</span></td></tr>
    <tr><td>Halloumi</td><td class="num">about 25g</td><td class="num">about 7.5g</td><td><span class="tag red">Red</span></td></tr>
    <tr><td>Brie and camembert</td><td class="num">about 27 to 29g</td><td class="num">about 8.5g</td><td><span class="tag red">Red</span></td></tr>
    <tr><td>Parmesan</td><td class="num">about 29g</td><td class="num">about 9g</td><td><span class="tag amber">Amber</span> (you use very little)</td></tr>
    <tr><td>Cheddar</td><td class="num">about 34g</td><td class="num">about 10g</td><td><span class="tag red">Red</span></td></tr>
    <tr><td>Stilton and other blue cheese</td><td class="num">about 35g</td><td class="num">about 10.5g</td><td><span class="tag red">Red</span></td></tr>
  </tbody>
</table></div>
<p>Figures are typical values and vary by brand. Check the label for the fat per 100g.</p>
<p>Parmesan is a useful exception. It's high in fat, but it's so strongly flavoured that a teaspoon or two grated over pasta goes a long way.</p>

<h2>Easy cheese swaps</h2>
<div class="swap-grid">
  <div class="swap">{food_img(root, "toast", "Toast", "swap-pic")}<div><b>Cheese on buttered toast</b><span>&rarr; Cottage cheese and sliced tomato on toast, no butter</span></div></div>
  <div class="swap">{food_img(root, "potato", "A potato", "swap-pic")}<div><b>Jacket potato with cheddar</b><span>&rarr; Jacket potato with cottage cheese and chives, or baked beans</span></div></div>
  <div class="swap">{food_img(root, "fast-food", "Pizza", "swap-pic")}<div><b>Cheesy pizza</b><span>&rarr; Thin crust, vegetable toppings, half the cheese</span></div></div>
  <div class="swap">{food_img(root, "low-fat-dairy", "Yoghurt", "swap-pic")}<div><b>Cream cheese dips</b><span>&rarr; Quark or fat-free yoghurt mixed with herbs and garlic</span></div></div>
</div>

<h2>Tips for getting more flavour from less cheese</h2>
<ul>
  <li><b>Choose strong cheese.</b> Mature or extra mature cheddar has more flavour, so you need less of it.</li>
  <li><b>Grate it, don't slice it.</b> Grated cheese spreads further than slices.</li>
  <li><b>Put it on top.</b> Cheese sprinkled on top of a dish, where you can see and taste it, goes further than cheese stirred into a sauce.</li>
  <li><b>Weigh it once.</b> Weigh out 30g one time so you know what a portion looks like.</li>
  <li><b>Make lighter sauces.</b> For cauliflower cheese or lasagne, make the sauce with skimmed milk and a small amount of strong cheese, and add mustard for extra flavour.</li>
</ul>

<h2>Cheese during a flare-up</h2>
<p>During a flare-up, it's best to avoid most cheese and stick to plain, gentle food. A spoonful of low-fat cottage cheese or quark is usually the only cheese worth trying on a bad day. Bring other cheeses back slowly once you feel better, starting with small portions of the lighter ones.</p>

<h2>The bottom line</h2>
<p>Cheese can stay in your diet. Make cottage cheese, quark and reduced-fat cheeses your everyday choices, keep full-fat cheese to a matchbox-sized portion, and choose strong flavours so a little goes further.</p>
"""
    return food_page(path, "Cheese and Gallstones: Which Cheeses Are Safe to Eat?", h1, desc, body, CHEESE_FAQ,
                     [CUH_DIET, NHS_SYMPTOMS, USDA], strip="Get the printable list of cheeses and dairy to choose or avoid.")
