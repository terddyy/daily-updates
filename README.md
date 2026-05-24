# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1397**
- Today's entries: **1**
- Today's note: `notes/2026-05-25.md`

### Latest Entry

- Timestamp: `2026-05-25T06:06:16+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 70
- `Accessibility`: 70
- `Architecture`: 70
- `Backend`: 70
- `CI/CD`: 70

### Recent Timeline

- `2026-05-25T06:06:16+08:00` | **Write decisions down** (Leadership)
- `2026-05-24T22:34:18+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-24T21:11:13+08:00` | **Measure before tuning** (Performance)
- `2026-05-24T20:40:07+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-24T20:07:23+08:00` | **Retry only safe operations** (Networking)
- `2026-05-24T18:21:25+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-24T17:42:10+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-24T15:46:57+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-24T14:43:57+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-24T09:20:00+08:00` | **Automate rollback paths** (DevOps)
