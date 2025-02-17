# import os

# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as gen_ai


# load_dotenv()

# st.set_page_config(
#     page_title="Chat with Optimus!",
#     page_icon=":brain:",  
#     layout="centered",  
# )

# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# gen_ai.configure(api_key=GOOGLE_API_KEY)
# model = gen_ai.GenerativeModel('gemini-pro')


# def translate_role_for_streamlit(user_role):
#     if user_role == "model":
#         return "assistant"
#     else:
#         return user_role


# if "chat_session" not in st.session_state:
#     st.session_state.chat_session = model.start_chat(history=[])


# st.title("🤖 Optimus")

# for message in st.session_state.chat_session.history:
#     with st.chat_message(translate_role_for_streamlit(message.role)):
#         st.markdown(message.parts[0].text)

# user_prompt = st.chat_input("Ask Optimus...")
# if user_prompt:
#     st.chat_message("user").markdown(user_prompt)

#     gemini_response = st.session_state.chat_session.send_message(user_prompt)

#     with st.chat_message("assistant"):
#         st.markdown(gemini_response.text)

import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyB_I0YPXXBym9K5TEvCdiqPbpMRk9GX95o"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def main():
    st.set_page_config(page_title="Chat with Optimus!", page_icon=":brain:")
    
    st.markdown(
        """
            <div style="text-align: center;">
                <h1>🤖 Optimus</h1>
                <h3>Your AI Chat Companion</h3>
                <p>Ask anything and get instant AI-powered responses!</p>
            </div>    
        """,
        unsafe_allow_html=True,
    )
    
    # Initialize chat session in Streamlit if not already present
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])
    
    # Display chat history
    for message in st.session_state.chat_session.history:
        role = "assistant" if message.role == "model" else message.role
        with st.chat_message(role):
            st.markdown(message.parts[0].text)
    
    # User input field
    user_prompt = st.text_area("Ask Optimus...")
    submit = st.button("Send")
    
    if submit and user_prompt:
        with st.spinner("Thinking..."):
            # Display user input
            st.chat_message("user").markdown(user_prompt)
            
            # Send user prompt to Gemini-Pro and get response
            gemini_response = st.session_state.chat_session.send_message(user_prompt)
            
            # Display Gemini-Pro response
            with st.chat_message("assistant"):
                st.markdown(gemini_response.text)

if __name__ == "__main__":
    main()
