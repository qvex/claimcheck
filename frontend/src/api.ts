/**
 * src/api.ts
 *
 * PURPOSE
 *   All non-streaming HTTP calls live here. Components never call fetch() directly.
 *
 * SHOULD CONTAIN
 *   - A single API base URL constant (or "/api" if you use the Vite proxy).
 *   - A small helper that performs a request, throws a useful Error on non-2xx (include the status and the
 *     backend's error detail), and parses JSON.
 *   - Typed functions: listExpenses(filters?), createExpense(data), deleteExpense(id), getSummary(month),
 *     ingestPolicy(), each returning the types from types.ts.
 *
 * NOT HERE: the chat stream. That's in hooks/useChatStream.ts, because it's stateful.
 */
