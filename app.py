import streamlit as st
import random
import os

# Set the title
st.title("Healing Bandaids 🩹✨")
st.subheader("Daily Reflection")

# Load all bandaid images
bandaid_folder = "bandaids"
bandaid_images = os.listdir(bandaid_folder)

# Pick a random bandaid
chosen_bandaid = random.choice(bandaid_images)
bandaid_path = os.path.join(bandaid_folder, chosen_bandaid)

# Display the bandaid
st.image(bandaid_path, use_container_width=True)

# Ask reflection question
st.write("**In what way does this resonate with you today?**")

user_input = st.text_area("Share your thoughts...")

# When the user submits
if user_input:
    st.success("Thank you for your vulnerability. You are doing beautiful work 🌟🫶🏽")
