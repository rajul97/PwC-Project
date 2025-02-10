import streamlit as st
import requests

# Set API URL (Update this with your deployed backend)
API_URL = "https://pwc-project.onrender.com/ask"  # Change this if needed

st.title("AI Chatbot")

user_input = st.text_input("Ask me anything:")
if st.button("Submit"):
    try:
        response = requests.post(API_URL, json={"question": user_input})
        if response.status_code == 200:
            st.write(response.json()["answer"])
        else:
            st.write("Error: Unable to connect to the AI service.")
    except Exception as e:
        st.write(f"Exception: {e}")
