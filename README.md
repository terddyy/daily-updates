# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2857**
- Today's entries: **2**
- Today's note: `notes/2026-08-29.md`

### Latest Entry

- Timestamp: `2026-08-29T18:04:24+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 143
- `Accessibility`: 143
- `Architecture`: 143
- `Backend`: 143
- `CI/CD`: 143

### Recent Timeline

- `2026-08-29T18:04:24+08:00` | **Write decisions down** (Leadership)
- `2026-08-29T11:10:01+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-28T17:54:46+08:00` | **Measure before tuning** (Performance)
- `2026-08-28T07:54:01+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-27T22:27:48+08:00` | **Retry only safe operations** (Networking)
- `2026-08-27T11:18:40+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-27T06:09:01+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-26T22:26:29+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-26T21:34:00+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-26T20:17:42+08:00` | **Automate rollback paths** (DevOps)
