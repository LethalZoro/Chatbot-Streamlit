import streamlit as st
import time
from openai import OpenAI

# display the chat history
"st.session_state object:", st.session_state
st.title("Chat History")
# st.write("This is the chat history")


def chat_history(history):
    responses = []
    for i in range(len(st.session_state.responses)):
        responses.append("User: ")
        responses.append(st.session_state.user[i])
        responses.append("ChatBot: ")
        responses.append(st.session_state.responses[i])

    history.write(responses)


if st.session_state.responses is not None:
    history = st.empty()
    chat_history(history)
