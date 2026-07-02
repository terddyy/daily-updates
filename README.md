# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1913**
- Today's entries: **16**
- Today's note: `notes/2026-07-02.md`

### Latest Entry

- Timestamp: `2026-07-02T22:16:26+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 96
- `Architecture`: 96
- `Backend`: 96
- `Code Quality`: 96
- `Databases`: 96

### Recent Timeline

- `2026-07-02T22:16:26+08:00` | **Retry only safe operations** (Networking)
- `2026-07-02T21:21:31+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-02T20:43:48+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-02T19:50:55+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-02T18:56:36+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-02T17:47:31+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-02T16:30:09+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-02T15:25:38+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-02T14:07:31+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-02T12:40:44+08:00` | **Log with stable keys** (Observability)
