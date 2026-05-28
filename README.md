# UX AI Toolkit

A local AI-powered UX review system built on Claude Code. Each agent lives in
its own folder and runs independently. Shared design system and research
knowledge lives in `shared/` and is available to all agents.

---

## What's inside

```
ux-ai-toolkit/
├── shared/                  ← Design system rules and research (fill these in)
└── ux-review-agent/         ← Reviews screens against the design system
```

---

## Setup

### 1. Install Claude Code

```bash
npm install -g @anthropic/claude-code
```

### 2. Clone this repo

```bash
git clone <your-repo-url>
cd ux-ai-toolkit
```

### 3. Fill in the knowledge files

Before the agent can give useful output, fill these in with your real content:

| File | What to add |
|---|---|
| `shared/design-system/components.md` | Component names, rules, when NOT to use |
| `shared/design-system/tokens.md` | Spacing, color, and typography scale |
| `shared/design-system/anti-patterns.md` | Common misuses you see in your product |
| `ux-review-agent/agent-config/rules/user-flows.md` | Key flows and expected behavior per step |

`shared/research/patterns.md` can stay empty until you have research data.

---

## Running the UX Review Agent

```bash
cd ux-review-agent
claude
```

### Trigger a review

Drop a screenshot into `inbox/`, then tell the agent:

```
"There's a new screen in inbox/. Run a ux-review."
"Review inbox/settings-page.png"
```

Or point it at a URL:

```
"Review the checkout flow at staging.myapp.com/checkout"
```

### Output

Reports are written to `outputs/` as `.json` (structured) and `.md` (readable).
Processed inputs are moved to `archive/`. Nothing is deleted.

---

## Contributing new knowledge

When you want to add or update design system rules, personas, or flows:

1. Create a branch: `git checkout -b add/[what-youre-adding]`
2. Edit the relevant file in `shared/` or `agent-config/rules/`
3. Open a pull request
4. The team lead reviews and merges

`inbox/`, `outputs/`, and `archive/` are in `.gitignore` — they never get pushed.

---

## Adding a new agent

1. Create a new folder at the repo root: `mkdir my-new-agent`
2. Add a `CLAUDE.md` and an `agent-config/` folder inside it
3. Reference `../shared/` for any design system or research knowledge
4. Add its `inbox/`, `outputs/`, `archive/` to `.gitignore`

Each agent is fully independent. Adding one never touches another.

---

## Agents

| Agent | Status | Purpose |
|---|---|---|
| `ux-review-agent` | Active | Single screen audit against the design system |
| `content-agent` | Planned | Copy, labels, and microcopy review |
| `qa-agent` | Planned | Functional checks: broken links, form failures, responsive |
