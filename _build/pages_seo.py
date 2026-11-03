"""Long-form SEO articles. Follow _build/WRITING_RULES.md:
simple words a 14-year-old understands, short sentences, no em dashes, long form,
answer the search fully, then one food, then the fridge guide."""
from layout import *
from pages_core import CUH_DIET, NHS_SYMPTOMS
from pages_pain import HSE_SYMPTOMS, UHB_GALLSTONES, pain_map
from pages_symptoms import article, one_food, related_for, NHS_CHOLECYSTITIS, NHS_COMPLICATIONS

NHS_TREATMENT = ("NHS: Gallstones treatment", "https://www.nhs.uk/conditions/gallstones/treatment/")
NICE_CG188 = ("NICE guideline CG188: Gallstone disease, diagnosis and management", "https://www.nice.org.uk/guidance/cg188/chapter/1-Recommendations")
IQWIG = ("InformedHealth.org (IQWiG): How can gallstones be treated?", "https://www.informedhealth.org/how-can-gallstones-be-treated.html")
NHS_WALES_REMOVAL = ("NHS 111 Wales: Gallbladder removal (cholecystectomy)", "https://111.wales.nhs.uk/gallbladderremoval(cholecystectomy)/")
UHB_TREATMENT = ("University Hospitals Bristol and Weston NHS Trust: Gallstone disease treatment", "https://uhbristol.nhs.uk/patients-and-visitors/your-hospitals/bristol-royal-infirmary/what-we-do/ogteam/conditions,-tests-and-treatments/gallstone-disease/treatment/")


# ======================================================================== WHERE IS THE PAIN
WHERE_FAQ = [
    ("Where is gallbladder pain felt?",
     "Most people feel it just under the ribs on the right side of their tummy, or in the middle of the upper tummy, just below where the ribs meet. It can spread round to the back and up to the right shoulder blade."),
    ("Where is the gallbladder located?",
     "Your gallbladder sits on the right side of your body, tucked under your liver and just below your lower ribs. It's a small pouch about the size of a small pear."),
    ("Can gallbladder pain be felt in the back?",
     "Yes. The pain often spreads to the back, especially to the area around or just below the right shoulder blade. Some people feel it between the shoulder blades."),
    ("Can gallbladder pain be on the left side?",
     "It's not common. Because the pain can sit in the middle of the upper tummy, some people feel it slightly to the left. But pain that's mainly on the left side usually has a different cause, so ask your GP to check it."),
    ("Can gallbladder pain feel like chest pain?",
     "It can be felt high up, close to the bottom of the chest. If you have chest pain, pain spreading to your arm, neck or jaw, or you feel short of breath, call 999 straight away, as these can be signs of a heart attack."),
    ("Why does gallbladder pain go to the shoulder?",
     "This is called referred pain. Nerves from the area around your gallbladder share pathways with nerves from your shoulder, so your brain can get mixed up about where the pain is really coming from."),
    ("Is gallbladder pain the same for women and men?",
     "Yes. It's felt in the same places. Women are more likely to get gallstones, though, so it's worth knowing the signs."),
]


