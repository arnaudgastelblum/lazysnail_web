---
layout: post
title: 'Power BI Desktop: Print in the A4 size'
date: 2018-08-24 11:30:52.000000000 +02:00
categories: "power-bi"
tags: [powerbi, tips]
comments: true
permalink: "/en/vertical-export-of-reports/"
parent: Power BI
---
# {{ page.title }}
{: .fs-9 }

<p>As you know, the <strong>August 2018 update of Power BI Desktop</strong> grants us the possibility to <strong>export in PDF</strong> directly from the Desktop. Two clicks and it's done. Great news right? I remember all the steps I had to go through to make it before, it still give me headache...</p>
<p>But by default, the report will be exported with the standard format of Power BI Desktop which can be for some end users or clients not very pleasant to read especially if they are used to an <strong>A4 page</strong>. The real question is then, how to export in that specific format? Here is the answer.</p>
<p>First, let's take our wonderful LazyDAX file and create a new page. Here is the default view you have when adding a new page.</p>
<p><img width="920" height="471" class="alignnone wp-image-386 " alt="" src="/assets/2018/08/Regular.png" /></p>
<p>Nothing special until there. What's interesting is the "Page View" button under the "View" tab. Once we click on it, we can select "Actual Size".</p>
<p><img width="310" height="183" class="alignnone wp-image-384" alt="" src="/assets/2018/08/PageView.png" /></p>
<p>By choosing "Actual Size" we will see the "real" size of the page, based on its dimensions.</p>
<p><img width="919" height="471" class="alignnone wp-image-381" alt="" src="/assets/2018/08/ActualSize.png" /></p>
<p>Now we can see that the page size exceed the usual limit of the report. But we want to make it like a A4 portrait page right? So, we are not done yet. You can select the "Format" pane of the report page, then "Page Size" and select "Custom" as "Type".&nbsp; Now, we just have to enter the custom size we want. I chose 794*1123 pixels because it is the A4 size at 96 PPI (depending of the printing, you can find more info about it <a href="https://www.papersizes.org/a-sizes-in-pixels.htm">here</a>).</p>
<p><img width="160" height="376" class="alignnone wp-image-382" alt="" src="/assets/2018/08/CustomSize.png" /></p>
<p>Now we have our A4 report page ready to be filled.</p>
<p><img width="919" height="471" class="alignnone wp-image-379" alt="" src="/assets/2018/08/A4Fill.png" /></p>
<p>As you can see, there is now a scroll bar on the right side of the report because of the dimension of the page. We now just have to export as PDF and that's it. You can click on the "File" button and then choose "Export to PDF".</p>
<p><img width="919" height="471" class="alignnone wp-image-387" alt="" src="/assets/2018/08/Export-1.png" /></p>
<p>You now just have to let Power BI make the work and here is the result.</p>
<p><img width="355" height="468" class="alignnone wp-image-385 " alt="" src="/assets/2018/08/PDF.png" /></p>
<p>The last report page is well in portrait format, while the others have been exported in the default format.</p>
<p>As you can see, there is nothing really difficult here but you just have to be aware of it.</p>
<p>&nbsp;</p>
