import streamlit as st
import time
from openai import OpenAI

client = OpenAI(api_key="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")
# ASSISTANT_ID ="asst_fWfbAUgTBe0FbftmfNGXRueb"
ASSISTANT_ID = "asst_fWfbAUgTBe0FbftmfNGXRueb"

# "st.session_state object:", st.session_state
# st.markdown(
#     " <style> div[class^='block-container'] { padding-right: 0;padding-left: 0; margin-right: 0;padding-left: 0; } </style> ", unsafe_allow_html=True)
st. set_page_config(layout="centered")
st.markdown("<h1 style='text-align: center; color: white;'>Personal ChatBot</h1>",
            unsafe_allow_html=True)


def chat_bot(message, thread):
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message,
    )
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=ASSISTANT_ID
    )
    print(f"Run created: {run.id}")
    while run.status in ['queued', 'in_progress', 'cancelling']:
        time.sleep(0.5)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        print(f"Run status: {run.status}")
    else:
        print(f"Run status: {run.status}")
    if run.status == 'completed':
        chat_history = client.beta.threads.messages.list(
            thread_id=thread.id
        )
    latest_message = chat_history.data[0]
    # print(latest_message.content[0].text.value)
    response = latest_message.content[0].text.value
    return response


def response(chat_area):
    # st.text("ChatBot: ")
    # chat_area = st.empty()
    # write some text in the chat area
    chat_area.write(
        st.session_state.responses[-1])


def app(i):
    thread = client.beta.threads.create()
    if "responses" not in st.session_state:
        st.session_state.responses = [""]
    # create some empty next lines
    st.markdown("***")
    st.text("ChatBot: ")
    chat_area = st.empty()

    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")

    user_input = st.text_input(
        "You: ", "", key="input")
    st.text("")
    submit_button = st.button('Submit')
    if submit_button or user_input != "":
        # response = chat_bot(user_input)
        st.session_state.responses.append(chat_bot(user_input, thread))
        response(chat_area)


app(10)
