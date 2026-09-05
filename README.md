# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2877**
- Today's entries: **15**
- Today's note: `notes/2026-09-05.md`

### Latest Entry

- Timestamp: `2026-09-05T22:21:42+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 144
- `Accessibility`: 144
- `Architecture`: 144
- `Backend`: 144
- `CI/CD`: 144

### Recent Timeline

- `2026-09-05T22:21:42+08:00` | **Write decisions down** (Leadership)
- `2026-09-05T22:10:14+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-09-05T21:34:27+08:00` | **Measure before tuning** (Performance)
- `2026-09-05T21:21:16+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-09-05T21:09:51+08:00` | **Retry only safe operations** (Networking)
- `2026-09-05T20:48:56+08:00` | **Batch similar tasks** (Productivity)
- `2026-09-05T19:48:00+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-09-05T19:20:27+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-09-05T19:09:11+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-09-05T18:48:13+08:00` | **Automate rollback paths** (DevOps)
