# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1797**
- Today's entries: **16**
- Today's note: `notes/2026-06-24.md`

### Latest Entry

- Timestamp: `2026-06-24T22:18:44+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 90
- `Accessibility`: 90
- `Architecture`: 90
- `Backend`: 90
- `CI/CD`: 90

### Recent Timeline

- `2026-06-24T22:18:44+08:00` | **Write decisions down** (Leadership)
- `2026-06-24T21:18:07+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-24T20:21:02+08:00` | **Measure before tuning** (Performance)
- `2026-06-24T19:27:55+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-24T18:26:19+08:00` | **Retry only safe operations** (Networking)
- `2026-06-24T17:12:06+08:00` | **Batch similar tasks** (Productivity)
- `2026-06-24T15:46:39+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-24T14:23:18+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-24T12:53:40+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-24T11:25:12+08:00` | **Automate rollback paths** (DevOps)
