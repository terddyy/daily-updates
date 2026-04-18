# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **53**
- Today's entries: **8**
- Today's note: `notes/2026-04-19.md`

### Latest Entry

- Timestamp: `2026-04-19T07:10:28+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 3
- `Architecture`: 3
- `Backend`: 3
- `Code Quality`: 3
- `Databases`: 3

### Recent Timeline

- `2026-04-19T07:10:28+08:00` | **Retry only safe operations** (Networking)
- `2026-04-19T06:07:50+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-19T05:09:40+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-19T04:08:45+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-19T03:15:48+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-19T02:11:08+08:00` | **Automate rollback paths** (DevOps)
- `2026-04-19T01:11:56+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-19T00:10:26+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-18T23:12:58+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-18T22:14:21+08:00` | **Log with stable keys** (Observability)
