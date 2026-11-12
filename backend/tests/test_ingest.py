"""RAG ingestion tests.

SHOULD COVER
- split_markdown_sections(): returns one entry per "## " section with the right titles, ignores the "#"
  title, and handles a trailing section with no newline.
- ingest_policy() run twice -> the row count stays the same (idempotent). Uses the fake embedder from conftest.
"""
