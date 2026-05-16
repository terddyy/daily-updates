# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1277**
- Today's entries: **5**
- Today's note: `notes/2026-05-16.md`

### Latest Entry

- Timestamp: `2026-05-16T20:39:06+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 64
- `Accessibility`: 64
- `Architecture`: 64
- `Backend`: 64
- `CI/CD`: 64

### Recent Timeline

- `2026-05-16T20:39:06+08:00` | **Write decisions down** (Leadership)
- `2026-05-16T20:03:48+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-16T19:36:19+08:00` | **Measure before tuning** (Performance)
- `2026-05-16T18:43:24+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-16T18:11:01+08:00` | **Retry only safe operations** (Networking)
- `2026-05-02T08:46:25+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-02T08:46:24+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-02T08:46:23+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-02T08:46:22+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-02T08:46:21+08:00` | **Automate rollback paths** (DevOps)
