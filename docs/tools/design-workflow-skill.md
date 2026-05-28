# Design Workflow Skill

Turns your NEED inputs into a design brief. Checks your screens before a sync. Runs in Claude chat — no terminal needed.

---

## When to use it

- Right after a kick-off, before opening Figma
- Before a weekly sync, to catch blockers early
- When you want to know which components to use for a NEED

> **Not sure which tool to use?** If screens are already on staging and you need a full audit, use the [UX Review Agent](tools/ux-review-agent.md) instead.

---

## Mode 1 — Brief synthesis

Turns scattered NEED inputs into a structured design brief.

### Input format

```
NEED: [one paragraph — what problem are we solving?]
Constraints: [list anything fixed — regulatory, technical, time]
Research findings: [list what you know, note high / medium / low confidence]
Known gaps: [list what you don't know yet]
```

If a field is empty, write `none`.

### Output

```
## Design brief — [NEED title]

### What we're solving
[One paragraph. Plain language.]

### What we know
- [Finding] — [confidence: high / medium / low]

### What we don't know
- [Gap] — [why it matters]

### DS components to use
- [Component] — [variant] — [why this one]

### High-priority risks
- [Only items that genuinely affect the design]

### Open questions to resolve
1. [Question]
```

The brief is ready when a designer could choose components and start a frame from it. If key information is still missing, the skill says so explicitly and stops.

---

## Mode 2 — Pre-sync review

Checks your screens against the brief and design system rules. Flags only blockers — nothing else.

### Input format

```
Brief: [paste the brief, or describe the goal]
Screens: [list each screen — components used, key interactions]
Decisions made: [any deliberate exceptions or trade-offs]
```

### Output

```
## Review — [NEED title] — [date]

### Blockers — fix before showing this
- [Issue] — [why it's a blocker] — [fix]

### Things to flag in the room
- [Issue] — [suggested action]

### Looks correct
- [Confirmed pattern]
```

If there are no blockers, the skill says: "No blockers found."

---

## What it flags

The skill only flags three things. Not more.

**1. Gap components**
Only one truly matters: **Form** — it has no Storybook reference and is high-frequency in tickets. Other gap components (AI button, AI side panel, Battery indicator, Universal action bar) are flagged only if you explicitly mention them.

**2. ERROR-severity rule violations**
From the design system's do/don't rules, only `severity=error`. Most common:
- Disabled primary button on incomplete form
- More than one primary button per context
- Hex values instead of semantic tokens
- Closing actions that aren't tertiary icon buttons

**3. Missing component coverage**
When your design needs something the DS doesn't have. The skill suggests the closest existing component and flags it for DS governance.

Everything else — warnings, minor nuances, polish — is ignored unless you ask.

---

## Knowledge the skill uses

| File | What it contains |
|---|---|
| `guidelines/component-status.json` | Component readiness and gap flags |
| `guidelines/do-dont-rules.json` | ERROR-severity violations |
| `guidelines/token-usage-rules.json` | Token constraints |
| `components/*.json` | Component variants and props |
