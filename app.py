import streamlit as st
import random
import os
from datetime import date

# --- CONFIG --- #
BANDAID_FOLDER = "bandaids"
BG_COLOR = "#d8b2d1"  # soft purple aesthetic 💜

# --- STYLING --- #
st.markdown(f"""
    <style>
    html, body, .stApp {{
        background-color: {BG_COLOR};
    }}
    .fade-in {{
        animation: fadeIn ease 2s;
    }}
    @keyframes fadeIn {{
        0% {{opacity:0;}}
        100% {{opacity:1;}}
    }}
    img {{
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-width: 80%;
        border-radius: 10px;
    }}
    .stTextInput, .stTextArea, .stButton {{
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 80%;
    }}
    </style>
""", unsafe_allow_html=True)

# --- APP TITLE --- #
st.title("Healing Bandaids 🩹✨")
st.sidebar.title("Navigation")
mode = st.sidebar.radio("Choose mode ✨", ["Healing Journal", "View All Bandaids", "Calendar View"])

# --- LOAD IMAGES --- #
bandaid_images = [img for img in os.listdir(BANDAID_FOLDER) if img.endswith(".png")]

# --- SESSION STATE --- #
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "show_next" not in st.session_state:
    st.session_state.show_next = False
if "chosen_bandaid" not in st.session_state:
    st.session_state.chosen_bandaid = random.choice(bandaid_images)
if "rerun_trigger" not in st.session_state:
    st.session_state.rerun_trigger = 0

# --- MODE: VIEW ALL BANDAIDS --- #
if mode == "View All Bandaids":
    st.header("All Healing Bandaids 🖼️")
    for img in bandaid_images:
        img_path = os.path.join(BANDAID_FOLDER, img)
        st.image(img_path, caption=img, use_container_width=True)
    st.info("When you're ready to reflect, go back to 'Healing Journal' on the sidebar ✍️")

# --- MODE: CALENDAR VIEW --- #
elif mode == "Calendar View":
    st.header("Mindful Moments Calendar 📅")
    st.write("Pick a day to reflect or just mark your presence 💖")
    selected_day = st.date_input("Pick a date", date.today())
    st.success(f"You're showing up for yourself today: {selected_day.strftime('%A, %B %d, %Y')} 🌟")

# --- MODE: HEALING JOURNAL --- #
else:
    st.subheader("Daily Reflection")

    bandaid_path = os.path.join(BANDAID_FOLDER, st.session_state.chosen_bandaid)

    # ✨ Fade-in bandaid image
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.image(bandaid_path, use_container_width=True, caption="Your Healing Bandaid 💖")
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("**In what way does this resonate with you today?**")

    if not st.session_state.show_next:
        user_input = st.text_area("Share your thoughts...", value=st.session_state.user_input)

        if user_input and user_input.strip() != "":
            st.session_state.user_input = user_input
            st.session_state.show_next = True
            st.success("Thank you for your vulnerability. You are doing beautiful work 🌟🫶🏽")

    # Show next button only after reflection
    if st.session_state.show_next:
        if st.button("See next Healing Bandaid?"):
            # Reset state manually instead of using experimental_rerun
            st.session_state.chosen_bandaid = random.choice(bandaid_images)
            st.session_state.user_input = ""
            st.session_state.show_next = False
            st.session_state.rerun_trigger += 1  # Safe trigger to refresh state
            st.experimental_rerun()
