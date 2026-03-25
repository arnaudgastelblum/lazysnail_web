---
layout: default
title: SQL Server
nav_order: 4
has_children: false
---
# SQL Server

<div class="category-header">

![SQL Server](../assets/2023/SQL-Server_500.png){: .image50}

</div>

## All Articles
{: .section-title }

<ul class="article-list">
  {% assign sorted_pages = site.pages | sort: 'date' | reverse %}
  {% for post in sorted_pages %}
    {% if post.date and post.categories contains "SQL-Server" %}
      <li class="article-item">
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span class="article-date">{{ post.date | date: "%d %b %Y" }}</span>
      </li>
    {% endif %}
  {% endfor %}
</ul>
