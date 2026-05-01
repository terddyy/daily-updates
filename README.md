# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **377**
- Today's entries: **105**
- Today's note: `notes/2026-05-01.md`

### Latest Entry

- Timestamp: `2026-05-01T09:05:12+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 19
- `Accessibility`: 19
- `Architecture`: 19
- `Backend`: 19
- `CI/CD`: 19

### Recent Timeline

- `2026-05-01T09:05:12+08:00` | **Write decisions down** (Leadership)
- `2026-05-01T09:05:11+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-01T09:05:10+08:00` | **Measure before tuning** (Performance)
- `2026-05-01T09:05:09+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-01T09:05:08+08:00` | **Retry only safe operations** (Networking)
- `2026-05-01T09:05:07+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-01T09:05:06+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-01T09:05:05+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-01T09:05:04+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-01T09:05:03+08:00` | **Automate rollback paths** (DevOps)
