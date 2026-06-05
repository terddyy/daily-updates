# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1559**
- Today's entries: **1**
- Today's note: `notes/2026-06-06.md`

### Latest Entry

- Timestamp: `2026-06-06T06:29:13+08:00`
- Title: **Use virtual environments by default**
- Category: `Python`
- Source: https://docs.python.org/3/library/venv.html
- Summary: Project-specific virtual environments prevent dependency leaks across projects and make builds more reproducible on CI.

### Top Categories

- `APIs`: 78
- `Accessibility`: 78
- `Architecture`: 78
- `Backend`: 78
- `CI/CD`: 78

### Recent Timeline

- `2026-06-06T06:29:13+08:00` | **Use virtual environments by default** (Python)
- `2026-06-05T22:41:07+08:00` | **Prefer small focused commits** (Git)
- `2026-06-05T21:35:33+08:00` | **Write decisions down** (Leadership)
- `2026-06-05T20:26:52+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-05T19:25:49+08:00` | **Measure before tuning** (Performance)
- `2026-06-05T18:08:04+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-05T16:33:22+08:00` | **Retry only safe operations** (Networking)
- `2026-06-05T15:10:01+08:00` | **Batch similar tasks** (Productivity)
- `2026-06-05T13:36:09+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-05T11:47:41+08:00` | **Use exponential backoff with jitter** (Reliability)
