import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage

# Connect to your chatbot code
from chatbot import llm, chat_history

st.set_page_config(page_title="Mistral Chatbot", page_icon="🤖")
st.title("🤖 Chatbot")

# Sidebar
with st.sidebar:
    if st.button("Clear chat"):
        del chat_history[1:]  # keep only the system message
        st.rerun()

# Show previous messages
for msg in chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# New message
user_input = st.chat_input("Type your message...")

if user_input and user_input.strip():
    with st.chat_message("user"):
        st.markdown(user_input)

    chat_history.append(HumanMessage(content=user_input))

    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking..."):
                result = llm.invoke(chat_history)
            st.markdown(result.content)
            chat_history.append(AIMessage(content=result.content))
        except Exception as e:
            st.error(f"Error: {e}")
            chat_history.pop()  # remove the failed message