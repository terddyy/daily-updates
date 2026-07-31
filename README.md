# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2277**
- Today's entries: **3**
- Today's note: `notes/2026-07-31.md`

### Latest Entry

- Timestamp: `2026-07-31T11:49:35+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 114
- `Accessibility`: 114
- `Architecture`: 114
- `Backend`: 114
- `CI/CD`: 114

### Recent Timeline

- `2026-07-31T11:49:35+08:00` | **Write decisions down** (Leadership)
- `2026-07-31T08:01:21+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-31T06:46:25+08:00` | **Measure before tuning** (Performance)
- `2026-07-30T21:15:05+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-30T19:33:56+08:00` | **Retry only safe operations** (Networking)
- `2026-07-30T17:43:15+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-30T15:12:19+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-30T12:20:17+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-30T09:02:29+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-30T07:42:12+08:00` | **Automate rollback paths** (DevOps)
