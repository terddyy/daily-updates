# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1313**
- Today's entries: **8**
- Today's note: `notes/2026-05-19.md`

### Latest Entry

- Timestamp: `2026-05-19T11:47:17+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 66
- `Architecture`: 66
- `Backend`: 66
- `Code Quality`: 66
- `Databases`: 66

### Recent Timeline

- `2026-05-19T11:47:17+08:00` | **Retry only safe operations** (Networking)
- `2026-05-19T10:22:21+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-19T09:19:02+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-19T08:09:52+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-19T07:38:38+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-19T07:09:02+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-19T06:35:37+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-19T06:10:44+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-18T22:04:16+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-18T20:45:00+08:00` | **Log with stable keys** (Observability)
