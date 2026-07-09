# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2013**
- Today's entries: **6**
- Today's note: `notes/2026-07-09.md`

### Latest Entry

- Timestamp: `2026-07-09T08:59:44+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 101
- `Architecture`: 101
- `Backend`: 101
- `Code Quality`: 101
- `Databases`: 101

### Recent Timeline

- `2026-07-09T08:59:44+08:00` | **Retry only safe operations** (Networking)
- `2026-07-09T08:09:44+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-09T07:38:15+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-09T07:09:16+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-09T06:36:43+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-09T06:09:11+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-08T22:35:36+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-08T21:38:17+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-08T20:49:36+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-08T20:03:00+08:00` | **Log with stable keys** (Observability)
