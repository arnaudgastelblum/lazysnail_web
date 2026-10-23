---
layout: default
title: AI
nav_order: 6
has_children: false
---
{% assign section = site.data.sections | where: "key", "ai" | first %}
{% assign article_count = 0 %}
{% for article in site.pages %}
{% if article.date %}
{% for category in section.categories %}
{% if article.categories contains category[0] %}
{% assign article_count = article_count | plus: 1 %}
{% break %}
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}

<header class="section-header" style="--accent: {{ section.accent }}">
<span class="section-header__icon" aria-hidden="true">{% include section-icon.html key=section.key %}</span>
<div class="section-header__copy">
<h1>{{ page.title | escape }}</h1>

<p class="section-header__count">{{ article_count }} {% if article_count == 1 %}article{% else %}articles{% endif %}</p>
</div>
</header>

## Built with AI
{: .section-title }

<p class="tools-intro">Tools I built with Claude Code, and now Codex too. All free.</p>

{% include tool-cards.html style="compact" ai=true %}

## All Articles
{: .section-title }

{% include article-list.html categories="ai" chips=false %}
