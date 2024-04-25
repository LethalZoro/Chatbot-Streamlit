import streamlit as st
import time
from openai import OpenAI

# display the chat history
# "st.session_state object:", st.session_state
st.title("Chat History")
# st.write("This is the chat history")


def chat_history(history):
    responses = []
    temp = []
    user = ""
    chatbot = ""
    for i in range(len(st.session_state.responses)):
        responses.append("User: ")
        if i < len(st.session_state.user) and st.session_state.user[i] is not None:
            responses.append(st.session_state.user[i])
        responses.append("ChatBot: ")
        responses.append(st.session_state.responses[i])
    history.write(responses)

    # temp.append(st.empty())
    # user = "User: \n"+st.session_state.user[i]+"\n"
    # temp[i].write(user)
    # temp.append(st.empty())
    # chatbot = "ChatBot: \n"+st.session_state.responses[i]+"\n"
    # temp[i+1].write(chatbot)


if st.session_state.responses is not None:
    history = st.empty()
    chat_history(history)
