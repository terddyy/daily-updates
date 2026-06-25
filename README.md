# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1813**
- Today's entries: **16**
- Today's note: `notes/2026-06-25.md`

### Latest Entry

- Timestamp: `2026-06-25T22:18:45+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 91
- `Architecture`: 91
- `Backend`: 91
- `Code Quality`: 91
- `Databases`: 91

### Recent Timeline

- `2026-06-25T22:18:45+08:00` | **Retry only safe operations** (Networking)
- `2026-06-25T21:17:26+08:00` | **Batch similar tasks** (Productivity)
- `2026-06-25T20:20:51+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-25T19:27:30+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-25T18:28:01+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-25T17:25:13+08:00` | **Automate rollback paths** (DevOps)
- `2026-06-25T16:10:42+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-25T14:47:49+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-25T13:25:19+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-25T11:46:46+08:00` | **Log with stable keys** (Observability)
