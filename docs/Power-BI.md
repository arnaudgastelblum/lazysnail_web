---
layout: default
title: Power BI
nav_order: 3
has_children: false
---
# Power BI

![Alt text](../assets/2023/PowerBI_IceCream_500.png){: .image60 }


<div style="background-color: #f0f4f8; border-left: 5px solid #3498db; padding: 20px; margin-top: 30px; border-radius: 5px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);">
  <h2 style="font-size: 1.6em; color: #2c3e50; margin-bottom: 15px;">📊 Latest Articles on Power BI</h2>
    {% assign sorted_pages = site.pages | sort: 'date' | reverse %}
    {% for post in sorted_pages %}
      {% if post.date and post.categories contains "power-bi" %}
          <a href="{{ post.url }}" style="font-size: 1em; color: #3498db; text-decoration: none; transition: color 0.3s ease;">
            {{ post.title }}
          </a>
          <span style="font-size: 0.8em; color: #888;"> - {{ post.date | date: "%d/%m/%Y" }}</span>
          <div style="height: 5px;"></div> <!-- Custom small space -->
      {% endif %}
    {% endfor %}
</div>
