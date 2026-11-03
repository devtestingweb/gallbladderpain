/* ==========================================================
   GallbladderPain.org site settings — edit these two blocks only.
   ========================================================== */

/* 1. BANNER AD
   Shown on every article page (in the side column and part-way down the article).
   Change it here and every page updates. Set enabled: false to hide it everywhere. */
var BANNER = {
  enabled: true,
  url: "https://example.com/your-offer-page",   // <-- paste your sales page / affiliate link
  headline: "Looking for extra digestive support?",
  text: "See the natural formula our readers ask about most.",
  button: "Learn more"
};

/* 2. EMAIL SIGN-UP FORM
   Paste the form "action" URL from MailerLite or Kit, and the name of their email field.
   While action is empty the form shows a test message instead of sending anything.
   Kit example:        action "https://app.kit.com/forms/1234567/subscriptions", emailField "email_address", nameField "first_name"
   MailerLite example: action "https://assets.mailerlite.com/jsonp/ACCOUNT_ID/forms/FORM_ID/subscribe", emailField "fields[email]", nameField "fields[name]" */
var OPTIN = {
  action: "",
  emailField: "email",
  nameField: "name",
  thankYouPage: "thank-you/"   // relative to the site root
};

/* ---------- no need to edit below this line ---------- */
(function () {
  var root = document.documentElement.getAttribute("data-root") || "";

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  if (BANNER.enabled) {
    var html =
      '<a class="ad" href="' + esc(BANNER.url) + '" rel="sponsored noopener" target="_blank">' +
      '<div class="ad-label">Advertisement</div>' +
      '<div class="ad-head">' + esc(BANNER.headline) + '</div>' +
      '<div class="ad-sub">' + esc(BANNER.text) + '</div>' +
      '<span class="ad-btn">' + esc(BANNER.button) + ' &rarr;</span></a>';
    document.querySelectorAll("[data-ad]").forEach(function (el) { el.innerHTML = html; });
  }

  document.querySelectorAll("form[data-optin]").forEach(function (form) {
    var email = form.querySelector('input[type="email"]');
    var name = form.querySelector('input[type="text"]');
    if (OPTIN.action) {
      form.action = OPTIN.action;
      form.method = "post";
      email.name = OPTIN.emailField;
      if (name) name.name = OPTIN.nameField;
      var redirect = document.createElement("input");
      redirect.type = "hidden";
      redirect.name = "redirect";
      redirect.value = new URL(root + OPTIN.thankYouPage, location.href).href;
      form.appendChild(redirect);
    } else {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var msg = form.querySelector(".msg") || document.createElement("p");
        msg.className = "msg";
        msg.textContent = "Test mode: the sign-up form isn't connected yet. Add your email provider's form address in assets/js/site.js.";
        form.appendChild(msg);
      });
    }
  });
})();

/* Floating "Get the free Fridge Guide" button (phones): hide it while a sign-up box is on screen,
   and on pages without a sign-up box. */
(function () {
  var bar = document.querySelector(".sticky-cta");
  if (!bar) return;
  if (!document.getElementById("get-guide")) { bar.remove(); document.body.style.paddingBottom = "0"; return; }
  if (!("IntersectionObserver" in window)) return;
  var visible = new Set();
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { e.isIntersecting ? visible.add(e.target) : visible.delete(e.target); });
    bar.classList.toggle("is-hidden", visible.size > 0);
  }, { threshold: 0.15 });
  document.querySelectorAll(".optin").forEach(function (el) { io.observe(el); });
})();
