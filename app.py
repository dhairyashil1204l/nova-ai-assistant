import streamlit as st
from utils.ai_model import get_ai_response

st.title("🤖 Nova AI Assistant")

user_input = st.text_input("Ask Nova anything:")

if user_input:

    with st.spinner("Nova is thinking..."):
        response = get_ai_response(user_input)

    st.write(response)