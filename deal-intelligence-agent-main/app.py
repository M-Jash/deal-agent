import streamlit as st
import json
import os
from groq import Groq
from datetime import datetime

# Initialize Groq Client
# Replace with your actual Groq API key


client = Groq()

# Simulate Hindsight Memory Layer locally for the hackathon demo
MEMORY_FILE = "hindsight_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(memories):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memories, f)

# Initialize Session State
if "memories" not in st.session_state:
    st.session_state.memories = load_memory()
    # Pre-load synthetic data if memory is empty (Crucial for the demo!)
    if not st.session_state.memories:
        st.session_state.memories = [
            "Call 1 (Sept 10): Sarah (VP Sales) loved the demo but noted Acme is undergoing Q4 budget cuts. Worried about the $120k upfront cost.",
            "Call 2 (Sept 15): Mark (Security Lead) needs assurance our servers are in the US and latency is < 50ms for SOC2 compliance.",
            "Call 3 (Sept 22): David (CFO) objected to annual billing. Competitor Datadog offered them a 15% discount and quarterly billing."
        ]
        save_memory(st.session_state.memories)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# UI Setup
st.set_page_config(page_title="Deal Intelligence Agent", layout="wide")
st.title("🤝 Deal Intelligence Agent")
st.markdown("### Powered by Hindsight Memory")
st.markdown("*An AI sales assistant that remembers every objection across calls to help you close the deal.*")

col1, col2 = st.columns([1, 2])

# Left Column: Memory Dashboard
with col1:
    st.subheader("🧠 Deal Memory Bank")
    st.caption("Past interactions retrieved for context:")
    for mem in st.session_state.memories:
        st.info(mem)
    
    st.divider()
    new_memory = st.text_area("Log new interaction:")
    if st.button("Save to Memory"):
        if new_memory:
            st.session_state.memories.append(f"New Log ({datetime.now().strftime('%b %d')}): {new_memory}")
            save_memory(st.session_state.memories)
            st.success("Memory updated!")
            st.rerun()

# Right Column: Chat Interface
with col2:
    st.subheader("💬 Call Prep Chat")
    
    # Display Chat History
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    # User Input
    user_input = st.chat_input("E.g., I'm heading into Call 4 with the CFO. What should I say?")
    
    if user_input:
        # 1. Display user message
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
            
        # 2. Build the prompt with Memory Context
        context = "\n".join(st.session_state.memories)
        system_prompt = f"""You are an elite Sales AI Assistant. Use the following memory of past interactions with this client to answer the user's request. 
        Be highly tactical, address specific objections mentioned in the memory, and provide actionable advice.
        
        MEMORY BANK:
        {context}
        """
        
        # 3. Call Groq LLM
        with st.chat_message("assistant"):
            with st.spinner("Analyzing past deal memory..."):
                try:
                    completion = client.chat.completions.create(
                        model="llama-3.1-70b-versatile", # Reliable Groq model
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_input}
                        ],
                        temperature=0.7,
                    )
                    response = completion.choices[0].message.content
                    st.markdown(response)
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"Error calling LLM: {e}")