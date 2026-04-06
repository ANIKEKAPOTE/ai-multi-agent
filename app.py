import streamlit as st
from agents.primary_agent import handle_request

st.title("🤖 Multi-Agent AI System")

user_input = st.text_input("Enter your request:")

if st.button("Run"):
    if user_input:
        result = handle_request(user_input)
        st.success(result)
    else:
        st.warning("Enter something")


        