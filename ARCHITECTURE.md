# 🏗️ DEEK AI ARCHITECTURE

## Overview

Deek (Artificial Intelligence Operating System - AIOS) is Vinay Kosuri's Personal AI Operating System.

The architecture is modular. Every component has a single responsibility, making the system scalable, maintainable, and easy to extend.

---

# High-Level Architecture

User
    │
    ▼
Controller
    │
    ▼
Intent Detector
    │
    ▼
Request
    │
    ▼
Planner
    │
    ▼
Tool Manager
    │
    ▼
Tools
    │
    ▼
Services (if required)
    │
    ▼
Response
    │
    ▼
Memory
    │
    ▼
User

---

# Core Components

## Controller

Coordinates the complete execution flow.

Responsibilities:
- Receive user requests
- Store conversation
- Detect intent
- Create Request object
- Execute Planner
- Execute Tool Manager
- Return final response

---

## Intent Detector

Determines the user's primary intent.

Examples:
- CHAT
- SEARCH
- WEATHER
- DATETIME
- CALCULATOR
- MEMORY
- MEMORY_SEARCH

---

## Request

Carries all information about the current task.

Current fields:
- intent
- question
- context

Future versions may include session, metadata, memory, and execution history.

---

## Planner

Creates an execution plan from the Request.

Example:

Request

↓

SEARCH

↓

CHAT

↓

MEMORY

The Planner decides what should happen, not how it is executed.

---

## Tool Manager

Executes the Planner's execution plan.

Responsibilities:
- Load tools
- Execute tools in order
- Pass context between tools
- Return final Response

---

## Response

Standard communication object used throughout Deek.

Current fields:
- success
- message
- source
- data
- results
- metadata

---

# AI Engine

The AI Engine provides reasoning and language generation.

Responsibilities:
- Load the language model
- Execute prompts
- Generate responses

The AI Engine is isolated from the rest of the architecture so models can be replaced without affecting other components.

---

# Memory System

Current capabilities:
- Store conversation
- Retrieve conversation
- Search conversation

Future versions:
- Short-term memory
- Long-term memory
- User preferences
- Project memory
- Semantic search

---

# Tools

Tools perform user-facing capabilities.

Current tools:
- Chat Tool
- Search Tool
- Calculator Tool
- Weather Tool
- Date & Time Tool
- Memory Tool
- Memory Search Tool

Every tool:
- Receives a Request
- Returns a Response

---

# Services

Services communicate with external systems.

Current services:
- Search Service
- Weather Service

Services never interact directly with the user.

---

# Plugin System

Plugin Loader automatically discovers all available tools.

Benefits:
- No manual registration
- Easy extensibility
- Scalable architecture

---

# Rule System

Rule Loader automatically discovers planning rules.

Benefits:
- Modular planning
- Easy expansion
- No Planner modification required

---

# Testing

The project includes an automated test discovery system.

Current testing verifies:
- Module loading
- Import validation

Future testing will include:
- Functional tests
- Integration tests
- Performance tests

---

# Design Principles

Every component should:

- Have a single responsibility.
- Be modular.
- Be reusable.
- Be extensible.
- Avoid duplicated logic.
- Follow the Request → Tool → Response architecture.

---

# Future Vision

Deek will evolve from a modular AI assistant into Vinay Kosuri's Personal Artificial Intelligence Operating System (AIOS).

Future capabilities include:
- Advanced reasoning
- Long-term memory
- Workflow automation
- Task management
- Calendar integration
- File management
- Voice interaction
- Vision capabilities
- Multi-device support
- Intelligent digital life management
