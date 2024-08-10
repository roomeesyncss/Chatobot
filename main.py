import streamlit as st
import google.generativeai as gen_ai

st.set_page_config(
    page_title="Chat with Conversa-Bot!",
    page_icon="💬",
    layout="centered",
)

GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "Conversa-Bot"
    else:
        return user_role

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.markdown(
    """
    <style>
    .streamlit-expanderHeader {
        font-size: 1.5rem;
        font-weight: bold;
        color: #4CAF50; /* Header text color */
    }
    .stButton>button {
        background-color: #f44336; /* Button color */
        color: white;
    }
    .user-message .element-container {
        background-color: #2196F3; /* User message background color */
        color: white;
    }
    .assistant-message .element-container {
        background-color: #FFEB3B; /* Assistant message background color */
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("💬 Chat with Conversa-Bot!")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input("Ask Conversa-Bot anything...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)

    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    with st.chat_message("Conversa-Bot"):
        st.markdown(gemini_response.text)
