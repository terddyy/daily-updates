# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1613**
- Today's entries: **3**
- Today's note: `notes/2026-06-10.md`

### Latest Entry

- Timestamp: `2026-06-10T07:46:08+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 81
- `Architecture`: 81
- `Backend`: 81
- `Code Quality`: 81
- `Databases`: 81

### Recent Timeline

- `2026-06-10T07:46:08+08:00` | **Retry only safe operations** (Networking)
- `2026-06-10T07:11:44+08:00` | **Batch similar tasks** (Productivity)
- `2026-06-10T06:35:31+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-09T22:25:32+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-09T21:29:02+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-09T20:16:32+08:00` | **Automate rollback paths** (DevOps)
- `2026-06-09T19:07:10+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-09T17:47:28+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-09T16:15:44+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-09T14:50:42+08:00` | **Log with stable keys** (Observability)
