# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

The GitHub **profile README** for the `jhonatsz` account. GitHub renders
`README.md` from the default branch of the repo named after the user
(`jhonatsz/jhonatsz`) at the top of <https://github.com/jhonatsz>. There is no
code, build, lint or test step: the repo is `README.md` plus `images/`.

Every push to the default branch is a live, public change to the profile page.

## Previewing changes

There is no local toolchain. Check rendering with a GitHub-flavored Markdown
preview (the page mixes Markdown and inline HTML, so a plain Markdown preview
is not accurate), or push to a branch and view the README on GitHub in both
light and dark themes before merging.

## How README.md is put together

Sections, top to bottom: banner image, greeting, About Me, Tech Stack, GitHub
Analytics, Connect with Me.

- **Layout is done with inline HTML**, not Markdown: `<img align="left|right">`
  floats, `height`/`width` attributes in `em`, `<br/>` line breaks and `&nbsp;`
  spacing. GitHub strips `style` attributes and CSS, so these attributes are the
  only layout tools. Most of the commit history is fine-tuning these values;
  small changes shift the whole page, so re-check rendering after any edit.
- **The right-floated `coding-3.gif`** sits beside the Tech Stack badges. The
  number of badges decides how the text wraps around it and where the Analytics
  section starts, so adding or removing badges can require re-tuning the image
  height.
- **Tech Stack badges** are shields.io images, one per line, all in the same
  shape: `https://img.shields.io/badge/-<Label>-white?style=flat&logo=<simple-icons slug>[&logoColor=<color>]`.
  Keep the white background and `style=flat`; set `logoColor` only when the
  default logo color is unreadable on white. URL-encode special characters in
  the label (`C%2B%2B`).
- **Connect badges** use the same shields.io pattern but with the brand color as
  the background and `logoColor=white`, each wrapped in an `<a>` link inside a
  centered `<p>`.
- **GitHub Analytics** cards come from the hosted service
  [ghstats.dev](https://ghstats.dev) (`/api/card` and `/api/langs`; options in
  its [README](https://github.com/rowkavdev/GitHub-profile-stats)). It replaced
  a self-hosted github-readme-stats Vercel deployment that was disabled in
  2026-11. ghstats.dev has no `buefy` theme, so both cards carry the same
  colour overrides (`bg`, `text`, `title_color`, `icon_color`, `border_color`)
  to keep that look; change them together. Both images use `height="176"` so
  they sit side by side within the README width. It only sees public activity.

## Images

Local assets live in `images/` and are referenced by relative path, which works
because the README is rendered from this repo's default branch.

## Markdown/HTML gotcha

Leave a blank line between a raw HTML block (`<a>…</a>`, `<br/>`) and the next
`###` heading. Without it the heading stays inside the HTML block and GitHub
shows it as literal `### …` text.
