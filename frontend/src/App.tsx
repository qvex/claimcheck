/**
 * src/App.tsx
 *
 * GOAL: Page layout, and the owner of the state that both halves of the page need.
 *
 * CONTRACT
 *   The layout and component list in the "ClaimCheck - Spec Sheet" note, section 8.
 *
 * CONSTRAINTS
 *   - When the agent saves an expense, the table and summary update without a page reload.
 *   - Refreshing the browser continues the same conversation.
 *   - App owns shared state only. Children load their own data.
 *
 * DONE WHEN
 *   - Approve an expense in chat -> the table updates. Reload -> the chat thread continues.
 *
 * LOOK UP
 *   - React: lifting state up
 *   - React: sharing state between components
 */
