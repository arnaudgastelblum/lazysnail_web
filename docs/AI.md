---
layout: default
title: AI
nav_order: 6
has_children: false
---
# AI

## All Articles
{: .section-title }

<ul class="article-list">
  {% assign sorted_pages = site.pages | sort: 'date' | reverse %}
  {% for post in sorted_pages %}
    {% if post.date and post.categories contains "ai" %}
      <li class="article-item">
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span class="article-date">{{ post.date | date: "%d %b %Y" }}</span>
      </li>
    {% endif %}
  {% endfor %}
</ul>
