---
layout: post
title: 'How to Make VS Code Look and Feel Like SSMS (SQL Server Management Studio)'
date: 2026-03-25
categories: "SQL-Server"
tags: [sql-server, vscode, ssms, productivity, keybindings, extension, query-shortcuts, column-selection]
comments: true
permalink: /sql-server/make-vs-code-look-and-feel-like-ssms
parent: SQL Server
---
# {{ page.title }}
{: .fs-9 }

{:toc}

{: .note-title :}
>Two free tools to bring your favorite SSMS features into VS Code:
>1. A **keybindings.json** file for SSMS-style column/box selection, and to free up `Ctrl+1` to `Ctrl+4` for query shortcuts
>2. A **VS Code extension** that replicates SSMS Query Shortcuts (`Ctrl+3` = `SELECT TOP 1000 * FROM ...`)
>
>Both files work together. Download links are at the bottom of each section.

---

## Why Switch from SSMS to VS Code?

VS Code is fast, lightweight, and extensible. With the [mssql extension](https://marketplace.visualstudio.com/items?itemName=ms-mssql.mssql), it connects to SQL Server and lets you write and run queries just like SSMS.

But if you have been using SSMS for years, two things will feel off right away:

- **Column selection does not work the same way.** In SSMS, `Alt+Shift+Arrow` gives you a clean rectangular (box) selection. In VS Code, the same shortcut creates multi-cursors, which behaves very differently.
- **Query Shortcuts are missing.** In SSMS, you can highlight a table name and press `Ctrl+3` to instantly run `SELECT TOP 1000 * FROM YourTable`. VS Code has no built-in equivalent.

This post solves both problems.

---

## Part 1: SSMS-Style Column Selection and Keybinding Fixes

### What this fixes

In SSMS, `Alt+Shift+Arrow` selects a rectangular block of text (box selection). The selection stays within a column and does not wrap to the next line. This is extremely useful when working with aligned SQL code.

VS Code uses the same shortcut for multi-cursor mode, which adds cursors on multiple lines instead. If you are coming from SSMS, this feels wrong.

### What you get

The custom keybindings file remaps VS Code to behave like SSMS:

| Shortcut | Behavior |
|----------|----------|
| `Alt+Shift+Arrow` | Column (box) selection, exactly like SSMS |
| `Alt+Shift+PageUp/PageDown` | Column select by page |
| `Shift+Arrow` | Normal text selection (no multi-cursor) |
| `Ctrl+Shift+Arrow` | Word-level selection |
| `Shift+Home/End` | Select to start/end of line |
| `Ctrl+R` | Toggle the results/terminal panel (same as SSMS `Ctrl+R`) |

### Toggle the results panel with Ctrl+R

In SSMS, pressing `Ctrl+R` hides or shows the results pane. This is very handy when you want more screen space for your query, or when you want to quickly check results and hide them again.

The keybindings file maps `Ctrl+R` to VS Code's `workbench.action.togglePanel` command, which toggles the bottom panel (terminal, results, problems). Same shortcut, same behavior.

### Important: freeing up Ctrl+1 to Ctrl+4

By default, VS Code uses `Ctrl+1`, `Ctrl+2`, `Ctrl+3`, and `Ctrl+4` to switch between editor groups (split panes). This means that without this keybindings file, the query shortcuts from Part 2 would conflict with these built-in VS Code shortcuts.

The keybindings file takes care of this: it **disables the default `Ctrl+1` to `Ctrl+4` editor group bindings**, so the query shortcut extension can use them without any conflict.

{: .warning :}
>**Both parts work together.** If you install the query shortcuts extension (Part 2) without this keybindings file, pressing `Ctrl+1` to `Ctrl+4` will switch editor groups instead of running your SQL queries. Make sure to install both.

### Installation

1. Open VS Code
2. Press `Ctrl+Shift+P` and type **"Preferences: Open Keyboard Shortcuts (JSON)"**
3. Paste the contents of the downloaded file into the JSON array
4. Add these two settings to your `settings.json` (`Ctrl+Shift+P` > **"Preferences: Open Settings (JSON)"**):

```json
"editor.columnSelection": false,
"editor.multiCursorModifier": "ctrlCmd"
```

{: .note :}
>`editor.columnSelection: false` prevents VS Code from using column selection as the default for all selections. `editor.multiCursorModifier: "ctrlCmd"` changes the multi-cursor trigger from `Alt+Click` to `Ctrl+Click`, which avoids conflicts with the column selection shortcuts.

### Download

[keybindings.json](../../assets/2026/visual-studio-code-ssms/keybindings.json)

---

## Part 2: SSMS Query Shortcuts (VS Code Extension)

### What this fixes

In SSMS, you can go to **Tools > Options > Environment > Keyboard > Query Shortcuts** and assign SQL templates to keyboard shortcuts. For example, `Ctrl+3` runs `SELECT TOP 1000 * FROM` with whatever table name you have selected.

This is one of the most popular SSMS productivity features (I wrote [a blog post about it back in 2019](/en/ssms-query-shortcuts-feel-like-a-super-man-developer/)). VS Code and the mssql extension do not offer this.

So I built a VS Code extension that brings it back.

{: .highlight :}
>I **vibe coded this extension with [Claude Code](https://claude.com/claude-code)**. I described the SSMS behavior I wanted to replicate, and Claude Code generated the full extension from scratch: the manifest (`package.json`), the keybindings, the settings schema, and the inject/execute/undo logic (`extension.js`). The whole thing was built through a conversation, not by writing code manually. So, you are informed :)

### Default shortcuts

| Shortcut | SQL Template |
|----------|-------------|
| `Alt+F1` | `EXEC sp_help '{0}'` |
| `Ctrl+1` | `EXEC sp_who` |
| `Ctrl+2` | `EXEC sp_lock` |
| `Ctrl+3` | `SELECT TOP 1000 * FROM {0}` |
| `Ctrl+4` | `SELECT COUNT(1) AS Nb FROM {0}` |
| `Ctrl+5` to `Ctrl+0` | Empty, ready for your own queries |

`{0}` is replaced by the text you have selected, or the word under your cursor.

{: .note :}
>Remember: `Ctrl+1` to `Ctrl+4` are used by VS Code by default to switch editor groups. The keybindings file from Part 1 disables those defaults so these query shortcuts work properly. The extension also scopes its shortcuts to `.sql` files only, so they will not interfere with your normal VS Code shortcuts in other file types.

### How to use it

1. Open a `.sql` file connected to a SQL Server database (via the mssql extension)
2. Select a table name, or just place your cursor on one
3. Press the shortcut (for example `Ctrl+3`)
4. The query runs and results appear in the results pane
5. Your code is **never modified**, and no new tab opens

### How it works under the hood

The extension uses a clever **inject, execute, undo** pattern to run your query without leaving any trace in your file:

1. **Capture** the current cursor position and selection
2. **Get the target text** by reading your selection, or if nothing is selected, by grabbing the word under your cursor (using VS Code's `getWordRangeAtPosition` API)
3. **Build the SQL** by replacing `{0}` in the template with the target text
4. **Append the generated query** at the very end of the current document, separated by a `-- [SSMS Shortcut]` comment line
5. **Select only the appended SQL** and call the mssql extension's `runQuery` command, which executes whatever text is currently selected
6. **Wait briefly** (500ms) for mssql to capture the query text
7. **Undo the insertion** with a single `undo` command, which restores the document to its original state
8. **Restore the cursor** to its original position

The result: the query runs, the results appear, and your file looks exactly as it did before. No leftover text, no new tabs, no modifications to your code.

### Customization

You can change any shortcut template in your VS Code `settings.json`:

```json
"ssmsShortcuts.shortcuts": {
    "altF1": "EXEC sp_help '{0}'",
    "ctrl1": "EXEC sp_who",
    "ctrl2": "EXEC sp_lock",
    "ctrl3": "SELECT TOP 1000 * FROM {0}",
    "ctrl4": "SELECT COUNT(1) AS Nb FROM {0}",
    "ctrl5": "",
    "ctrl6": "",
    "ctrl7": "",
    "ctrl8": "",
    "ctrl9": "",
    "ctrl0": ""
}
```

Replace any empty string with your own SQL template. Use `{0}` wherever you want the selected text to be inserted.

### Installation

1. Download the extension zip below
2. Unzip it
3. Copy the `ssms-query-shortcuts` folder to:
   ```
   %USERPROFILE%\.vscode\extensions\
   ```
4. Restart VS Code

{: .warning :}
>The [mssql extension](https://marketplace.visualstudio.com/items?itemName=ms-mssql.mssql) must be installed and your `.sql` file must be connected to a SQL Server database for the query shortcuts to work.

### Download

[ssms-query-shortcuts.zip](../../assets/2026/visual-studio-code-ssms/ssms-query-shortcuts.zip)

---

## Quick Setup Checklist

If you want the full SSMS experience in VS Code, here is everything in order:

1. Install the [mssql extension](https://marketplace.visualstudio.com/items?itemName=ms-mssql.mssql)
2. Download and apply the [keybindings.json](../../assets/2026/visual-studio-code-ssms/keybindings.json) for column selection and to free up `Ctrl+1` to `Ctrl+4`
3. Add `editor.columnSelection: false` and `editor.multiCursorModifier: "ctrlCmd"` to your settings
4. Download and install the [ssms-query-shortcuts extension](../../assets/2026/visual-studio-code-ssms/ssms-query-shortcuts.zip)
5. Restart VS Code
6. Open a `.sql` file, connect to your database, and enjoy your SSMS shortcuts
