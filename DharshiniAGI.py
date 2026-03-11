import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="Dharshini's AGI", page_icon="🧠")

st.title("Simple Chatbot")

if not GROQ_API_KEY:
    st.error("⚠️ GROQ API key not found. Please set GROQ_API_KEY in .env file")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Hi! :)")

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=st.session_state.messages,
    temperature=0.7,
    max_tokens=256
    )
    response = completion.choices[0].message.content

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
