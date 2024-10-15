import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Input text box for user's name
name = st.text_input("Enter your name:")

# Display a greeting message
if name:
    st.write(f"Hello, {name}! Welcome to Streamlit!")
