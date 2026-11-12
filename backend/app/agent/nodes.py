"""GOAL: The units of work in the agent graph, plus the decisions about where to go next.

CONTRACT
  The agent graph diagram in the "ClaimCheck - Spec Sheet" note, section 5. Every box and every arrow must exist somewhere in your code.

CONSTRAINTS
  - Saving an expense always passes through a human-confirmation step first. No path skips it.
  - Approve, edit and reject are all handled. Reject must leave the conversation in a valid state (every tool call the model made still gets a response).
  - Only tools write to the database. The confirmation step never does.
  - Non-expense tool calls don't require confirmation.

DONE WHEN
  - From a terminal script, a new expense pauses the run, and resuming with each of the 3 decisions behaves correctly.

FRAMEWORK HINTS (only the parts that would otherwise block you)
  - Pausing for a human is done with interrupt(). The payload you pass is what the client receives.
  - On resume, LangGraph RE-RUNS the interrupted node from the top. Anything before interrupt() must be side-effect free.
  - Chat model providers expect every tool call to be answered by a tool message. Keep that in mind for 'reject'.

LOOK UP
  - LangGraph: human-in-the-loop / interrupt
  - LangGraph: conditional edges
  - LangGraph prebuilt ToolNode
"""
