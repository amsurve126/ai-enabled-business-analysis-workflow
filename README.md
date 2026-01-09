# AI-Enabled Business Analysis Workflow

## Overview
Business Analysts often spend significant time converting unstructured stakeholder inputs—such as meeting notes, emails, and discussion summaries—into structured requirements documentation. This manual process can be time-consuming, inconsistent, and prone to missed details.

This project demonstrates an **AI-assisted Business Analysis automation workflow** that converts raw stakeholder inputs into structured Business Analysis artefacts, improving documentation efficiency, consistency, and traceability while **supporting (not replacing)** analyst judgment.


## Problem Statement
In many organisations, Business Analysts face challenges such as:
- Unstructured and incomplete stakeholder inputs
- Time-consuming manual creation of user stories and acceptance criteria
- Inconsistent requirement classification
- Limited visibility into gaps, ambiguities, and risks early in the lifecycle

These challenges can lead to delays, rework, and misalignment between business and delivery teams.


## Objective
The objective of this project is to:
- Assist Business Analysts in structuring requirements documentation
- Improve clarity and consistency of BA artefacts
- Identify gaps, ambiguities, and risks early
- Demonstrate a practical, enterprise-safe application of AI in Business Analysis

## Solution Overview
The solution uses a **prompt-driven AI workflow** to transform stakeholder meeting notes into:

- User Stories
- Acceptance Criteria (Gherkin format)
- Requirement Classification (Business / Functional / Non-Functional)
- Risks, gaps, and open questions

The system is designed as a **decision-support tool**, ensuring analysts retain ownership and control over final outputs.

## Role of the Business Analyst
This solution is intentionally designed with a human-in-the-loop approach.

The AI generates draft artefacts based on stakeholder inputs; however:
- All outputs are intended to be reviewed, refined, and validated by a Business Analyst
- Ambiguities and risks identified by the system require human judgment and stakeholder clarification
- The solution supports faster analysis, not automated decision-making

This mirrors how AI-assisted tools are evaluated and adopted in regulated and enterprise environments.


## Architecture
Stakeholder Notes (Text)
        ↓
Prompt Templates (BA-focused)
        ↓
AI Model (LLM)
        ↓
Structured BA Artefacts
        ↓
Human-Readable TXT Output

The architecture is intentionally simple and modular to reflect how AI-assisted tools are prototyped in real consulting and enterprise environments.


## Project Structure
This structure highlights how inputs, prompts, processing logic, and outputs are separated.

ai-ba-automation/
│
├── data/
│   └── sample_meeting_notes.txt
│
├── prompts/
│   ├── user_story_prompt.txt
│   ├── acceptance_criteria_prompt.txt
│   ├── classification_prompt.txt
│   └── risk_flag_prompt.txt
│
├── src/
│   └── ba_automation.py
│
├── outputs/
│   └── ba_output.txt
│
└── README.md


## Sample Input
**Stakeholder Meeting Notes (example):**
The business wants to launch a mobile application for existing insurance customers.
Customers should be able to view policy details and download policy documents.
The application must be secure and comply with regulatory standards.
The business wants to reduce customer service calls by enabling self-service features.
Notification mechanisms are not yet decided.


## Sample Output
The system generates a single, structured Business Analysis deliverable that includes:

- Clearly written user stories with business value
- Acceptance criteria using Gherkin syntax
- Requirement classification (Business / Functional / Non-Functional)
- Identified risks, ambiguities, and missing information

Output is written to a **human-readable `.txt` file**, reflecting real BA documentation rather than machine-only formats.

The sample output included in this repository was generated using real AI responses and then reviewed for clarity and realism.

In practice, outputs would be iteratively refined based on stakeholder feedback and delivery constraints.

## Security & Configuration
- API keys are managed via **environment variables**
- No credentials are stored in source code or committed to version control
- This ensures the project is safe to share publicly on GitHub


## Technology Stack
- Python
- OpenAI API (LLM)
- Prompt-based orchestration
- File-based input/output


## Key Learnings
- AI can significantly accelerate early-stage Business Analysis activities
- Prompt design has a direct impact on output quality
- AI is most effective as a **BA assistant**, not a replacement
- Clear structure and traceability are critical for enterprise adoption


## Future Enhancements
- Confidence scoring for generated requirements
- Support for multiple stakeholder personas
- Requirement traceability matrix generation
- UI-based input instead of text files
- Extension to process flows and data requirements


## Author
**Amar D. Surve**  
Business Analyst | Data & AI Automation | Decision support & Operational Strategy.


## Disclaimer
This project is a **portfolio demonstration** only.  
All data used is fictional and does not represent any real organisation or client.