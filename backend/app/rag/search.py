"""GOAL: Given a question, return the most relevant policy chunks, with enough information to cite them.

CONSTRAINTS
  - Similarity is computed in the database, not by loading all vectors into Python.
  - Decide what happens when nothing is relevant. Returning the 'least bad' chunk can mislead the model.

DONE WHEN
  - 'Can I claim a solo dinner?' returns the Meals section first.

LOOK UP
  - pgvector distance operators
  - When an ANN index (HNSW) starts to matter
"""
