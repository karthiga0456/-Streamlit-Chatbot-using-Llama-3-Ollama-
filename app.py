import streamlit as st
import ollama
import shelve

st.title("Streamlit Chatbot by Llama3")

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"

if "ollama_model" not in st.session_state:
    st.session_state["ollama_model"] = "llama3"

def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])

def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages

if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()

with st.sidebar:
    if st.button("Delete Chat History"):
        st.session_state.messages = []
        save_chat_history([])

for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        message_placeholder = st.empty()
        full_response = ""

        response = ollama.chat(
            model=st.session_state["ollama_model"],
            messages=st.session_state["messages"]
        )

        full_response = response["message"]["content"]
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})

save_chat_history(st.session_state.messages)
