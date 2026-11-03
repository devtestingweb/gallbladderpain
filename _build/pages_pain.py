"""Gallbladder pain and symptoms guides."""
from layout import *
from pages_core import CUH_DIET, NHS_SYMPTOMS, FOOD_CARDS, cards

HSE_SYMPTOMS = ("HSE (Ireland): Gallstones symptoms", "https://www2.hse.ie/conditions/gallstones/symptoms/")
UHB_GALLSTONES = ("University Hospitals Bristol and Weston NHS Trust: Gallstone disease", "https://uhbristol.nhs.uk/patients-and-visitors/your-hospitals/bristol-royal-infirmary/what-we-do/ogteam/conditions,-tests-and-treatments/gallstone-disease/")

PAIN_FAQ = [
    ("Where is gallbladder pain felt?",
     "Usually at the top of the tummy, just under the ribs on the right-hand side, or in the middle of the upper tummy. It can spread to your back or your right shoulder blade."),
    ("How long does gallbladder pain last?",
     "A typical attack lasts from around 30 minutes to a few hours, then gradually eases. The NHS advises getting urgent advice from your GP or NHS 111 if tummy pain lasts longer than 30 minutes. Pain that lasts many hours, or comes with a fever, can mean the gallbladder is inflamed and needs treatment."),
    ("What does a gallbladder attack feel like?",
     "Most people describe a severe, constant pain that builds up and doesn't ease when you change position, pass wind or go to the toilet. Many people also feel sick, vomit or sweat."),
    ("Why does gallbladder pain often happen at night?",
     "Attacks often come 30 minutes to an hour after eating, especially after a fatty meal, and evening meals tend to be the biggest of the day. Many people find their attacks wake them in the night."),
    ("Can gallbladder pain go away on its own?",
     "A single attack usually settles by itself within a few hours. But the gallstones are still there, so more attacks are likely. See your GP if you think you've had gallbladder pain, even if it has gone."),
    ("Can gallstones make you tired or dizzy?",
     "Many people feel drained and washed out after an attack, and feeling faint or dizzy can happen with severe pain or vomiting. Ongoing tiredness or dizziness has many possible causes, so mention it to your GP rather than assuming it's your gallbladder."),
    ("Can gallbladder pain feel like a heart attack?",
     "Pain high in the tummy can sometimes be hard to tell apart from heart pain. If you have chest pain, pain spreading to your arm, neck or jaw, or you feel breathless, call 999 straight away."),
]


def pain_map(root):
    return f"""<figure class="pain-map">
  <img src="{root}assets/img/pain-map.svg" width="640" height="380" alt="Diagram of the body. Front: pain under the ribs on the right and in the middle of the upper tummy. Back: pain spreading to the right shoulder blade." loading="lazy">
  <figcaption>Gallbladder pain usually starts under the ribs on the right or in the middle of the upper tummy. It can spread to the back and the right shoulder blade.</figcaption>
</figure>"""


