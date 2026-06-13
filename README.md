# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1659**
- Today's entries: **2**
- Today's note: `notes/2026-06-14.md`

### Latest Entry

- Timestamp: `2026-06-14T07:09:47+08:00`
- Title: **Use virtual environments by default**
- Category: `Python`
- Source: https://docs.python.org/3/library/venv.html
- Summary: Project-specific virtual environments prevent dependency leaks across projects and make builds more reproducible on CI.

### Top Categories

- `APIs`: 83
- `Accessibility`: 83
- `Architecture`: 83
- `Backend`: 83
- `CI/CD`: 83

### Recent Timeline

- `2026-06-14T07:09:47+08:00` | **Use virtual environments by default** (Python)
- `2026-06-14T06:12:38+08:00` | **Prefer small focused commits** (Git)
- `2026-06-13T22:30:05+08:00` | **Write decisions down** (Leadership)
- `2026-06-13T21:36:54+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-13T19:16:54+08:00` | **Measure before tuning** (Performance)
- `2026-06-13T15:58:51+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-13T14:38:26+08:00` | **Retry only safe operations** (Networking)
- `2026-06-13T11:20:21+08:00` | **Batch similar tasks** (Productivity)
- `2026-06-13T07:11:12+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-12T21:52:37+08:00` | **Use exponential backoff with jitter** (Reliability)
