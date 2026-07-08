# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2000**
- Today's entries: **13**
- Today's note: `notes/2026-07-08.md`

### Latest Entry

- Timestamp: `2026-07-08T16:38:31+08:00`
- Title: **Write one behavior per test**
- Category: `Testing`
- Source: https://martinfowler.com/bliki/UnitTest.html
- Summary: Single-purpose tests fail with clearer intent and reduce time spent diagnosing what actually regressed.

### Top Categories

- `Testing`: 101
- `APIs`: 100
- `Accessibility`: 100
- `Architecture`: 100
- `Backend`: 100

### Recent Timeline

- `2026-07-08T16:38:31+08:00` | **Write one behavior per test** (Testing)
- `2026-07-08T15:37:25+08:00` | **Use virtual environments by default** (Python)
- `2026-07-08T14:36:28+08:00` | **Prefer small focused commits** (Git)
- `2026-07-08T13:41:28+08:00` | **Write decisions down** (Leadership)
- `2026-07-08T12:36:16+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-08T11:23:35+08:00` | **Measure before tuning** (Performance)
- `2026-07-08T10:01:37+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-08T09:13:47+08:00` | **Retry only safe operations** (Networking)
- `2026-07-08T08:38:33+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-08T07:48:44+08:00` | **Keep runbooks close to code** (Documentation)
