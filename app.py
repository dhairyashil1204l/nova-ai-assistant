import streamlit as st

#Page Configuration
st.set_page_config(
    page_title="Nova AI"
)

#Title
st.title("Nova AI Assistant")

st.write("Your Personal AI Assistant")

#Store Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User Input
user_input = st.chat_input("Ask Nova AI anything...")

if user_input:
    #Add user message
    st.session_state.messages.append(
         {
             "role": "user",
             "content": user_input
         }
    )

    with st.chat_message("user"):
        st.write(user_input)

    #Temporary AI Response
    ai_response = "Hello! I am Nova AI, My intelligence module will be connected soon"

    #Add AI message
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content": ai_response
        }
    )

    with st.chat_message("assistant"):
        st.write(ai_response)