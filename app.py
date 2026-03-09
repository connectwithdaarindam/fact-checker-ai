import streamlit as st
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

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

st.title("✅ Fact-Checker AI Assistant")

user_input = st.text_input("Ask a factual question:")

if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    answer = response["choices"][0]["message"]["content"]
    st.write(answer)