def where_pain():
    path = "where-is-gallbladder-pain-felt/"
    root = "../"
    h1 = "Where Is Gallbladder Pain Felt? Front, Back, Shoulder and Left Side Explained"
    desc = "Where gallbladder pain is felt: under the right ribs, the upper middle of the tummy, the back and the right shoulder blade. Simple diagrams, what each spot means, and when to get help."
    body = f"""
<p class="lede">You've got a pain under your ribs and you're wondering: is that my gallbladder? This guide shows you exactly where gallbladder pain is felt, why it can turn up in your back or shoulder, and how to tell it apart from other kinds of pain.</p>
{red_flags()}

<h2>The short answer</h2>
<p>Gallbladder pain is usually felt in one of these places:</p>
<ul>
  <li><b>Just under your ribs on the right side.</b> This is the most common spot.</li>
  <li><b>In the middle of your upper tummy,</b> just below where your ribs meet.</li>
  <li><b>In your back,</b> often around or just below your right shoulder blade.</li>
  <li><b>In your right shoulder.</b></li>
</ul>
<p>You might feel it in just one of these places, or in a few at once. It often starts at the front and then spreads round to the back.</p>
{pain_map(root)}

<h2>Where is your gallbladder?</h2>
<p>Before we talk about pain, it helps to know where your gallbladder actually is. It's a small pouch, about the size of a small pear. It sits on the right side of your body, tucked underneath your liver and just below your lower ribs.</p>
<p>Its job is simple. Your liver makes a green-yellow liquid called <b>bile</b>, which helps you break down fat. Your gallbladder stores the bile and squeezes it out into your gut when you eat. That's why fatty meals can set off gallbladder pain: they make the gallbladder squeeze hard.</p>
<p>If you put your hand flat on the right side of your tummy, just under your ribs, your gallbladder is roughly underneath your fingers. That's why most people feel the pain there.</p>

<h2>Pain under the right ribs</h2>
<p>This is the classic gallbladder spot. The pain is usually:</p>
<ul>
  <li><b>Sudden.</b> It comes on fast, often 30 minutes to an hour after a meal, or in the night.</li>
  <li><b>Strong and steady.</b> It doesn't come and go in waves like a cramp. It builds up and stays.</li>
  <li><b>Hard to get comfortable with.</b> Changing position, passing wind or going to the toilet doesn't usually help.</li>
</ul>
<p>A normal attack usually eases off within a few hours. If the area stays very sore when you press it, or it hurts more when you breathe in deeply, your gallbladder might be inflamed. That needs a doctor. Read more about the <a href="{root}inflamed-gallbladder/">signs of an inflamed gallbladder</a>.</p>

<h2>Pain in the middle of your upper tummy</h2>
<p>Lots of people don't feel gallbladder pain on the right at all. Instead they feel it in the middle of the upper tummy, right below the breastbone. This area is sometimes called the "pit of the stomach".</p>
<p>Because this is also where you'd feel indigestion or heartburn, gallbladder pain here is easy to mistake for a bad stomach. The difference is usually how strong it is. Gallbladder pain is often much more severe than indigestion, it lasts longer, and antacids don't help.</p>

<h2>Pain in your back</h2>
<p>Gallbladder pain often spreads round to your back. People describe it as:</p>
<ul>
  <li>a pain just below the right shoulder blade</li>
  <li>a pain between the shoulder blades</li>
  <li>a band of pain that seems to go right through from front to back</li>
</ul>
<p>Back pain from your gallbladder usually comes with tummy pain at the same time, and it usually starts after eating or at night. A pulled muscle in your back is different. It normally hurts more when you move, twist or bend, and you can often point to one sore spot.</p>
<p>One important warning: if you have severe tummy pain that spreads to your back and you're being sick, call 999 or go to A&amp;E. This can be a sign of an inflamed pancreas (pancreatitis), which can be caused by a gallstone.</p>

<h2>Pain in your right shoulder</h2>
<p>It sounds strange, but gallbladder pain can show up in your right shoulder or the tip of your shoulder. Doctors call this <b>referred pain</b>.</p>
<p>Here's what's going on. The nerves around your gallbladder share some of their "wiring" with nerves that come from your shoulder area. When the gallbladder sends a pain signal, your brain can get confused about where it's coming from, and you feel it in your shoulder instead of, or as well as, your tummy.</p>
<p>So if you've got right shoulder pain that comes on after a meal, alongside a pain under your ribs, your gallbladder could be the reason.</p>

{ad_slot()}

<h2>Can gallbladder pain be on the left side?</h2>
<p>This is one of the most searched questions about gallbladder pain in the UK, so let's be clear.</p>
<p>Your gallbladder is on the right. So gallbladder pain is usually on the right, or in the middle. Because the middle of your upper tummy is close to the left side, some people do feel it slightly to the left. But if your pain is mainly on the left, something else is more likely to be causing it.</p>
<p>That doesn't mean you should ignore it. It means you should get it checked by your GP, so they can find the real cause.</p>

<h2>Can gallbladder pain feel like chest pain?</h2>
<p>Gallbladder pain can be felt high up, near the bottom of your chest. That can be scary, because chest pain can also be a sign of a heart problem.</p>
<p><b>Never guess with chest pain.</b> Call 999 straight away if you have:</p>
<ul>
  <li>pain or tightness in your chest</li>
  <li>pain that spreads to your arm, neck, jaw or back</li>
  <li>shortness of breath, sweating or feeling sick with the chest pain</li>
</ul>
<p>It's always better to be checked and told it's your gallbladder than to stay at home with a heart attack.</p>

<h2>Is it my gallbladder or something else?</h2>
<p>Pain in the upper tummy can have lots of causes. Only a doctor can tell you for sure, usually with a quick ultrasound scan. But here's a rough guide to how gallbladder pain compares with other common causes:</p>
<div class="table-wrap"><table>
  <thead><tr><th>What it might be</th><th>What it often feels like</th></tr></thead>
  <tbody>
    <tr><td><b>Gallbladder</b></td><td>Strong, steady pain under the right ribs or upper middle of the tummy. Often after a fatty meal or at night. Can spread to the back or right shoulder. Lasts from around 30 minutes to a few hours.</td></tr>
    <tr><td><b>Indigestion or heartburn</b></td><td>A burning feeling behind the breastbone or in the upper tummy. Usually milder. Often gets better with antacids.</td></tr>
    <tr><td><b>Trapped wind</b></td><td>Crampy pain that moves around. Usually eases when you pass wind or go to the toilet.</td></tr>
    <tr><td><b>Pulled muscle</b></td><td>Hurts more when you move, twist or press on one spot. Not linked to eating.</td></tr>
    <tr><td><b>Kidney stone</b></td><td>Severe pain in the side or back, often moving down towards the groin. Can come in waves.</td></tr>
    <tr><td><b>Heart problem</b></td><td>Chest pain or tightness, possibly spreading to the arm, neck or jaw. <b>Call 999.</b></td></tr>
  </tbody>
</table></div>
<p>This table is just to help you describe your pain to a doctor. It's not a way to diagnose yourself.</p>

<h2>When does gallbladder pain usually happen?</h2>
<p>Where the pain is gives you one clue. When it happens gives you another. Gallbladder pain often:</p>
<ul>
  <li><b>starts 30 minutes to an hour after eating,</b> especially after a big or fatty meal</li>
  <li><b>wakes you up in the night,</b> often after a large evening meal</li>
  <li><b>comes in attacks,</b> with weeks or even months between them</li>
</ul>
<p>If your pain follows this pattern, write it down. Note where it hurt, how long it lasted and what you'd eaten. Your GP will find this really useful. For more on the pattern, read our guide to <a href="{root}gallbladder-attack/">gallbladder attacks</a>.</p>

<h2>What to tell your GP</h2>
<p>Being clear about where your pain is helps your GP work out what's going on faster. Try to tell them:</p>
<ol>
  <li><b>Where it started,</b> and where it spread to (point to the spots)</li>
  <li><b>What it felt like:</b> sharp, dull, burning, crampy or steady</li>
  <li><b>How long it lasted</b></li>
  <li><b>What you'd eaten</b> before it started</li>
  <li><b>Anything else</b> you noticed, like feeling sick, sweating, a high temperature or yellow skin</li>
</ol>
<p>If your GP thinks it's your gallbladder, you'll usually be sent for an ultrasound scan. It's quick, it doesn't hurt, and it's the best way to see gallstones.</p>

<h2>What you can do right now</h2>
<p>Wherever you feel it, gallbladder pain usually has the same trigger: a meal that makes your gallbladder squeeze too hard. That means the food on your plate is the one thing you can change today. Small, regular meals with less fat in each one make attacks less likely for most people. Let's start with one food that's behind a lot of attacks.</p>
"""
    food = one_food(root, "avoid", "fatty-meat", "Bacon and sausages",
        "<p>A bacon sandwich or a couple of sausages might not feel like a big meal, but they're packed with fat, and they're usually fried too. That's a double hit for your gallbladder. Try lean ham, grilled skinless chicken or turkey instead, and save the full English for a very rare treat.</p>",
        "foods-to-avoid-with-gallstones/", "See all the foods to avoid, with easy swaps")
    return article(path, "Where Is Gallbladder Pain Felt? Front, Back, Shoulder & Left Side", h1, desc,
                   "Where is the pain felt?", body, WHERE_FAQ, food,
                   [NHS_SYMPTOMS, HSE_SYMPTOMS, UHB_GALLSTONES, NHS_CHOLECYSTITIS], related_for(path))


