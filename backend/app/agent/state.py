"""GOAL: Define what the agent remembers between steps. This is also what the checkpointer persists.

CONSTRAINTS
  - Keep it minimal. Don't store anything that can be derived from what's already there.
  - Updates from nodes must merge into the conversation, not overwrite it.

DONE WHEN
  - You can explain, in one sentence, how a node's returned update is merged into the existing state.

FRAMEWORK HINTS (only the parts that would otherwise block you)
  - LangGraph merges state updates using 'reducers'. The message reducer appends new messages AND replaces a message that has the same id. That second behavior matters when the user edits an expense.
  - A built-in messages state exists. Define your own once anyway, to understand it.

LOOK UP
  - LangGraph: state, reducers, add_messages
"""
