# 🤝 Deal Intelligence Agent

An AI sales assistant built for the Hack with Hyderabad Hackathon that remembers every objection across calls to help sales reps close deals.

## The Problem
Sales reps waste hours re-reading CRM notes before calls. Generic chatbots cannot help because they lack context across the entire deal cycle. 

## The Solution
The Deal Intelligence Agent acts as a persistent co-pilot. It uses Hindsight memory to track objections raised, stakeholder concerns, and pricing discussions across multiple calls, instantly generating highly tactical, context-aware call prep.

## How Hindsight Memory is Used (Core Feature)
Instead of a stateless LLM wrapper, this agent leverages persistent memory to learn the deal context:
1. **Memory Ingestion:** After every sales call, a summary of objections and stakeholder concerns is saved to the Memory Bank.
2. **Contextual Recall:** When a rep asks for call prep, the agent retrieves the historical deal memory and feeds it to the Groq LLM.
3. **The Result:** The agent gives specific advice (e.g., handling SOC2 compliance or competing against Datadog) rather than generic sales tips. 

## Tech Stack
* **Frontend:** Streamlit
* **LLM:** Groq (openai/gpt-oss-20b)
* **Memory Layer:** Hindsight Cloud / Local JSON fallback for demo reliability
