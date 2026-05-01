# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **275**
- Today's entries: **3**
- Today's note: `notes/2026-05-01.md`

### Latest Entry

- Timestamp: `2026-05-01T09:03:30+08:00`
- Title: **Measure before tuning**
- Category: `Performance`
- Source: https://perf.wiki/
- Summary: Profiling first prevents optimization of cold paths and helps teams target changes with measurable user impact.

### Top Categories

- `APIs`: 14
- `Architecture`: 14
- `Backend`: 14
- `CI/CD`: 14
- `Code Quality`: 14

### Recent Timeline

- `2026-05-01T09:03:30+08:00` | **Measure before tuning** (Performance)
- `2026-05-01T09:03:29+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-01T09:03:28+08:00` | **Retry only safe operations** (Networking)
- `2026-04-29T01:33:04+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-29T00:35:09+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-28T23:47:35+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-28T21:34:24+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-28T20:33:48+08:00` | **Automate rollback paths** (DevOps)
- `2026-04-28T19:32:58+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-28T18:39:17+08:00` | **Optimize first contentful view** (Frontend)
