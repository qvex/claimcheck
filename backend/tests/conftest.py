"""GOAL: Shared test setup that makes tests fast, isolated and free.

CONSTRAINTS
  - Tests never touch your dev database.
  - Tests never call a real LLM or embedding API.
  - Each test starts from a known state.
  - API tests exercise the real routes, with the database dependency swapped for the test one.

DONE WHEN
  - The whole suite runs offline, and it passes twice in a row.

LOOK UP
  - pytest fixtures and scopes
  - FastAPI TestClient and dependency_overrides
"""
