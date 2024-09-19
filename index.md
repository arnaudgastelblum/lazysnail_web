---
layout: default
title: Home
nav_order: 1
description: "Lazysnail.net"
permalink: /
---

{:refdef: style="text-align: center;"}
![Lazysnail](assets/logo_lazysnail.png)
{: refdef}

<div style="background-color: #f0f4f8; border-left: 5px solid #3498db; padding: 15px;">
  <strong style="font-size: 1.5em;">🚀 Welcome to Lazy Snail’s Data Trails!</strong>
  <p>Join me as I explore Microsoft Fabric, Power BI, SQL Server, Obsidian, and share my personal tips and reflections on unlocking the power of data.</p>
</div>


<div style="background-color: #f0f4f8; border-left: 5px solid #3498db; padding: 15px; margin-top: 20px;">
  <h2 style="font-size: 1.5em; color: #2c3e50;">📚 Latest Articles</h2>
  <ul style="list-style-type: none; padding-left: 0;">
    {% assign sorted_pages = site.pages | sort: 'date' | reverse %}
    {% for post in sorted_pages limit: 5 %}
      {% if post.date %}
        <li style="margin-bottom: 0,5px;">
          <a href="{{ post.url }}" style="font-size: 0.9em; color: #3498db; text-decoration: none;">
            {{ post.title }}
          </a>
          <span style="font-size: 0.7em; color: #888;"> - {{ post.date | date: "%d/%m/%Y" }}</span>
        </li>
      {% endif %}
    {% endfor %}
  </ul>
</div>