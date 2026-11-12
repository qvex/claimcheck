"""Vector similarity search over policy chunks using pgvector.

SHOULD CONTAIN
- `search_policy(db, query: str, k: int = 3) -> list[{section, content, score}]`
    embed_query(query) -> ORDER BY cosine distance to the stored embeddings -> LIMIT k.
    Convert the distance into a similarity score for readability.
- (Optional) a minimum-similarity threshold, so totally unrelated questions return nothing rather than
  the "least bad" chunk.

NOTE: with ~6-20 rows, no vector index is needed (exact search is instant). Adding HNSW is a stretch
goal; write down at what row count it starts to matter.
"""
