# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **37**
- Today's entries: **15**
- Today's note: `notes/2026-04-18.md`

### Latest Entry

- Timestamp: `2026-04-18T15:26:02+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 2
- `Accessibility`: 2
- `Architecture`: 2
- `Backend`: 2
- `CI/CD`: 2

### Recent Timeline

- `2026-04-18T15:26:02+08:00` | **Write decisions down** (Leadership)
- `2026-04-18T14:24:38+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-18T13:32:22+08:00` | **Measure before tuning** (Performance)
- `2026-04-18T12:46:15+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-04-18T11:02:07+08:00` | **Retry only safe operations** (Networking)
- `2026-04-18T09:33:45+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-18T08:20:45+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-18T07:13:22+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-18T06:12:35+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-18T05:14:42+08:00` | **Automate rollback paths** (DevOps)
