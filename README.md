# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1317**
- Today's entries: **12**
- Today's note: `notes/2026-05-19.md`

### Latest Entry

- Timestamp: `2026-05-19T17:32:14+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 66
- `Accessibility`: 66
- `Architecture`: 66
- `Backend`: 66
- `CI/CD`: 66

### Recent Timeline

- `2026-05-19T17:32:14+08:00` | **Write decisions down** (Leadership)
- `2026-05-19T16:13:34+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-19T14:49:13+08:00` | **Measure before tuning** (Performance)
- `2026-05-19T13:25:59+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-19T11:47:17+08:00` | **Retry only safe operations** (Networking)
- `2026-05-19T10:22:21+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-19T09:19:02+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-19T08:09:52+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-19T07:38:38+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-19T07:09:02+08:00` | **Automate rollback paths** (DevOps)
