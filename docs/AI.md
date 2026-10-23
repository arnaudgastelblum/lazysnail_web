---
layout: default
title: AI
nav_order: 6
has_children: false
---
# AI

{:refdef: style="text-align: center;"}
  ![The Lazysnail AI mascot](/assets/2026/site/ai-snail.webp){: .mascot }
{: refdef}

## Built with AI
{: .section-title }

<p class="tools-intro">Tools I built with Claude Code, and now Codex too. All free.</p>

{% include tool-cards.html style="compact" ai=true %}

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
