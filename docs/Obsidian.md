---
layout: default
title: Obsidian
nav_order: 5
has_children: false
---
# Obsidian

<div class="category-header">

{:refdef: style="text-align: center;"}
  ![Obsidian](../assets/2023/ObsidianLazysnail copy_500.png){: .image50}
{: refdef}

</div>

## All Articles
{: .section-title }

<ul class="article-list">
  {% assign sorted_pages = site.pages | sort: 'date' | reverse %}
  {% for post in sorted_pages %}
    {% if post.date and post.categories contains "Obsidian" %}
      <li class="article-item">
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span class="article-date">{{ post.date | date: "%d %b %Y" }}</span>
      </li>
    {% endif %}
  {% endfor %}
</ul>
