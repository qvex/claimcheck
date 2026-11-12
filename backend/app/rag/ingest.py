"""GOAL: Load the policy document into the vector table, so it can be searched.

CONSTRAINTS
  - Each chunk is a self-contained, citable unit. Decide the chunking strategy and be able to justify it.
  - Idempotent: re-running never creates duplicates.
  - The text-splitting logic is testable without a database or an embedding API.
  - Can be run from the command line as well as through the API.

DONE WHEN
  - Running it twice yields the same chunk count. test_ingest.py passes.
"""
