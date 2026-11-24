# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

The GitHub **profile README** for the `jhonatsz` account. GitHub renders
`README.md` from the default branch of the repo named after the user
(`jhonatsz/jhonatsz`) at the top of <https://github.com/jhonatsz>. There is no
code, build, lint or test step: the repo is `README.md` plus `images/`, and one
generator script for the banner (`scripts/gen_banner.py`).

Every push to the default branch is a live, public change to the profile page.

## Changes go through pull requests

Never push to `main` directly. Put every change on a branch (`fix/<topic>`,
`feat/<topic>` or `docs/<topic>`, with no author segment), push the branch and
open a pull request. The owner merges; don't merge it yourself unless asked.

The one exception is the `update-cards` workflow, whose `github-actions[bot]`
commits the regenerated card SVGs straight to `main`. To preview a card
change before merging, run the workflow against the branch
(`gh workflow run update-cards.yml --ref <branch>`); the bot then commits the
cards to that branch.

## Previewing changes

There is no local toolchain. Check rendering with a GitHub-flavored Markdown
preview (the page mixes Markdown and inline HTML, so a plain Markdown preview
is not accurate), or push to a branch and view the README on GitHub in both
light and dark themes before merging.

## How README.md is put together

The page has a hacker/terminal theme: green `00ff41` on near-black `0d0208`
everywhere. Sections, top to bottom: Matrix-rain banner, `$ cat about.txt`,
`$ ls ~/stack`, `$ git stats`, `$ uptime`, `$ ping jhonatsz`.

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
  AWS has no slug either and its logo is too long for a data URI, so its badge
  is a saved shields.io SVG at `images/badge-aws.svg`. The list is kept to
  about 15 cloud and platform tools on purpose; swap entries rather than grow it.
- **Connect badges** use the same pattern, each wrapped in an `<a>` link inside
  a centered `<p>`. LinkedIn has no simple-icons slug any more, so its badge
  embeds the logo as a URL-encoded base64 SVG data URI in `logo=`.
- **`$ git stats`** is three cards: the stats card (with rank) and the
  languages card side by side, then the streak card on its own row. The
  first two are generated in this repo and the streak card is hosted, so one
  outage doesn't blank the whole section. All carry the same Matrix palette
  (green `00ff41` on near-black `0d0208`, border `003b00`) under differently named colour
  parameters; change them together. All three images use `height="176"`.
  The two rows are sized to line up: both generated cards hide their titles,
  the stats card uses `line_height=28` so its height (183) is close to the
  languages card's (185), and the streak card's `card_width=818` makes it
  as wide as the row above (about 738 px). Changing `langs_count`, the stat
  lines or a title changes those sizes, so recompute the streak width.
  - The streak card is hosted:
    [github-readme-streak-stats](https://github.com/DenverCoder1/github-readme-streak-stats)
    (`streak-stats.demolab.com`). A failing hosted card still returns an SVG,
    so check the card text, not the HTTP status.
  - The stats card (with rank) and the languages card are files in this
    repo, `images/stats.svg` and `images/top-langs.svg`,
    rendered daily by `.github/workflows/update-cards.yml` with
    [github-readme-stats-action](https://github.com/stats-organization/github-readme-stats-action)
    and committed by `github-actions[bot]`. Don't hand-edit them; change the
    `options` lines in the workflow and run it (`gh workflow run
    update-cards.yml`). The bot pushes to `main`, so pull before committing.
    It counts private repos only when the `STATS_TOKEN` secret holds a
    read-only PAT; without it the workflow token sees public repos only. The
    action and its `core_version` are pinned because the job handles that
    token; bump them deliberately.
  - History: these replaced ghstats.dev, which returned HTTP 500 for every
    user on 2026-11-25 when its shared GitHub token was rate limited, and
    which had replaced a self-hosted github-readme-stats Vercel deployment
    disabled earlier in 2026-11.

- **`$ uptime`** is a 31-day contribution graph from
  [github-readme-activity-graph](https://github.com/Ashutosh00710/github-readme-activity-graph)
  (public Vercel instance), coloured to match the cards. It plots the
  public contribution calendar, so private work appears only if the account
  setting to show private contributions is on.

## Images

Local assets live in `images/` and are referenced by relative path, which works
because the README is rendered from this repo's default branch.

- `images/matrix-banner.svg` is the live banner: falling glyphs plus a typed
  name line, animated with CSS only (GitHub serves SVGs as images, so scripts
  never run). It is generated, not hand-edited: change `scripts/gen_banner.py`
  and run `python3 scripts/gen_banner.py images/matrix-banner.svg`.
- `images/stats.svg` and `images/top-langs.svg` are the stats and languages
  cards, regenerated daily by the
  `update-cards` workflow (see `$ git stats` above).
- `images/banner.png` is the previous banner, kept as a backup and not
  referenced by the README.

## Markdown/HTML gotcha

Leave a blank line between a raw HTML block (`<a>…</a>`, `<br/>`) and the next
`###` heading. Without it the heading stays inside the HTML block and GitHub
shows it as literal `### …` text.
