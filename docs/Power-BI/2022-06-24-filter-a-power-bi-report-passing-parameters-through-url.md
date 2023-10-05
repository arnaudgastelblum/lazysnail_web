---
layout: post
title: Filter a Power BI report passing parameters through URL
date: 2022-06-24 13:32:32.000000000 +02:00
categories: "power-bi"
tags: [powerbi, tips]
comments: true
permalink: "/en/filter-a-power-bi-report-passing-parameters-through-url/"
parent: Power BI
---
# {{ page.title }}
{: .fs-9 }

<p><!-- wp:uagb/table-of-contents {"block_id":"f07976da","classMigrate":true,"headingTitle":"Contents"} /--></p>
<p><!-- wp:spacer {"height":"52px"} --></p>
<div style="height:52px" aria-hidden="true" class="wp-block-spacer"></div>
<p><!-- /wp:spacer --></p>
<p><!-- wp:paragraph --></p>
<p>
<p>Power BI offers us a very sympathetic way to <strong>bring a bit more flexibility into our Reports</strong>. It’s not a brand-new feature, but I’m not sure that you know it!</p>
<p>You can display a report and automatically have a page filtered by the parameters you define in the URL.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:spacer {"height":"40px"} --></p>
<div style="height:40px" aria-hidden="true" class="wp-block-spacer"></div>
<p><!-- /wp:spacer --></p>
<p><!-- wp:heading --></p>
<h2>Why is it cool?</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:list --></p>
<ul>
<li>We can create an <strong>embed report</strong> and include it on a website/intranet. It’s possible to create a button, or menu to dynamically filter and display our report. (Microsoft provides an example: <a href="https://powerbi.microsoft.com/en-us/blog/easily-embed-secure-power-bi-reports-in-your-internal-portals-or-websites/">https://powerbi.microsoft.com/en-us/blog/easily-embed-secure-power-bi-reports-in-your-internal-portals-or-websites/</a></li>
<li>It’s also possible to filter a report from a <strong>Power Apps</strong></li>
<li>We can create <strong>our own bookmarks</strong> (in your browser or in your email)</li>
<li>We can <strong>add filters on fields that are not suggested / available in the Filter Pane</strong></li>
</ul>
<p><!-- /wp:list --></p>
<p><!-- wp:spacer {"height":"40px"} --></p>
<div style="height:40px" aria-hidden="true" class="wp-block-spacer"></div>
<p><!-- /wp:spacer --></p>
<p><!-- wp:heading --></p>
<h2>But</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:list --></p>
<ul>
<li>It’s indeed not a way to add security to your reports!! (Filter can be removed by your users) => The Row-level security is what you need.</li>
<li>It’s not possible to use it in an iframe with a report “published to web”</li>
</ul>
<p><!-- /wp:list --></p>
<p><!-- wp:paragraph --></p>
<p>First, Microsoft wrote already a nice article on this topic. I suggest you read it for more information.<br /><a href="https://docs.microsoft.com/en-us/power-bi/collaborate-share/service-url-filters">https://docs.microsoft.com/en-us/power-bi/collaborate-share/service-url-filters</a></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:spacer {"height":"40px"} --></p>
<div style="height:40px" aria-hidden="true" class="wp-block-spacer"></div>
<p><!-- /wp:spacer --></p>
<p><!-- wp:heading --></p>
<h2>How to</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:list --></p>
<ul>
<li>Open your report in Power BI Service and go to the page you want to filter</li>
<li>Click on the address bar and at the end of this line, add the following code ?filter=</li>
</ul>
<p><!-- /wp:list --></p>
<p><!-- wp:image {"id":5307,"sizeSlug":"large","linkDestination":"none"} --></p>
<figure class="wp-block-image size-large"><img src="{{ site.baseurl }}/assets/2022/06/1_NoFilter-1024x605.png" alt="" class="wp-image-5307" /><br />
<figcaption>This is the example used in this article. (You can also download this Power BI on this website. Search LazyDAX on the main page)</figcaption>
</figure>
<p><!-- /wp:image --></p>
<p><!-- wp:spacer {"height":"40px"} --></p>
<div style="height:40px" aria-hidden="true" class="wp-block-spacer"></div>
<p><!-- /wp:spacer --></p>
<p><!-- wp:heading --></p>
<h2>Filter on numeric value</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:code --></p>
<pre class="wp-block-code"><code>?filter=Calendar/Year eq 2022</code></pre>
<p><!-- /wp:code --></p>
<p><!-- wp:paragraph --></p>
<p>The first part of this expression refers to the dimension (Table) -> <strong>Calendar</strong><br />The second part refers to the attribute name in this dimension -> <strong>Year</strong><br /><strong>eq </strong>means <strong>equals</strong></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:image {"id":5316,"width":225,"height":445,"sizeSlug":"large","linkDestination":"none"} --></p>
<figure class="wp-block-image size-large is-resized"><img src="{{ site.baseurl }}/assets/2022/06/image-516x1024.png" alt="" class="wp-image-5316" width="225" height="445" /></figure>
<p><!-- /wp:image --></p>
<p><!-- wp:image {"id":5308,"sizeSlug":"large","linkDestination":"none"} --></p>
<figure class="wp-block-image size-large"><img src="{{ site.baseurl }}/assets/2022/06/2_Filter_EqualOneYear-1024x750.png" alt="" class="wp-image-5308" /></figure>
<p><!-- /wp:image --></p>
<p><!-- wp:spacer {"height":"40px"} --></p>
<div style="height:40px" aria-hidden="true" class="wp-block-spacer"></div>
<p><!-- /wp:spacer --></p>
<p><!-- wp:heading --></p>
<h2>Filter multiple numeric values</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:code --></p>
<pre class="wp-block-code"><code>?filter=Calendar/Year <strong>in </strong>(2022, 2023)</code></pre>
<p><!-- /wp:code --></p>
<p><!-- wp:image {"id":5309,"sizeSlug":"large","linkDestination":"none"} --></p>
<figure class="wp-block-image size-large"><img src="{{ site.baseurl }}/assets/2022/06/3_Filter_2Years-1024x734.png" alt="" class="wp-image-5309" /></figure>
<p><!-- /wp:image --></p>
<p><!-- wp:spacer {"height":"40px"} --></p>
<div style="height:40px" aria-hidden="true" class="wp-block-spacer"></div>
<p><!-- /wp:spacer --></p>
<p><!-- wp:heading --></p>
<h2>Filter on a text value</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:code --></p>
<pre class="wp-block-code"><code>?filter=Product/ProductCategory eq 'Fruit'</code></pre>
<p><!-- /wp:code --></p>
<p><!-- wp:image {"id":5310,"width":823,"height":569,"sizeSlug":"large","linkDestination":"none"} --></p>
<figure class="wp-block-image size-large is-resized"><img src="{{ site.baseurl }}/assets/2022/06/4_Filter_EqString-1024x709.png" alt="" class="wp-image-5310" width="823" height="569" /></figure>
<p><!-- /wp:image --></p>
<p><!-- wp:spacer {"height":"40px"} --></p>
<div style="height:40px" aria-hidden="true" class="wp-block-spacer"></div>
<p><!-- /wp:spacer --></p>
<p><!-- wp:heading --></p>
<h2>Filter multiple Text values</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:image {"id":5311,"sizeSlug":"large","linkDestination":"none"} --></p>
<figure class="wp-block-image size-large"><img src="{{ site.baseurl }}/assets/2022/06/4_Filter_ListString-1024x727.png" alt="" class="wp-image-5311" /></figure>
<p><!-- /wp:image --></p>
<p><!-- wp:spacer {"height":"40px"} --></p>
<div style="height:40px" aria-hidden="true" class="wp-block-spacer"></div>
<p><!-- /wp:spacer --></p>
<p><!-- wp:heading --></p>
<h2>Add Multiple filter on differents attributes</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:code --></p>
<pre class="wp-block-code"><code>?filter=Customer/Country in ('Belgium', 'Nederland') and Product/ProductCategory eq 'Fruit' and Calendar/Year ge 2021</code></pre>
<p><!-- /wp:code --></p>
<p><!-- wp:image {"id":5312,"sizeSlug":"large","linkDestination":"none"} --></p>
<figure class="wp-block-image size-large"><img src="{{ site.baseurl }}/assets/2022/06/5_MultiplesFilters-1024x584.png" alt="" class="wp-image-5312" /></figure>
<p><!-- /wp:image --></p>
<p><!-- wp:spacer {"height":"40px"} --></p>
<div style="height:40px" aria-hidden="true" class="wp-block-spacer"></div>
<p><!-- /wp:spacer --></p>
<p><!-- wp:heading --></p>
<h2>More operators are available</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:image {"id":5317,"width":558,"height":391,"sizeSlug":"large","linkDestination":"none"} --></p>
<figure class="wp-block-image size-large is-resized"><img src="{{ site.baseurl }}/assets/2022/06/image-1-1024x719.png" alt="" class="wp-image-5317" width="558" height="391" /><br />
<figcaption>Source: Microsoft website (see url below)</figcaption>
</figure>
<p><!-- /wp:image --></p>
<p><!-- wp:paragraph --></p>
<p>Like mentioned at the beginning, everything is already well explained on the Microsoft website: <a href="https://docs.microsoft.com/en-us/power-bi/collaborate-share/service-url-filters">https://docs.microsoft.com/en-us/power-bi/collaborate-share/service-url-filters</a></p>
<p><!-- /wp:paragraph --></p>
