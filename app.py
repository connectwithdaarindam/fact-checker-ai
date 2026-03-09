import streamlit as st
from openai import OpenAI
import os

st.title("✅ Fact-Checker AI Assistant")

# --- Safe API Key Handling ---
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("API key not found. Please add it in Streamlit Secrets.")
    st.stop()

client = OpenAI(api_key=api_key)

# --- System Prompt ---
system_prompt = """
You are a Fact-Checker AI Assistant.

You must answer ONLY factual, verifiable questions related to:
- History
- Science
- Geography
- Data
- Real-world events

If the question is NOT factual, opinion-based, creative, hypothetical,
or if the information cannot be confidently verified,
you MUST respond EXACTLY with:

"I cannot confirm this information."

Rules:
- Do not guess
- Do not generate opinions
- Do not create stories or poems
- Do not provide speculative answers
- Only provide verified facts
"""

# --- User Input ---
user_input = st.text_input("Ask a factual question:")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    answer = response.choices[0].message.content
    st.write(answer)
