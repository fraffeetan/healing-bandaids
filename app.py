import streamlit as st
import random
import os

# Set the background image
st.markdown("""
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://github.com/fraffeetan/healing-bandaids/blob/16899cd1b531424138fb2e2e2ac269aebc46201d/paper.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
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

# Display the bandaid
st.image(bandaid_path, use_container_width=True)

# Ask reflection question
st.write("**In what way does this resonate with you today?**")

user_input = st.text_area("Share your thoughts...")

# When the user submits
if user_input:
    st.success("Thank you for your vulnerability. You are doing beautiful work 🌟🫶🏽")
