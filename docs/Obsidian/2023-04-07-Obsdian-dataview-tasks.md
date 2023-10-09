---
layout: post
title: Managing efficiently your tasks with Obsidian and Dataview
date: 2023-04-07
categories: "Obsidian"
tags: [obsidian]
comments: true
parent: Obsidian
permalink: /obsidian/Obsdian-dataview-tasks
---
# {{ page.title }}
{: .no_toc }


![](../../assets/2023/obsidianTask.png){: .image80 }


## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Efficient Task Management for Enhanced Productivity 💼

In any profession, mastering task management is the cornerstone to achieving success and maintaining productivity. The digital age has graced us with a plethora of note-taking tools that have revolutionized the way we organize our tasks. One standout is **Obsidian** — a top-tier note-taking app that boasts the **Dataview plugin**.

With the Dataview plugin, users can:
- Craft custom views 🎨
- Set timely reminders ⏰
- Monitor their progress 📈
- And so much more!

In the course of this guide, we'll dive deep into harnessing the power of the Dataview plugin within Obsidian, setting you on the path to optimal productivity.

## Install Dataview 📥

You should install the `dataview` plugin first! 
Open Obsidian, go to `settings` > `Community plugins` > `Browse` and search for `dataview` 
Do not forget to enable it when it's installed.


## Usage 📝

Now go to a note (new or existing), and write a block code.

<pre>
  <code>
```dataview

```  
  </code>
</pre>

Alright, currently, nothing's occurring!


## List All Tasks 📋

Insert `TASK` into the code block you've set up, and watch the magic unfold! ✨

```
TASK

```

The provided code showcases all the tasks within your Obsidian Vault.

## List All Open Tasks 🚀

To display tasks that are still ongoing (not finished)

```
TASK
WHERE !completed
```

## Displaying Tasks Exclusive to a File (either current or specified) 📁

Show only the tasks originating from the file we're currently viewing.

``` 
TASK 
WHERE file.path = this.file.path 
  AND !completed
```



## Sorting Tasks Using Tags 🏷️

Scan the entire Vault for unresolved tasks labeled with the `#todo` tag. 
This method facilitates the organization of my tasks based on the project category or specific requirement. 
I utilize the `#perso` tag for cataloging personal thoughts, and I have distinct tags for each client and project (occasionally by individual). 
The usage of my `#todo` tag is unique, which I'll elaborate on shortly.

```
TASK
WHERE !completed
 AND contains(text, "#todo")
SORT text ASC
```

## Capitalization in Tags 🔠

When I access Obsidian from my iPad or iPhone, the initial letter of a tag often gets capitalized automatically. Instead of adjusting it by hand, I've tweaked my dataview query to specifically target tags that start with an uppercase letter.

```
TASK
WHERE !completed
 AND contains(upper(text), "#TODO")
SORT text ASC
```


## Task Prioritization Using the `#todo` Tag 🌟

The `#todo` tag is integral to my workflow. As days progress, I continually add tasks to my Vault. However, at the start of each day, I sift through and determine which tasks warrant immediate attention (or which ones I need to keep at the forefront).
I overlay the `#todo` tag on any existing tags for this purpose. 
The subsequent query is showcased at the beginning of every Daily note to accentuate these tasks.

```
TASK
WHERE !completed
 AND contains(upper(text), "#TODO")
SORT text ASC
```



## Search from a Variable 🔍

{: .note }
>Previously, that was my method of operation. However, now I lean more towards using #tags.

In various notes, you might opt to utilize YAML variables. If so, the code below will be beneficial in fetching a list of uncompleted tasks from notes that have a particular result:

``` 
TASK
WHERE contains(MOC, YourYAMLVariable)
AND !completed
SORT file.mtime DESC
```

This assists in pinpointing tasks associated with the specified YAML variable that haven't been completed yet.



## Using Tags Effectively 🏷️

Imagine writing checkbox with multiple #tag
For example:

![](/../assets/2023/2023-10-06-15-45-19.png)

By writing this code into Obsidian

![](/../assets/2023/2023-10-06-15-45-59.png)


I get this result

![](/../assets/2023/2023-10-06-15-46-22.png)


Tags become really handy when you use them for different purposes, like identifying a project, naming a person, marking a status, or even setting a category.

What I love about this system is its flexibility. You can add these tags in any note, be it your daily thoughts, meeting notes, or just any random jotting. And the best part? You can pull all this tagged information together in one place.

I made a central note called `Index`. This is where I link to all my main content maps, project ideas, or any other major thoughts. I've also added several to-do lists right there for easy reference.


I hope you'll find it beneficial and assign meanings to the tags that assist you in your daily routine. 🌟