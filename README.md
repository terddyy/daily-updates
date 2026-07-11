# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2057**
- Today's entries: **16**
- Today's note: `notes/2026-07-11.md`

### Latest Entry

- Timestamp: `2026-07-11T20:49:20+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 103
- `Accessibility`: 103
- `Architecture`: 103
- `Backend`: 103
- `CI/CD`: 103

### Recent Timeline

- `2026-07-11T20:49:20+08:00` | **Write decisions down** (Leadership)
- `2026-07-11T20:22:12+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-11T19:48:43+08:00` | **Measure before tuning** (Performance)
- `2026-07-11T18:53:45+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-11T18:28:18+08:00` | **Retry only safe operations** (Networking)
- `2026-07-11T17:03:59+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-11T16:23:16+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-11T15:41:12+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-11T15:00:02+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-11T13:05:19+08:00` | **Automate rollback paths** (DevOps)
