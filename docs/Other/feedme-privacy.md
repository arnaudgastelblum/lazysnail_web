---
layout: default
title: FeedMe privacy policy
nav_exclude: true
search_exclude: true
permalink: /tools/feedme/privacy
description: "FeedMe's privacy policy: it runs entirely on your PC, with no account, no server of its own and no analytics."
---
# FeedMe privacy policy
{: .fs-8 }

FeedMe is a feed reader for Windows. It runs entirely on your computer: no account, no server of its own, no analytics, no advertising.

## What FeedMe stores, and where

Your subscriptions, articles, offline copies, highlights, notes, comments, reading positions and settings are stored in a database file on your computer. Nothing is uploaded anywhere. Where that file lives depends on the version you use:

- **Microsoft Store version**: in the app's private storage. Uninstalling FeedMe removes it.
- **Installer version**: in `%APPDATA%\FeedMe`. Uninstalling FeedMe keeps it, so a reinstall finds your library. Delete that folder to remove it.
- **Standalone (zip) version**: in the `FeedMe Data` folder next to `FeedMe.exe`. Delete that folder to remove it.

The same folder holds a small error log, which helps understand a problem if you choose to report one. It never leaves your computer.

You can back up or restore your library in **Settings**, under **Your data**.

## What FeedMe connects to

FeedMe only connects to the internet to do what you ask of it:

- **The feeds you follow**, to check for new articles, on the schedule you choose in Settings or only when you ask. For YouTube channels and subreddits, that means youtube.com and reddit.com.
- **The websites your articles come from**: to show the images and media of an article, which load from their own servers when you read it, to fetch an article's full text when you ask for it, to keep an offline copy of what you save to Read later, and to fetch each site's icon. Loading a full article can open the page in a hidden browser window inside FeedMe, so that pages built with JavaScript can be read. That window is isolated: it has no access to your library, your files, or anything else in FeedMe, and it is closed as soon as the text is read.
- **Websites you type or paste** into FeedMe, or send from your browser, to find their feed or to save a page.
- **Embedded videos.** A YouTube video shows a thumbnail from YouTube. The video itself only loads when you press play, through YouTube's privacy-enhanced mode (`youtube-nocookie.com`). Videos embedded inside an article (YouTube, through the same mode, or Vimeo) load from those services when the article is shown.

These are ordinary web requests: like any browser, they reveal your IP address to the site being contacted, and FeedMe identifies itself as FeedMe with its version. It adds no identifier of its own and sends your reading history to no one.

## The clipboard

If the clipboard suggestion is on (it is by default), FeedMe reads the clipboard when it starts and when you switch back to it, to see whether you have just copied a web address, so that it can offer to follow that site or save the page. The address is only shown to you. It is not stored or sent anywhere unless you choose one of those actions. When you turn this off in **Settings**, FeedMe no longer reads the clipboard at all, except when you paste yourself.

## Links from your browser

The optional **Follow in FeedMe** and **Read later in FeedMe** bookmarks open FeedMe with the address of the page you are on. Your browser asks before opening FeedMe. Nothing else is shared.

## Instapaper (optional)

If you connect an Instapaper account, your Instapaper username and password are encrypted with Windows' own data protection and stored on your computer. When you send an article to Instapaper, FeedMe sends Instapaper (`https://www.instapaper.com`), over an encrypted connection, your credentials, the article's address and title, and the name of the feed it came from. Nothing is sent to Instapaper otherwise. You can remove your credentials at any time in Settings.

## Children

FeedMe does not collect any information from anyone, including children.

## Changes

If this policy changes, the new version will be published on this page with a new date.

Questions: [contact me on LinkedIn](https://www.linkedin.com/in/arnaud-gastelblum/).

Last updated: 12 November 2026.
