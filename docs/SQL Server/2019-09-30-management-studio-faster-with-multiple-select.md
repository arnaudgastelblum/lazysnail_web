---
layout: post
title: Management Studio - Faster with multiple select
date: 2019-09-30
categories: "SQL-Server"
tags: [other, sql-server]
comments: true
permalink: "/en/management-studio-faster-with-multiple-select/"
parent: SQL Server
---
# {{ page.title }}
{: .fs-9 }


<p>In SQL Server Management Studio (<strong>SSMS</strong> for close friends) but also in a multitude of text editors (such as <strong>Notepad++</strong> for example), you can make <strong>multiple selections</strong>.</p>
<p>I thought it was something everyone knew, but I realize that I often look like a magician every time I do it.</p>
<p>I'm delighted to pretend to be <span style="color: #ff00ff;">Harry Potter</span>, but I think it's time for this little game to stop!</p>
<p><strong>Look by yourself how simple it is!</strong></p>


<h2>How?</h2>

<p>You should press the keys <strong>[ALT]</strong> + <strong>[Shift]</strong> simultaneously and move your cursor <strong>[Up]</strong> and / or <strong>[Down]</strong> to select your text.</p>

![](../../assets/2019/SSMS_FasterWithMultipleSelect/MultipleSelect_BasicSelection.webp)


<h2>One useful case</h2>

<p>Sometimes we have to surround our text with<strong> single quotes</strong>. (for example: to add multiple codes to an IN clause in a test query)</p>
<p><strong>No need to add them one by one and make sure you do not have space at the end</strong>.<br />Here is the method:</p>

![](../../assets/2019/SSMS_FasterWithMultipleSelect/MultipleSelect_Surround-1.webp)

<p>Like mentioned above, this tip is not an exclusivity in SSMS, you can also do the same in <g class="gr_ gr_3 gr-alert gr_gramm gr_inline_cards gr_run_anim Grammar multiReplace" id="3" data-gr-id="3">many</g> different text editor.</p>

