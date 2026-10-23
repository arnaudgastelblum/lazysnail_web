---
layout: default
title: Tools
nav_exclude: true # in the menu as the "My tools" group (_includes/nav-tools.html)
permalink: /tools/
description: "Free tools I built: screenshots that explain, Fabric and Power BI helpers, an Obsidian plugin, VS Code extensions."
---
{% assign platforms = site.data.tools | map: "kind" | join: " · " | split: " · " | uniq %}
<section class="thero">
  <p class="thero__kicker">Tools</p>
  <h1 class="thero__title">Tools I built for my own work.<br><span>Free for yours.</span></h1>
  <p class="thero__lead">When the tool I need is missing or too heavy, I build my own. Cards marked Demo play when you hover them.</p>
  <ul class="thero__facts">
    <li><strong>{{ site.data.tools.size }}</strong> tools</li>
    <li><strong>All</strong> free</li>
    <li>{{ platforms | join: " · " }}</li>
  </ul>
</section>

{% include tool-cards.html style="featured" %}

{% include tool-cards.html style="grid" %}

<p class="tfootnote">How I build them: with <a href="/ai/two-ai-developers">Claude Code and Codex</a>. They write a lot of the code, the decisions stay mine.</p>
