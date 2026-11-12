/**
 * src/types.ts
 *
 * GOAL: Mirror the backend's contract in TypeScript, so mismatches are caught at compile time.
 *
 * CONTRACT
 *   The backend schemas and the SSE event types (the "ClaimCheck - Spec Sheet" note, section 7).
 *
 * CONSTRAINTS
 *   - Values that can only be one of a few strings are union types, not plain string.
 *   - SSE events are modeled so that switching on the event type gives you correctly typed data in each branch.
 *   - Decide how money is represented on the client, given how Decimal is serialized to JSON, and stay consistent.
 *
 * DONE WHEN
 *   - Changing a field name breaks the build in every place that uses it.
 *
 * LOOK UP
 *   - TypeScript discriminated unions
 */
