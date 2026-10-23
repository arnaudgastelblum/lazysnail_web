---
layout: default
title: Power BI & Fabric
nav_order: 2
has_children: false
description: "Power BI and Microsoft Fabric: semantic models, DAX, SQL warehouses and the tooling around them."
---
{% assign section = site.data.sections | where: "key", "power-bi" | first %}
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
<p class="section-lead">Semantic models first, then DAX, SQL warehouses in Fabric, and the small tools that make a data team faster.</p>
<p class="section-header__count">{{ article_count }} {% if article_count == 1 %}article{% else %}articles{% endif %}</p>
</div>
</header>

## All Articles
{: .section-title }

{% include article-list.html categories="power-bi,fabric" %}
