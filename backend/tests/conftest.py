"""Shared pytest fixtures.

SHOULD CONTAIN
- A fixture that points the app at TEST_DATABASE_URL, creates the tables before the test session and drops
  them after (or truncates between tests).
- A `db` session fixture.
- A `client` fixture: FastAPI TestClient, with the `get_db` dependency overridden to use the test session.
- A fake embedding function (deterministic vectors of the right dimension), patched in so tests never call
  the real embedding API.

AVOID: tests that touch your dev database or the real LLM/embedding APIs.
"""
