"""GOAL: Trigger (re)ingestion of the policy document.

CONSTRAINTS
  - Safe to call repeatedly: the end state is the same whether you call it once or five times.

DONE WHEN
  - Calling it twice leaves the same number of chunks as calling it once.
"""
