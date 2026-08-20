# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2717**
- Today's entries: **5**
- Today's note: `notes/2026-08-20.md`

### Latest Entry

- Timestamp: `2026-08-20T09:12:53+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 136
- `Accessibility`: 136
- `Architecture`: 136
- `Backend`: 136
- `CI/CD`: 136

### Recent Timeline

- `2026-08-20T09:12:53+08:00` | **Write decisions down** (Leadership)
- `2026-08-20T07:47:01+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-20T07:21:45+08:00` | **Measure before tuning** (Performance)
- `2026-08-20T06:50:59+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-20T06:23:54+08:00` | **Retry only safe operations** (Networking)
- `2026-08-19T22:18:03+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-19T21:43:03+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-19T20:45:42+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-19T19:52:37+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-19T19:27:54+08:00` | **Automate rollback paths** (DevOps)
