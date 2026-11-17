---
layout: default
title: "Arnaud Gastelblum, Data Architect for Fabric & Power BI"
nav_title: Home
nav_order: 1
description: "Arnaud Gastelblum, freelance Data Architect. Microsoft Fabric, Power BI and data modelling, with AI in my daily work."
permalink: /
---

<div class="home">

<section class="home-hero" aria-labelledby="home-name">
<div class="home-hero__copy">
<h1 id="home-name">Arnaud Gastelblum</h1>
<p class="home-hero__role">Data Architect, Microsoft Fabric &amp; Power BI</p>
<p class="home-hero__intro">I turn business questions into Kimball data models, then build them in SQL on Microsoft Fabric. I deliver Power BI semantic models and coach teams on modelling, SQL and DAX. AI is part of my daily work, and in my spare time I vibe code the tools I miss.</p>
<p class="home-hero__links">
<a class="home-link home-link--strong" href="/contact/">Get in touch</a>
<a class="home-link" href="{% link docs/About.md %}">About me</a>
</p>
{% if site.data.profile.available %}<p class="home-hero__meta">{{ site.data.profile.availability_label }}</p>{% endif %}
</div>
<img class="home-hero__portrait" src="/assets/2026/site/arnaud-cartoon.jpg" alt="Portrait of Arnaud Gastelblum" width="480" height="528">
</section>

<section class="home-section" aria-labelledby="home-tools-title">
<div class="home-section__head">
<h2 id="home-tools-title">Tools I vibe coded</h2>
<a class="home-link" href="/ai/two-ai-developers">How I build with AI</a>
</div>
<p class="home-section__sub">Built in my spare time with Claude Code and Codex, and free to use.</p>
{% include tool-picker.html %}
</section>

<section class="home-section" aria-labelledby="home-latest-title">
<div class="home-section__head">
<h2 id="home-latest-title">Latest articles</h2>
<a class="home-link" href="/articles/">All articles</a>
</div>
{% include article-list.html limit=6 %}
<p class="home-sections">{% for s in site.data.sections %}<a class="home-link" href="{{ s.url }}">{{ s.name }}</a>{% endfor %}</p>
</section>

</div>
