# Working with AI

How to use AI tools effectively, safely, and in a way that keeps you in control.

---

## The mindset

AI tools in this toolkit are **assistants, not decision-makers.** They flag issues, suggest options, and synthesise information — but every decision stays with the designer.

A few principles that make this work well:

**Keep AI informed, not assumed.**
AI has no memory between sessions unless you give it context. A well-written prompt at the start of a session is the difference between generic output and precise, useful output.

**Bound the task.**
Ask for one thing at a time. "Review this screen" works. "Fix my whole design process" does not. The more specific the input, the more actionable the output.

**Review before committing.**
Always read what the AI produces before acting on it. A finding might be technically correct but wrong for your specific context. You own the judgment call.

**Maintain the source of truth.**
The knowledge base in `shared/` is the ground truth — not the AI's output. If a finding conflicts with a known design decision, update the knowledge base and re-run, don't just accept the finding.

**Use the save/inspect cycle.**
At the end of every working session, save your progress. At the start of the next, inspect before diving in. This keeps the AI grounded in what's actually happened.

---

## Utility prompts

These are reusable prompts for common moments in a working session. Copy and paste them as-is, or adapt to your context.

---

### Save

Use at the end of a session to commit work, update docs, and leave a clear trail for next time.

```
Save

This is a good place to save our progress. Review the git status and all currently
outstanding changes. Update the README.md file and any other documentation as necessary.
Group all changes into logical commits, commit them with concise summary messages,
and then push the changes to the repository.

Update your memories to reflect our progress and what should be worked on next
so that we can pick up where we left off next time.
```

---

### Inspect

Use at the start of a session to get the AI back up to speed before any work begins.

```
Inspect

Inspect the documentation, codebase, git history, and your memories to get back
up to speed on the project and plan what to work on next.
```

---

### New chat

Use when a conversation has gone on too long and you need a clean slate. This produces a handoff prompt you can paste into a fresh session.

```
New chat

We have done a lot of work in this chat. I need to start a fresh session.
Please write a comprehensive prompt that I can paste into a new chat.
Include the next steps and describe it as clearly as possible.
Add rules and guidelines to keep it consistent.
```

---

### Interview me

Use when you're starting something new and the AI needs more context — or when you feel like it's making assumptions and you want to correct them before they compound.

```
Interview me

I want you to interview me to fill in the gaps in your understanding of this project
and what I need. Ask me one question at a time, starting with the most important unknown.
Focus on: what's unclear, what decisions haven't been made yet, and what context you
need to give me better guidance. Don't summarise or suggest until I tell you the
interview is done.
```

---

## When to trust the output — and when not to

| Situation | Trust level | What to do |
|---|---|---|
| Finding matches a known design rule | High | Accept, log in report |
| Finding is about a gap component (Form, etc.) | Medium | Verify manually — coverage is limited |
| Finding contradicts a deliberate decision | Low | Reject, add context to knowledge base |
| Suggestion involves a pattern not in the DS | Low | Treat as heuristic only, clearly label it |
| Output feels generic or vague | Low | Add more context and re-run |

---

## Red lines

Things the AI should never do in this workflow — push back if it tries.

- **Make final design decisions.** It flags, you decide.
- **Override the design system.** If the DS says X, the agent says X. Exceptions are documented, not silently ignored.
- **Add findings it can't ground in a rule or source.** Every finding should reference either a KB JSON rule, a ZH doc guideline, a do/don't rule, or a named heuristic.
- **Guess at user intent.** If context is missing, it should ask — not assume.