# ======================================================================== TREATMENT
TREAT_FAQ = [
    ("What is the main treatment for gallstones?",
     "If gallstones are causing symptoms, the main treatment in the UK is an operation to remove the gallbladder, usually done by keyhole surgery. If they aren't causing any symptoms, you usually don't need any treatment."),
    ("Can gallstones be treated without surgery?",
     "Sometimes. If they cause no symptoms, they can be left alone. Tablets can dissolve some small stones, but only a small number of people are suitable, it takes months, and stones often come back. Changing what you eat can reduce attacks for some people, but it won't get rid of the stones."),
    ("Can you live without a gallbladder?",
     "Yes. Your liver still makes bile. It just drips straight into your gut instead of being stored first. Most people go back to a normal diet after recovering, although some notice looser poo for a while."),
    ("How long does it take to recover from gallbladder removal?",
     "Most people go home the same day as keyhole surgery, or the next day. Many people go back to work within 1 to 2 weeks, depending on their job. Avoid heavy lifting for a few weeks."),
    ("Can gallstones be dissolved with tablets?",
     "A medicine called ursodeoxycholic acid can slowly dissolve some small gallstones made of cholesterol. It has to be taken for months, it only suits a small number of people, and new stones often form after you stop."),
    ("What painkillers can I take for gallstones?",
     "The NHS mentions paracetamol and ibuprofen for gallstone pain while you wait for treatment, and stronger painkillers if the pain is severe. Check with a pharmacist which ones are safe for you."),
    ("What is ERCP?",
     "ERCP is a test and treatment that uses a thin, bendy tube with a camera, passed through your mouth, to reach the main bile duct. It's used to remove gallstones that have got stuck in that duct."),
]


