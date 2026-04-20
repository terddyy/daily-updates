# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **79**
- Today's entries: **11**
- Today's note: `notes/2026-04-20.md`

### Latest Entry

- Timestamp: `2026-04-20T11:03:09+08:00`
- Title: **Use virtual environments by default**
- Category: `Python`
- Source: https://docs.python.org/3/library/venv.html
- Summary: Project-specific virtual environments prevent dependency leaks across projects and make builds more reproducible on CI.

### Top Categories

- `APIs`: 4
- `Accessibility`: 4
- `Architecture`: 4
- `Backend`: 4
- `CI/CD`: 4

### Recent Timeline

- `2026-04-20T11:03:09+08:00` | **Use virtual environments by default** (Python)
- `2026-04-20T09:33:57+08:00` | **Prefer small focused commits** (Git)
- `2026-04-20T08:21:58+08:00` | **Write decisions down** (Leadership)
- `2026-04-20T07:11:13+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-20T06:08:07+08:00` | **Measure before tuning** (Performance)
- `2026-04-20T05:10:38+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-04-20T04:09:12+08:00` | **Retry only safe operations** (Networking)
- `2026-04-20T03:16:23+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-20T02:11:39+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-20T01:11:47+08:00` | **Use exponential backoff with jitter** (Reliability)
