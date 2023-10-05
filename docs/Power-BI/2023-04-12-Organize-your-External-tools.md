---
layout: post
title: Organize your External tools
date: 2023-04-12
categories: "power-bi"
tags: [powerbi, tips]
comments: true
parent: Power BI
permalink: /power-bi/Organize-your-External-tools
---
# {{ page.title }}
{: .fs-9 }

![](../../assets/2023/Power%20BI%20Extensions/Ribbon.png)

In your journey, you may need additional tools that go beyond the capabilities of what is built into Power BI. This is where external tools for Power BI come in.

External tools are add-ons that can be integrated into the Power BI workspace to extend its functionality. They are developed by third-party vendors rather than Microsoft and can be used to enhance data analysis capabilities, provide advanced visuals, and automate various data processing tasks.

External tools can come in many forms. They can be standalone executable files, web applications, or plugins that are installed directly into the Power BI desktop application. Some external tools may require a separate license or subscription to use, while others may be free.


# Most used External tools

- Tabular Editor (2.xx - Free version) [https://github.com/TabularEditor/TabularEditor](https://github.com/TabularEditor/TabularEditor)
- DAX Studio [https://daxstudio.org](https://daxstudio.org)
- ALM Toolkit [http://alm-toolkit.com](http://alm-toolkit.com/)


This tools is pretty useful, it allows you to download and install many different External tools. [https://powerbi.tips/product/business-ops](https://powerbi.tips/product/business-ops/)



# But!!

{: .note }
Yes! The downside of this! When you install a ton of external tools, just for a test, you can have multiple icons that you no longer use.



# Organize your External tools

## Where to change?

You can organize, remove, rename or change the icon by following this folder on your machine.

`C:\Program Files (x86)\Common Files\Microsoft Shared\Power BI Desktop\External Tools`


## File name == Alphabeticaly sorted == Ribbon sort

![](../../assets/2023/Power%20BI%20Extensions/Folder.png)

In the Power BI Ribbon, their file name (which is not the one displayed in Power BI) will be sort alphabeticaly.
You can provide a numeric value upfront to help them to be sorted. (This is how sidetools does)  


## Inside each file
You can edit each file in your favorite text editor and change the differents value.

![](../../assets/2023/Power%20BI%20Extensions/FileContent.png)


### Image
You can change what's inside the `iconData` value and provide a base64 code for you image.
It's possible to generate a base64 text code from an image  [https://codebeautify.org/image-to-base64-converter](https://codebeautify.org/image-to-base64-converter)