def treatment():
    path = "gallstones-treatment/"
    root = "../"
    h1 = "Gallstones Treatment: Every Option Explained in Plain English"
    desc = "All the treatments for gallstones explained simply: when you don't need treatment, keyhole surgery, recovery, tablets to dissolve stones, ERCP, pain relief, and what you can do yourself."
    body = f"""
<p class="lede">Been told you have gallstones and now you're wondering what happens next? This guide walks you through every treatment option in plain English, so you can understand your choices and ask your doctor the right questions.</p>
{red_flags()}

<h2>The quick version</h2>
<div class="table-wrap"><table>
  <thead><tr><th>Your situation</th><th>Usual treatment</th></tr></thead>
  <tbody>
    <tr><td>Gallstones with no symptoms</td><td>Usually no treatment. You just keep an eye out for symptoms.</td></tr>
    <tr><td>Gallstones causing pain</td><td>An operation to remove the gallbladder, usually by keyhole surgery</td></tr>
    <tr><td>Waiting for an operation</td><td>Painkillers when needed, and a low-fat diet that avoids your trigger foods</td></tr>
    <tr><td>A stone stuck in the main bile duct</td><td>ERCP (a camera tube through the mouth) to remove it, usually with gallbladder removal too</td></tr>
    <tr><td>An inflamed gallbladder</td><td>Hospital treatment, and often surgery within about a week</td></tr>
    <tr><td>Small cholesterol stones, mild symptoms, and surgery isn't right for you</td><td>Sometimes tablets to slowly dissolve the stones</td></tr>
  </tbody>
</table></div>
<p>Now let's go through each one properly.</p>

<h2>Option 1: No treatment at all</h2>
<p>This surprises a lot of people. If your gallstones aren't causing any symptoms, you usually don't need any treatment. Lots of people have gallstones for years without knowing. They're often found by accident, for example during a scan for something else.</p>
<p>UK guidelines say that if your stones aren't causing problems, doctors should reassure you rather than treat you. Surgery always has some risks, so it's not worth doing an operation for stones that aren't bothering you.</p>
<p>What you should do is know the signs. If you start getting pain under your right ribs, especially after meals, see your GP. Read about the <a href="{root}gallbladder-symptoms/">10 signs of a gallbladder problem</a> so you know what to look out for.</p>

<h2>Option 2: Changing what you eat</h2>
<p>Food can't dissolve gallstones. Anyone who tells you otherwise is not being honest with you. But food can make a real difference to how often you get attacks.</p>
<p>Here's why. Fat makes your gallbladder squeeze. If there's a stone in the way, that squeeze hurts. So eating less fat in each meal means your gallbladder doesn't have to squeeze as hard, which can mean fewer and milder attacks.</p>
<p>Some NHS hospitals say that for some people, cutting down on fat reduces their symptoms so much that they don't need any other treatment. For most people, though, diet is something you do <em>alongside</em> treatment, especially while you wait for an operation.</p>
<p>The basics are:</p>
<ul>
  <li>eat smaller meals, more regularly, and don't skip breakfast</li>
  <li>cut back on fried food, fatty meat, takeaways, butter, cream and full-fat cheese</li>
  <li>fill up on vegetables, fruit, oats, beans and wholegrains</li>
  <li>if you need to lose weight, do it slowly</li>
</ul>
<p>Our <a href="{root}gallstones-diet/">gallstones diet guide</a> goes into this in lots more detail.</p>

<h2>Option 3: Painkillers</h2>
<p>Painkillers don't fix gallstones, but they help you get through an attack. The NHS mentions paracetamol and ibuprofen for gallstone pain while you're waiting for treatment, and says stronger painkillers may be given if the pain is severe.</p>
<p>Research suggests anti-inflammatory painkillers like ibuprofen work particularly well for gallstone pain. But they're not safe for everyone. For example, they may not suit you if you have a stomach ulcer, kidney problems, some types of asthma, or you take blood thinners. Always check with a pharmacist or GP first.</p>
<p>We've written a whole guide on <a href="{root}gallbladder-pain-relief/">gallbladder pain relief</a> if you want to know more.</p>

{ad_slot()}

<h2>Option 4: Removing the gallbladder (cholecystectomy)</h2>
<p>If your gallstones are causing pain, the main treatment in the UK is an operation to take out your gallbladder. The medical name is a <b>cholecystectomy</b> (say it like "coh-lee-sis-TEK-tuh-mee"). Around 70,000 of these operations are done in England every year, so it's one of the most common operations there is.</p>
<p>Why take out the whole gallbladder, and not just the stones? Because if the gallbladder stays, new stones usually form again. Removing it is the only way to stop the attacks for good.</p>

<h3>Keyhole surgery</h3>
<p>Most gallbladder operations are done by <b>keyhole surgery</b> (also called laparoscopic surgery). Here's how it works:</p>
<ul>
  <li>You're asleep the whole time, under a general anaesthetic.</li>
  <li>The surgeon makes a few small cuts, usually four: one near your belly button and a few on the right side of your tummy.</li>
  <li>They gently fill your tummy with gas so they have room to see.</li>
  <li>A thin tube with a tiny camera goes in through one cut, and small tools go in through the others.</li>
  <li>The surgeon removes the gallbladder through one of the cuts.</li>
</ul>
<p>UK guidelines say this should usually be done as a <b>day case</b>, which means many people go home the same day. Some people stay one night.</p>

<h3>Open surgery</h3>
<p>Sometimes keyhole surgery isn't possible, for example if the gallbladder is very inflamed. Then the surgeon makes one bigger cut in your tummy instead. This is called open surgery. It usually means more pain afterwards and a longer recovery.</p>

<h3>Recovery</h3>
<ul>
  <li><b>Going home:</b> usually the same day or the next day after keyhole surgery.</li>
  <li><b>Back to work:</b> many people go back within 1 to 2 weeks, depending on their job.</li>
  <li><b>Heavy lifting and hard exercise:</b> avoid these for about four weeks.</li>
  <li><b>Common side effects:</b> feeling sick, indigestion, some tummy pain or diarrhoea. These usually get better on their own.</li>
</ul>
<p>Get urgent advice after surgery if your pain gets worse, your wound looks red or has pus, your skin or eyes turn yellow, or you get a high temperature.</p>

<h3>Can you live without a gallbladder?</h3>
<p>Yes, and most people live completely normally. Your liver keeps making bile. Without a gallbladder to store it, the bile just drips straight into your gut instead. Most people can go back to a normal, healthy diet once they've recovered. Some people notice looser poo or more trips to the toilet, especially after fatty meals. This often settles with time.</p>

<h2>Option 5: ERCP for stuck stones</h2>
<p>Sometimes a gallstone slips out of the gallbladder and gets stuck in the main tube that carries bile to your gut. This tube is called the <b>common bile duct</b>. A stuck stone here can cause yellow skin (jaundice) or an inflamed pancreas.</p>
<p>To get it out, doctors use something called <b>ERCP</b>. You're given medicine to make you sleepy, then a long, thin, bendy tube with a camera on the end is passed through your mouth, down through your stomach, to where the bile duct opens. The doctor widens the opening so the stone can come out.</p>
<p>ERCP is usually done before or after the gallbladder is removed. For people who aren't fit enough for surgery, it can sometimes be the main treatment.</p>

<h2>Option 6: Tablets to dissolve gallstones</h2>
<p>There is a medicine that can dissolve some gallstones. It's called <b>ursodeoxycholic acid</b> (UDCA for short). It's a type of bile acid that slowly breaks down stones made of cholesterol.</p>
<p>It sounds like the perfect answer, but there are big catches:</p>
<ul>
  <li><b>It only works on some stones.</b> They have to be small, made mainly of cholesterol, and still inside the gallbladder.</li>
  <li><b>It's slow.</b> You usually have to take it for several months.</li>
  <li><b>Stones often come back</b> once you stop taking it.</li>
  <li><b>Only a small number of people are offered it,</b> usually those with mild symptoms or very rare attacks, or people who can't have surgery.</li>
</ul>
<p>If you'd like to avoid surgery, it's fair to ask your doctor whether this could be an option for you. Just know it isn't suitable for most people.</p>

<h2>What about shock wave treatment?</h2>
<p>You might have heard of using shock waves to break up stones. This is called lithotripsy. It's used a lot for kidney stones, but it's very rarely used for gallstones in the UK today, because keyhole surgery works so much better.</p>

<h2>What about natural remedies and "flushes"?</h2>
<p>You'll find lots of websites promising to "flush out" or "dissolve" gallstones with olive oil, apple juice, lemon, vinegar or herbs. There's no good evidence that any of these get rid of gallstones.</p>
<p>The popular "gallbladder flush" is a good example. People drink a lot of olive oil and juice, and then find green lumps in the toilet. They think these are stones. In fact, they're usually soft clumps made from the oil itself mixing with digestive juices. Worse, drinking a large amount of oil makes your gallbladder squeeze hard, which can actually set off an attack.</p>
<p>If you try something "natural", please don't let it delay getting proper help, especially if you have any of the warning signs at the top of this page.</p>

<h2>Questions to ask your doctor</h2>
<p>Taking a list into your appointment helps you remember everything. You could ask:</p>
<ol>
  <li>Are my gallstones definitely causing my symptoms?</li>
  <li>Do I need treatment, or can we wait and see?</li>
  <li>If I need surgery, will it be keyhole? Will I go home the same day?</li>
  <li>How long is the waiting list, and what should I do while I wait?</li>
  <li>Could tablets to dissolve the stones work for me?</li>
  <li>Which painkillers are safe for me to take during an attack?</li>
  <li>What should I eat, and what should I avoid?</li>
</ol>

<h2>What you can do while you wait</h2>
<p>Waiting lists for gallbladder surgery can be long. The good news is that while you wait, the NHS and UK guidelines agree on one thing you can do yourself: avoid the foods and drinks that set off your symptoms, and keep your meals low in fat.</p>
<p>That's where small, everyday swaps make a real difference. Here's one of the easiest.</p>
"""
    food = one_food(root, "choose", "lean-protein", "Egg whites (and eggs, cooked the right way)",
        "<p>Eggs are cheap, filling and full of protein, but nearly all the fat is in the yolk. Egg whites have almost none. An omelette made with one whole egg and two whites gives you a proper meal with the fat of just one egg. When you do have whole eggs, boil or poach them instead of frying.</p>",
        "eggs-and-gallstones/", "Read our full guide to eggs and gallstones")
    return article(path, "Gallstones Treatment: Every Option Explained (UK Guide)", h1, desc,
                   "Gallstones treatment", body, TREAT_FAQ, food,
                   [NHS_TREATMENT, NICE_CG188, IQWIG, NHS_WALES_REMOVAL, UHB_TREATMENT, CUH_DIET], related_for(path))


