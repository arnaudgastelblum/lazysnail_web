---
layout: default
title: Contact
nav_order: 1.6
permalink: /contact/
description: "Write to Arnaud Gastelblum, Data Architect for Microsoft Fabric and Power BI: a project, a question, or just hello."
---
{%- comment -%}
  The contact form. Messages go through Web3Forms to Arnaud's inbox: the address is never in the page.
  The access key (public by design: it can only send to that inbox) is in _data/profile.yml.
  The form is sent in the background, so the visitor stays here and sees a thank-you line.
{%- endcomment -%}
<div class="home">
<section class="home-section home-section--first" aria-labelledby="contact-title">
<h1 id="contact-title">Get in touch</h1>
<p class="home-section__lead">A project on Fabric or Power BI, a question about an article or a tool, or just to say hello: write to me here and I'll get back to you.</p>
</section>
<section class="home-section">
<form class="contact-form" data-contact action="https://api.web3forms.com/submit" method="POST">
<input type="hidden" name="access_key" value="{{ site.data.profile.contact_form_key }}">
<input type="hidden" name="subject" value="New message from lazysnail.net">
<input type="hidden" name="from_name" value="lazysnail.net">
<input type="hidden" name="redirect" value="{{ site.url }}/contact/?sent=1">
<input type="checkbox" name="botcheck" class="contact-form__trap" tabindex="-1" autocomplete="off" aria-hidden="true">
<p class="contact-form__field"><label for="contact-name">Name</label><input id="contact-name" name="name" type="text" autocomplete="name" required></p>
<p class="contact-form__field"><label for="contact-email">Email</label><input id="contact-email" name="email" type="email" autocomplete="email" required></p>
<p class="contact-form__field"><label for="contact-message">Message</label><textarea id="contact-message" name="message" rows="6" required></textarea></p>
<p class="contact-form__actions"><button type="submit" class="contact-form__send">Send</button><span class="contact-form__status" role="status" aria-live="polite"></span></p>
<p class="contact-form__note">Your message goes straight to my inbox through Web3Forms. Nothing is kept on this site.</p>
</form>
<p class="home-sections"><a class="home-link" href="https://www.linkedin.com/in/arnaud-gastelblum/">Prefer LinkedIn? Message me there</a></p>
</section>
</div>
<script>
  /* Send the form in the background and answer on the page; without JavaScript, or if that fails, the form is posted normally. No // comments: the page is minified onto one line. */
  document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelector('[data-contact]');
    if (!form || !window.fetch) return;
    var button = form.querySelector('.contact-form__send');
    var status = form.querySelector('.contact-form__status');
    var thanks = 'Thanks, your message is on its way. I’ll get back to you soon.';
    if (/[?&]sent=1/.test(location.search)) { status.textContent = thanks; status.className = 'contact-form__status is-sent'; }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var data = {};
      new FormData(form).forEach(function (value, key) { if (key !== 'redirect') data[key] = value; });
      button.disabled = true;
      status.textContent = 'Sending…';
      status.className = 'contact-form__status';
      fetch(form.action, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { return r.json(); })
        .then(function (r) {
          if (!r.success) throw new Error(r.message || 'not sent');
          form.reset();
          status.textContent = thanks;
          status.className = 'contact-form__status is-sent';
        })
        .catch(function (err) {
          /* The browser could not reach the service in the background: send the form the classic way, the service brings the visitor back here with ?sent=1. */
          if (err instanceof TypeError) { form.submit(); return; }
          status.textContent = 'Sorry, the message could not be sent. Please try again, or write to me on LinkedIn.';
          status.className = 'contact-form__status is-error';
        })
        .then(function () { button.disabled = false; });
    });
  });
</script>
