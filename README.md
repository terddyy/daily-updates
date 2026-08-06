# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2337**
- Today's entries: **11**
- Today's note: `notes/2026-08-06.md`

### Latest Entry

- Timestamp: `2026-08-06T14:09:47+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 117
- `Accessibility`: 117
- `Architecture`: 117
- `Backend`: 117
- `CI/CD`: 117

### Recent Timeline

- `2026-08-06T14:09:47+08:00` | **Write decisions down** (Leadership)
- `2026-08-06T13:05:35+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-06T11:51:52+08:00` | **Measure before tuning** (Performance)
- `2026-08-06T10:39:29+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-06T09:36:07+08:00` | **Retry only safe operations** (Networking)
- `2026-08-06T08:46:44+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-06T08:06:46+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-06T07:34:25+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-06T07:08:13+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-06T06:37:44+08:00` | **Automate rollback paths** (DevOps)
