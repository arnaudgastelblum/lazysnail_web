---
layout: post
title: Pie Chart is bad!
date: 2019-07-30
categories: "power-bi"
tags: [powerbi, tips]
comments: true
permalink: "/en/pie-chart-is-bad/"
parent: Power BI
---
# {{ page.title }}
{: .fs-9 }

During my presentation at Power Saturday in Paris, I wanted to demonstrate to an already very optimistic public that Power BI is a great tool and that modeling is a must-have for their reports. (Data Modelling is not the subject here)
Power BI a super tool? Yes, and to complete this idea, I added some slides to highlight each piece of the tool.

<p><strong>One of the slides showed the ease and elegance of the visuals.</strong><br /> After a quick search on Google images, I copied a screenshot created by a user in Power BI and added it to my presentation.</p>
<p>In the audience, two friends looked at me with a horrible face. <strong>The damage was done, I had slipped the image of a Pie Chart!</strong></p>
<p>Nothing crazy, isn't it? But when you know a bit of the history of the Pie Chart, we realize that this visual component is not recommended in the world of Data Viz. This blog post also follows some more or less tense discussions between colleagues.</p>


{: .note-title :}
>I wrote this article for many reasons:
>
>This point is already super documented on internet but some people never read them before. (I provide links at the end)
>I wanted to convinced myself first, and created a Power BI file to confirm this point. (CFR the following screenshot)


<h2>I was a Pie Chart lover</h2>

![pie chart lover](../../assets/2019/PieChartIsBad/PieChart_1.jpeg)


<p>I know that its use is not recommended and I try not to use it.<br />But yes, I liked it!<br />• It's beautiful!<br />• It's colorful!<br />• <strong>It gives a professional look to our reports!</strong><br />• It shows information!<br />• <strong>It gives me some pride to not use tables or matrix. (Yes, I like numbers, not you?)</strong></p>
<p>I think we are used to seeing this kind of visualization since our earliest childhood in commercial brochures, professional documents.</p>
<p>The Pie Chart is visual, and help us to return <g class="gr_ gr_16 gr-alert gr_gramm gr_inline_cards gr_run_anim Grammar multiReplace" id="16" data-gr-id="16">informations</g> quickly. <strong>But unfortunately, this information is not always the right one.</strong></p>



<h2>Why?</h2>

<p>To compare groups, we evaluate the difference of the <strong>amplitude of the angles</strong> while a histogram will request us to <strong>compare lengths</strong> between them.</p>
<p>A long description is not needed, I would prefer to show you 2 set of data, both represented in a Pie Chart and histogram.</p>
<p><span style="color: #ff6600;"><strong>Your first look</strong> will give you some information, but not as much precise compared to the two histograms below. It's possible to have quick information, but very hard to have a clear interpretation of them.<br /> </span></p>
<p><strong><span style="color: #ff6600;">If I didn't <g class="gr_ gr_12 gr-alert gr_gramm gr_inline_cards gr_run_anim Grammar multiReplace" id="12" data-gr-id="12">convince</g> you, try to sort each portion from the smallest to the biggest. Try to do the same with the histogram and compare the time elapsed for both.</span></strong></p>

![pie chart](../../assets/2019/PieChartIsBad/PieChart_2.webp)

## More info

<p><a href="https://www.data-to-viz.com/caveat/pie.html">https://www.data-to-viz.com/caveat/pie.html</a></p>
<p><a href="https://medium.com/@clmentviguier/the-hate-of-pie-charts-harms-good-data-visualization-cc7cfed243b6">https://medium.com/@clmentviguier/the-hate-of-pie-charts-harms-good-data-visualization-cc7cfed243b6</a></p>
