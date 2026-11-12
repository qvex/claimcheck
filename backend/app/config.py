"""GOAL: Make configuration typed, validated and read from the environment in exactly one place.

CONSTRAINTS
  - Every variable in .env.example is represented and typed.
  - A missing or malformed variable fails loudly at startup, not halfway through a request.
  - The API key can never show up in logs or error output.
  - No other module reads os.environ directly.

DONE WHEN
  - Removing a required variable from .env makes startup fail with a clear message naming it.

LOOK UP
  - pydantic-settings
  - pydantic SecretStr
"""