# ======================================================================== PAIN RELIEF
RELIEF_FAQ = [
    ("What is the best pain relief for gallstones?",
     "The NHS mentions paracetamol and ibuprofen for gallstone pain while you wait for treatment, with stronger painkillers if it's severe. Research suggests anti-inflammatory painkillers like ibuprofen work particularly well, but they're not safe for everyone, so check with a pharmacist first."),
    ("How can I relieve gallbladder pain at home?",
     "Stop eating while the pain is bad, sip water, take a painkiller that's safe for you, and rest in whatever position is most comfortable. Some people find a warm (not hot) hot water bottle comforting. If the pain lasts longer than 30 minutes, get urgent advice from your GP or NHS 111."),
    ("Does a hot water bottle help gallbladder pain?",
     "Some people find gentle warmth comforting, but it won't treat the cause. Don't use anything too hot, and don't let it delay getting help if the pain is severe or doesn't settle."),
    ("What position helps gallbladder pain?",
     "There's no position that's proven to help. Most people simply find the position that feels least uncomfortable. If no position helps at all and the pain is severe, that's another reason to get medical help."),
    ("Does apple cider vinegar help gallbladder pain?",
     "There's no good evidence that apple cider vinegar, lemon water, peppermint tea or any other home remedy relieves gallbladder pain or treats gallstones."),
    ("Should I go to A&E for gallbladder pain?",
     "Call 999 or go to A&E if the pain is sudden and severe, spreads to your back with vomiting, or comes with a high temperature, shivering, or yellow skin or eyes. If the pain lasts longer than 30 minutes, get urgent advice from your GP or NHS 111."),
    ("Can I drink alcohol with painkillers for gallbladder pain?",
     "Some painkillers, such as those containing codeine, shouldn't be mixed with alcohol. During a flare-up it's best to avoid alcohol completely. Ask your pharmacist about your specific medicine."),
]


