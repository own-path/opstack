---
name: monid
version: 0.1.7
description: >-
  Free live web search and clean page fetch via TinyFish on the Monid CLI. Use
  whenever you need current information from the web, search results, news,
  research papers, or the readable text of a URL — and whenever the user
  mentions "monid" or "tinyfish". Both endpoints cost $0 and never draw down
  the Monid wallet balance. Exception: if the user already has a dedicated
  web-search tool or MCP for the job, use that instead.
---

# Free web search & fetch (TinyFish via Monid)

Two endpoints, both **$0/call**, both verified healthy:

| Need | Command |
|---|---|
| Search the live web | `monid run -p tinyfish -e /search --query '{...}' -w 60` |
| Read pages as Markdown | `monid run -p tinyfish -e /fetch -i '{...}' -w 60` |

Search returns ranked snippets only. When you need the actual page text, pipe the
result URLs into `/fetch` — it is also free.

Set `NO_COLOR=1` for clean, parseable output.

## Search — `-p tinyfish -e /search`

Parameters go in `--query` (they are query params, not a body).

```bash
NO_COLOR=1 monid run -p tinyfish -e /search -w 60 --query '{
  "query": "NVIDIA Q4 FY2025 revenue",
  "purpose": "compare reported revenue against analyst estimates"
}'
```

- `query` (required) — natural language; `site:` operators work but the domain
  filters below are preferred.
- `purpose` — a short statement of the task the results are for. It is an extra
  ranking signal, so it is worth setting.
- `domain_type` — `web` (default), `news` (adds publisher and date), or
  `research_paper` (adds authors, venue, year, cited_by_count, pdf_url).
- `include_domains` / `exclude_domains` — comma-separated, e.g.
  `"include_domains": "github.com,arxiv.org"`.
- `recency_minutes`, or `after_date` / `before_date` for calendar bounds.
- `location` / `language` — country and language codes; default US / en.
- `page` — 0-10.

Returns `position`, `title`, `url`, `site_name`, `snippet` per result.

## Fetch — `-p tinyfish -e /fetch`

Parameters go in `-i` (a JSON **body**).

```bash
NO_COLOR=1 monid run -p tinyfish -e /fetch -w 60 -i '{
  "urls": ["https://example.com/pricing"],
  "format": "markdown"
}'
```

- `urls` (required) — 1 to 10 http(s) URLs, fetched in parallel. Private IPs,
  localhost and cloud metadata endpoints are rejected.
- `format` — `markdown` (default), semantic `html`, or a `json` document tree.
- `include_selectors` / `exclude_selectors` — CSS scoping. A total miss returns
  `candidate_selectors` hints rather than silently falling back to the whole page.
- `ttl` — omit for any cached copy, `0` to force a live fetch, or a max age in
  seconds.
- `links` / `image_links` — return absolute URLs.

HTML, PDF, JSON and plain text are supported; images are not. A per-URL failure
never fails the batch — it lands in `errors[]` with a code such as
`target_http_error`, `page_not_found`, `timeout` or `bot_blocked`.

## Rate limits

Search 30/min (500/hour). Fetch 150 URLs/min (1,000/day). Both free, no
per-request charge.

## Cost rule — the only one that matters here

Monid's wider catalog is **paid per run** and spends real balance. This skill
covers the two free TinyFish endpoints and nothing else.

- Never run any other provider or endpoint without asking first, and say what it
  will cost. `monid balance` shows what is left.
- Do not "discover" your way onto a paid scraper because it looks like a better
  fit. If TinyFish search + fetch cannot do the job, say so and let the user
  decide, rather than spending their balance on their behalf.
- If the user already has a dedicated tool for the task, use that instead.

## Troubleshooting

- **"No active API key"** — `monid keys add -k <key> -l main`, then
  `monid keys list` to confirm which key is active (★).
- **Run not `COMPLETED`** — check with `monid runs get -r <runId>`. Status values
  are UPPERCASE. `BLOCKED` is terminal and means a workspace budget/run cap
  stopped it; that only applies to paid endpoints, not these.
- `-w 60` waits up to 60s. Search is ~2.5s typical, fetch ~7s (21s tail).
