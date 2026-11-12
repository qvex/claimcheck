"""GOAL: Give the model three capabilities: record an expense, answer spending questions, look up policy.

CONTRACT
  The Tools table in the "ClaimCheck - Spec Sheet" note, section 5.

CONSTRAINTS
  - The model never writes SQL. Tools take typed parameters and call the repository or the RAG search.
  - Recording an expense happens only after the human approved it. The tool itself just records.
  - Tool outputs are short (tokens cost money and attention).
  - Tools run outside HTTP requests, so they manage their own DB sessions.

DONE WHEN
  - Each tool works when called directly from a REPL with hand-written arguments, before any LLM is involved.

FRAMEWORK HINTS (only the parts that would otherwise block you)
  - The tool's docstring and parameter descriptions are what the model reads to decide when and how to call it. Treat them as prompt text.

LOOK UP
  - LangChain: defining tools with typed args schemas
  - chat model bind_tools
"""
