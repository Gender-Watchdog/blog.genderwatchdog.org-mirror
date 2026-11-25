# CLAUDE.md

Jekyll blog mirrored to GitHub Pages (blog.genderwatchdog.org), with posts also published on Bear Blog. Site config: `_config.yml` (kramdown/GFM, `future: true`).

## Repo layout

- `_posts/` — published posts, committed. Filename: `YYYY-MM-DD-slug.md`.
- `secret-files/` — private working files, gitignored, never committed. `secret-files/blog-posts/` holds raw imported drafts that `_posts/` entries are periodically synced from.
- `.github/copilot-instructions.md` — also gitignored; local-only Copilot instructions. This file is the Claude-native equivalent — don't maintain both in parallel unless asked.

## Syncing a `_posts/` file from its `secret-files/blog-posts/` source draft

When asked to update a post to match its imported draft:

1. Read both files and diff for new/changed sections, footnotes, and frontmatter.
2. Port new content into the `_posts/` version, preserving its established structure and citation style — do not just overwrite with the draft's frontmatter (see below).
3. Convert any Markdown links in new content to the HTML link format required by `_posts/` (see Formatting Rules).
4. Update the `title` timestamp and `last_modified_at` (see below).
5. Extend `tags` in frontmatter if new sections introduce new named entities/topics. Only rewrite `summary`/`meta_description` if the update meaningfully changes the post's overall thrust.

`_posts/` frontmatter carries more fields than the source draft (`layout`, `slug`, `lang`, `tags`, `meta_description`, `bearblog_url`, plus `gh_pages_url`/`summary` also present in the draft) — keep the `_posts/` superset, only pulling in content changes from the draft, not its frontmatter shape.

## Formatting rules

**Title timestamp and `last_modified_at`** — every content update to a `_posts/` file requires the YAML `title` to append/replace the stamp **and** `last_modified_at` to be set to the same timestamp:
```yaml
title: "Original Title (updated at YYYY-MM-DDTHH:MM:SSZ)"
last_modified_at: YYYY-MM-DDTHH:MM:SSZ
```
Replace an existing `(updated at ...)` and an existing `last_modified_at`; never accumulate multiple. Use the user-supplied timestamp if given, otherwise one `date -u +"%Y-%m-%dT%H:%M:%SZ"` value for both. Translations use their language's wording in the title (e.g. `（更新于 …Z）`) but the identical ISO time and the same `last_modified_at`. A first publication carries neither. `last_modified_at` feeds the sitemaps and JSON-LD `dateModified`, but the templates still read the title stamp when it's missing, so older posts keep working.

**Links** — never embed link text as Markdown `[description](URL)` where the description isn't the raw URL. Description precedes the link, URL fully visible. In `_posts/` files specifically, use HTML (kramdown/GFM chokes on complex unescaped URLs in Markdown link syntax):
```
Description: <a href="URL">URL</a>
```

**Images** — if an imported draft uses GitHub image links, use those same links everywhere in the `_posts/` version, including the `image:` frontmatter field. Don't make local copies under `assets/`; they're unnecessary, since this low-traffic site doesn't need faster image loading.

## Do not

- Don't commit or push without explicit user confirmation, even after a successful sync/edit.
- Don't edit `.github/copilot-instructions.md` unless asked — it's a separate, independently maintained instruction file.
- Don't start the Jekyll preview server (`bundle exec jekyll serve --future`) unless the user wants to preview changes.
