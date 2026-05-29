# Design Workflow Skill

Turns your NEED inputs into a design brief. Checks your screens before a sync. Runs in Claude chat — no setup needed.

---

## When to use it

- Right after a kick-off, before opening Figma
- Before a weekly sync, to catch blockers early
- When you're unsure which components to use for a NEED

> **Not sure which tool to use?** If your screens are already on staging and you need a full audit, use the [UX Review Agent](tools/ux-review-agent.md) instead.

---

## Mode 1 — Brief synthesis

Takes your scattered NEED inputs and turns them into a structured design brief.

### What to paste in

```
NEED: [one paragraph — what problem are we solving?]
Constraints: [list anything fixed — regulatory, technical, time]
Research findings: [list what you know, note high / medium / low confidence]
Known gaps: [list what you don't know yet]
```

If a field is empty, write `none`.

### What you get back

```
## Design brief — [NEED title]

### What we're solving
[One paragraph. Plain language.]

### What we know
- [Finding] — [confidence: high / medium / low]

### What we don't know
- [Gap] — [why it matters]

### Components to use
- [Component] — [variant] — [why this one]

### High-priority risks
- [Only items that genuinely affect the design]

### Open questions to resolve
1. [Question]
```

The brief is ready when you could open Figma and start a frame from it. If something key is missing, the skill says so and stops — it won't produce a brief that isn't usable.

---

## Mode 2 — Pre-sync review

Checks your screens against the brief and design system rules before a weekly sync. Flags only blockers.

### What to paste in

```
Brief: [paste the brief, or describe the goal in a sentence]
Screens: [list each screen — components used, key interactions]
Decisions made: [any deliberate exceptions or trade-offs you made]
```

### What you get back

```
## Review — [NEED title] — [date]

### Blockers — fix before showing this
- [Issue] — [why it's a blocker] — [fix]

### Things to flag in the room
- [Issue] — [suggested action]

### Looks correct
- [Confirmed pattern]
```

If there are no blockers: "No blockers found."

---

## What the skill flags — and what it doesn't

The skill flags three things only. Not four. Not "just one more thing."

**1. Components with incomplete design system coverage**
One in particular matters: **Form** — it's the most common component in tickets and the one with the least complete documentation. The skill flags it if you're using it, so you know to double-check manually.

**2. Must-fix rule violations**
The design system has rules with two levels: must-fix and should-fix. The skill only surfaces must-fix. The most common ones:
- Disabled primary button on an incomplete form (should be active instead)
- More than one primary button in the same context
- Using raw colour values instead of design tokens
- Closing actions that use the wrong button type

**3. Components your design needs but the system doesn't have**
If you're designing something that doesn't map to any existing component, the skill flags it and suggests the closest alternative. This gets it on the radar for the design system team.

Everything else — should-fix warnings, minor nuances, polish — is ignored unless you ask for it.
