---
layout: post
title: Create a gradient background for Power BI
date: 2022-10-13 12:36:04.000000000 +02:00
categories: "power-bi"
tags: [powerbi, tips]
comments: true
permalink: "/en/create-a-gradient-background-for-power-bi/"
parent: Power BI
---
# {{ page.title }}
{: .fs-9 }

![Alt text](../../assets/2023/PowerBIGradian.png){: .image60 }

Diving deep into data transformation, modeling, and analytics, visualization has traditionally been my Achilles' heel. Nevertheless, I'm ardently working to enhance this skill!

A universal principle that is especially pertinent to reports and data visualization is: simplicity is key. Overcomplicating with excessive frills isn't necessary; straightforwardness often wins the day.

In my visual designs, I opt for a minimalist color palette and limit the number of visuals, ensuring that users can easily grasp the content presented on a page.



## Gradient background

{:refdef: style="text-align: center;"}
![gradiant](../../assets/2022/10/gradiant.jpg)
{: refdef}

<p>But when it’s time to add some unuseful stuff to our report, what I like the most is to add a gradient background. No need to add a flashy color variation!! I like to switch between one color and his very close variation. Like a “middle blue” to a “dark blue”.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>Many Power BI blogs mention PowerPoint to create a gradient background. And indeed, it’s not that a bad idea. But for some reason, PowerPoint generates images with a very ugly layer. (Like a rainbow)</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>I only have this issue when I publish my report on Power BI Services, but not on Power BI Desktop. (Is it related to my 4K screen or compression? No idea)</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>But if you encounter the same issue, or if you want to learn another way to do it, I’m explaining here how to do it with Paint .net.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:block {"ref":5367} /--></p>
<p><!-- wp:heading {"level":1} --></p>
<h1>Paint.net</h1>
<p><!-- /wp:heading --></p>
<p><!-- wp:paragraph --></p>
<p>Paint .net is my favorite images/graphics editor. It’s free, contains almost everything I need, and is not too complex to understand.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>You can download it here <a href="https://www.dotpdn.com/downloads/pdn.html">https://www.dotpdn.com/downloads/pdn.html</a></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:block {"ref":5367} /--></p>
<p><!-- wp:heading {"level":1} --></p>
<h1>How to create a gradient image with paint.net</h1>
<p><!-- /wp:heading --></p>
<p><!-- wp:paragraph --></p>
<p>Open Paint .net application and create a new canvas. (I recommend you to keep the same size as you use in your Power BI)</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>In the toolbox, choose the Gradient tool</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:image {"align":"center","id":5356,"width":123,"height":281,"sizeSlug":"full","linkDestination":"none"} --></p>
<figure class="wp-block-image aligncenter size-full is-resized"><img src="{{ site.baseurl }}/assets/2022/10/1.png" alt="" class="wp-image-5356" width="123" height="281" /><br />
<figcaption>Gradient tool</figcaption>
</figure>
<p><!-- /wp:image --></p>
<p><!-- wp:paragraph --></p>
<p>Now that the gradient tool is selected, go to the Colors pane and click "More"</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:image {"align":"center","id":5357,"width":288,"height":391,"sizeSlug":"full","linkDestination":"none"} --></p>
<figure class="wp-block-image aligncenter size-full is-resized"><img src="{{ site.baseurl }}/assets/2022/10/2_Primary_Secondary.png" alt="" class="wp-image-5357" width="288" height="391" /></figure>
<p><!-- /wp:image --></p>
<p><!-- wp:spacer {"height":"33px"} --></p>
<div style="height:33px" aria-hidden="true" class="wp-block-spacer"></div>
<p><!-- /wp:spacer --></p>
<p><!-- wp:paragraph --></p>
<p>First, you have to <strong>select a "Primary" Color</strong>. It's the one selected by default, but you can select it by using the dropdown list and chose "Primary" or by click the square on the top.<br />Use the color picker or paste an Hexadecimal RGB value. (I highly recommend you to use it)</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>You can find interesting color on <a href="https://coolors.co/palettes/trending">https://coolors.co/palettes/trending</a></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>When it's done, <strong>select the "Secondary" color</strong>. I usually paste the same color as the primary but change the "V" slider to a more lighter value (but very close)</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:image {"align":"center","id":5358,"width":484,"height":412,"sizeSlug":"full","linkDestination":"none"} --></p>
<figure class="wp-block-image aligncenter size-full is-resized"><img src="{{ site.baseurl }}/assets/2022/10/3_Hexa.png" alt="" class="wp-image-5358" width="484" height="412" /></figure>
<p><!-- /wp:image --></p>
<p><!-- wp:spacer {"height":"24px"} --></p>
<div style="height:24px" aria-hidden="true" class="wp-block-spacer"></div>
<p><!-- /wp:spacer --></p>
<p><!-- wp:paragraph --></p>
<p>Go to your canvas and click on the left button of your mouse, drag the cursor and release the button.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:image {"align":"center","id":5359,"width":622,"height":467,"sizeSlug":"large","linkDestination":"none"} --></p>
<figure class="wp-block-image aligncenter size-large is-resized"><img src="{{ site.baseurl }}/assets/2022/10/4_Draw-1024x770.png" alt="" class="wp-image-5359" width="622" height="467" /></figure>
<p><!-- /wp:image --></p>
<p><!-- wp:spacer {"height":"37px"} --></p>
<div style="height:37px" aria-hidden="true" class="wp-block-spacer"></div>
<p><!-- /wp:spacer --></p>
<p><!-- wp:paragraph --></p>
<p>Save this image into a .png file and use it in Power BI Desktop.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:image {"align":"center","id":5360,"width":666,"height":400,"sizeSlug":"large","linkDestination":"none"} --></p>
<figure class="wp-block-image aligncenter size-large is-resized"><img src="{{ site.baseurl }}/assets/2022/10/5_PowerBI-1024x615.png" alt="" class="wp-image-5360" width="666" height="400" /></figure>
<p><!-- /wp:image --></p>