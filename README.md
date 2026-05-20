# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1339**
- Today's entries: **2**
- Today's note: `notes/2026-05-21.md`

### Latest Entry

- Timestamp: `2026-05-21T07:10:49+08:00`
- Title: **Use virtual environments by default**
- Category: `Python`
- Source: https://docs.python.org/3/library/venv.html
- Summary: Project-specific virtual environments prevent dependency leaks across projects and make builds more reproducible on CI.

### Top Categories

- `APIs`: 67
- `Accessibility`: 67
- `Architecture`: 67
- `Backend`: 67
- `CI/CD`: 67

### Recent Timeline

- `2026-05-21T07:10:49+08:00` | **Use virtual environments by default** (Python)
- `2026-05-21T06:37:42+08:00` | **Prefer small focused commits** (Git)
- `2026-05-20T22:43:00+08:00` | **Write decisions down** (Leadership)
- `2026-05-20T21:40:31+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-20T20:37:56+08:00` | **Measure before tuning** (Performance)
- `2026-05-20T19:42:06+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-20T18:36:26+08:00` | **Retry only safe operations** (Networking)
- `2026-05-20T17:30:07+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-20T16:12:54+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-20T14:49:42+08:00` | **Use exponential backoff with jitter** (Reliability)
