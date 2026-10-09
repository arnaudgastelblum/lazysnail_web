---
layout: default
title: Fabric
nav_order: 3
has_children: false
nav_exclude: true
---
# Fabric

{: .note }
> Fabric now lives with Power BI: see [Power BI & Fabric](Power-BI). The Fabric articles are listed below too.

{:refdef: style="text-align: center;"}
  ![Fabric](../assets/2024/Fabric.webp){: .image50}
{: refdef}


## All Articles
{: .section-title }

<ul class="article-list">
  {% assign sorted_pages = site.pages | sort: 'date' | reverse %}
  {% for post in sorted_pages %}
    {% if post.date and post.categories contains "fabric" %}
      <li class="article-item">
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span class="article-date">{{ post.date | date: "%d %b %Y" }}</span>
      </li>
    {% endif %}
  {% endfor %}
</ul>
