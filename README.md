# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2397**
- Today's entries: **26**
- Today's note: `notes/2026-08-08.md`

### Latest Entry

- Timestamp: `2026-08-08T22:30:18+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 120
- `Accessibility`: 120
- `Architecture`: 120
- `Backend`: 120
- `CI/CD`: 120

### Recent Timeline

- `2026-08-08T22:30:18+08:00` | **Write decisions down** (Leadership)
- `2026-08-08T21:46:44+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-08T21:20:29+08:00` | **Measure before tuning** (Performance)
- `2026-08-08T20:49:43+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-08T20:27:05+08:00` | **Retry only safe operations** (Networking)
- `2026-08-08T19:40:25+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-08T19:24:55+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-08T19:01:13+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-08T18:25:54+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-08T18:10:31+08:00` | **Automate rollback paths** (DevOps)
