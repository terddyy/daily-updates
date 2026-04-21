# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **115**
- Today's entries: **2**
- Today's note: `notes/2026-04-22.md`

### Latest Entry

- Timestamp: `2026-04-22T01:22:19+08:00`
- Title: **Measure before tuning**
- Category: `Performance`
- Source: https://perf.wiki/
- Summary: Profiling first prevents optimization of cold paths and helps teams target changes with measurable user impact.

### Top Categories

- `APIs`: 6
- `Architecture`: 6
- `Backend`: 6
- `CI/CD`: 6
- `Code Quality`: 6

### Recent Timeline

- `2026-04-22T01:22:19+08:00` | **Measure before tuning** (Performance)
- `2026-04-22T00:24:00+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-04-21T23:28:11+08:00` | **Retry only safe operations** (Networking)
- `2026-04-21T22:33:54+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-21T21:32:55+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-21T20:20:01+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-21T19:25:20+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-21T18:29:17+08:00` | **Automate rollback paths** (DevOps)
- `2026-04-21T17:32:24+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-21T16:35:36+08:00` | **Optimize first contentful view** (Frontend)