def pain_relief():
    path = "gallbladder-pain-relief/"
    root = "../"
    h1 = "Gallbladder Pain Relief: What Actually Helps (and What Doesn't)"
    desc = "How to relieve gallbladder pain: which painkillers the NHS mentions, what to do during an attack, home remedies that don't work, when to go to A&E, and how to stop the next attack."
    body = f"""
<p class="lede">When gallbladder pain hits, all you want is for it to stop. This guide tells you what really helps, what's a waste of time, and when pain relief isn't enough and you need a doctor.</p>
{red_flags()}

<h2>First: is this an emergency?</h2>
<p>Before you think about painkillers, check the warning signs above. Painkillers can hide how bad things are, so it's important to know when to stop trying to manage at home.</p>
<div class="table-wrap"><table>
  <thead><tr><th>If you have...</th><th>Do this</th></tr></thead>
  <tbody>
    <tr><td>Sudden, severe tummy pain</td><td>Call 999 or go to A&amp;E</td></tr>
    <tr><td>Pain spreading to your back, and you're being sick</td><td>Call 999 or go to A&amp;E</td></tr>
    <tr><td>A high temperature, or you feel hot, cold and shivery</td><td>Call 999 or go to A&amp;E</td></tr>
    <tr><td>Yellow skin, or yellow in the whites of your eyes</td><td>Call 999 or go to A&amp;E</td></tr>
    <tr><td>Chest pain, or pain spreading to your arm, neck or jaw</td><td>Call 999</td></tr>
    <tr><td>Tummy pain lasting longer than 30 minutes</td><td>Get an urgent GP appointment or contact NHS 111</td></tr>
  </tbody>
</table></div>
<p>Don't drive yourself to hospital. Ask someone to take you, or call an ambulance.</p>

<h2>What to do during a gallbladder attack</h2>
<p>If none of the emergency signs apply, here's what helps most people get through an attack.</p>
<h3>1. Stop eating</h3>
<p>Food, especially fatty food, makes your gallbladder squeeze. While you're in pain, give it a rest. Don't eat anything until the pain has gone.</p>
<h3>2. Sip water</h3>
<p>Small sips of water are fine and help if you've been sick. Avoid alcohol, fizzy drinks and anything creamy or milky.</p>
<h3>3. Take a painkiller that's safe for you</h3>
<p>We cover which ones in the next section.</p>
<h3>4. Get as comfortable as you can</h3>
<p>There's no special position that's proven to help gallbladder pain. Most people just find the position that hurts least, whether that's lying on their side, sitting up or curling up. Some people find gentle warmth from a hot water bottle (wrapped in a towel, never too hot) comforting. It won't fix anything, but it may help you feel a little better.</p>
<h3>5. Keep track of time</h3>
<p>Note when the pain started. If it lasts longer than 30 minutes, the NHS says to get urgent advice from your GP or NHS 111.</p>
<h3>6. Write it down afterwards</h3>
<p>Once it's over, jot down what you ate, when the pain started, where it hurt and how long it lasted. This helps your GP, and helps you spot your own trigger foods.</p>

<h2>Which painkillers help with gallbladder pain?</h2>
<p>The NHS mentions two everyday painkillers for gallstone pain while you're waiting for treatment:</p>
<ul>
  <li><b>Paracetamol</b></li>
  <li><b>Ibuprofen</b></li>
</ul>
<p>If the pain is severe, your doctor may give you something stronger.</p>
<p>Research suggests that anti-inflammatory painkillers, called NSAIDs (ibuprofen is one of these), work particularly well for gallstone pain, better than medicines that relax the muscles.</p>
<div class="callout">
  <h3>Check before you take ibuprofen</h3>
  <p>Ibuprofen and other NSAIDs aren't safe for everyone. They may not be right for you if you:</p>
  <ul>
    <li>have had a stomach ulcer or bleeding from your stomach</li>
    <li>have kidney, liver or heart problems</li>
    <li>have asthma that's made worse by these medicines</li>
    <li>take blood thinners or certain other medicines</li>
    <li>are pregnant</li>
  </ul>
  <p>A pharmacist can tell you in a couple of minutes what's safe for you. Always read the leaflet, and never take more than the dose it says.</p>
</div>
<p>If your attacks keep coming back, speak to your GP. Painkillers help you cope, but they don't stop the attacks happening.</p>

{ad_slot()}

<h2>Home remedies that don't work</h2>
<p>If you search online for gallbladder pain relief, you'll find a long list of home remedies. It's natural to want to try something, so here's the honest truth about the most common ones.</p>
<div class="table-wrap"><table>
  <thead><tr><th>Remedy</th><th>Does it relieve gallbladder pain?</th></tr></thead>
  <tbody>
    <tr><td>Apple cider vinegar</td><td>No good evidence it helps. It can also upset your stomach.</td></tr>
    <tr><td>Lemon water</td><td>No evidence it helps the pain. Water is fine, the lemon doesn't add anything.</td></tr>
    <tr><td>Peppermint tea</td><td>No evidence for gallbladder pain. Some people find it soothing, which is fine.</td></tr>
    <tr><td>Olive oil and juice "flush"</td><td>No evidence it works, and a big dose of oil can actually <b>trigger</b> an attack.</td></tr>
    <tr><td>Turmeric</td><td>No good evidence for gallstone pain.</td></tr>
    <tr><td>Epsom salts</td><td>No evidence for gallstones, and they can cause diarrhoea.</td></tr>
  </tbody>
</table></div>
<p>A cup of herbal tea won't hurt you. The danger is when a home remedy makes you wait at home when you should be getting help. If you have any of the warning signs, skip the remedies and get medical advice.</p>

<h2>Gallbladder pain at night</h2>
<p>Lots of gallbladder attacks happen in the evening or wake people from sleep. That's often because dinner is the biggest meal of the day, and many attacks start 30 minutes to an hour after eating.</p>
<p>If your attacks tend to happen at night, try:</p>
<ul>
  <li>making your evening meal smaller and lower in fat</li>
  <li>having your bigger meal at lunchtime instead</li>
  <li>leaving a couple of hours between eating and going to bed</li>
  <li>skipping late-night snacks like crisps, cheese, chocolate or takeaways</li>
</ul>

<h2>After the attack: how to feel better</h2>
<p>Once the pain has gone, your tummy might feel sore or bruised for a day or two. Go gently:</p>
<ul>
  <li>eat small, plain, low-fat meals, like porridge, toast, rice, plain potatoes or soup</li>
  <li>bring other foods back slowly, one at a time</li>
  <li>keep sipping water</li>
  <li>book a GP appointment to talk about what happened, even if you feel fine now</li>
</ul>
<p>Our <a href="{root}gallstones-diet/">gallstones diet guide</a> has a full gentle menu for the day after an attack.</p>

<h2>The best pain relief is preventing the next attack</h2>
<p>Painkillers help you get through an attack. But the thing that really makes a difference is having fewer attacks in the first place. For most people, that comes down to food:</p>
<ul>
  <li><b>Eat smaller meals, more often.</b> Big meals make your gallbladder squeeze hard.</li>
  <li><b>Don't skip meals.</b> Long gaps let bile build up.</li>
  <li><b>Cut back on the worst triggers:</b> fried food, fatty meat, takeaways, cream, butter and full-fat cheese.</li>
  <li><b>Spread your fat out</b> across the day instead of having it all at once.</li>
</ul>
<p>If attacks keep coming back even when you're careful, talk to your GP about <a href="{root}gallstones-treatment/">treatment options</a>. An operation to remove the gallbladder is the only way to stop attacks for good.</p>
<p>In the meantime, here's one thing many people don't think about when they're in pain.</p>
"""
    food = one_food(root, "avoid", "food/alcohol.svg", "Alcohol during a flare-up",
        "<p>When your gallbladder is playing up, alcohol is best avoided completely. Some painkillers, like those containing codeine, shouldn't be mixed with it. And the food that comes with drinking, like crisps, takeaways and next-morning fry-ups, is exactly what sets off attacks. Once you're feeling better, a small drink with a light meal is fine for many people.</p>",
        "alcohol-and-gallstones/", "Read our full guide to alcohol and gallstones")
    return article(path, "Gallbladder Pain Relief: What Actually Helps (and What Doesn't)", h1, desc,
                   "Pain relief", body, RELIEF_FAQ, food,
                   [NHS_TREATMENT, NHS_SYMPTOMS, IQWIG, HSE_SYMPTOMS, UHB_GALLSTONES], related_for(path))
