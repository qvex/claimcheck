"""GOAL: Express the database schema as ORM models.

CONTRACT
  The tables in the "ClaimCheck - Spec Sheet" note, section 6 (Data Model). Translate that SQL; don't redesign it.

CONSTRAINTS
  - The database itself enforces the rules (constraints), not just Python.
  - Money is exact. No floating point anywhere in the path.
  - The vector column's size must match the embedding model's output dimension.
  - Don't model the LangGraph checkpoint tables. The checkpointer owns them.

DONE WHEN
  - The tables exist with the expected columns, constraints and indexes when you inspect them in psql.

LOOK UP
  - SQLAlchemy 2.0 typed mappings (Mapped / mapped_column)
  - pgvector's SQLAlchemy integration
"""
