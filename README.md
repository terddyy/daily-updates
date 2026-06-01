# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1497**
- Today's entries: **6**
- Today's note: `notes/2026-06-01.md`

### Latest Entry

- Timestamp: `2026-06-01T09:28:08+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 75
- `Accessibility`: 75
- `Architecture`: 75
- `Backend`: 75
- `CI/CD`: 75

### Recent Timeline

- `2026-06-01T09:28:08+08:00` | **Write decisions down** (Leadership)
- `2026-06-01T08:09:29+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-01T07:39:04+08:00` | **Measure before tuning** (Performance)
- `2026-06-01T07:08:40+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-01T06:36:25+08:00` | **Retry only safe operations** (Networking)
- `2026-06-01T06:08:27+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-31T21:57:22+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-31T21:12:16+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-31T20:34:30+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-31T19:49:34+08:00` | **Automate rollback paths** (DevOps)
