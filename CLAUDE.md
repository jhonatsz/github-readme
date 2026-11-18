# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

The GitHub **profile README** for the `jhonatsz` account. GitHub renders
`README.md` from the default branch of the repo named after the user
(`jhonatsz/jhonatsz`) at the top of <https://github.com/jhonatsz>. There is no
code, build, lint or test step: the repo is `README.md` plus `images/`, and one
generator script for the banner (`scripts/gen_banner.py`).

Every push to the default branch is a live, public change to the profile page.

## Previewing changes

There is no local toolchain. Check rendering with a GitHub-flavored Markdown
preview (the page mixes Markdown and inline HTML, so a plain Markdown preview
is not accurate), or push to a branch and view the README on GitHub in both
light and dark themes before merging.

## How README.md is put together

The page has a hacker/terminal theme: green `00ff41` on near-black `0d0208`
everywhere. Sections, top to bottom: Matrix-rain banner, `$ cat about.txt`,
`$ ls ~/stack`, `$ git stats`, `$ ping jhonatsz`.

- **GitHub strips `style` attributes, CSS and scripts**, so the theme comes
  only from images, badges and code blocks. The page background stays GitHub's
  own; the page looks best in dark mode.
- **Section headings are commands** in inline code (`` ### `$ ls ~/stack` ``),
  with no emoji.
- **About** is a fenced `text` code block of `> key  value` lines, which GitHub
  renders as a monospace panel. Keep the value column aligned.
- **Tech Stack badges** are shields.io images, one per line, all in the same
  shape: `https://img.shields.io/badge/-<Label>-0d0208?style=flat-square&logo=<simple-icons slug>&logoColor=00ff41`.
  URL-encode special characters in the label (`C%2B%2B`). A wrong or retired
  slug still returns HTTP 200 but with no logo, so check the SVG contains an
  `<image` element after adding one (`css3` and `linkedin` are retired).
- **Connect badges** use the same pattern, each wrapped in an `<a>` link inside
  a centered `<p>`. LinkedIn has no simple-icons slug any more, so its badge
  embeds the logo as a URL-encoded base64 SVG data URI in `logo=`.
- **GitHub Analytics** cards come from the hosted service
  [ghstats.dev](https://ghstats.dev) (`/api/card` and `/api/langs`; options in
  its [README](https://github.com/rowkavdev/GitHub-profile-stats)). It replaced
  a self-hosted github-readme-stats Vercel deployment that was disabled in
  2026-11. Both cards carry the same colour overrides (`bg`, `text`,
  `title_color`, `icon_color`, `border_color`) for a Matrix look: green
  `00ff41` on near-black `0d0208`; change them together. Both images use `height="176"` so
  they sit side by side within the README width. It only sees public activity.

## Images

Local assets live in `images/` and are referenced by relative path, which works
because the README is rendered from this repo's default branch.

- `images/matrix-banner.svg` is the live banner: falling glyphs plus a typed
  name line, animated with CSS only (GitHub serves SVGs as images, so scripts
  never run). It is generated, not hand-edited: change `scripts/gen_banner.py`
  and run `python3 scripts/gen_banner.py images/matrix-banner.svg`.
- `images/banner.png` is the previous banner, kept as a backup and not
  referenced by the README.

## Markdown/HTML gotcha

Leave a blank line between a raw HTML block (`<a>…</a>`, `<br/>`) and the next
`###` heading. Without it the heading stays inside the HTML block and GitHub
shows it as literal `### …` text.
