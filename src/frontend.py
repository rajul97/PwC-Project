import streamlit as st
import requests

st.title("AI Chatbot")

user_input = st.text_input("Ask me anything:")
if st.button("Submit"):
    response = requests.post("http://127.0.0.1:5000/ask", json={"question": user_input})
    st.write(response.json()["answer"])
