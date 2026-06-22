# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1759**
- Today's entries: **5**
- Today's note: `notes/2026-06-22.md`

### Latest Entry

- Timestamp: `2026-06-22T09:02:08+08:00`
- Title: **Use virtual environments by default**
- Category: `Python`
- Source: https://docs.python.org/3/library/venv.html
- Summary: Project-specific virtual environments prevent dependency leaks across projects and make builds more reproducible on CI.

### Top Categories

- `APIs`: 88
- `Accessibility`: 88
- `Architecture`: 88
- `Backend`: 88
- `CI/CD`: 88

### Recent Timeline

- `2026-06-22T09:02:08+08:00` | **Use virtual environments by default** (Python)
- `2026-06-22T07:47:09+08:00` | **Prefer small focused commits** (Git)
- `2026-06-22T07:11:41+08:00` | **Write decisions down** (Leadership)
- `2026-06-22T06:41:11+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-22T06:10:31+08:00` | **Measure before tuning** (Performance)
- `2026-06-21T22:16:56+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-21T21:16:08+08:00` | **Retry only safe operations** (Networking)
- `2026-06-21T20:26:40+08:00` | **Batch similar tasks** (Productivity)
- `2026-06-21T19:43:25+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-21T17:20:06+08:00` | **Use exponential backoff with jitter** (Reliability)
