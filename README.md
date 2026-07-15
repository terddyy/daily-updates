# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2137**
- Today's entries: **2**
- Today's note: `notes/2026-07-16.md`

### Latest Entry

- Timestamp: `2026-07-16T06:35:25+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 107
- `Accessibility`: 107
- `Architecture`: 107
- `Backend`: 107
- `CI/CD`: 107

### Recent Timeline

- `2026-07-16T06:35:25+08:00` | **Write decisions down** (Leadership)
- `2026-07-16T06:08:10+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-15T22:22:46+08:00` | **Measure before tuning** (Performance)
- `2026-07-15T21:33:49+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-15T20:45:17+08:00` | **Retry only safe operations** (Networking)
- `2026-07-15T20:10:43+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-15T19:35:18+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-15T18:56:59+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-15T18:12:42+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-15T17:15:49+08:00` | **Automate rollback paths** (DevOps)
