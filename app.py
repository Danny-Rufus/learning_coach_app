import streamlit as st
from learning_chain import get_response

st.title("AI learning coach")

topic = st.text_input("What do you want to learn?")
time = st.text_input("How much time do you have?")
level = st.selectbox(
    "Select your level", ["Beginner", "Intermediate", "Advanced"], index=0
)

if st.button("Generate"):
    if topic and time:
        with st.spinner("Thinking..."):
            response = get_response(topic, time, level)

        st.markdown(response)
