---
layout: default
title: Home
nav_order: 1
description: "Lazysnail.net"
permalink: /
---

{:refdef: style="text-align: center;"}
  ![LazySnail](assets/images/logo_lazysnail.png)
{: refdef}

{: .note-title } 
>**   You landed on a data lover web page!
>
> I’m sharing my discoveries and thought about **Microsoft Power BI**, **SQL Server**, **Obsidian** and **Data** in general.

{:refdef: style="text-align: center;"}
  [YouTube](docs/Youtube){: .btn .btn-purple .mr-4  } 
  [Practice DAX](./en/lazydax-a-power-bi-file-for-your-presentation-discoveries-or-learn-dax){: .btn .btn-green .mr-4  }
{: refdef}


{% comment %}

---
# Latest articles

<ul>
    {% assign posts = site.pages | sort: 'last_modified' | reverse %}
    {% for post in posts %}

      {% if post.last_modified and post.last_modified != '' %}
        <li><code><font color="#5C5962">[{{  post.parent }}]</font></code>    <a href="{{ post.url }}">{{ post.title }}</a></li>
      {% endif %}
    {% endfor %}
</ul>


{% endcomment %}

