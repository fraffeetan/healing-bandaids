import streamlit as st
import random
import os
from datetime import date

# --- CONFIG --- #
BANDAID_FOLDER = "bandaids"
BG_COLOR = "#d8b2d1"

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
    .sparkle {{
        display: flex;
        justify-content: center;
        font-size: 2rem;
        animation: breathe 8s ease-in-out infinite;
        animation-delay: 1s;
    }}
    @keyframes breathe {{
        0%   {{ transform: scale(1); }}
        25%  {{ transform: scale(4); }}
        50%  {{ transform: scale(4); }}
        75%  {{ transform: scale(1); }}
        100% {{ transform: scale(1); }}
    }}
    </style>
""", unsafe_allow_html=True)

# --- APP TITLE + NAVIGATION --- #
st.title("Healing Bandaids 🩹✨")
st.sidebar.title("Navigation")
mode = st.sidebar.radio("Choose mode ✨", ["Healing Journal", "I Am Here Calendar", "View All Bandaids"])

# --- LOAD BANDAID IMAGES --- #
bandaid_images = [img for img in os.listdir(BANDAID_FOLDER) if img.endswith(".png")]

# --- SESSION STATE INIT --- #
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "show_next" not in st.session_state:
    st.session_state.show_next = False
if "chosen_bandaid" not in st.session_state:
    st.session_state.chosen_bandaid = random.choice(bandaid_images)
if "calendar_marked" not in st.session_state:
    st.session_state.calendar_marked = False
if "rerun_trigger" not in st.session_state:
    st.session_state.rerun_trigger = 0

# --- MODE: HEALING JOURNAL --- #
if mode == "Healing Journal":
    st.subheader("Daily Reflection")

    bandaid_path = os.path.join(BANDAID_FOLDER, st.session_state.chosen_bandaid)

    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.image(bandaid_path, use_container_width=True, caption="Your Healing Bandaid 💖")
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("**In what way does this resonate with you today?**")

    if not st.session_state.show_next:
        user_input = st.text_area("Share your thoughts...", value=st.session_state.user_input, height=150)

        if user_input and user_input.strip() != "":
            st.session_state.user_input = user_input
            st.session_state.show_next = True
            st.success("Thank you for your vulnerability. You are doing beautiful work 🌟🫶🏽")

    if st.session_state.show_next:
        if st.button("See next Healing Bandaid?"):
            st.session_state.chosen_bandaid = random.choice(bandaid_images)
            st.session_state.user_input = ""
            st.session_state.show_next = False
            st.session_state.rerun_trigger += 1
            st.experimental_rerun()

# --- MODE: I AM HERE CALENDAR --- #
elif mode == "I Am Here Calendar":
    st.header("I Am Here Calendar 📅")
    today = date.today()
    st.write(f"Today's date: **{today.strftime('%A, %B %d, %Y')}**")

    if not st.session_state.calendar_marked:
        if st.button("✨ I am here"):
            st.session_state.calendar_marked = True

    if st.session_state.calendar_marked:
        st.success("You are Here.")
        st.markdown('<div class="sparkle">✨</div>', unsafe_allow_html=True)
        st.caption("Breathe in… and out… 💫 Let this sparkle guide your presence.")

# --- MODE: VIEW ALL BANDAIDS --- #
elif mode == "View All Bandaids":
    st.header("All Healing Bandaids 🖼️")
    for img in bandaid_images:
        img_path = os.path.join(BANDAID_FOLDER, img)
        st.image(img_path, caption="", use_container_width=True)
    st.info("When you're ready to reflect, go back to 'Healing Journal' on the sidebar ✍️")

