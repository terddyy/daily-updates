# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2237**
- Today's entries: **3**
- Today's note: `notes/2026-07-25.md`

### Latest Entry

- Timestamp: `2026-07-25T14:39:57+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 112
- `Accessibility`: 112
- `Architecture`: 112
- `Backend`: 112
- `CI/CD`: 112

### Recent Timeline

- `2026-07-25T14:39:57+08:00` | **Write decisions down** (Leadership)
- `2026-07-25T07:32:10+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-25T06:17:55+08:00` | **Measure before tuning** (Performance)
- `2026-07-24T21:06:31+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-24T19:41:52+08:00` | **Retry only safe operations** (Networking)
- `2026-07-24T17:54:34+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-24T15:17:44+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-24T12:32:26+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-24T09:09:32+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-24T07:39:22+08:00` | **Automate rollback paths** (DevOps)
