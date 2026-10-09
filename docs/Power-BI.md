---
layout: default
title: Power BI & Fabric
nav_order: 2
has_children: false
description: "Power BI and Microsoft Fabric: semantic models, DAX, SQL warehouses and the tooling around them."
---
# Power BI & Fabric

<p class="section-lead">Semantic models first, then DAX, SQL warehouses in Fabric, and the small tools that make a data team faster.</p>

![Power BI and Fabric](/assets/2026/site/fabric-powerbi.webp){: .section-art }

## All Articles
{: .section-title }

<ul class="article-list">
  {% assign sorted_pages = site.pages | sort: 'date' | reverse %}
  {% for post in sorted_pages %}
    {% if post.date and post.categories contains "power-bi" or post.date and post.categories contains "fabric" %}
      <li class="article-item">
        <span>
          {% if post.categories contains "fabric" %}<span class="article-category">Fabric</span>{% else %}<span class="article-category">Power BI</span>{% endif %}
          <a href="{{ post.url }}">{{ post.title }}</a>
        </span>
        <span class="article-date">{{ post.date | date: "%d %b %Y" }}</span>
      </li>
    {% endif %}
  {% endfor %}
</ul>
