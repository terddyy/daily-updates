# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1937**
- Today's entries: **6**
- Today's note: `notes/2026-07-04.md`

### Latest Entry

- Timestamp: `2026-07-04T13:19:05+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 97
- `Accessibility`: 97
- `Architecture`: 97
- `Backend`: 97
- `CI/CD`: 97

### Recent Timeline

- `2026-07-04T13:19:05+08:00` | **Write decisions down** (Leadership)
- `2026-07-04T11:46:01+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-04T09:19:22+08:00` | **Measure before tuning** (Performance)
- `2026-07-04T08:42:50+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-04T06:49:27+08:00` | **Retry only safe operations** (Networking)
- `2026-07-04T06:24:32+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-03T22:16:31+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-03T21:22:30+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-03T20:42:32+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-03T19:49:48+08:00` | **Automate rollback paths** (DevOps)
