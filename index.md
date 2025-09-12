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


<div style="background-color: #e8f5e8; border-left: 5px solid #27ae60; padding: 20px; margin: 20px 0; border-radius: 5px;">
 <h2 style="font-size: 1.4em; color: #2c3e50; margin-bottom: 15px;">📊 LazyDAX - Free Power BI Practice File</h2>
 <p style="margin-bottom: 15px; color: #34495e;">A comprehensive Power BI file designed to help you learn DAX, test measures, and explore Power BI features. Perfect for presentations, training, or personal practice.</p>
 
 <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-bottom: 15px;">
  <div style="flex: 1; min-width: 200px;">
   <strong style="color: #27ae60;">✨ What's included:</strong>
   <ul style="margin: 5px 0; padding-left: 20px; color: #555;">
    <li>Complete star schema with sample data</li>
    <li>DAX measures organized by function type</li>
    <li>Multiple visual examples and templates</li>
    <li>Ready-to-use without server connections</li>
   </ul>
  </div>
  <div style="flex: 1; min-width: 200px;">
   <strong style="color: #27ae60;">🎯 Perfect for:</strong>
   <ul style="margin: 5px 0; padding-left: 20px; color: #555;">
    <li>Learning and testing DAX functions</li>
    <li>Creating presentations and demos</li>
    <li>Exploring Power BI capabilities</li>
    <li>Training sessions and workshops</li>
   </ul>
  </div>
 </div>
 
 <div style="text-align: center;">
  <a href="https://github.com/arnaudgastelblum/LazyDAX/raw/master/LazyDAX.pbix" style="display: inline-block; background-color: #27ae60; color: white; padding: 12px 25px; text-decoration: none; border-radius: 5px; font-weight: bold; margin-right: 10px;">
   📥 Download LazyDAX.pbix
  </a>
  <a href="/power-bi/lazydax" style="display: inline-block; background-color: #3498db; color: white; padding: 12px 25px; text-decoration: none; border-radius: 5px; font-weight: bold;">
   📖 Learn More
  </a>
 </div>
</div>


