# 🤝 Deal Intelligence Agent

**A persistent AI sales co-pilot that remembers every objection, stakeholder concern, and nuance across the entire deal cycle to help reps close faster.**

---

## ⚠️ The Problem

Sales cycles are complex, multi-call marathons. To prepare for a follow-up call, sales reps waste hours digging through fragmented CRM notes, transcripts, and emails just to regain context.

While generic AI chatbots exist, they fail in B2B sales because they lack **deal continuity**. They treat every query as a blank slate, offering generic sales tips instead of hyper-specific, context-aware strategies based on what happened in the last three meetings.

## 💡 The Solution

Enter the **Deal Intelligence Agent**.

Acting as a persistent, highly tactical co-pilot, this agent leverages **Hindsight Memory** to track objections, technical concerns, and pricing discussions across multiple calls. Instead of generic advice, it instantly generates targeted call preparation materials tailored to the specific hurdles of your active deal.

## 🧠 Core Feature: Hindsight Memory Pipeline

The Deal Intelligence Agent isn't just another stateless LLM wrapper. It utilizes a persistent memory architecture to genuinely understand and learn the context of your ongoing deals.

* 📥 **Memory Ingestion:** After every sales call, a summary of newly raised objections, competitor mentions, and stakeholder concerns is automatically saved to the Memory Bank.
* 🔄 **Contextual Recall:** When a rep requests call prep, the agent doesn't just look at the prompt. It retrieves the complete historical deal memory and feeds it directly into the LLM context window.
* 🎯 **Actionable Results:** The agent delivers highly specific, strategic advice. Instead of saying "build trust," it advises on exactly how to address the CTO's previous concerns about SOC2 compliance or how to position your pricing model against Datadog based on the prospect's comments from two weeks ago.

## 🛠️ Tech Stack

This project is built for speed, context-retention, and reliability:

| Component | Technology | Description |
| --- | --- | --- |
| **Frontend** | Streamlit | Lightweight, Python-based UI for rapid interaction and fast deployment. |
| **LLM Engine** | Groq | Powered by `openai/gpt-oss-20b` for lightning-fast, high-quality inference. |
| **Memory Layer** | Hindsight Cloud | Dedicated memory management for seamless multi-turn deal context tracking. |
| **Fallback System** | Local JSON | A local fallback mechanism ensuring demo reliability even if cloud services are interrupted. |

## 🗺️ Future Roadmap

* **CRM Integration:** Native syncing with Salesforce and HubSpot to auto-ingest meeting notes.
* **Multi-Stakeholder Mapping:** Automatic identification of decision-makers vs. champions based on call sentiment.
* **Objection Trend Analysis:** Dashboard views showing which competitors or technical objections are stalling the most deals across the team.

## Tech Stack
* **Frontend:** Streamlit
* **LLM:** Groq (openai/gpt-oss-20b)
* **Memory Layer:** Hindsight Cloud / Local JSON fallback for demo reliability
