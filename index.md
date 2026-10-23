---
layout: default
title: Home
nav_order: 1
description: "Arnaud Gastelblum, freelance data consultant. Microsoft Fabric, Power BI and data modeling, with AI in my daily work."
permalink: /
---

{% assign labels = "power-bi:Power BI|fabric:Fabric|SQL-Server:SQL Server|ai:AI|Obsidian:Obsidian|other:Tools" | split: "|" %}

<section class="hero-pro is-compact">
  <div class="hero-pro__side">
    <img class="hero-pro__photo" src="/assets/2023/Arnaud_Cartoon.png" alt="Arnaud Gastelblum">
    <div class="hero-pro__links">
      <a href="https://www.linkedin.com/in/arnaud-gastelblum/">LinkedIn</a>
      <a href="{% link docs/About.md %}">About me</a>
    </div>
  </div>
  <div class="hero-pro__text">
    <p class="hero-pro__kicker">Freelance data consultant</p>
    <h1 class="hero-pro__name">Arnaud Gastelblum</h1>
    <p class="hero-pro__line">I build data models people trust, on <strong>Microsoft Fabric</strong> and <strong>Power BI</strong>. AI is part of my daily work, and my notes live in <strong>Obsidian</strong>.</p>
  </div>
</section>

<div class="pillars">
  {% assign n_bi = 0 %}{% assign n_sql = 0 %}{% assign n_ai = 0 %}{% assign n_obs = 0 %}
  {% for p in site.pages %}{% if p.date %}
    {% if p.categories contains "power-bi" or p.categories contains "fabric" %}{% assign n_bi = n_bi | plus: 1 %}{% endif %}
    {% if p.categories contains "SQL-Server" %}{% assign n_sql = n_sql | plus: 1 %}{% endif %}
    {% if p.categories contains "ai" %}{% assign n_ai = n_ai | plus: 1 %}{% endif %}
    {% if p.categories contains "Obsidian" %}{% assign n_obs = n_obs | plus: 1 %}{% endif %}
  {% endif %}{% endfor %}
  <a class="pillar" href="{% link docs/Power-BI.md %}">
    <span class="pillar__name">Power BI &amp; Fabric</span>
    <span class="pillar__desc">Semantic models, DAX, Fabric warehouses</span>
    <span class="pillar__count">{{ n_bi }} articles</span>
  </a>
  <a class="pillar" href="{% link docs/SQL Server.md %}">
    <span class="pillar__name">SQL Server</span>
    <span class="pillar__desc">T-SQL, SSIS, SSMS, the solid ground</span>
    <span class="pillar__count">{{ n_sql }} articles</span>
  </a>
  <a class="pillar" href="{% link docs/AI.md %}">
    <span class="pillar__name">AI</span>
    <span class="pillar__desc">Claude Code, Codex, AI in a data job</span>
    {% assign ai_tools = site.data.tools | where: "ai", true %}
    <span class="pillar__count">{{ n_ai }} articles · {{ ai_tools.size }} tools</span>
  </a>
  <a class="pillar" href="{% link docs/Obsidian.md %}">
    <span class="pillar__name">Obsidian</span>
    <span class="pillar__desc">Notes, tasks, a calm way to work</span>
    <span class="pillar__count">{{ n_obs }} articles</span>
  </a>
</div>

## Latest articles
{: .section-title }

<ul class="article-list">
  {% assign sorted_pages = site.pages | sort: 'date' | reverse %}
  {% assign count = 0 %}
  {% for post in sorted_pages %}
    {% if post.date and count < 8 %}
      {% assign label = post.categories %}
      {% for pair in labels %}{% assign kv = pair | split: ":" %}{% if post.categories contains kv[0] %}{% assign label = kv[1] %}{% endif %}{% endfor %}
      <li class="article-item">
        <span>
          <span class="article-category">{{ label }}</span>
          <a href="{{ post.url }}">{{ post.title }}</a>
        </span>
        <span class="article-date">{{ post.date | date: "%d %b %Y" }}</span>
      </li>
      {% assign count = count | plus: 1 %}
    {% endif %}
  {% endfor %}
</ul>

## Tools I built
{: .section-title }

{% include tool-cards.html style="compact" home=true %}

<p class="tools-more" style="--accent: #1b8aa6"><a class="tlink" href="/tools/">See all {{ site.data.tools.size }} tools</a></p>
