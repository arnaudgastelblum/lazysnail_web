---
layout: default
title: SQL Server
nav_order: 4
has_children: false
---
{% assign section = site.data.sections | where: "key", "sql-server" | first %}
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

## All Articles
{: .section-title }

{% include article-list.html categories="SQL-Server" chips=false %}
