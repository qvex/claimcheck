"""GOAL: Tell the model how to behave: when to use which tool, and what it must never do.

CONTRACT
  The 'system prompt essentials' in the "ClaimCheck - Spec Sheet" note, section 5.

CONSTRAINTS
  - The model must know today's date (to resolve 'yesterday'), and it must not be hardcoded.
  - The model must never invent amounts or dates. It asks a clarifying question instead.
  - Policy answers cite their source section.
  - Don't repeat what the tool descriptions already say. The model sees both.

DONE WHEN
  - The acceptance tests about missing amounts and policy citations (spec section 12) pass.
"""
