# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1677**
- Today's entries: **9**
- Today's note: `notes/2026-06-15.md`

### Latest Entry

- Timestamp: `2026-06-15T16:28:47+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 84
- `Accessibility`: 84
- `Architecture`: 84
- `Backend`: 84
- `CI/CD`: 84

### Recent Timeline

- `2026-06-15T16:28:47+08:00` | **Write decisions down** (Leadership)
- `2026-06-15T14:07:59+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-15T12:13:02+08:00` | **Measure before tuning** (Performance)
- `2026-06-15T10:42:04+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-15T09:31:44+08:00` | **Retry only safe operations** (Networking)
- `2026-06-15T08:12:30+08:00` | **Batch similar tasks** (Productivity)
- `2026-06-15T07:42:07+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-15T07:09:48+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-15T06:31:45+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-14T22:31:01+08:00` | **Automate rollback paths** (DevOps)
