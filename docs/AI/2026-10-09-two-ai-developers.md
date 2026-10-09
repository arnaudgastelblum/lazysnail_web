---
layout: post
title: "Two AI developers and me: how I build with Claude Code and Codex"
date: 2026-10-09
categories: "ai"
tags: [claude-code, codex, ai, workflow]
comments: true
parent: AI
permalink: /ai/two-ai-developers
description: "One Claude Code conversation that hands work to Claude subagents and to OpenAI's Codex, has each one review the other, and spreads the usage over two subscriptions."
---
# {{ page.title }}
{: .fs-9 }

I pay for two AI plans: Claude and ChatGPT. I could use them in two windows and copy things from one to the other. Instead, I talk to **one** Claude Code conversation, and it hands work to Codex (OpenAI) by itself.

This is how I built [Snailkit](/obsidian/snailkit), the Obsidian plugin I just released.

![Me, Claude Code as the lead, Claude subagents, codex-dev and codex-review](/assets/2026/two-ai-developers/team.webp)

## The setup

Claude Code can call **subagents**. Two of mine don't run Claude: they run the Codex command line, so the work goes to GPT and is billed to my ChatGPT plan.

- **codex-dev** can write code. It gets a written brief, works on a precise set of files, and never commits.
- **codex-review** is read-only. It reads a diff and lists the real problems it finds.

Claude Code stays the lead. It plans, splits the work, writes the briefs, puts everything together, tests, and handles git. I talk to it in French, about what I want. I decide, and I test on my own vault and on my phone.

## The rules

They live in my personal `CLAUDE.md`, so every conversation follows them:

```text
Keep on Claude: planning, anything that needs this conversation, git, small edits.
Send to codex-dev: work that fits in a written brief and can be checked afterwards.
Send to codex-review: any substantial change written by Claude.
GPT sees nothing of the conversation: every brief stands alone.
Codex never commits. Claude reads the diff and owns the result.
```

The last two lines matter most. A brief has to say the goal, the files, the constraints and the command that proves it works. Writing that well is half the job.

## What it looks like for real

- **Cross review catches real bugs.** Claude built a new tag picker. GPT reviewed it and found six real problems, for example a task saved under the wrong tag in an empty list. Claude fixed all six before I ever saw them.
- **Each one catches the other.** Obsidian's automated review flagged a hundred warnings. GPT could not reproduce them. Claude found why: a type library that the review machine didn't have. Then it proved it by hiding that library on my machine.
- **Two streams at once.** On the phone redesign, GPT reworked the Home tab while Claude reworked Tasks, on separate files, at the same time.
- **The boring work goes out.** GPT cleaned up the plugin's styles and checked 273 cases to prove nothing changed on screen.

## Ask three, keep one

Before building something visual, I ask for several mockups from one brief. Opus does one, Fable another, GPT a third, or GPT challenges the idea instead. I open them side by side and choose. For the tag picker, Fable's version won.

![One brief, three mockups, one choice](/assets/2026/two-ai-developers/mockups.webp)

It also works for plain ideas: "here is my plan, tell me what's wrong with it" to a model that wrote none of it.

## Spreading the usage

Every task Codex takes is usage that doesn't count on my Claude plan. When one plan runs low, I just say so, and Claude sends more work to the other side. Same conversation, nothing to copy and paste.

## What it doesn't do

It doesn't make me a spectator. Codex once read an old brief and reviewed the wrong code, and Claude had to catch it. Every result still gets read, built, [tested in the real app](/ai/ai-tests-real-app), and then tested by me. The AIs write most of the code. The decisions, the taste and the "no, not like this" are still mine.

{: .note }
> Want to try it? Start small: one `codex-review` subagent that reviews Claude's diff before you commit. It's the cheapest way to get a second pair of eyes.
