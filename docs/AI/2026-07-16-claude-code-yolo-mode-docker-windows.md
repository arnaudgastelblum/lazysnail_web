---
layout: post
title: "Claude Code YOLO Mode on Windows: Skip Permissions Safely with Docker"
date: 2026-07-16
categories: "ai"
tags: [claude-code, docker, windows]
comments: true
parent: AI
permalink: /ai/claude-code-yolo-mode-docker-windows
description: "How to run Claude Code with --dangerously-skip-permissions on Windows, inside a Docker container, with a simple 'yolo' PowerShell alias."
---
# {{ page.title }}
{: .fs-9 }

{:toc}

{: .note-title :}
>What?
>
>By default, Claude Code asks you to confirm every file change and every command it wants to run. That is the safe way to work, but it gets tedious fast. There is a flag to skip all those confirmations, and the community calls it **YOLO mode**. Running it inside Docker keeps it from touching anything outside your project folder.

## The flag

Claude Code can run without asking for any permission:

```
claude --dangerously-skip-permissions
```

The name says it all. Claude will edit files, run commands and install packages without ever asking you. No more pressing Enter fifty times per session.

## Why run it in Docker?

Because "dangerously" is not a joke. With this flag, Claude can run any command on your machine. A bad instruction, or a misunderstanding, and it could delete files or mess with your system.

The fix is simple: run Claude Code inside a Docker container. The container only sees the current folder. Your Windows files, your documents, your system are out of reach. Worst case, Claude breaks the container, and you throw it away.

## Prerequisite: Docker Desktop

You need Docker Desktop installed on Windows. Download it here and follow the installer:

[Install Docker Desktop on Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

Once installed, make sure Docker Desktop is running before using the alias below.

## Create the yolo alias

We will add a `yolo` function to your PowerShell profile, so you can type `yolo` in any project folder and get Claude Code in YOLO mode, safely contained.

Open your PowerShell profile:

```
notepad $PROFILE
```

If notepad asks to create the file, say yes. Then paste this function and save:

```powershell
function yolo {
    docker run -it --rm -u node -v claude_auth:/home/node -v "${PWD}:/app" -w /app node:22 npx -y @anthropic-ai/claude-code --dangerously-skip-permissions
}
```

Close and reopen your terminal so the profile loads.

## How to use it

Go to your project folder and type:

```
cd C:\my-project
yolo
```

The first time, Docker downloads the Node image and Claude Code asks you to log in. After that, you are in a normal Claude Code session, except it never asks for permission again.

## What the command does

A quick breakdown, so you know what you are running:

- `docker run -it --rm` starts a temporary container and deletes it when you quit
- `-u node` runs as a normal user instead of root
- `-v claude_auth:/home/node` stores your Claude login in a Docker volume, so you only log in once
- `-v "${PWD}:/app"` mounts the current folder into the container. This is the only folder Claude can see
- `-w /app` sets that folder as the working directory
- `node:22 npx -y @anthropic-ai/claude-code` runs the latest Claude Code with Node
- `--dangerously-skip-permissions` the YOLO part

That last mount is the whole point: Claude has full freedom inside `/app`, which is just your project folder, and nothing else.

## One warning

YOLO mode inside Docker protects your machine, not your project. Claude can still rewrite or delete anything in the folder you launched it from. Use git, commit often, and you will always be able to roll back.
