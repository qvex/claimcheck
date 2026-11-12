/**
 * src/components/SummaryBar.tsx
 *
 * PURPOSE
 *   Current-month totals per category, plus the grand total, at a glance.
 *
 * PROPS: refreshKey
 *
 * SHOULD CONTAIN
 *   - Fetches api.getSummary(currentMonth) when refreshKey changes.
 *   - Small tiles, one per category with a non-zero total, sorted by amount.
 *   - It must agree with the agent's answer to "how much on food this month?" (an acceptance test).
 *
 * FIRST TO CUT if you're behind schedule.
 */
