---
layout: post
title: Your data model first!
date: 2021-12-23 09:25:20.000000000 +01:00
categories: "power-bi"
tags: [powerbi, tips]
comments: true
permalink: "/en/your-data-model-first/"
parent: Power BI
---
# {{ page.title }}
{: .fs-9 }

<p><!-- wp:paragraph --></p>
<p>At this end of the year, I thought it’s time for me to bring you a gift!!<br />It’s a very important subject that I mention to my coworkers and it’s 80% of a success power bi story!</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:heading --></p>
<h2>All the focus is on the tech part.</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:paragraph --></p>
<p>All developers (yes, you are!!), spend a huge amount of time to understand their sources, their transformation, and the magic that happens in their DAX measures!<br />And, to be honest, that’s normal!</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:heading --></p>
<h2>So why this article?</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:paragraph --></p>
<p>After 1 week, 2 months, or more time, we are very proud of our dataset! (Yes, I’m not talking about reports, but dataset which can be used in many reports)<br />Our model contains a lot of data, all the information needed is there! But is it easy for an external person to use it? (a User, a colleague, your kids, ..)<br />Sometimes yes, sometimes no.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>Some complexity exists:</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:list --></p>
<ul>
<li>Too many tables</li>
<li>Too many relationships and the difficulty to know the interaction between tables.</li>
<li>The model keeps the complexity of the source systems.</li>
</ul>
<p><!-- /wp:list --></p>
<p><!-- wp:paragraph --></p>
<p>But ok! We did a huge work to clean and provide this model! Everything work!! Our users can take 2 or 3 hours and try to understand the logic behind it!</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>I like to mention it. I love cars!! But I know nothing about it!! Do I need to understand how an engine work to drive a car? It’s a real plus, but not mandatory.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:heading --></p>
<h2>So what do I suggest?</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:paragraph --></p>
<p>It doesn’t take much time, and it can help you to keep an eye on your goal. (Yes!! Provide a very shiny dataset)<br />Before every model, I recommend you to draw your model on a sheet of paper.<br />You already know the information you have to present and how your user group this information. If not, it’s the perfect time to ask your users and write their buzzwords on paper.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>Before each project, ask them to present you their job and the different tools they use. It would help you to have a clear view of their logic behind, their needs, and also what’s missing now.<br />At this point, I only write huge keywords on paper.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:image {"id":5072,"sizeSlug":"full","linkDestination":"none"} --></p>
<figure class="wp-block-image size-full"><img src="{{ site.baseurl }}/assets/2021/12/1_Brainstorming-Small.jpg" alt="" class="wp-image-5072" /></figure>
<p><!-- /wp:image --></p>
<p><!-- wp:paragraph --></p>
<p>When I’m back on my desk, I’m looking at this brainstorming paper, and try to group the different keywords into a logic.<br />That’s how tables bring to life, and because I’m a Kimball huge fan let's call them Dimensions!</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:image {"id":5073,"sizeSlug":"full","linkDestination":"none"} --></p>
<figure class="wp-block-image size-full"><img src="{{ site.baseurl }}/assets/2021/12/2_Model-Small.jpg" alt="" class="wp-image-5073" /></figure>
<p><!-- /wp:image --></p>
<p><!-- wp:paragraph --></p>
<p>So now, with these tables you have the user point of view of their data, all the magic (and fun) is to prepare the data to fit in it!<br />But hey, with Power Query, SQL, it’s just a piece of cake! Isn’t?</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:heading --></p>
<h2>In conclusion</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:paragraph --></p>
<p>Do not jump directly into the source's data, keep an eye on your expectation first. Ask your users, talk to your colleagues and try to build the model of your dream.<br />It’s possible! During your development, you may change some tables, and that’s completely normal! But at least, if you keep your original model, everybody will win in the end.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>I wish you all the best in your data journey!<br />What a fun job!!</p>
<p><!-- /wp:paragraph --></p>
