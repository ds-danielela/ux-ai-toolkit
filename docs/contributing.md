# Contributing

How to add to the toolkit — design system knowledge, new tools, or documentation.

---

## The principle

All shared knowledge lives in `shared/`. All changes go through a pull request so nothing gets overwritten accidentally.

---

## Adding design system knowledge

### Updating a component rule

1. Find the file in `shared/design-system/components/[name].component.json`
2. Edit the relevant field
3. Open a pull request with a description of what changed and why

### Adding a new do/don't rule

1. Open `shared/design-system/guidelines/do-dont-rules.json`
2. Add a new rule object following the existing format
3. Set `severity` to `"error"` or `"warning"`
4. Open a pull request

### Adding a persona

1. Create a new file in `shared/research/personas/[name].md`
2. Follow the structure in `shared/research/personas/template.md`
3. Ground every observation in a real research session or interview
4. Open a pull request

---

## Adding a user flow

1. Open `agents/ux-review/agent-config/rules/user-flows.md`
2. Add a new section following the template at the top of the file
3. Describe each step and what "correct" looks like
4. Open a pull request

---

## Adding a new tool

### New skill (chat-based)

1. Create `skills/[your-skill-name]/SKILL.md`
2. Follow the format of `skills/ux-design-workflow-assistant/SKILL.md`
3. Reference `shared/` for any design system knowledge
4. Add a page to this docs site under `docs/tools/`
5. Update `docs/_sidebar.md`
6. Open a pull request

### New agent (terminal-based)

1. Create `agents/[your-agent-name]/`
2. Add `CLAUDE.md` and `agent-config/` inside it
3. Reference `../../shared/` for design system and research knowledge
4. Add `inbox/`, `outputs/`, `archive/` to `.gitignore`
5. Add a page to this docs site under `docs/tools/`
6. Update `docs/_sidebar.md`
7. Open a pull request

---

## Updating this docs site

All docs live in `docs/`. Each page is a `.md` file. To add or edit:

1. Edit or create the `.md` file in `docs/`
2. Update `docs/_sidebar.md` if you're adding a new page
3. Open a pull request

---

## Versioning

The toolkit uses [semantic versioning](https://semver.org/):

| Type | When to increment | Example |
|---|---|---|
| Patch `0.0.x` | Bug fix, small knowledge update | `v0.1.1` |
| Minor `0.x.0` | New tool, new skill, new agent | `v0.2.0` |
| Major `x.0.0` | Breaking change to structure or API | `v1.0.0` |

To release a new version:
1. Update the version in `docs/index.html` (the `v0.x` badge in the sidebar)
2. Create a git tag: `git tag v0.2.0 && git push --tags`
3. GitHub creates a release automatically

---

## Questions

Open an issue on GitHub or reach out to the team lead.
