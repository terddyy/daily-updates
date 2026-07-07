# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1975**
- Today's entries: **4**
- Today's note: `notes/2026-07-07.md`

### Latest Entry

- Timestamp: `2026-07-07T08:09:15+08:00`
- Title: **Measure before tuning**
- Category: `Performance`
- Source: https://perf.wiki/
- Summary: Profiling first prevents optimization of cold paths and helps teams target changes with measurable user impact.

### Top Categories

- `APIs`: 99
- `Architecture`: 99
- `Backend`: 99
- `CI/CD`: 99
- `Code Quality`: 99

### Recent Timeline

- `2026-07-07T08:09:15+08:00` | **Measure before tuning** (Performance)
- `2026-07-07T07:38:46+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-07T07:09:20+08:00` | **Retry only safe operations** (Networking)
- `2026-07-07T06:33:26+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-06T22:45:30+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-06T21:32:20+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-06T20:08:49+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-06T18:36:48+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-06T16:45:26+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-06T15:13:14+08:00` | **Optimize first contentful view** (Frontend)
