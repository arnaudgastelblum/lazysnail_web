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
{: .fs-9 }

Managing tasks efficiently is crucial for productivity and success in any field. With the rise of digital note-taking tools, organizing tasks has become much more streamlined and convenient. Obsidian, a popular note-taking app, offers a Dataview plugin that enables users to manage tasks effectively. This plugin allows users to create custom views, set reminders, and track progress, among other features. In this article, we will explore how to use the Dataview plugin in Obsidian to manage tasks efficiently and increase productivity.


{: .note-title } 
> Prerequisites
> 
> You should install the `dataview` plugin first!
> 
> Open Obsidian, go to `settings` > `Community plugins` > `Browse` and search for `dataview`
> 
> Do not forget to enable it when it's installed.

All dataview code present below should be included into a command block.
For example:

![ObsidianCodeBlock](../assets/ObsidianCodeBlock.png)

## List all tasks

The following code lists all the existing tasks in your Obsidian Vault.

```
TASK

```

## List all opened tasks

To list only tasks in progress (not yet completed)

```
TASK
WHERE !completed
```

## List of tasks in a file only (current file and specified file)

Limit to the tasks created in the file we are in.

``` 
TASK 
WHERE file.path = this.file.path 
  AND !completed
```



## List of tasks by tag

Search in the entire Vault for open tasks containing the tag `#todo`.
This allows me to sort my tasks by project type or need.
I personally have a `#perso` tag to store my personal ideas, a tag by client and also by projects. (Sometime by person)
My `#todo` tag is a bit different, I'll talk about it later.

```
TASK
WHERE !completed
 AND contains(text, "#todo")
SORT text ASC
```

## Using the upper case

I use Obsidian from my iPad or iPhone, and when I write a tag the first letter is often capitalized. Rather than manually changing it, I modify my dataview query to force the search on the uppercase tags.

```
TASK
WHERE !completed
 AND contains(upper(text), "#TODO")
SORT text ASC
```


## Prioritizing tasks with the todo tag

The `#todo` tag is part of a thought process. Over time I add tasks to my Vault. But every morning as I start my day I prioritise the tasks that need to be done during the day. (or not to be lost sight of)
I use the `#todo` tag on top of the other tags. 
The following query is displayed at the top of each Daily note, to highlight them.

```
TASK
WHERE !completed
 AND contains(upper(text), "#TODO")
SORT text ASC
```



## Misc

### Search from a variable


``` 
TASK
WHERE contains(MOC, [[YourYAMLVariable]])
AND !completed
SORT file.mtime DESC
```