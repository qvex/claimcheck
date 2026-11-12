"""Health check endpoint.

SHOULD CONTAIN
- GET /health -> {"status": "ok"}.
- (Nice to have) a cheap DB ping (SELECT 1) that reports "db": "ok" or "down", so you can tell
  "API up but DB down" apart.

WHY: the first thing you build. It proves the server, CORS and the frontend-to-backend call all work.
"""
