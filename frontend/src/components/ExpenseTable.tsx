/**
 * src/components/ExpenseTable.tsx
 *
 * PURPOSE
 *   Shows saved expenses (newest first) with a delete action.
 *
 * PROPS: refreshKey (refetch whenever it changes)
 *
 * SHOULD CONTAIN
 *   - Data loading in useEffect via api.listExpenses(), with refreshKey in the dependency array.
 *   - All three UI states: loading, error (with a retry button) and empty ("No expenses yet").
 *   - Rows keyed by expense id; amount formatted as currency (Intl.NumberFormat with en-IN / INR).
 *   - A source badge (agent vs manual).
 *   - Delete with a confirm() prompt; then refetch or remove the row locally.
 *   - Effect cleanup that ignores late responses (an "ignore" flag or AbortController), to avoid race conditions.
 */
