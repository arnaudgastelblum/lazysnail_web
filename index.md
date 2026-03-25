---
layout: default
title: Home
nav_order: 1
description: "Tips and tools for Power BI, SQL Server, and Microsoft Fabric developers"
permalink: /
---

<div class="hero">
  <img src="assets/logo_lazysnail.png" alt="LazySnail" class="hero__logo">
  <p class="hero__tagline">
    Practical tips, tools, and tutorials for <strong>Power BI</strong>, <strong>SQL Server</strong>, and <strong>Microsoft Fabric</strong> developers.
  </p>
</div>

## Browse by Topic
{: .section-title }

<div class="category-grid">
  {% assign fabric_count = 0 %}{% assign pbi_count = 0 %}{% assign sql_count = 0 %}{% assign obsidian_count = 0 %}{% assign other_count = 0 %}
  {% for page in site.pages %}{% if page.date %}{% if page.categories contains "fabric" %}{% assign fabric_count = fabric_count | plus: 1 %}{% endif %}{% if page.categories contains "power-bi" %}{% assign pbi_count = pbi_count | plus: 1 %}{% endif %}{% if page.categories contains "SQL-Server" %}{% assign sql_count = sql_count | plus: 1 %}{% endif %}{% if page.categories contains "Obsidian" %}{% assign obsidian_count = obsidian_count | plus: 1 %}{% endif %}{% if page.categories contains "other" %}{% assign other_count = other_count | plus: 1 %}{% endif %}{% endif %}{% endfor %}
  <a href="/docs/Power-BI" class="category-card">
    <span class="category-card__icon">📊</span>
    <span class="category-card__info">
      <span class="category-card__name">Power BI</span>
      <span class="category-card__count">{{ pbi_count }} articles</span>
    </span>
  </a>
  <a href="/docs/SQL%20Server" class="category-card">
    <span class="category-card__icon">🛢️</span>
    <span class="category-card__info">
      <span class="category-card__name">SQL Server</span>
      <span class="category-card__count">{{ sql_count }} articles</span>
    </span>
  </a>
  <a href="/docs/Fabric" class="category-card">
    <span class="category-card__icon">🧵</span>
    <span class="category-card__info">
      <span class="category-card__name">Microsoft Fabric</span>
      <span class="category-card__count">{{ fabric_count }} articles</span>
    </span>
  </a>
  <a href="/docs/Obsidian" class="category-card">
    <span class="category-card__icon">🧠</span>
    <span class="category-card__info">
      <span class="category-card__name">Obsidian</span>
      <span class="category-card__count">{{ obsidian_count }} articles</span>
    </span>
  </a>
  <a href="/docs/Other" class="category-card">
    <span class="category-card__icon">📚</span>
    <span class="category-card__info">
      <span class="category-card__name">Other</span>
      <span class="category-card__count">{{ other_count }} articles</span>
    </span>
  </a>
</div>

## Latest Articles
{: .section-title }

<ul class="article-list">
  {% assign sorted_pages = site.pages | sort: 'date' | reverse %}
  {% assign count = 0 %}
  {% for post in sorted_pages %}
    {% if post.date and count < 8 %}
      <li class="article-item">
        <span>
          <span class="article-category">{{ post.categories }}</span>
          <a href="{{ post.url }}">{{ post.title }}</a>
        </span>
        <span class="article-date">{{ post.date | date: "%d %b %Y" }}</span>
      </li>
      {% assign count = count | plus: 1 %}
    {% endif %}
  {% endfor %}
</ul>

<div class="promo-box">
  <div class="promo-box__title">LazyDAX - Free Power BI Practice File</div>
  <p class="promo-box__description">A comprehensive Power BI file designed to help you learn DAX, test measures, and explore Power BI features. Perfect for presentations, training, or personal practice.</p>
  <ul class="promo-box__features">
    <li>Complete star schema with sample data</li>
    <li>DAX measures organized by function type</li>
    <li>Multiple visual examples and templates</li>
    <li>Ready to use without server connections</li>
  </ul>
  <div class="promo-box__buttons">
    <a href="https://github.com/arnaudgastelblum/LazyDAX/raw/master/LazyDAX.pbix" class="btn-primary-custom">Download LazyDAX.pbix</a>
    <a href="/en/lazydax-a-power-bi-file-for-your-presentation-discoveries-or-learn-dax/" class="btn-secondary-custom">Learn More</a>
  </div>
</div>
