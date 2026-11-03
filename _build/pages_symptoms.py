"""Pain- and symptom-led articles.
Formula: answer the search properly -> FAQ -> one food to have or avoid -> fridge guide sign-up."""
from layout import *
from pages_core import CUH_DIET, NHS_SYMPTOMS, FOOD_CARDS, cards
from pages_pain import HSE_SYMPTOMS, UHB_GALLSTONES, pain_map

NHS_CHOLECYSTITIS = ("NHS: Acute cholecystitis", "https://www.nhs.uk/conditions/acute-cholecystitis/")
NHS_COMPLICATIONS = ("NHS: Gallstones complications", "https://www.nhs.uk/conditions/gallstones/complications/")
NHS_CAUSES = ("NHS: Gallstones causes", "https://www.nhs.uk/conditions/gallstones/prevention/")
NHS_ICP = ("NHS: Itching and intrahepatic cholestasis of pregnancy", "https://www.nhs.uk/pregnancy/complications/itching-and-intrahepatic-cholestasis/")
STINTON = ("Stinton LM, Shaffer EA. Epidemiology of gallbladder disease: cholelithiasis and cancer. Gut and Liver, 2012", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3343155/")


def one_food(root, kind, img, food, text, href, link_text):
    """The single food each article ends on, followed by the fridge guide sign-up."""
    label = "One food to avoid" if kind == "avoid" else "One food to choose"
    tag = "red" if kind == "avoid" else "green"
    return f"""<section class="one-food" aria-labelledby="one-food-h">
  <div class="one-food-card {tag}">
    <img src="{root}assets/img/{img if "." in img else "food/" + img + ".webp"}" alt="{esc(food)}" loading="lazy">
    <div>
      <div class="one-food-label">{label}</div>
      <h2 id="one-food-h">{esc(food)}</h2>
      {text}
      <p><a href="{root}{href}">{esc(link_text)} &rarr;</a></p>
    </div>
  </div>
  <p class="one-food-next">That's just one food. Your fridge guide sorts more than 50 everyday foods into what to choose, what to limit and what to eat on a bad day, so you never have to guess at a meal again.</p>
</section>
{optin(root, "inline", "Get the free printable Gallstones Fridge Guide", anchor=True)}"""


def article(path, title, h1, desc, crumb, body, faq_items, food_block, src, related=None):
    root = "../"
    rel = related or FOOD_CARDS
    main = f"""<h1>{h1}</h1>
{byline()}
{body}
{faq(faq_items)}
{food_block}
<h2>Keep reading</h2>
{cards(root, rel)}
{author_box(root)}
{sources(src)}"""
    return page(path, title, desc, main,
                crumbs=[("Home", ""), ("Gallbladder pain", "gallbladder-pain/"), (crumb, path)],
                schema=[article_schema(path, h1, desc), faq_schema(faq_items)])


SYMPTOM_CARDS = [
    ("gallbladder-pain/", "Gallbladder pain", "Where it hurts, what triggers it and when to get help.", "pain-map.svg"),
    ("gallbladder-symptoms/", "Gallbladder symptoms", "10 signs of a gallbladder problem.", "pain-map.svg"),
    ("where-is-gallbladder-pain-felt/", "Where is the pain felt?", "Front, back, shoulder and left side explained.", "pain-map.svg"),
    ("gallbladder-attack/", "Gallbladder attack", "What it feels like and what to do.", "pain-map.svg"),
    ("gallbladder-pain-relief/", "Gallbladder pain relief", "What actually helps, and what doesn't.", "pain-map.svg"),
    ("gallstones-treatment/", "Gallstones treatment", "Every option explained in plain English.", "pain-map.svg"),
    ("gallstones-symptoms-in-women/", "Gallstones in women", "Symptoms, pain location and pregnancy.", "pain-map.svg"),
    ("inflamed-gallbladder/", "Inflamed gallbladder", "Signs of cholecystitis and infection.", "pain-map.svg"),
]


def related_for(path):
    paths = [c[0] for c in SYMPTOM_CARDS]
    i = paths.index(path) if path in paths else -1
    picks = [SYMPTOM_CARDS[(i + k) % len(SYMPTOM_CARDS)] for k in range(1, 4)]
    return picks + [("foods-to-avoid-with-gallstones/", "Foods to avoid with gallstones", "The complete list of common triggers, with easy swaps.", "fatty-meat")]


# ---------------------------------------------------------------- SYMPTOMS
SYMPTOMS_FAQ = [
    ("What are the first signs of gallbladder problems?",
     "For most people the first sign is a sudden, severe pain under the ribs on the right or in the middle of the upper tummy, often after a meal or at night. Many people have gallstones for years without any symptoms at all."),
    ("Can you have gallstones without symptoms?",
     "Yes. Most people with gallstones never have symptoms, and the stones are often found by chance on a scan for something else. Treatment usually isn't needed unless they start causing problems."),
    ("Do gallstones cause bloating and burping?",
     "Many people with gallstones report bloating, burping and indigestion, but these symptoms are very common and have many other causes, so on their own they don't point to the gallbladder. Severe pain under the right ribs is the more typical sign."),
    ("How do doctors check for gallstones?",
     "Usually with an ultrasound scan of your tummy, which is quick and painless. You may also have blood tests to check your liver and look for infection."),
    ("Can gallbladder problems cause pain on the left side?",
     "Gallbladder pain is usually on the right or in the middle of the upper tummy. Pain mainly on the left side is more likely to have another cause, so it's worth getting it checked by your GP."),
    ("Can gallstones go away on their own?",
     "Small stones sometimes pass out of the gallbladder by themselves, but most gallstones stay put. If they're causing symptoms, the usual long-term treatment is keyhole surgery to remove the gallbladder."),
]


def symptoms():
    path = "gallbladder-symptoms/"
    h1 = "Gallbladder Symptoms: 10 Signs of a Gallbladder Problem"
    desc = "The 10 most common signs of gallbladder problems and gallstones, from pain under the right ribs to yellow skin, which symptoms are an emergency, and what to do next."
    root = "../"
    body = f"""
<p class="lede">If you've had a pain under your ribs that stopped you in your tracks, you'll want to know if it's your gallbladder. Here are the signs doctors look for, which ones are an emergency, and what you can do about it.</p>
{red_flags()}

<h2>Most gallstones cause no symptoms at all</h2>
<p>It's worth knowing this first. Most people with gallstones never feel a thing, and many only find out by chance during a scan for something else. Symptoms usually start when a stone blocks the narrow tube that drains your gallbladder. That's when the signs below appear.</p>

<h2>The 10 signs of a gallbladder problem</h2>
<h3>1. Sudden, severe pain under the right ribs</h3>
<p>The classic sign. The pain is usually just under your ribs on the right-hand side, or in the middle of your upper tummy below the breastbone. It tends to build quickly and stay severe and steady, rather than coming and going.</p>
<h3>2. Pain spreading to your back or right shoulder blade</h3>
<p>Gallbladder pain often travels round to your back or up to the right shoulder blade. Many people are surprised by this and think they've pulled a muscle.</p>
{pain_map(root)}
<h3>3. Pain after eating, especially a fatty meal</h3>
<p>Attacks often start 30 minutes to an hour after a meal. A fatty meal makes the gallbladder squeeze hard, and if a stone is in the way, that squeeze hurts.</p>
<h3>4. Pain that wakes you at night</h3>
<p>Many attacks happen in the evening or wake people from sleep, often after a large evening meal.</p>
<h3>5. Feeling sick or being sick</h3>
<p>Nausea and vomiting are common during an attack. Unlike some stomach upsets, being sick doesn't usually ease the pain.</p>
<h3>6. Sweating during the pain</h3>
<p>Many people break out in a sweat when an attack is at its worst.</p>
<h3>7. Pain that won't settle, with tenderness under the ribs</h3>
<p>A normal attack eases within a few hours. If the pain lasts longer, the area under your right ribs is very tender, and it hurts more when you breathe in deeply, your gallbladder may be inflamed. This is called <a href="{root}inflamed-gallbladder/">cholecystitis</a> and needs treatment.</p>
<h3>8. A high temperature or shivering</h3>
<p>A fever, or feeling hot and cold and shivery, alongside tummy pain can mean an infection. Get help straight away.</p>
<h3>9. Yellow skin or eyes, and itchy skin</h3>
<p>If a stone blocks the main bile duct, bile backs up into your blood. This causes jaundice: yellowing of the skin or the whites of the eyes. It can be harder to spot on brown or black skin, so check the whites of the eyes. Itchy skin often comes with it.</p>
<h3>10. Dark pee and pale poo</h3>
<p>Darker urine and paler stools than usual are another sign that bile isn't flowing properly. Together with yellowing, they mean you need medical advice urgently.</p>

{ad_slot()}

<h2>Which symptoms are an emergency?</h2>
<div class="table-wrap"><table>
  <thead><tr><th>Symptom</th><th>What to do</th></tr></thead>
  <tbody>
    <tr><td>Tummy pain lasting longer than 30 minutes</td><td>Get an urgent GP appointment or contact NHS 111</td></tr>
    <tr><td>Sudden, severe tummy pain</td><td>Call 999 or go to A&amp;E</td></tr>
    <tr><td>Pain spreading to your back, with vomiting</td><td>Call 999 or go to A&amp;E</td></tr>
    <tr><td>High temperature, or feeling hot, cold and shivery</td><td>Call 999 or go to A&amp;E</td></tr>
    <tr><td>Yellow skin or yellowing whites of the eyes</td><td>Call 999 or go to A&amp;E</td></tr>
    <tr><td>An attack that has passed</td><td>Book a GP appointment to talk about it</td></tr>
  </tbody>
</table></div>

<h2>What about bloating, burping and indigestion?</h2>
<p>Lots of people with gallstones say they feel bloated, burp a lot or get indigestion, especially after rich food. It's real, but these symptoms are so common in everyone that on their own they can't tell you it's your gallbladder. The pain is the giveaway. If you only have bloating and indigestion, your GP may look at other causes first.</p>

<h2>How gallbladder problems are diagnosed</h2>
<p>If your GP thinks it's your gallbladder, you'll usually have an ultrasound scan of your tummy. It's quick, painless and the best way to see gallstones. Blood tests can check your liver and look for signs of infection. If the stones are causing symptoms, you'll be offered treatment, which is most often keyhole surgery to remove the gallbladder.</p>

<h2>What you can do right now</h2>
<p>While you wait for tests or treatment, the biggest thing in your control is what's on your plate. Large, fatty meals are the most common trigger for attacks. Eating smaller meals, more regularly, and cutting back on the worst trigger foods makes a real difference for most people. So let's start with one.</p>
"""
    food = one_food(root, "avoid", "fried", "Fried food",
        "<p>Chips, fried chicken, battered fish and the full English are the number one trigger people report. Frying soaks food in oil, and a big hit of fat is exactly what makes a gallbladder with stones in it squeeze hard. The good news: you can keep the crunch by oven-baking or air-frying with a teaspoon of oil instead.</p>",
        "fried-food-and-gallstones/", "Read the full guide to fried food and gallstones")
    return article(path, "Gallbladder Symptoms: 10 Signs of a Gallbladder Problem (UK)", h1, desc, "Gallbladder symptoms",
                   body, SYMPTOMS_FAQ, food, [NHS_SYMPTOMS, NHS_COMPLICATIONS, NHS_CHOLECYSTITIS, HSE_SYMPTOMS, UHB_GALLSTONES],
                   related_for(path))


# ---------------------------------------------------------------- WOMEN
WOMEN_FAQ = [
    ("Are gallstone symptoms different in women?",
     "The symptoms themselves are the same in women and men: pain under the right ribs or in the upper middle of the tummy, often spreading to the back or right shoulder blade, sometimes with sickness. Women are simply more likely to get gallstones in the first place."),
    ("Why are women more likely to get gallstones?",
     "Mainly because of the hormone oestrogen, which raises the amount of cholesterol in bile. That's why pregnancy, the combined pill and HRT are all linked to a higher risk. Women are roughly twice as likely as men to develop gallstones, and the gap narrows after the menopause."),
    ("Where is gallbladder pain felt in a woman?",
     "In the same place as in men: under the ribs on the right-hand side or in the middle of the upper tummy. It can spread to the back and the right shoulder blade."),
    ("Can gallbladder pain be on the left side in women?",
     "It's unusual. Gallbladder pain can be felt in the middle of the upper tummy, which some people describe as more to the left, but pain mainly on the left side usually has another cause. See your GP to get it checked."),
    ("Are gallstones common in pregnancy?",
     "Pregnancy hormones make gallstones and biliary sludge (thickened bile) more likely. Many cases cause no symptoms and settle after the birth. If you have tummy pain in pregnancy, contact your midwife or GP."),
    ("Can the contraceptive pill cause gallstones?",
     "Pills containing oestrogen have been linked to a small increase in gallstone risk, mainly in women who are already prone to them. Don't stop your contraception because of this; talk to your GP or pharmacist if you're worried."),
]


def women():
    path = "gallstones-symptoms-in-women/"
    h1 = "Gallstones Symptoms in Women: Signs, Pain Location and Pregnancy"
    desc = "Gallstone and gallbladder symptoms in women: where the pain is felt, why women are twice as likely to get gallstones, pregnancy, the pill and HRT, and when to get help."
    root = "../"
    body = f"""
<p class="lede">Gallstones are far more common in women than in men, and many women put up with the pain for months before getting answers. Here's what the symptoms look like, why women are more at risk, and what you can do to help yourself.</p>
{red_flags()}

<h2>Women are about twice as likely to get gallstones</h2>
<p>Being a woman is one of the main risk factors for gallstones, alongside being over 40 and carrying extra weight. Women are roughly twice as likely as men to develop them, especially during the years they can have children. After the menopause, the gap narrows.</p>
<p>The main reason is the hormone oestrogen. It raises the amount of cholesterol in your bile, and most gallstones in the UK are made mainly of cholesterol. Progesterone also slows down how well the gallbladder empties, so bile sits for longer. That's why anything that raises these hormones is linked to gallstones.</p>
<div class="table-wrap"><table>
  <thead><tr><th>Risk factor</th><th>Why it matters</th></tr></thead>
  <tbody>
    <tr><td>Pregnancy</td><td>Higher hormone levels make thick bile (sludge) and stones more likely</td></tr>
    <tr><td>Having had several pregnancies</td><td>The risk builds up with each pregnancy</td></tr>
    <tr><td>Combined contraceptive pill</td><td>A small increase in risk, mainly in women already prone to gallstones</td></tr>
    <tr><td>HRT containing oestrogen</td><td>Linked to more gallbladder problems after the menopause</td></tr>
    <tr><td>Being over 40, or carrying extra weight</td><td>Two of the biggest risk factors for everyone</td></tr>
    <tr><td>Rapid weight loss or crash dieting</td><td>Makes gallstones more likely to form</td></tr>
  </tbody>
</table></div>
<p>Don't stop the pill or HRT because of this. The increase is small for most women, and your GP can help you weigh it up.</p>

<h2>Gallbladder symptoms in women</h2>
<p>The symptoms are the same as in men. What's different is how often they're put down to something else, like indigestion, IBS or a back problem. The signs to look for are:</p>
<ul>
  <li><b>Sudden, severe pain</b> under the ribs on the right, or in the middle of the upper tummy</li>
  <li><b>Pain spreading</b> to your back or right shoulder blade</li>
  <li><b>Pain after a meal,</b> especially a fatty one, or pain that wakes you at night</li>
  <li><b>Feeling sick or being sick,</b> and sweating with the pain</li>
  <li><b>Pain lasting from around 30 minutes to a few hours,</b> then easing off</li>
</ul>
<p>For the full list, including the signs of something more serious, read our guide to <a href="{root}gallbladder-symptoms/">the 10 signs of a gallbladder problem</a>.</p>

<h2>Where is gallbladder pain felt in women?</h2>
<p>Exactly where it's felt in men. Your gallbladder sits under your liver on the right-hand side, so the pain is usually under the right ribs or in the middle of your upper tummy, and it can spread to your back and right shoulder blade.</p>
{pain_map(root)}
<p><b>What about the left side?</b> Lots of women search for this. Because the pain can sit in the middle of the upper tummy, some people feel it more towards the left. But pain mainly on the left side is more likely to have another cause, so ask your GP to check it.</p>

{ad_slot()}

<h2>Gallstones in pregnancy</h2>
<p>Pregnancy hormones make bile thicker and slow down the gallbladder, so gallstones and "sludge" are more common when you're pregnant. Many cases cause no symptoms, and sludge often clears after the birth.</p>
<p>If you have tummy pain while pregnant, contact your midwife or GP. Your team will talk you through the options, which often start with changes to what you eat and pain relief that's safe in pregnancy.</p>
<div class="callout">
  <h3>Itching in pregnancy is a different condition</h3>
  <p>Very itchy skin in pregnancy, especially on the palms of the hands or soles of the feet, or itching that's worse at night, can be a sign of a liver condition called intrahepatic cholestasis of pregnancy (ICP). It isn't caused by gallstones, but it needs checking quickly. The NHS advises calling your maternity unit straight away, or NHS 111 if you can't reach them.</p>
</div>

<h2>Why women's gallbladder pain gets missed</h2>
<p>Many women are told it's indigestion, stress or a pulled muscle, sometimes for months. If your pain matches the pattern above, and especially if it follows meals or wakes you at night, tell your GP exactly that: where it hurts, how long it lasts, and what you'd eaten. A simple ultrasound scan is usually all it takes to find gallstones.</p>

<h2>What you can do right now</h2>
<p>Whatever your age or stage of life, what you eat is the one thing you can change today. Large, fatty meals are the most common trigger, and some everyday foods carry far more fat than people realise. Here's one that's in almost every kitchen.</p>
"""
    food = one_food(root, "avoid", "low-fat-dairy", "Whole milk",
        "<p>Milk goes into tea, coffee, cereal and sauces several times a day, so the type you buy really adds up. A glass of whole milk has around 7g of fat; the same glass of skimmed has less than half a gram. Switching to skimmed or 1% is one of the easiest changes you can make, and you keep all the calcium, which matters for women's bones.</p>",
        "milk-and-gallstones/", "Compare every milk in our milk and gallstones guide")
    return article(path, "Gallstones Symptoms in Women: Signs, Pain Location & Pregnancy", h1, desc, "Gallstones in women",
                   body, WOMEN_FAQ, food, [NHS_SYMPTOMS, NHS_CAUSES, STINTON, NHS_ICP], related_for(path))


# ---------------------------------------------------------------- ATTACK
ATTACK_FAQ = [
    ("How long does a gallbladder attack last?",
     "Usually from around 30 minutes to a few hours, then it gradually eases. The NHS advises getting urgent advice from your GP or NHS 111 if tummy pain lasts longer than 30 minutes."),
    ("What does a gallbladder attack feel like?",
     "A sudden, severe, steady pain under the right ribs or in the middle of the upper tummy, which can spread to your back or right shoulder blade. Many people feel sick, vomit or sweat. Moving, passing wind or going to the toilet doesn't usually ease it."),
    ("What triggers a gallbladder attack?",
     "Attacks often come 30 minutes to an hour after eating, especially after a large or fatty meal, and often at night. Fried food, takeaways, fatty meat and full-fat dairy are the triggers people mention most."),
    ("What should I eat after a gallbladder attack?",
     "Keep to small, plain, low-fat meals for a day or two: porridge made with water or skimmed milk, toast, rice, plain potatoes, broth-based soup, bananas and steamed vegetables. Bring other foods back slowly."),
    ("Is a gallbladder flare-up the same as an attack?",
     "People use \"flare-up\" in different ways, but usually they mean the same thing as an attack: a bout of gallbladder pain. If you have pain on and off for days, or pain that doesn't settle, see your GP."),
    ("Will I need surgery after a gallbladder attack?",
     "Not necessarily after one attack. But if attacks keep coming back, the usual treatment is keyhole surgery to remove the gallbladder. Your GP will talk through the options."),
]


def attack():
    path = "gallbladder-attack/"
    h1 = "Gallbladder Attack: Symptoms, How Long It Lasts and What to Do"
    desc = "What a gallbladder attack (biliary colic) feels like, how long it lasts, what triggers it, what to do during an attack and what to eat afterwards."
    root = "../"
    body = f"""
<p class="lede">A gallbladder attack can be one of the most painful things you've ever felt, and it often strikes without warning in the middle of the night. Here's how to recognise one, what to do while it's happening, and how to make the next one less likely.</p>
{red_flags()}

<h2>What a gallbladder attack feels like</h2>
<p>Doctors call a typical attack <b>biliary colic</b>. It usually follows the same pattern:</p>
<ul>
  <li><b>Sudden, severe pain</b> under your ribs on the right, or in the middle of your upper tummy</li>
  <li><b>It builds and stays steady,</b> rather than coming in waves</li>
  <li><b>It can spread</b> to your back or right shoulder blade</li>
  <li><b>Nothing eases it:</b> changing position, passing wind, going to the toilet or being sick doesn't help</li>
  <li><b>Sweating, feeling sick or vomiting</b> are common</li>
</ul>
{pain_map(root)}

<h2>How long does a gallbladder attack last?</h2>
<div class="facts">
  <div class="fact"><b>30 min to hours</b><span>How long a typical attack lasts before easing</span></div>
  <div class="fact"><b>30 to 60 min</b><span>After a meal is when many attacks start</span></div>
  <div class="fact"><b>Weeks or months</b><span>Between attacks for many people</span></div>
</div>
<p>Most attacks ease off within a few hours, once the stone moves or the gallbladder relaxes. If the pain lasts longer than 30 minutes, the NHS advises getting urgent advice from your GP or NHS 111. Pain that goes on for many hours, especially with a fever, can mean your gallbladder has become <a href="{root}inflamed-gallbladder/">inflamed</a>.</p>

<h2>Why attacks happen</h2>
<p>Your gallbladder stores bile and squeezes it out when you eat, especially when you eat fat. If a gallstone is sitting at the exit, that squeeze pushes against a blocked opening, and that's the pain. It's why attacks so often follow a big or fatty meal, and why they're common in the evening and at night after the biggest meal of the day.</p>

{ad_slot()}

<h2>What to do during a gallbladder attack</h2>
<ol>
  <li><b>Check the warning signs.</b> Call 999 if the pain is sudden and severe, spreads to your back with vomiting, or comes with a high temperature, shivering or yellow skin or eyes.</li>
  <li><b>Get advice if it lasts.</b> If the pain lasts longer than 30 minutes, get an urgent GP appointment or contact NHS 111.</li>
  <li><b>Stop eating.</b> Don't eat while the pain is severe. Small sips of water are fine.</li>
  <li><b>Ask about pain relief.</b> A pharmacist, GP or NHS 111 can tell you which painkillers are safe for you.</li>
  <li><b>Make a note.</b> Write down when it started, how long it lasted and what you last ate. It helps your doctor, and it helps you spot your own triggers.</li>
</ol>

<h2>After the attack: the next 48 hours</h2>
<p>Your gallbladder area may feel sore and bruised for a day or two. Give it an easy time with small, plain, low-fat meals: porridge, dry toast, rice, plain potatoes, broth-based soups, steamed vegetables, skinless chicken and white fish. Bring other foods back gradually. Book a GP appointment to talk about what happened, even if you feel fine now.</p>

<h2>Making the next attack less likely</h2>
<ul>
  <li><b>Eat smaller meals, more regularly,</b> and don't skip breakfast</li>
  <li><b>Make your evening meal a lighter one</b></li>
  <li><b>Cut back on the big triggers:</b> fried food, takeaways, fatty and processed meat, cream, butter and full-fat cheese</li>
  <li><b>Spread any fat you eat across the day</b> instead of having it in one meal</li>
</ul>
<p>If attacks keep coming back, the usual treatment is keyhole surgery to remove the gallbladder. Your GP can refer you. In the meantime, food is the thing most in your control, and some foods are genuinely kind to a sore gallbladder.</p>
"""
    food = one_food(root, "choose", "banana", "Bananas",
        "<p>When you're recovering from an attack and don't know what's safe, reach for a ripe banana. It has almost no fat (about 0.4g), it's soft and easy to digest, and it's on every gentle-foods list for flare days. Slice one onto porridge made with water or skimmed milk for one of the kindest breakfasts you can have.</p>",
        "bananas-and-gallstones/", "Read why bananas are so gallbladder-friendly")
    return article(path, "Gallbladder Attack: Symptoms, How Long It Lasts & What to Do", h1, desc, "Gallbladder attack",
                   body, ATTACK_FAQ, food, [NHS_SYMPTOMS, HSE_SYMPTOMS, UHB_GALLSTONES, CUH_DIET], related_for(path))


# ---------------------------------------------------------------- INFLAMED / INFECTED
INFLAMED_FAQ = [
    ("What are the signs of an inflamed gallbladder?",
     "A sudden, sharp pain in the upper right of your tummy that spreads towards your right shoulder, doesn't go away within a few hours, and is worse when you breathe in deeply. The area is usually very tender. You may also have a high temperature, feel sick or be sick, sweat or lose your appetite."),
    ("How is an inflamed gallbladder different from a gallbladder attack?",
     "A normal attack eases within a few hours. With an inflamed gallbladder (cholecystitis), the pain carries on, the area is tender to touch, and there's often a fever. It needs medical treatment."),
    ("Can an inflamed gallbladder heal on its own?",
     "You shouldn't wait to find out. Acute cholecystitis usually needs hospital treatment, and without it there's a risk of serious complications such as the gallbladder tearing or the infection spreading."),
    ("How is an infected gallbladder treated?",
     "Usually in hospital, with fluids through a drip, pain relief and antibiotics if there's an infection. Removing the gallbladder with keyhole surgery is often recommended, sometimes within a week of diagnosis."),
    ("What causes an inflamed gallbladder?",
     "About 95% of cases are caused by a gallstone or thick bile (sludge) blocking the gallbladder's exit. Bile builds up, the gallbladder swells and becomes inflamed, and sometimes it becomes infected."),
    ("What should I eat while waiting for gallbladder surgery?",
     "NHS advice for people waiting for surgery is a low-fat diet and avoiding foods that trigger your symptoms. Small, regular meals built around vegetables, fruit, wholegrains and lean protein suit most people."),
]


def inflamed():
    path = "inflamed-gallbladder/"
    h1 = "Inflamed or Infected Gallbladder: Signs of Cholecystitis and When to Get Help"
    desc = "The signs of an inflamed or infected gallbladder (acute cholecystitis), how it differs from a normal gallbladder attack, how it's treated, and what to eat while you wait for surgery."
    root = "../"
    body = f"""
<p class="lede">Most gallbladder attacks ease within a few hours. When the pain doesn't go away, the gallbladder may have become inflamed or infected. This is called acute cholecystitis, and it's the time to stop waiting it out and get medical help.</p>
{red_flags()}

<h2>Signs of an inflamed gallbladder</h2>
<ul>
  <li><b>Sudden, sharp pain in the upper right of your tummy,</b> often spreading towards your right shoulder</li>
  <li><b>Pain that doesn't go away</b> within a few hours, unlike a normal attack</li>
  <li><b>Tenderness:</b> the area under your right ribs hurts to touch</li>
  <li><b>Pain that's worse when you breathe in deeply</b></li>
  <li><b>A high temperature,</b> or feeling hot and shivery</li>
  <li><b>Feeling sick, being sick, sweating</b> or losing your appetite</li>
  <li><b>Yellowing</b> of the skin or the whites of the eyes, in some people</li>
</ul>

<h2>Normal attack or inflamed gallbladder?</h2>
<div class="table-wrap"><table>
  <thead><tr><th></th><th>Typical gallbladder attack</th><th>Inflamed gallbladder (cholecystitis)</th></tr></thead>
  <tbody>
    <tr><td><b>How long</b></td><td>30 minutes to a few hours, then eases</td><td>Keeps going for many hours or days</td></tr>
    <tr><td><b>Temperature</b></td><td>Usually normal</td><td>Often a fever or shivering</td></tr>
    <tr><td><b>Tenderness</b></td><td>Sore, but eases after</td><td>Very tender to touch, worse on breathing in</td></tr>
    <tr><td><b>What to do</b></td><td>Urgent GP or NHS 111 if it lasts over 30 minutes</td><td>Get medical help the same day; 999 if severe</td></tr>
  </tbody>
</table></div>

<h2>What causes it</h2>
<p>In about 95% of cases, a gallstone or thick, gritty bile (called sludge) blocks the narrow tube leading out of the gallbladder. Bile builds up inside, pressure rises, and the gallbladder becomes swollen and inflamed. Sometimes bacteria get in and it becomes infected too.</p>
<p>Much less often, the gallbladder becomes inflamed without any stones. This mostly happens in people who are already very unwell, for example after major surgery, serious injury or a severe infection.</p>

{ad_slot()}

<h2>How it's treated</h2>
<p>Acute cholecystitis usually means a stay in hospital. Treatment normally includes:</p>
<ul>
  <li><b>Resting the gut:</b> not eating or drinking for a while, with fluids through a drip</li>
  <li><b>Pain relief</b></li>
  <li><b>Antibiotics</b> if there's an infection, sometimes for up to a week</li>
  <li><b>Surgery to remove the gallbladder,</b> usually by keyhole surgery. It's often done within a week of diagnosis if you're well enough, to stop it happening again.</li>
</ul>
<p>If surgery isn't safe for you, doctors may drain the gallbladder with a thin tube instead.</p>

<h2>Why you shouldn't wait it out</h2>
<p>Without treatment, an inflamed gallbladder can lead to serious problems, such as part of the gallbladder dying (gangrene) or the gallbladder tearing, which spreads infection through the tummy. These need emergency surgery. Getting help early makes them far less likely.</p>

<h2>Life after an inflamed gallbladder</h2>
<p>Once you're home, and especially while you're waiting for surgery, food matters. NHS advice for people waiting for gallbladder surgery is a low-fat diet and avoiding the foods that trigger your symptoms. Small, regular meals built around vegetables, fruit, wholegrains and lean protein are the safest pattern. And there's one food that catches out more people than almost any other.</p>
"""
    food = one_food(root, "avoid", "cheese", "Full-fat cheese",
        "<p>Cheddar, brie, stilton and halloumi are around a third fat. A cheese sandwich, cheesy pasta or a cheese board can deliver more fat in one sitting than the rest of your day put together. Swap to cottage cheese or quark most of the time, and when you do have hard cheese, keep it to a matchbox-sized portion of something strong.</p>",
        "cheese-and-gallstones/", "See our cheese chart, from lightest to heaviest")
    return article(path, "Inflamed or Infected Gallbladder: Signs of Cholecystitis", h1, desc, "Inflamed gallbladder",
                   body, INFLAMED_FAQ, food, [NHS_CHOLECYSTITIS, NHS_COMPLICATIONS, NHS_SYMPTOMS, NHS_CAUSES], related_for(path))
