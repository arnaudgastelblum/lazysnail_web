---
layout: default
title: Home
nav_order: 1
description: "Arnaud Gastelblum, freelance data consultant. Microsoft Fabric, Power BI and data modeling, with AI in my daily work."
permalink: /
---

<section class="home-profile" aria-labelledby="home-name">
<div class="home-profile__copy">
<p class="home-eyebrow">Independent data consultant</p>
<h1 id="home-name">Arnaud Gastelblum</h1>
<p class="home-profile__title">Data Architect, Microsoft Fabric &amp; Power BI</p>
<p class="home-profile__intro">I turn business questions into Kimball data models, then build them in SQL on Microsoft Fabric. I deliver Power BI semantic models and coach teams on modelling, SQL and DAX.</p>
<p class="home-profile__location">Belgium &middot; Hybrid in the Brussels area</p>
<div class="home-profile__actions">
<a class="home-profile__primary" href="https://www.linkedin.com/in/arnaud-gastelblum/">Let's talk on LinkedIn <span aria-hidden="true">&rarr;</span></a>
<a class="home-profile__secondary" href="{% link docs/About.md %}">About me <span aria-hidden="true">&rarr;</span></a>
</div>
{% if site.data.profile.available %}
<p class="home-profile__availability">{{ site.data.profile.availability_label }}</p>
{% endif %}
</div>
<div class="home-profile__visual" style="--accent: #6d5ef5">
<div class="home-profile__frame"><img src="/assets/2023/Arnaud_Cartoon.png" alt="Cartoon portrait of Arnaud Gastelblum" width="231" height="254"></div>
<span class="home-profile__chip home-profile__chip--fabric">Microsoft Fabric</span>
<span class="home-profile__chip home-profile__chip--bi">Power BI</span>
<span class="home-profile__chip home-profile__chip--kimball">Kimball</span>
<span class="home-profile__chip home-profile__chip--sql">SQL</span>
</div>
</section>
<div class="home-proof" aria-label="Experience">
<p><strong>18 years</strong><span>on the Microsoft data platform</span></p>
<p><strong>Across sectors</strong><span>Lottery, automotive, financial regulation, insurance and retail</span></p>
</div>

<section class="home-topics" aria-labelledby="home-topics-title">
<div class="home-topics__heading">
<p class="home-eyebrow">From my workbench</p>
<h2 id="home-topics-title">What I write about</h2>
</div>
{%- assign ai_tools = site.data.tools | where: "ai", true -%}
<div class="home-topics__grid">
{%- for s in site.data.sections -%}
{%- if s.key == "other" -%}{%- continue -%}{%- endif -%}
{%- assign n = 0 -%}
{%- for p in site.pages -%}{%- if p.date -%}{%- assign hit = false -%}{%- for cat in s.categories -%}{%- if p.categories contains cat[0] -%}{%- assign hit = true -%}{%- endif -%}{%- endfor -%}{%- if hit -%}{%- assign n = n | plus: 1 -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- case s.key -%}
{%- when "power-bi" -%}{%- assign blurb = "How I build semantic models in Fabric, DAX included." -%}
{%- when "sql-server" -%}{%- assign blurb = "The T-SQL, SSIS and SSAS I use on projects." -%}
{%- when "ai" -%}{%- assign blurb = "How I work with coding agents day to day." -%}
{%- when "obsidian" -%}{%- assign blurb = "How I keep my notes and tasks in Obsidian." -%}
{%- else -%}{%- assign blurb = "" -%}
{%- endcase -%}
<article class="home-topic" style="--accent: {{ s.accent }}">
<div class="home-topic__head"><span class="home-topic__tile">{% include section-icon.html key=s.key %}</span><h3 class="home-topic__name">{{ s.name | escape }}</h3></div>
<p class="home-topic__blurb">{{ blurb }}</p>
<a class="home-topic__link" href="{{ s.url }}" aria-label="{{ s.name | escape }}: {{ n }} article{% unless n == 1 %}s{% endunless %}{% if s.key == "ai" %}, {{ ai_tools.size }} tools built with AI{% endif %}"><span class="home-topic__count">{{ n }} article{% unless n == 1 %}s{% endunless %} <span class="home-topic__arrow" aria-hidden="true">&rarr;</span></span>{% if s.key == "ai" %}<span class="home-topic__extra">{{ ai_tools.size }} tools built with AI</span>{% endif %}</a>
</article>
{%- endfor -%}
</div>
</section>

## Latest articles
{: .section-title }

{% include article-list.html limit=8 %}

## Tools I built
{: .section-title }

{% include tool-cards.html style="compact" home=true %}

<p class="tools-more" style="--accent: #1b8aa6"><a class="tlink" href="/tools/">See all {{ site.data.tools.size }} tools</a></p>
