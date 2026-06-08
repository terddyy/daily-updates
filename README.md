# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1597**
- Today's entries: **2**
- Today's note: `notes/2026-06-09.md`

### Latest Entry

- Timestamp: `2026-06-09T07:10:42+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 80
- `Accessibility`: 80
- `Architecture`: 80
- `Backend`: 80
- `CI/CD`: 80

### Recent Timeline

- `2026-06-09T07:10:42+08:00` | **Write decisions down** (Leadership)
- `2026-06-09T06:35:05+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-08T22:10:04+08:00` | **Measure before tuning** (Performance)
- `2026-06-08T20:32:29+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-08T18:55:11+08:00` | **Retry only safe operations** (Networking)
- `2026-06-08T17:07:45+08:00` | **Batch similar tasks** (Productivity)
- `2026-06-08T15:16:58+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-08T13:39:54+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-08T11:49:25+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-08T10:26:09+08:00` | **Automate rollback paths** (DevOps)
