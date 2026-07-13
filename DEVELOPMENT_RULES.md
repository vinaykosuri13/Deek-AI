# 🛠️ DEEK AI DEVELOPMENT RULES

## Purpose

This document defines the engineering rules for developing Deek.

Every new feature should follow these rules to keep the project clean, scalable, and maintainable.

---

# Rule 1 — Build with Purpose

Every feature must support Deek's vision.

Ask before coding:

- Does this help Deek understand?
- Does this help Deek remember?
- Does this help Deek reason?
- Does this help Deek plan?
- Does this help Deek execute?
- Does this help Deek automate?
- Does this help Deek manage Vinay's digital life?

If the answer is NO, the feature should not be built.

---

# Rule 2 — Design Before Coding

Never start coding immediately.

Follow this order:

1. Understand the problem.
2. Define the goal.
3. Design the complete feature.
4. Review the design.
5. Implement the feature.
6. Test the feature.
7. Update documentation.
8. Commit to GitHub.

---

# Rule 3 — Complete Features

Avoid repeatedly modifying the same feature for small improvements.

Instead:

- Design the complete version.
- Implement it once.
- Test it thoroughly.
- Release it.

One feature = One complete implementation.

---

# Rule 4 — Single Responsibility

Every file should have one clear responsibility.

Examples:

- Controller coordinates requests.
- Planner creates execution plans.
- Tool Manager executes plans.
- Tools perform user-facing tasks.
- Services communicate with external systems.

---

# Rule 5 — Modular Architecture

Keep components independent.

Controllers should not contain tool logic.

Tools should not contain planner logic.

Services should not interact directly with users.

---

# Rule 6 — Standard Communication

Every tool must:

Receive:

Request

Return:

Response

Do not return random values or custom formats.

---

# Rule 7 — Reuse Existing Code

Before creating new code:

- Check existing modules.
- Reuse functions where possible.
- Avoid duplicate logic.

---

# Rule 8 — Documentation

Every major milestone should update:

- README.md
- ROADMAP.md
- ARCHITECTURE.md

Documentation is part of development.

---

# Rule 9 — Testing

Before every commit:

- Run the test suite.
- Fix all failures.
- Review the code.

Never commit failing code.

---

# Rule 10 — GitHub Commits

Each commit should represent one complete milestone.

Good examples:

- Add Weather Tool
- Introduce Plugin Loader
- Implement Memory Search
- Complete Intelligence Phase 1

Avoid commits for incomplete work.

---

# Rule 11 — AI Operating System Mindset

Always think beyond answering questions.

Instead ask:

"How can Deek manage this?"

Management is more valuable than simple responses.

---

# Rule 12 — Long-Term Vision

Deek is not just an AI assistant.

Deek is Vinay Kosuri's Personal Artificial Intelligence Operating System.

Every new feature should move Deek closer to that vision.

---

# Development Workflow

Idea

↓

Discussion

↓

Architecture Design

↓

Implementation

↓

Testing

↓

Documentation

↓

GitHub Commit

↓

Next Feature

---

# Final Principle

Build Deek slowly.

Build Deek correctly.

Build Deek once.

Quality is more important than speed.
