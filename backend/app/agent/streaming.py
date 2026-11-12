"""GOAL: Translate LangGraph's stream into the app's own small set of SSE events, so the frontend never depends on LangGraph internals.

CONTRACT
  The SSE event types in the "ClaimCheck - Spec Sheet" note, section 7.

CONSTRAINTS
  - Only the assistant's reply tokens are streamed as text (not tool internals or other nodes' output).
  - The client learns when a tool starts, when confirmation is needed, and when the turn is over.
  - Every stream ends with exactly one terminal event (done or error), no matter what fails.
  - Everything sent is plain JSON (watch out for Decimal and date).

DONE WHEN
  - curl output shows well-formed frames for a normal turn, a confirmation pause and a forced error.

FRAMEWORK HINTS (only the parts that would otherwise block you)
  - LangGraph can stream several modes at once. One gives token-level message chunks, another gives per-node updates.
  - Message chunks carry metadata telling you which node produced them. Use it to filter.
  - An interrupt shows up in the updates stream under a special key.
  - An SSE frame is 'event:' and 'data:' lines followed by a blank line.

LOOK UP
  - LangGraph: streaming (stream_mode)
  - MDN: Server-sent events format
"""
