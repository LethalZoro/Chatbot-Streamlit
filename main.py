import streamlit as st
import time
from openai import OpenAI

client = OpenAI(api_key=st.secrets["API_KEY"])
# ASSISTANT_ID ="asst_fWfbAUgTBe0FbftmfNGXRueb"
ASSISTANT_ID = "asst_fWfbAUgTBe0FbftmfNGXRueb"
st. set_page_config(page_title="ChatBot",
                    page_icon="icon.png", layout="centered")


# "st.session_state object:", st.session_state
st.markdown(
    " <style> div[class^='block-container'] { padding-top: 1rem;} </style> ", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: white;'>Personal ChatBot</h2>",
            unsafe_allow_html=True)

if "temp" not in st.session_state:
    st.session_state.temp = [""]


def chat_bot(message, thread):

    runs_list = client.beta.threads.runs.list(thread_id=thread.id).data

    if runs_list:  # Check if the list is not empty
        last_run = runs_list[0]

        # Wait for the last run to complete before starting a new one
        while last_run.status in ['queued', 'in_progress', 'cancelling']:
            time.sleep(1)
            last_run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=last_run.id
            )
            print(f"Last run status: {last_run.status}")

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
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        print(f"Run status: {run.status}")
    else:
        print(f"Run status: {run.status}")
    st.session_state.temp.append(run.status)
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


def main():
    if "thread" not in st.session_state:
        st.session_state.thread = client.beta.threads.create()
    if "responses" not in st.session_state:
        st.session_state.responses = [""]
    # create some empty next lines
    st.markdown("***")
    st.markdown("<h4 style='text-align: left; color: white;'>ChatBot:</h4>",
                unsafe_allow_html=True)
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
    col1, col2 = st.columns([10, 2])

    with col1:
        user_input = st.text_area(
            "You: ", "", key="input", height=80, on_change=None)
        # st.text("")
        # submit_button = st.button('Submit') submit_button or

    with col2:
        button = st.button("Enter", use_container_width=True)
    if button or user_input != "":
        # response = chat_bot(user_input)
        st.session_state.responses.append(
            chat_bot(st.session_state.input, st.session_state.thread))
        response(chat_area)
    styl = f"""
    <style>
        body {{
            background-color: #0e1117;
        }}
        .stTextArea {{
        position: fixed;
        bottom: 2rem;
        background-color: #0e1117;
        }}
    </style>
    """
    st.markdown(styl, unsafe_allow_html=True)
    styl_button = f"""
    <style>
        .stButton {{
        position: fixed;
        background-color: #0e1117;
        bottom: 2rem;
        background-color: #0e1117;
        align-items: center;
        margin-bottom: 1.5rem;
        }}
    </style>
    """
    st.markdown(styl_button, unsafe_allow_html=True)
    # make the buttun fixed on the right side


main()
