---
layout: default
title: Power BI
nav_order: 2
has_children: false
---
# Power BI

<div class="category-header">

![Power BI](../assets/2023/PowerBI_IceCream_500.png){: .image50 }

</div>

## All Articles
{: .section-title }

<ul class="article-list">
  {% assign sorted_pages = site.pages | sort: 'date' | reverse %}
  {% for post in sorted_pages %}
    {% if post.date and post.categories contains "power-bi" %}
      <li class="article-item">
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span class="article-date">{{ post.date | date: "%d %b %Y" }}</span>
      </li>
    {% endif %}
  {% endfor %}
</ul>
