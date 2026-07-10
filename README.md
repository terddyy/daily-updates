# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2033**
- Today's entries: **9**
- Today's note: `notes/2026-07-10.md`

### Latest Entry

- Timestamp: `2026-07-10T13:39:27+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 102
- `Architecture`: 102
- `Backend`: 102
- `Code Quality`: 102
- `Databases`: 102

### Recent Timeline

- `2026-07-10T13:39:27+08:00` | **Retry only safe operations** (Networking)
- `2026-07-10T12:10:41+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-10T10:44:34+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-10T09:42:57+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-10T08:58:27+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-10T08:10:55+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-10T07:41:43+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-10T07:09:53+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-10T06:32:26+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-09T22:44:51+08:00` | **Log with stable keys** (Observability)