def gallbladder_pain():
    from pages_foods import avoid_grid
    root = "../"
    path = "gallbladder-pain/"
    h1 = "Gallbladder Pain: Where It Hurts, What Triggers It and When to Get Help"
    desc = "What gallbladder pain feels like, where you feel it, how long an attack lasts, the foods that trigger it, and the warning signs that mean you need help straight away."
    main = f"""<h1>{h1}</h1>
{byline()}
<p class="lede">Gallbladder pain can come on suddenly and frighteningly hard. This guide explains what's happening, how to tell a typical attack from something more serious, and the simple food changes that make the next one less likely.</p>

{red_flags()}

<h2>What an attack is usually like</h2>
<div class="facts">
  <div class="fact"><b>A few hours</b><span>A typical attack lasts 30 minutes to a few hours, then eases</span></div>
  <div class="fact"><b>After eating</b><span>Often 30 to 60 minutes after a meal, especially a fatty one</span></div>
  <div class="fact"><b>At night</b><span>Attacks commonly wake people up</span></div>
  <div class="fact"><b>Weeks apart</b><span>Episodes can be weeks or months apart</span></div>
</div>
<p>Doctors call a typical gallstone attack <b>biliary colic</b>. Despite the name, the pain usually isn't the coming-and-going kind. It tends to build up and stay severe and constant, then slowly fade over a few hours. Changing position, passing wind, going to the toilet or being sick doesn't usually ease it. Many people also feel sick, vomit or break out in a sweat.</p>

<h2>Where you feel gallbladder pain</h2>
<p>Your gallbladder sits under your liver, tucked under the ribs on the right-hand side. That's where most people feel the pain, or in the middle of the upper tummy just below the breastbone. It can spread round to your back and up to your right shoulder blade.</p>
{pain_map(root)}

<h2>What causes the pain</h2>
<p>Your gallbladder stores bile, a fluid that helps you digest fat. When you eat, especially something fatty, your body tells the gallbladder to squeeze and push bile out through a narrow tube. If a gallstone gets in the way and blocks that exit, the squeezing gallbladder pushes against the blockage, and that causes the pain. When the stone shifts or the gallbladder relaxes, the pain fades.</p>
<p>That's why food matters so much. A large, fatty meal makes your gallbladder squeeze harder, and that makes an attack more likely.</p>

{optin(root, "inline", "Get the printable list of foods that trigger gallbladder pain", anchor=True)}

<h2>The foods most likely to trigger an attack</h2>
<p>These are the usual suspects. Each has a full guide with portion sizes and easy swaps.</p>
{avoid_grid(root)}
<p>Want the full picture? Read our <a href="{root}foods-to-avoid-with-gallstones/">complete list of foods to avoid</a> and the <a href="{root}gallstones-diet/">gallstones diet guide</a>, which includes a gentle menu for the days after an attack.</p>

{ad_slot()}

<h2>When it's more than a normal attack</h2>
<p>Sometimes a gallstone causes a more serious problem. These need medical treatment, so get help quickly if you notice them.</p>
<div class="table-wrap"><table>
  <thead><tr><th>Problem</th><th>Signs to look out for</th></tr></thead>
  <tbody>
    <tr><td><b>Inflamed gallbladder</b> (cholecystitis)</td><td>Pain that lasts much longer than a normal attack, often many hours, especially with a high temperature</td></tr>
    <tr><td><b>Blocked bile duct</b></td><td>Yellow skin or yellowing whites of the eyes (jaundice), dark pee, pale stools, itchy skin, fever and shivering</td></tr>
    <tr><td><b>Inflamed pancreas</b> (pancreatitis)</td><td>Sudden, severe pain in the upper tummy that spreads to the back, often with vomiting</td></tr>
  </tbody>
</table></div>

<h2>Is it gallbladder pain or something else?</h2>
<p>Pain in the upper tummy can have lots of causes, including indigestion, a stomach ulcer, trapped wind, a pulled muscle and, more rarely, the heart. Only a doctor can tell you for certain, usually with an ultrasound scan. A few clues point towards the gallbladder:</p>
<ul>
  <li>The pain is under the right ribs or in the middle of the upper tummy, and may spread to your right shoulder blade.</li>
  <li>It's severe and steady rather than a dull ache.</li>
  <li>It often follows a fatty meal or wakes you at night.</li>
  <li>Antacids, passing wind or going to the toilet don't ease it.</li>
</ul>
<p><b>Chest pain is different.</b> If you have pain in your chest, pain spreading to your arm, neck or jaw, or you feel short of breath, call 999.</p>

<h2>What to do during an attack</h2>
<ul>
  <li><b>Check the warning signs</b> at the top of this page. If the pain lasts longer than 30 minutes, get urgent advice from your GP or NHS 111.</li>
  <li><b>Don't eat</b> while the pain is severe. Small sips of water are fine.</li>
  <li><b>Ask a pharmacist, GP or NHS 111</b> about pain relief that's safe for you, especially if you take other medicines.</li>
  <li><b>Note the time it started</b> and what you last ate. It helps your doctor, and helps you spot your triggers.</li>
  <li><b>Afterwards, eat gently.</b> Small, low-fat meals such as porridge, toast, rice, soup and bananas for the next day or two.</li>
</ul>

<h2>Making the next attack less likely</h2>
<p>You can't dissolve gallstones with food, and nobody should promise you that. But what you eat has a real effect on how often your gallbladder is pushed into an attack:</p>
<ul>
  <li><b>Keep meals small and regular,</b> and don't skip breakfast.</li>
  <li><b>Cut back on the big triggers:</b> fried food, fatty meat, takeaways, cream, butter and full-fat cheese.</li>
  <li><b>Spread any fat you do eat</b> across the day instead of having it all in one meal.</li>
  <li><b>Fill up on fibre</b> from vegetables, fruit, oats, beans and wholegrains.</li>
  <li><b>If you need to lose weight, go slowly,</b> no faster than about 1kg (2lb) a week.</li>
</ul>
<p>Many people are offered surgery to remove the gallbladder if attacks keep coming back. Talk to your GP about whether that's right for you.</p>

{faq(PAIN_FAQ)}

{optin(root, "inline", "Keep the trigger foods list on your fridge")}

<h2>More on gallbladder symptoms</h2>
{cards(root, [("gallbladder-symptoms/", "Gallbladder symptoms", "10 signs of a gallbladder problem.", "pain-map.svg"), ("gallbladder-attack/", "Gallbladder attack", "What it feels like and what to do.", "pain-map.svg"), ("gallstones-symptoms-in-women/", "Gallstones in women", "Symptoms, pain location and pregnancy.", "pain-map.svg"), ("inflamed-gallbladder/", "Inflamed gallbladder", "Signs of cholecystitis and infection.", "pain-map.svg"), ("where-is-gallbladder-pain-felt/", "Where is the pain felt?", "Front, back, shoulder and left side explained.", "pain-map.svg"), ("gallbladder-pain-relief/", "Gallbladder pain relief", "What actually helps, and what doesn't.", "pain-map.svg"), ("gallstones-treatment/", "Gallstones treatment", "Every option explained in plain English.", "pain-map.svg"), ("gallstones-diet/", "The gallstones diet", "What to eat, what to limit, and a gentle menu for flare-ups.", "vegetables")])}

<h2>Food guides</h2>
{cards(root, [("gallstones-diet/", "The gallstones diet", "What to eat, what to limit, and a gentle menu for flare-ups.", "vegetables")] + FOOD_CARDS[:-1])}

{author_box(root)}
{sources([NHS_SYMPTOMS, HSE_SYMPTOMS, UHB_GALLSTONES, CUH_DIET])}"""
    return page(path, "Gallbladder Pain: Where It Hurts, Triggers & When to Get Help", desc, main,
                crumbs=[("Home", ""), ("Gallbladder pain", path)],
                schema=[article_schema(path, h1, desc), faq_schema(PAIN_FAQ)], nav_current=path)
