---
layout: default
title: Home
nav_order: 1
description: "Tips and tools for Power BI, SQL Server, and Microsoft Fabric developers"
permalink: /
---

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

<div class="promo-box promo-box--blue">
  <div class="promo-box__title">Code Formatter - DAX & SQL</div>
  <p class="promo-box__description">Format your DAX and SQL code instantly. A free online tool to keep your queries clean and readable.</p>
  <div class="promo-box__buttons">
    <a href="https://code.lazysnail.net" class="btn-primary-custom" target="_blank">Open Code Formatter</a>
  </div>
</div>

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
