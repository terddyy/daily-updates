# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1477**
- Today's entries: **10**
- Today's note: `notes/2026-05-30.md`

### Latest Entry

- Timestamp: `2026-05-30T19:00:52+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 74
- `Accessibility`: 74
- `Architecture`: 74
- `Backend`: 74
- `CI/CD`: 74

### Recent Timeline

- `2026-05-30T19:00:52+08:00` | **Write decisions down** (Leadership)
- `2026-05-30T17:27:20+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-30T14:34:08+08:00` | **Measure before tuning** (Performance)
- `2026-05-30T13:21:12+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-30T11:46:45+08:00` | **Retry only safe operations** (Networking)
- `2026-05-30T10:21:40+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-30T08:09:54+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-30T07:36:05+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-30T06:57:13+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-30T06:18:14+08:00` | **Automate rollback paths** (DevOps)
