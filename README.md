# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2117**
- Today's entries: **3**
- Today's note: `notes/2026-07-15.md`

### Latest Entry

- Timestamp: `2026-07-15T07:19:54+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 106
- `Accessibility`: 106
- `Architecture`: 106
- `Backend`: 106
- `CI/CD`: 106

### Recent Timeline

- `2026-07-15T07:19:54+08:00` | **Write decisions down** (Leadership)
- `2026-07-15T06:48:39+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-15T06:22:28+08:00` | **Measure before tuning** (Performance)
- `2026-07-14T22:54:20+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-14T22:00:39+08:00` | **Retry only safe operations** (Networking)
- `2026-07-14T21:14:55+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-14T20:42:40+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-14T20:09:48+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-14T19:31:48+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-14T18:52:53+08:00` | **Automate rollback paths** (DevOps)
