# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **673**
- Today's entries: **401**
- Today's note: `notes/2026-05-01.md`

### Latest Entry

- Timestamp: `2026-05-01T09:10:08+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 34
- `Architecture`: 34
- `Backend`: 34
- `Code Quality`: 34
- `Databases`: 34

### Recent Timeline

- `2026-05-01T09:10:08+08:00` | **Retry only safe operations** (Networking)
- `2026-05-01T09:10:07+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-01T09:10:06+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-01T09:10:05+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-01T09:10:04+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-01T09:10:03+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-01T09:10:02+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-01T09:10:01+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-01T09:10:00+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-01T09:09:59+08:00` | **Log with stable keys** (Observability)
