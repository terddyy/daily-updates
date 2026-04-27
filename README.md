# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **255**
- Today's entries: **6**
- Today's note: `notes/2026-04-28.md`

### Latest Entry

- Timestamp: `2026-04-28T05:22:05+08:00`
- Title: **Measure before tuning**
- Category: `Performance`
- Source: https://perf.wiki/
- Summary: Profiling first prevents optimization of cold paths and helps teams target changes with measurable user impact.

### Top Categories

- `APIs`: 13
- `Architecture`: 13
- `Backend`: 13
- `CI/CD`: 13
- `Code Quality`: 13

### Recent Timeline

- `2026-04-28T05:22:05+08:00` | **Measure before tuning** (Performance)
- `2026-04-28T04:23:13+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-04-28T03:31:28+08:00` | **Retry only safe operations** (Networking)
- `2026-04-28T02:26:08+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-28T01:30:17+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-28T00:32:09+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-27T23:33:55+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-27T22:40:27+08:00` | **Automate rollback paths** (DevOps)
- `2026-04-27T21:32:56+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-27T20:29:47+08:00` | **Optimize first contentful view** (Frontend)
