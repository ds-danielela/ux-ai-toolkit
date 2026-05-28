# Severity Framework

Every finding must be assigned one of these four levels. Use the definitions
below — do not invent new levels.

---

## Critical

**Meaning:** Blocks task completion or prevents a user from proceeding.
**Examples:**
- No error feedback on a required form field
- A focus trap that locks keyboard users
- A missing form label (screen reader cannot identify the field)
- A CTA that does nothing when clicked

**Rule:** If a user cannot complete their goal because of this issue, it is Critical.

---

## Major

**Meaning:** Design system violation that creates visual or behavioral inconsistency.
**Examples:**
- Wrong component used (ButtonPrimary for a destructive action)
- Off-scale spacing or color value
- Token used incorrectly (e.g. color-primary on an error state)

**Rule:** If a specific rule in `../shared/design-system/` is violated, it is at least Major.

---

## Minor

**Meaning:** Works correctly, but a better option exists within the design system.
**Examples:**
- Suboptimal component choice that still functions
- Unclear label that could be more specific
- Layout that works but doesn't follow convention

**Rule:** If it functions but could be improved without changing behavior, it is Minor.

---

## Suggestion

**Meaning:** Polish, consistency, or copy improvement. No rule violated.
**Examples:**
- Button label that's correct but could be more descriptive
- Alignment nudge
- Microcopy that could be clearer

**Rule:** If it's a nice-to-have rather than a fix, it is a Suggestion.
