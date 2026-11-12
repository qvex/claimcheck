"""GOAL: One place that turns text into vectors, so the rest of the code doesn't care which provider you use.

CONSTRAINTS
  - Documents and queries may need different handling. Check your provider's guidance.
  - A dimension mismatch with the database column is caught here, with a clear message.
  - Easy to replace with a fake in tests.

DONE WHEN
  - A REPL call returns a vector of the configured dimension.

LOOK UP
  - Your provider's embeddings docs (LangChain integration)
"""
