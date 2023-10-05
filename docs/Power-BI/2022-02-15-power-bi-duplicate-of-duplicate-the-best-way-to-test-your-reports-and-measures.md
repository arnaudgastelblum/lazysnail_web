---
layout: post
title: 'Power BI: Duplicate of Duplicate - The best way to test your reports and measures'
date: 2022-02-15 08:55:11.000000000 +01:00
categories: "power-bi"
tags: [powerbi, tips]
comments: true
permalink: "/en/power-bi-duplicate-of-duplicate-the-best-way-to-test-your-reports-and-measures/"
parent: Power BI
---
# {{ page.title }}
{: .fs-9 }

<p><!-- wp:paragraph --></p>
<p>This article seems obvious, but that's something that I do a lot, and this is the first thing I do when somebody asks me a question.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>After many weeks, some clients tell me: "Now<strong>, I'm using your technique too"</strong></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>But I don't feel to own this! It's pretty simple, but in fact, if you didn't use it before, it can help you a lot!</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:pullquote --></p>

<p>So, yes, I'm duplicating my page!</p>
<p><cite>A lot!!!!</cite>

<h2 id="a-focus-version">A focus version:</h2>

<div class="wp-block-image">
<figure class="aligncenter size-full is-resized"><img src="/assets/2022/02/image-5.png" alt="" class="wp-image-5160" width="400" height="302" /></figure>
</div>
<p><!-- /wp:image --></p>
<p><!-- wp:paragraph --></p>
<p>When I have an issue or a question, <strong>the first thing I do</strong> (after crying),<strong> it's duplicate the page</strong>.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>On this page, I remove everything not useful to test</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:list --></p>
<ul>
<li>Visuals</li>
<li>Images</li>
</ul>
<p><!-- /wp:list --></p>
<p><!-- wp:paragraph --></p>
<p>I transform all the visuals I want to test (hopefully only one) into a table.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>Let's call it the "<strong><mark style="background-color:rgba(0, 0, 0, 0)" class="has-inline-color has-vivid-green-cyan-color">focus version</mark></strong>"</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:heading --></p>
<h2 id="test-your-filter-context">Test your filter context:</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:paragraph --></p>
<p>When I have a cleaner version of my report I can <strong>duplicate it.</strong> (again)</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:image {"align":"center"} --></p>
<div class="wp-block-image">
<figure class="aligncenter"><img src="{{ site.baseurl }}/assets/2022/02/f6e80202aad027758143bbb97a6f856f.png" alt="Introduction To Textures in Direct3D 11 (Windows) | Data design, Texture,  Visualisation" /></figure>
</div>
<p><!-- /wp:image --></p>
<p><!-- wp:paragraph --></p>
<p>On this new page, I <strong>remove one by one</strong>:</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:list --></p>
<ul>
<li>Filter on slicers</li>
<li>Filter in the filter pane (Be careful to remove the one hidden)</li>
<li>Hidden Slicers (Synced slicers)</li>
</ul>
<p><!-- /wp:list --></p>
<p><!-- wp:paragraph --></p>
<p><strong>Until my values change and I can understand them.</strong></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>This step helps me to trust the data and understand the measure. It also helps me to trust the behavior of each filters.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:heading --></p>
<h2 id="test-one-particular-case">Test one particular case:</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:paragraph --></p>
<p>You are the best and main debugger of Power BI!</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:image {"align":"center"} --></p>
<div class="wp-block-image">
<figure class="aligncenter"><img src="{{ site.baseurl }}/assets/2022/02/83827-200.png" alt="debug Icon - Download debug Icon 83827 | Noun Project" /></figure>
</div>
<p><!-- /wp:image --></p>
<p><!-- wp:paragraph --></p>
<p>Based on the previous topic, now you are confident with your evaluation context! I would recommend you to filter on a very specific case available in your data.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>For example:&nbsp;</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:list --></p>
<ul>
<li>One transaction ID (one row in your sales table)</li>
<li>One Invoice Id</li>
</ul>
<p><!-- /wp:list --></p>
<p><!-- wp:paragraph --></p>
<p>Many users don't look their data at a very low level, and trust me, that's very important!</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>If you know the story and behavior of your DAX measure for a very specific case, you can predict how it will work for 2 and many more.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:heading --></p>
<h2 id="split-your-measures-and-display-their-result">Split your measures and display their result</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:paragraph --></p>
<p>In our DAX measure, we can have multiple steps and complexity. That's why the best practice is to use Variables (VAR), and I know that you already use it!</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:image {"align":"center"} --></p>
<div class="wp-block-image">
<figure class="aligncenter"><img src="{{ site.baseurl }}/assets/2022/02/Metal-Cover-VGA-Touch-Screen-Monitor-voor-Industri-le-PC-Mini-pc-monitor-MINI-itx.jpg" alt="Metal Cover VGA Touch Screen Monitor voor Industriële PC. Mini pc monitor  MINI itx Display|touch screen monitor|vga touch screentouch screen -  AliExpress" /></figure>
</div>
<p><!-- /wp:image --></p>
<p><!-- wp:paragraph --></p>
<p>But do you test it? How to do it?</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:list --></p>
<ul>
<li>Duplicate your measure (yes, Duplicate duplicate everywhere) and change the RETURN section by returning the value of one of your variable.</li>
</ul>
<p><!-- /wp:list --></p>
<p><!-- wp:paragraph --></p>
<p>Many month after our work some changes can impact our measure!&nbsp;</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:list --></p>
<ul>
<li>Relation between tables can be different</li>
<li>Data aren't the same again</li>
<li>You change the slicer with a different attribute! (Same value, but different attribute, ..)</li>
</ul>
<p><!-- /wp:list --></p>
<p><!-- wp:paragraph --></p>
<p>By testing your old good variables, you can trust and confirm how they work. (Specially if everything is still ok for your evaluation context)</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:heading --></p>
<h2 id="conclusion">Conclusion:</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:paragraph --></p>
<p>Most of the time, on a report, crowded with many visuals we aren't able to find the main reason for our "problem".</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>We keep focus on not useful stuff and we are to scare (or lazy) to have a look deep dive.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>In two sentences:</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:list {"ordered":true} --></p>
<ol>
<li><mark style="background-color:rgba(0, 0, 0, 0)" class="has-inline-color has-vivid-green-cyan-color"><strong>Less is more</strong></mark></li>
<li><mark style="background-color:rgba(0, 0, 0, 0)" class="has-inline-color has-vivid-green-cyan-color"><strong>Duplicate your page et destroy everything</strong></mark></li>
</ol>
<p><!-- /wp:list --></p>
<p><!-- wp:paragraph --></p>
<p>Bonus: Duplicate page and measure is one point! But don't forget to duplicate your .PBIX file.. In case of emergency :)</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>I wish you all the best and a lot of duplication.</p>
<p><!-- /wp:paragraph --></p>
