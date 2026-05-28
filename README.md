# UX AI Toolkit

AI-powered UX tools for a medical/dental software design team. Built on Claude.

**Agents** run in the terminal and review staging screens autonomously.
**Skills** run in Claude chat and help designers think through work before and during design.

They serve different moments in the workflow — see below.

---

## Repo structure

```
ux-ai-toolkit/
├── shared/                          ← Design system knowledge — read by all tools
│   ├── design-system/
│   │   ├── components/              ← JSON per component (variants, props, rules)
│   │   ├── foundations/             ← Color, spacing, typography, border, radius
│   │   ├── guidelines/              ← Do/don't rules, token rules, component status
│   │   ├── tokens/                  ← Full design token JSON (light + dark)
│   │   └── docs/                    ← ZeroHeight export (components, patterns, templates)
│   └── research/
│       └── patterns.md              ← Cross-user behavioral patterns (add when available)
│
├── agents/
│   └── ux-review/                   ← Reviews staging screens, writes structured reports
│
├── skills/
│   └── ux-design-workflow-assistant/ ← Design brief synthesis + pre-sync review (chat)
│
├── .gitignore
└── README.md
```

---

## When to use what

| Moment | Tool | How |
|---|---|---|
| About to start a NEED — need to synthesise inputs into a brief | **Skill** | Paste NEED + research into Claude chat |
| Designed something — want a quick check before weekly sync | **Skill** | Paste brief + screens into Claude chat |
| Screens are on staging — need a full structured audit | **Agent** | Drop screenshot or URL in `inbox/`, run from terminal |

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

---

## Using the UX Review Agent

```bash
cd agents/ux-review
claude
```

Drop a screenshot into `inbox/`, then tell the agent:

```
"There's a new screen in inbox/. Run a ux-review."
"Review inbox/settings-page.png"
"Review the checkout flow at staging.myapp.com/checkout"
```

Reports are written to `outputs/` as `.json` (structured) and `.md` (readable).
Processed inputs move to `archive/`. Nothing is deleted.

`inbox/`, `outputs/`, and `archive/` are in `.gitignore` — they never get pushed.

---

## Using the Design Workflow Skill

Install the skill in Cowork or Claude chat by pointing it at:
```
skills/ux-design-workflow-assistant/SKILL.md
```

Then in chat, paste your NEED in this format:
```
NEED: [one paragraph]
Constraints: [bulleted]
Research findings: [bulleted, with confidence level]
Known gaps: [what you don't know]
```

The skill produces a design brief. Use the same skill to review screens before a sync.

---

## Contributing knowledge

When you want to add or update design system rules, personas, or flows:

1. Branch: `git checkout -b add/[what-youre-adding]`
2. Edit the relevant file in `shared/`
3. Open a pull request
4. Team lead reviews and merges

---

## Adding a new agent

1. Create `agents/your-agent-name/`
2. Add `CLAUDE.md` and `agent-config/` inside it
3. Reference `../../shared/` for design system and research knowledge
4. Add its `inbox/`, `outputs/`, `archive/` to `.gitignore`
5. Update this README

Each agent is fully independent. Adding one never touches another.

---

## Tools

| Tool | Type | Status | Purpose |
|---|---|---|---|
| `agents/ux-review` | Agent | Active | Single screen audit against the design system |
| `skills/ux-design-workflow-assistant` | Skill | Active | Brief synthesis + pre-sync review |
