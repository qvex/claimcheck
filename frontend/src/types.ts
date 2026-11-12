/**
 * src/types.ts
 *
 * PURPOSE
 *   Shared TypeScript types that mirror the backend's Pydantic schemas. One source of truth for the frontend.
 *
 * SHOULD CONTAIN
 *   - `Category`: a union of the six category string literals (must match the backend enum).
 *   - `Expense` and `ExpenseCreate` (amount as a string or number; know which, and why: Decimal arrives as a JSON string).
 *   - `Summary`: month + totals per category.
 *   - `ChatMessage`: id, role ("user" | "assistant" | "tool"), text, optional tool name.
 *   - `SseEvent`: a DISCRIMINATED UNION over the 5 event types (token | tool | interrupt | done | error),
 *     each with its own data shape, so a switch statement on `type` is fully type-checked.
 *   - `ChatStatus`: "idle" | "streaming" | "awaiting_confirm" | "error".
 *   - `Decision`: "approve" | "reject" | "edit".
 */
