# UX AI Toolkit — Component Status

Cross-reference of all 59 design-system components (from `guidelines/component-status.json` v0.33.0) against the knowledge-base JSON records and the ZeroHeight markdown docs available to the `ux-review-agent`.

**Coverage columns**
- **KB JSON** — structured record in `shared/design-system/components/` (variants, props, rules, states)
- **ZH MD** — narrative doc in `shared/design-system/docs/components/`
- **DS flags** — `figma_ready / doc_ready / storybook_ready` from `component-status.json`
- **Agent coverage** — what the agent can draw on when it encounters this component in a review

**Agent coverage key**
| Level | Meaning |
|---|---|
| ✅ Full | KB JSON + ZH MD. Agent has structured rules and narrative guidance. |
| 📄 Docs only | ZH MD only. Agent has narrative docs; no structured props/rules file. |
| ❌ None | No KB JSON and no ZH MD. Agent falls back to heuristics only. |

---

## Summary

| | Count |
|---|---|
| Total design-system components | 59 |
| Full coverage (KB JSON + ZH MD) | 23 |
| Docs only (ZH MD, no KB JSON) | 34 |
| No coverage | 2 |
| DS gaps (doc or storybook not ready) | 5 |

---

## Full component table

| Component | Category | KB JSON | ZH MD | DS flags | Agent coverage | Agent flag |
|---|---|---|---|---|---|---|
| Accordion | Layout | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Alert dialog | Overlays | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| AI button | Actions | — | — | ✓/✗/✓ | ❌ None | ⚠️ doc_ready=false — no usage rules. Findings will be heuristic only. |
| AI side panel | Layout | — | — | ✓/✗/✓ | ❌ None | ⚠️ doc_ready=false — no usage rules. Findings will be heuristic only. |
| Avatar | Identity | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Banner | Feedback | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Battery indicator | Display | — | ✓ | ✓/✓/✗ | 📄 Docs only | ⚠️ storybook_ready=false — no code reference to verify prop usage. |
| Button | Actions | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Card | Layout | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Checkbox | Forms | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Color dot | Display | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Container | Layout | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Date input | Forms | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Dental chart | Specialised | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Divider | Layout | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Dropdown | Forms | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Dropzone overlay | Forms | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Empty state | Feedback | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Form | Forms | — | ✓ | ✓/✓/✗ | 📄 Docs only | ⚠️ storybook_ready=false — HIGH RISK. High-frequency component, no code reference. |
| Hero modal | Overlays | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Info button | Actions | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Info modal | Overlays | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Inline notification | Feedback | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Link | Actions | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| List | Layout | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Main menu | Navigation | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Media gallery | Media | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Media tile | Media | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Modal | Overlays | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Notification badge | Display | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Notification menu | Navigation | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Option list | Navigation | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Page header | Layout | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Password field | Forms | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Popover | Overlays | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Progress bar | Display | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Progress circle | Display | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Progress circle filled | Display | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Progress menu | Navigation | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Radio button | Forms | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Search | Forms | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Segmented control | Forms | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Show more | Layout | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Side sheet | Overlays | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Skeleton | Display | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Slider | Forms | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Snackbar | Feedback | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Switch | Forms | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Tab | Navigation | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Table | Layout | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Tag | Display | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Text area | Forms | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Text field | Forms | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Timeline stepper | Navigation | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Toast | Feedback | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Toggle button | Actions | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Tooltip | Display | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Top bar | Navigation | ✓ | ✓ | ✓/✓/✓ | ✅ Full | — |
| Universal action bar | Layout | — | ✓ | ✓/✓/✗ | 📄 Docs only | ⚠️ storybook_ready=false — no code reference. |
| User menu | Navigation | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |
| Wizard | Navigation | — | ✓ | ✓/✓/✓ | 📄 Docs only | — |

---

## DS gaps (flagged in component-status.json)

These 5 components have incomplete design-system documentation or missing references. The agent will flag these in review output.

| Component | Gap | Risk |
|---|---|---|
| AI button | `doc_ready=false` | No usage rules — agent findings heuristic only |
| AI side panel | `doc_ready=false` | No usage context, slots, or restrictions documented |
| Battery indicator | `storybook_ready=false` | No code reference to verify props |
| Form | `storybook_ready=false` | HIGH — high-frequency component, no code reference |
| Universal action bar | `storybook_ready=false` | No code reference to verify slot structure |

---

## Components with full agent coverage (23)

These have both a KB JSON record and a ZeroHeight MD doc. The agent can give precise, rule-referenced findings for these.

Accordion, Avatar, Banner, Button, Checkbox, Empty state, Hero modal, List, Media gallery, Media tile, Option list, Page header, Popover, Radio button, Search, Segmented control, Slider, Switch, Tab, Text field, Timeline stepper, Toast, Top bar

---

## Components with docs only (34)

These have a ZeroHeight MD doc but no KB JSON record. The agent can give narrative-based findings but cannot reference structured props or variant rules.

Alert dialog, Card, Color dot, Container, Date input, Dental chart, Divider, Dropdown, Dropzone overlay, Form, Info button, Info modal, Inline notification, Link, Main menu, Modal, Notification badge, Notification menu, Password field, Progress bar, Progress circle, Progress circle filled, Progress menu, Show more, Side sheet, Skeleton, Snackbar, Table, Tag, Text area, Toggle button, Tooltip, Universal action bar, User menu, Wizard

---

## Components with no coverage (2)

The agent has no knowledge files for these. It will flag when it encounters them and fall back to heuristics only.

AI button, AI side panel

---

*Generated 2026-05-28. DS catalog version: 0.33.0. KB JSON records: 23 of 59. ZH MD docs: 57 of 59.*
