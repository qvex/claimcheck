"""Loads data/policy.md into the policy_chunks table.

SHOULD CONTAIN
- `split_markdown_sections(text) -> list[(section_title, content)]`
    A pure function that splits on "## " headings and skips the top-level title. Easy to unit test.
- `ingest_policy(db, path) -> int`
    read file -> split -> embed all chunks in one batch -> delete existing rows -> insert new rows
    -> commit -> return the count.
- A `__main__` entry point so it can also be run as `python -m app.rag.ingest`.

DESIGN NOTE
- Chunk by heading, not by fixed token count: the sections are small and meaningful, and the section
  name doubles as the citation.

AVOID: appending on every run (duplicates). Ingest must be idempotent.
"""
