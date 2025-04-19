import streamlit as st
import random
import os

# Set the background color
st.markdown("""
    <style>
    .stApp {
        background-color: #d8b2d1;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        text-align: center;
    }
    .stButton button {
        display: block;
        margin: 10px auto;
        background-color: #f1c6d9;
        color: #4a4a4a;
        font-size: 16px;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #e0a8b3;
    }
    </style>
    """, unsafe_allow_html=True)

# Set the title
st.title("Healing Bandaids 🩹✨")
st.subheader("Daily Reflection")

# Load all bandaid images
bandaid_folder = "bandaids"
bandaid_images = os.listdir(bandaid_folder)

# Pick a random bandaid
chosen_bandaid = random.choice(bandaid_images)
bandaid_path = os.path.join(bandaid_folder, chosen_bandaid)
