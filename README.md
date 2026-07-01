# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1893**
- Today's entries: **11**
- Today's note: `notes/2026-07-01.md`

### Latest Entry

- Timestamp: `2026-07-01T18:07:14+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 95
- `Architecture`: 95
- `Backend`: 95
- `Code Quality`: 95
- `Databases`: 95

### Recent Timeline

- `2026-07-01T18:07:14+08:00` | **Retry only safe operations** (Networking)
- `2026-07-01T16:37:46+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-01T15:10:22+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-01T13:37:23+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-01T11:47:18+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-01T10:22:15+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-01T09:23:31+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-01T08:09:10+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-01T07:35:16+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-01T06:58:43+08:00` | **Log with stable keys** (Observability)
