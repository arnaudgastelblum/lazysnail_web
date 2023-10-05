---
layout: post
title: How to stay always "Available" in Microsoft Teams with Excel
categories: "other"
tags: [misc]
comments: true
permalink: "/en/how-to-stay-available-in-microsoft-teams-with-excel/"
parent: Other
---
[Download the Excel file on GitHub](https://github.com/arnaudgastelblum/Misc/raw/main/LazySnail.xlsm){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
<p>Or create your own Excel file by reading the text below (and copy / paste the vba code)</p>

{: .warning :}
>I published this article long time ago now, but this is one of the most visited page on my website! You lazy people!



## How it started?

{: .note :}
>First it was a private joke, with this article it's now a public joke.</p>

<p>Our client switched from <strong>Skype to Teams</strong> and it was a very cool improvement. My colleagues told me with a bit of fun: <strong><em>"Teams is cool, but you can't change the time before appearing away!"</em></strong>. And it's true, we can't! Somebody said, "If you install a software who will click randomly on your screen, you will not appear away anymore". Yes,.. but our software policy does not allow us to install anything on our computers.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>It gave me an idea! Thanks to our very good old friend, Excel!  People will say "Lazy is smart", Arnaud is "funny" or any other reason. But I had fun with Excel and his perfect VBA editor.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>My colleague <strong><a href="https://twitter.com/thesqlgrrrl">Isabelle </a></strong>(and also <a href="https://en.wikipedia.org/wiki/Abraham_Maslow">Maslow</a>) will say :</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:image {"id":4534,"sizeSlug":"large"} --></p>
<figure class="wp-block-image size-large"><img src="{{ site.baseurl }}/assets/2020/10/image-2-1024x102.png" alt="" class="wp-image-4534" /><br />
<figcaption><a href="https://en.wiktionary.org/wiki/if_all_you_have_is_a_hammer,_everything_looks_like_a_nail">https://en.wiktionary.org/wiki/if_all_you_have_is_a_hammer,_everything_looks_like_a_nail</a></figcaption>
</figure>
<p><!-- /wp:image --></p>
<p><!-- wp:paragraph --></p>
<p>My hammer is Excel and Code.. I agree.. (nail or snail.. it's just a "s" who is missing)</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>I created a small excel sheet who will loop until you ask it to finish and will move your mouse cursor every 5 seconds.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:quote --></p>
<blockquote class="wp-block-quote"><p>My joy is shared between. </p>
<p><strong>"I'm the Microsoft BI guy who uses Microsoft Office and VBA code to do a joke". </strong></p>
<p>and </p>
<p><strong>"People will see me as a very lazy guy!! isn't the name of his website!?!". </strong></p>
<p>Anyway, if you read this article, then it's because I think you will pick the first idea. I'm I wrong? :)</p>
</blockquote>


<h2>Where can you download it?</h2>

<p class="has-text-align-left has-medium-font-size"><a href="https://github.com/arnaudgastelblum/Misc/raw/main/LazySnail.xlsm"><img class="wp-image-4540" style="width: 64px;" src="{{ site.baseurl }}/assets/2020/10/download.png" alt="" /></a> <a href="https://github.com/arnaudgastelblum/Misc/raw/main/LazySnail.xlsm">You can download the excel sheet on my github repo.</a> </p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph {"align":"left","fontSize":"medium"} --></p>
<p class="has-text-align-left has-medium-font-size"><em>(If you want your own excel sheet, the code is also available at the end of this post)</em></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><strong><em>Thanks to Rafi for his 64 bits version!</em></strong></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:heading --></p>
<h2>How does it look like?</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:image {"align":"center","id":4516,"sizeSlug":"large","className":"is-style-default"} --></p>
<div class="wp-block-image is-style-default">
<figure class="aligncenter size-large"><img src="{{ site.baseurl }}/assets/2020/10/image-1.png" alt="" class="wp-image-4516" /></figure>
</div>
<p><!-- /wp:image --></p>
<p><!-- wp:paragraph --></p>
<p>This is how it looks in Excel. You can start the timer by clicking on the <strong>start button</strong> or CTRL + l (like lazysnail) or start manually the macro named "DoNotSleep".</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><strong>To stop the timer, you have to press any key.</strong></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:heading --></p>
<h2>Do you have the VBA code?</h2>
<p><!-- /wp:heading --></p>
<p><!-- wp:paragraph --></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>If you are curious and want to build your own Excel, let's copy the following VBA code:</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:enlighter/codeblock {"language":"visualbasic"} --></p>

```vb
Public Declare PtrSafe Function SetCursorPos Lib "user32" (ByVal x As LongPtr, ByVal y As LongPtr) As LongPtr
Public Declare PtrSafe Sub mouse_event Lib "user32" (ByVal dwFlags As LongPtr, ByVal dx As LongPtr, ByVal dy As LongPtr, ByVal cButtons As LongPtr, ByVal dwExtraInfo As LongPtr)
Public Const MOUSEEVENTF_LEFTDOWN = &amp;H2
Public Const MOUSEEVENTF_LEFTUP = &amp;H4
Public Const MOUSEEVENTF_RIGHTDOWN As LongPtr = &amp;H8
Public Const MOUSEEVENTF_RIGHTUP As LongPtr = &amp;H10

Sub DoNotSleepPlease()

Dim i As Integer

For i = 1 To 9999
    'For Info, number of iteration
    'Cells(1, 1) = i
    If Cells(3, 5) = "" Then
        SetCursorPos 200, 200 'x and y position
        mouse_event MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0
        mouse_event MOUSEEVENTF_LEFTUP, 0, 0, 0, 0
        WaitPlease
        
        
        SetCursorPos 300, 300 'x and y position
        mouse_event MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0
        mouse_event MOUSEEVENTF_LEFTUP, 0, 0, 0, 0
        WaitPlease
        
        SetCursorPos 400, 400 'x and y position
        mouse_event MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0
        mouse_event MOUSEEVENTF_LEFTUP, 0, 0, 0, 0
        WaitPlease
        
        SetCursorPos 500, 500 'x and y position
        mouse_event MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0
        mouse_event MOUSEEVENTF_LEFTUP, 0, 0, 0, 0
        WaitPlease
    Else
        Exit For
    End If
    Next i
End Sub


Sub WaitPlease()
    Dim sngWaitEnd As Single
    sngWaitEnd = Timer + 5
    Do
      DoEvents
      Cells(3, 3).Value = Timer
    Loop Until Timer >= sngWaitEnd
End Sub
```
