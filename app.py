import streamlit as st
import random
import os

# Set the background color
st.markdown("""
    <style>
    .stImage {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .stTextInput, .stTextArea {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 80%;
    }
    .stButton {
        display: block;
        margin-left: auto;
        margin-right: auto;
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

# Initialize session state for user input and button visibility
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "show_next" not in st.session_state:
    st.session_state.show_next = False

# Display text area for user input
user_input = st.text_area("Share your thoughts...", value=st.session_state.user_input)

# When the user submits
if user_input:
    st.session_state.user_input = user_input
    st.session_state.show_next = True
    st.success("Thank you for your vulnerability. You are doing beautiful work 🌟🫶🏽")

# Show "Next" button if applicable
if st.session_state.show_next:
    if st.button("See next Healing Bandaid?"):
        st.session_state.show_next = False
        st.session_state.user_input = ""
        st.experimental_rerun()
