"""Endpoint to (re)ingest the policy document into the vector table.

SHOULD CONTAIN
- POST /policy/ingest -> {"chunks": n}
  Calls `app.rag.ingest.ingest_policy(...)`, which reads data/policy.md, chunks, embeds and stores it.
- Idempotent behavior: running it twice must not duplicate rows (ingest replaces old chunks).

NOTE: in a real system this would be an admin-only or offline job. Here it's an endpoint for convenience.
"""
