/**
 * src/components/MessageList.tsx
 *
 * PURPOSE
 *   Renders the conversation: user bubbles, assistant bubbles (growing as tokens stream in) and small
 *   tool-activity chips.
 *
 * PROPS: messages: ChatMessage[], status
 *
 * SHOULD CONTAIN
 *   - A list rendered with a stable `key` per message (the message id, never the array index).
 *   - A typing indicator while status === "streaming" and the last assistant message is still empty.
 *   - An empty state ("Try: spent 450 on lunch yesterday").
 *
 * AVOID: rendering assistant text as HTML (no dangerouslySetInnerHTML). Plain text is safe.
 */
