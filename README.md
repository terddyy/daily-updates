# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2253**
- Today's entries: **2**
- Today's note: `notes/2026-07-28.md`

### Latest Entry

- Timestamp: `2026-07-28T07:34:05+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 113
- `Architecture`: 113
- `Backend`: 113
- `Code Quality`: 113
- `Databases`: 113

### Recent Timeline

- `2026-07-28T07:34:05+08:00` | **Retry only safe operations** (Networking)
- `2026-07-28T06:18:07+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-27T21:53:15+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-27T19:21:14+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-27T15:51:04+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-27T12:06:01+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-27T08:14:23+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-27T07:13:13+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-27T06:12:18+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-26T22:14:47+08:00` | **Log with stable keys** (Observability)
