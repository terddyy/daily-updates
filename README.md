# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2193**
- Today's entries: **4**
- Today's note: `notes/2026-07-19.md`

### Latest Entry

- Timestamp: `2026-07-19T17:26:38+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 110
- `Architecture`: 110
- `Backend`: 110
- `Code Quality`: 110
- `Databases`: 110

### Recent Timeline

- `2026-07-19T17:26:38+08:00` | **Retry only safe operations** (Networking)
- `2026-07-19T15:15:30+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-19T09:01:49+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-19T06:24:52+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-18T22:52:41+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-18T20:04:38+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-18T17:56:28+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-18T16:19:34+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-18T12:14:15+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-18T09:05:38+08:00` | **Log with stable keys** (Observability)
