"""Thin wrapper around the embedding model.

SHOULD CONTAIN
- `embed_texts(texts: list[str]) -> list[list[float]]` for documents (batched).
- `embed_query(text: str) -> list[float]` for search queries (some providers distinguish document vs query).
- Construction of the provider's embedding client from settings (EMBEDDING_MODEL, LLM_API_KEY).
- A check that the returned vector length == settings.EMBEDDING_DIM, with a clear error if not
  (a mismatch with the DB column is a classic first-run bug).

WHY A WRAPPER: swapping providers later touches one file, and tests can patch one function.
"""
