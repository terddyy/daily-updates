# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2693**
- Today's entries: **4**
- Today's note: `notes/2026-08-19.md`

### Latest Entry

- Timestamp: `2026-08-19T07:47:12+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 135
- `Architecture`: 135
- `Backend`: 135
- `Code Quality`: 135
- `Databases`: 135

### Recent Timeline

- `2026-08-19T07:47:12+08:00` | **Retry only safe operations** (Networking)
- `2026-08-19T07:21:38+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-19T06:50:48+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-19T06:22:54+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-18T22:17:05+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-18T21:31:28+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-18T20:45:01+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-18T19:51:13+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-18T19:24:55+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-18T18:45:54+08:00` | **Log with stable keys** (Observability)
