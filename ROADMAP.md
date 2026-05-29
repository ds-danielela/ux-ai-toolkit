# UX AI Toolkit — Roadmap

Future work, in priority order. Each phase builds on the previous one.
Check items off as they get done. Add new ideas at the bottom.

---

## Phase 1 — Foundation ✅ Done

The repo is live, the agent works, the skill is active.

- [x] Repo structure with clean `agents/` and `skills/` separation
- [x] `shared/design-system/` knowledge base (components, tokens, foundations, guidelines, docs)
- [x] `agents/ux-review` — single screen audit against the design system
- [x] `skills/ux-design-workflow-assistant` — design brief synthesis + pre-sync review
- [x] `.gitignore` keeping work product (inbox, outputs, archive) local only
- [x] `component-status.md` — coverage map for all 59 components
- [x] README with setup instructions and contribution guide

---

## Phase 2 — Knowledge gaps

Fill the remaining empty files and close the most important coverage gaps.

**Trigger: when the team starts using the agent regularly and findings feel too generic.**

- [ ] `agents/ux-review/agent-config/rules/user-flows.md`
  Add your 2–3 most-reviewed product flows. Describe each step and what "correct" looks like.
  Format: see the template already in the file.

- [ ] `shared/research/patterns.md`
  Add cross-user behavioral patterns from real research rounds.
  Only add after at least one round of user research is synthesised.

- [ ] Persona files — `shared/research/personas/`
  One `.md` file per real persona, grounded in session observations.
  Copy the template structure from the original prompt.
  Activates persona-review mode in the agent.

- [ ] Close KB JSON gaps
  23 of 59 components have full structured coverage. The 36 with docs-only coverage
  produce less precise findings. Priority components to add JSON records for:
  - Form (HIGH RISK — `storybook_ready=false`, high-frequency in tickets)
  - Alert dialog
  - Card
  - Modal
  - Dropdown

---

## Phase 3 — More skills and agents

Add tools for more moments in the workflow.

**Trigger: Phase 1 tools are in active use and designers are asking for more.**

- [ ] `skills/a11y-check` — WCAG 2.1 AA accessibility review skill (chat-based)
  Check contrast, focus states, form labels, touch targets, heading hierarchy.

- [ ] `agents/content-review` — copy, labels, microcopy, and tone review
  Reads UX findings as additional context. Receives JSON from `agents/ux-review/outputs/`.

- [ ] `agents/qa-review` — functional checks on staging
  Broken links, JS errors, form submission failures, responsive breakpoints.
  Runs via Playwright alongside the UX agent.

- [ ] `skills/persona-review` — review through a specific user's lens (chat-based)
  Loads persona file from `shared/research/personas/` and reviews through their
  behavioral model. Requires Phase 2 persona files to be filled in first.

---

## Phase 4 — Storybook integration

Connect live component code to the knowledge base.

**Trigger: Storybook is stable and the team wants prop-level accuracy in findings.**

- [ ] Export Storybook data into `shared/design-system/storybook/`
  Similar to how ZeroHeight was exported. One file per component.
  Write an export script (extend `guidelines/rebuild_guidelines.py`).

- [ ] Update KB JSON records for gap components using Storybook props
  This upgrades Battery indicator, Form, Universal action bar from flagged to full coverage.

- [ ] Update agent SKILL.md to load Storybook data when available
  Storybook data becomes a third source alongside KB JSON and ZH MD.

---

## Phase 5 — MCP server

Wrap the knowledge base as a live queryable server.

**Trigger: 3+ people using the toolkit and file-based updates feel like friction.**

- [ ] `mcp-server/` — Node.js MCP server over `shared/design-system/`
  Tools to expose:
  - `list_components` — all component names and categories
  - `get_component(name)` — full JSON record for a component
  - `get_rules(severity?)` — do/don't rules, filterable by severity
  - `get_token(category?)` — design tokens, filterable
  - `get_component_status` — coverage and gap summary
  Stack: Node.js + `@modelcontextprotocol/sdk`

- [ ] Update agents to call MCP tools instead of reading files
  Swap `Read ../../shared/design-system/components/button.json`
  for `get_component("button")`.

- [ ] Update skills to reference MCP server
  Skills load design system knowledge via MCP instead of file paths.

- [ ] Host the MCP server
  Once hosted, developers and designers connect without cloning the repo.
  This becomes the proper dependency model for other teams.

---

## Phase 6 — Documentation site

A Carbon-style public (or internal) reference for the toolkit.

**Trigger: onboarding new designers regularly, or developers want to discover available tools.**

- [ ] GitHub Pages site auto-generated from the repo
  Renders README, ROADMAP, and component-status.md into a browsable page.
  Free for private repos on most GitHub plans. Zero extra hosting.

- [ ] Best practices section
  How to write a good NEED. When to use each tool. How to contribute.

- [ ] Tool index page
  One card per agent and skill: what it does, when to use it, how to trigger it.

- [ ] Component coverage dashboard
  Visual version of `component-status.md` — shows full vs. docs-only vs. no coverage
  at a glance, with gap flags highlighted.

---

## Backlog — ideas without a phase yet

Things worth tracking but not scheduled.

- Orchestrator agent — coordinates ux-review + content-review + qa-review in one run
- Slack/Teams integration — post review reports to a channel automatically
- Figma plugin — trigger a review directly from Figma without touching the terminal
- CI integration — run `agents/ux-review` as part of a staging deploy pipeline
- Multi-language support — extend agent output to support languages other than English
- Guided wizard / routing skill — `skills/toolkit-guide` — a yes/no decision tree that
  asks the designer where they are in their workflow and routes them to the right tool.
  Decision tree: kick-off done? → screens on staging? → brief ready? → picks the correct
  agent or skill mode. Can be a chat skill (in-conversation routing) and/or a static
  interactive page in the docs site.

---

*Last updated: 2026-05-28*
