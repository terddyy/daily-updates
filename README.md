# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **75**
- Today's entries: **7**
- Today's note: `notes/2026-04-20.md`

### Latest Entry

- Timestamp: `2026-04-20T06:08:07+08:00`
- Title: **Measure before tuning**
- Category: `Performance`
- Source: https://perf.wiki/
- Summary: Profiling first prevents optimization of cold paths and helps teams target changes with measurable user impact.

### Top Categories

- `APIs`: 4
- `Architecture`: 4
- `Backend`: 4
- `CI/CD`: 4
- `Code Quality`: 4

### Recent Timeline

- `2026-04-20T06:08:07+08:00` | **Measure before tuning** (Performance)
- `2026-04-20T05:10:38+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-04-20T04:09:12+08:00` | **Retry only safe operations** (Networking)
- `2026-04-20T03:16:23+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-20T02:11:39+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-20T01:11:47+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-20T00:10:17+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-19T23:13:17+08:00` | **Automate rollback paths** (DevOps)
- `2026-04-19T22:14:28+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-19T21:26:08+08:00` | **Optimize first contentful view** (Frontend)
