/**
 * src/hooks/useChatStream.ts
 *
 * GOAL: Encapsulate everything about talking to the agent (sending, streaming, pausing for confirmation, resuming), so components only render state and call actions.
 *
 * CONTRACT
 *   The /chat and /chat/resume endpoints and the SSE event types in the "ClaimCheck - Spec Sheet" note, section 7.
 *
 * CONSTRAINTS
 *   - Text appears as it streams, not all at the end.
 *   - The UI always knows which phase it's in (idle, streaming, waiting for confirmation, error) and can't end up in an impossible combination.
 *   - Leaving the page cancels an in-flight stream.
 *   - The parent is told when an expense has been saved.
 *
 * DONE WHEN
 *   - A message streams in token by token, the confirm step appears exactly when the server asks for it, and errors are shown, not swallowed.
 *
 * FRAMEWORK HINTS (only the parts that would otherwise block you)
 *   - The browser's EventSource only supports GET. Your endpoints are POST, so read the fetch response body as a stream instead.
 *   - Network chunks don't line up with SSE frames. Buffer and split on frame boundaries.
 *   - Appending tokens with state that's captured at render time causes stale-closure bugs. Use the functional form of setState.
 *   - In development, StrictMode runs effects twice on purpose. Make your cleanup correct rather than disabling it.
 *
 * LOOK UP
 *   - MDN: ReadableStream / getReader / TextDecoder
 *   - React: custom hooks
 *   - AbortController
 */
