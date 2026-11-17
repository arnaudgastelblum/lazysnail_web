---
layout: default
title: All articles
nav_exclude: true # reached from the home page and from the end of every article
permalink: /articles/
description: "Every article on LazySnail, newest first: Power BI and Microsoft Fabric, SQL Server, AI and Obsidian."
---
{%- assign article_count = 0 -%}
{%- for p in site.pages -%}{%- if p.date -%}{%- assign article_count = article_count | plus: 1 -%}{%- endif -%}{%- endfor %}
<div class="home">
<section class="home-section home-section--first" aria-labelledby="articles-title">
<h1 id="articles-title">All articles</h1>
<p class="home-section__lead">{{ article_count }} articles, newest first.</p>
<p class="home-sections">{% for s in site.data.sections %}<a class="home-link" href="{{ s.url }}">{{ s.name }}</a>{% endfor %}</p>
</section>
<section class="home-section">
{% include article-list.html %}
</section>
</div>
