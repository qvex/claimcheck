"""GOAL: Wire the nodes into a compiled, persistent agent.

CONTRACT
  Must match the agent graph in the "ClaimCheck - Spec Sheet" note, section 5, exactly. If the code and the diagram disagree, fix one of them.

CONSTRAINTS
  - Built by hand from nodes and edges. Don't use the prebuilt ReAct agent (compare with it afterwards if you're curious).
  - Takes its persistence (checkpointer) from outside, so tests can use an in-memory one and the server a Postgres one.

DONE WHEN
  - The Mermaid diagram LangGraph generates from your compiled graph matches the spec's diagram.
  - In a script, a second message in the same thread remembers the first.

LOOK UP
  - LangGraph StateGraph, compile(checkpointer=...)
  - get_graph().draw_mermaid()
"""
