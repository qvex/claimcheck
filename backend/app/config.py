"""Central configuration, loaded from environment variables / .env.

SHOULD CONTAIN
- A `Settings` class (pydantic-settings BaseSettings) with typed fields matching `.env.example`:
  DATABASE_URL, TEST_DATABASE_URL, LLM_PROVIDER, LLM_API_KEY, CHAT_MODEL, EMBEDDING_MODEL,
  EMBEDDING_DIM (int), FRONTEND_ORIGIN.
- Pointing it at the `.env` file.
- A cached accessor, e.g. `get_settings()` wrapped in lru_cache, so settings are read once.
- Treating LLM_API_KEY as a secret type so it never prints in logs or reprs.

AVOID
- Reading `os.environ` anywhere else in the codebase. Everything goes through Settings.

CONCEPTS PRACTICED: 12-factor config, typed settings, secret handling.
"""
