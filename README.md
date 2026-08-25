# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2833**
- Today's entries: **3**
- Today's note: `notes/2026-08-26.md`

### Latest Entry

- Timestamp: `2026-08-26T07:26:29+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 142
- `Architecture`: 142
- `Backend`: 142
- `Code Quality`: 142
- `Databases`: 142

### Recent Timeline

- `2026-08-26T07:26:29+08:00` | **Retry only safe operations** (Networking)
- `2026-08-26T06:56:14+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-26T06:26:39+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-25T22:21:19+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-25T21:27:35+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-25T20:15:52+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-25T19:43:38+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-25T19:04:39+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-25T18:32:14+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-25T17:51:19+08:00` | **Log with stable keys** (Observability)
