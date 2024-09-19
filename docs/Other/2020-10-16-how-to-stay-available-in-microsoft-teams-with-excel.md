---
layout: post
title: How to stay always "Available" in Microsoft Teams with Excel
categories: "other"
date: 2020-10-16
tags: [misc]
comments: true
permalink: "/en/how-to-stay-available-in-microsoft-teams-with-excel/"
parent: Other
---

## Stay available on Microsoft Teams
{: .no_toc }


![](../../assets/2023/TeamsAway.png){: .image80 }


## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

{: .warning-title :}
>`^^`
>
>I wrote this article quite a while back, yet it remains one of the most frequented pages on my site! Oh, you lazy people! 😉

{: .new-title :}
>Download
>
>You can either download the Excel file directly or set up a macro in Excel using the code provided below.



---

## How Did It Begin? 🚀

Initially, it was an inside joke. But now, thanks to this article, it's **a public jest**.

When our client transitioned from Skype to Teams, we noticed a **significant improvement**. My colleagues humorously pointed out:
> "Teams is great, but you can't alter the duration before being marked as 'away'!"

And they were right; there's no such option. Someone then suggested:
> "What if you had software that randomly clicked on your screen? You wouldn't be marked 'away' then."

While this might work, our software guidelines prohibit us from adding any external programs to our systems.

## Inspiration Struck! 💡

That's when inspiration struck, courtesy of our trusty old friend, **Excel**. Some might quip:
> "Laziness breeds innovation," 

while others might jest about my quirky sense of humor. Regardless, I had a blast utilizing Excel and its versatile VBA editor.

My colleague Isabelle (and perhaps Maslow) would reference this: 

[If all you have is a hammer, everything looks like a nail](https://en.wiktionary.org/wiki/if_all_you_have_is_a_hammer,_everything_looks_like_a_nail)

To me, Excel and coding are like my trusty hammer. Whether you see it as a 'nail' or 'snail', it's all in the addition of a single 's'.

I devised a simple Excel sheet that runs in a loop until terminated, moving your mouse cursor every five seconds.

## Emotions & Perceptions 🎭

My emotions are a mix of:

- **Proud**: "I'm the Microsoft BI enthusiast who employed Microsoft Office and VBA code for a playful purpose."
  
- **Amused**: "Am I now perceived as the ultimate procrastinator, mirroring the theme of my website?"

Regardless, if you're reading this, I believe you'd lean towards the former sentiment. **Am I off the mark?** :)


## What's the Appearance? 🖼️

![](/assets/2020/10/image-1.png)

This is its appearance in Excel. 
Initiate the timer by either clicking the start button, pressing CTRL + L (as in 'lazysnail'), or manually activating the macro titled "DoNotSleep". 
To halt the timer, simply press any key.


## Download the Excel 📥

The file is available on GitHub
[https://github.com/arnaudgastelblum/Misc/raw/main/LazySnail.xlsm](https://github.com/arnaudgastelblum/Misc/raw/main/LazySnail.xlsm)



## Construct Your VBA Macro 🛠️

*Thanks to Rafi for his 64 bits version!*



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
