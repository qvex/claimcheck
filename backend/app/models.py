"""SQLAlchemy ORM models: the database schema in Python.

SHOULD CONTAIN
- `Expense` -> table `expenses`, matching the spec's SQL:
    id (big int PK), amount (Numeric(12, 2), CHECK amount > 0), currency (3 chars, default 'INR'),
    category (text), description (text), spent_on (date), source ('agent' | 'manual', CHECK constraint),
    created_at (timestamptz, server default now()).
    Indexes: spent_on; (category, spent_on).
- `PolicyChunk` -> table `policy_chunks`:
    id, section (text), content (text), embedding (pgvector `Vector(settings.EMBEDDING_DIM)`).
- Use SQLAlchemy 2.0 typed style (Mapped[...] / mapped_column).

AVOID
- Float for money. Use Numeric in the DB and Decimal in Python.
- Defining LangGraph checkpoint tables. The checkpointer creates and owns those.

CONCEPTS PRACTICED: relational modeling, constraints, indexes, vector columns.
"""
