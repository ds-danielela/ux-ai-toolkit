# UX Review Agent

Full audit of your screens against the design system. Writes a report with every issue graded by severity — ready to share with your team or attach to a handoff.

---

## When to use it

- Your screens are on staging and you want a thorough, documented audit
- You need a shareable report for a handoff or design review
- You want to check multiple screens in one go

> **Not sure which tool to use?** If your screens aren't on staging yet, use the [Design Workflow Skill](tools/design-workflow-skill.md) instead.

---

## How to run a review

### Step 1 — Start the agent

Open Terminal and run:

```bash
cd ~/Documents/ux-ai-toolkit/agents/ux-review
claude
```

### Step 2 — Give it something to review

Drop a screenshot into the `ux-ai-toolkit/agents/ux-review/inbox/` folder, then tell the agent:

```
There's a new screen in inbox/. Run a ux-review.
```

Or point it at a staging URL directly:

```
Review the screen at staging.ourapp.com/appointments/confirm
```

### Step 3 — Read the report

Your report appears in the `outputs/` folder as a dated `.md` file — open it in any text editor or Markdown viewer.

---

## What it checks

| Area | What the agent looks for |
|---|---|
| Component usage | Is the right component used in this context? |
| Spacing, color, typography | Are values using the correct design tokens? |
| Design system rules | Does anything violate a named rule? |
| Labels and copy | Outcome-focused labels? Sentence case? |
| Missing states | Error, loading, and empty states covered? |
| Usability | Nielsen's 10 usability principles as a secondary check |

---

## Severity levels

| Level | What it means |
|---|---|
| **Critical** | Blocks task completion — fix before shipping |
| **Major** | Design system violation causing inconsistency |
| **Minor** | Works, but a better option exists |
| **Suggestion** | Polish or copy improvement — no rule violated |

---

## What a report looks like

```
# UX Review — Checkout Step 2
Date: 2026-05-28

## Critical (1)
- Payment CTA: Primary button used for a destructive action.
  Replace with the destructive button variant.

## Major (1)
- Postcode field: No inline error shown on invalid input.
  Add an error message directly below the field.

## Minor (1)
- Section header: Font size is off the type scale.
  Use the correct heading token.

## Suggestions (1)
- Continue button: "Next" doesn't describe what happens next.
  Consider "Continue to payment".

---
Total: 1 Critical, 1 Major, 1 Minor, 1 Suggestion
```

---

## Component coverage

The agent knows some components better than others. Components with full design system documentation produce precise, rule-referenced findings. Components with only narrative documentation produce less specific findings. Two components have no structured documentation yet and are reviewed on general usability principles only.

See the [Component Coverage](design-system/component-status.md) page for the full breakdown.
