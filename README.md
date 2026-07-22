# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2217**
- Today's entries: **7**
- Today's note: `notes/2026-07-22.md`

### Latest Entry

- Timestamp: `2026-07-22T19:55:52+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 111
- `Accessibility`: 111
- `Architecture`: 111
- `Backend`: 111
- `CI/CD`: 111

### Recent Timeline

- `2026-07-22T19:55:52+08:00` | **Write decisions down** (Leadership)
- `2026-07-22T17:58:52+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-22T15:21:51+08:00` | **Measure before tuning** (Performance)
- `2026-07-22T12:34:00+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-22T09:08:19+08:00` | **Retry only safe operations** (Networking)
- `2026-07-22T07:41:20+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-22T06:36:18+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-21T22:13:37+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-21T19:59:58+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-21T18:01:21+08:00` | **Automate rollback paths** (DevOps)
