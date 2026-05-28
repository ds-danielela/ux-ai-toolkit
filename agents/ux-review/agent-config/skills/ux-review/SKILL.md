# Skill: ux-review

## Purpose

Single screen audit. Takes a screenshot from `inbox/` or a URL and produces
a structured findings report graded by severity.

---

## When to use

```
"Review inbox/settings-page.png"
"Run a ux-review on this screen"
"Audit the checkout step at staging.myapp.com/checkout/step-2"
```

---

## Steps

### 1. Load rules
- `agent-config/rules/severity-framework.md`
- `agent-config/rules/review-mode.md`

### 2. Identify components on screen
Look at the input and list every component visible. Then load the relevant files:
- `../../shared/design-system/components/[name].component.json` — structured rules
- `../../shared/design-system/docs/components/[name].md` — narrative guidance

### 3. Load foundations and guidelines
Always load these regardless of what's on screen:
- `../../shared/design-system/guidelines/do-dont-rules.json` — named rules with severity
- `../../shared/design-system/guidelines/token-usage-rules.json` — token constraints
- `../../shared/design-system/foundations/color-tokens-semantic.md` — color token roles
- `../../shared/design-system/foundations/typography.md` — type scale
- `../../shared/design-system/foundations/spacing.md` — spacing scale

Load these if relevant to the screen:
- `../../shared/design-system/docs/patterns/forms.md` — if a form is present
- `../../shared/design-system/docs/patterns/navigation.md` — if navigation is present
- `../../shared/design-system/docs/patterns/loading.md` — if loading states are relevant
- `../../shared/design-system/docs/patterns/notifications.md` — if banners, toasts, or alerts are present
- `../../shared/research/patterns.md` — for behavioral context

### 4. Review the screen against

- **Component usage** — is the right component used for the context?
- **Token compliance** — are spacing, color, and typography values on-scale?
- **Do/don't rules** — does anything match a named rule in `do-dont-rules.json`?
- **Labels and copy** — do they describe the outcome? Are they sentence case?
- **Missing states** — are error, loading, and empty states accounted for?
- **Nielsen's heuristics** — as a secondary lens for anything not covered by DS rules

### 5. Produce output

Write two files to `outputs/`:

**`YYYY-MM-DD-[screen-name].json`**
```json
[
  {
    "severity": "Critical | Major | Minor | Suggestion",
    "location": "Specific element and screen area",
    "component": "Component name if applicable",
    "issue": "What is wrong",
    "rule_violated": "The specific rule ID or name from the knowledge files",
    "recommendation": "Concrete fix"
  }
]
```

**`YYYY-MM-DD-[screen-name].md`**
```markdown
# UX Review — [Screen Name]
Date: YYYY-MM-DD | Screen: [file or URL]

## Critical (n)
- **[Location]**: [Issue]. [Recommendation].

## Major (n)
- ...

## Minor (n)
- ...

## Suggestions (n)
- ...

---
Total: n Critical, n Major, n Minor, n Suggestion
```

### 6. Archive input
Move the processed file from `inbox/` to `archive/`. Do not delete it.

---

## Rules

- Every finding must have a location, a violated rule (with ID if from `do-dont-rules.json`), and a recommendation
- Do not invent rules not present in the knowledge files
- If a component has no JSON file in `components/`, fall back to the narrative doc in `docs/components/`
- If neither exists, note the gap and apply heuristic-based findings clearly labelled as such
- Do not produce findings without evidence from the screen
