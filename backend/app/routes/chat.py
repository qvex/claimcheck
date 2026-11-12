"""GOAL: Let the browser talk to the agent: start a turn, resume after a confirmation, and stream everything back live.

CONTRACT
  The /chat and /chat/resume rows in the "ClaimCheck - Spec Sheet" note, section 7, plus the SSE event types listed there.

CONSTRAINTS
  - Each conversation is identified by the client's thread id. Same id means same memory.
  - Responses stream as they're produced. The client never waits for the whole answer.
  - A failure mid-stream reaches the client as an error event, not a dropped connection.
  - Reuse the graph built at startup.

DONE WHEN
  - curl with -N against /chat shows events arriving incrementally.
  - A paused conversation can be resumed and finishes correctly.

FRAMEWORK HINTS (only the parts that would otherwise block you)
  - Thread identity is passed to LangGraph through the run config's 'configurable' section.
  - Resuming a paused graph means invoking it with a Command carrying the resume value, not with a new message.
  - SSE responses need caching disabled.

LOOK UP
  - FastAPI StreamingResponse
  - LangGraph: persistence / threads
  - LangGraph: Command(resume=...)
"""
