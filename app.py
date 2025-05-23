import streamlit as st
import random
import os
from datetime import date, datetime, timedelta
import pandas as pd

st.set_page_config(
    page_title="Healing Bandaids 🩹✨",
    page_icon="🦋",
    layout="centered"
)

# CONFIG
BANDAID_FOLDER = "bandaids"
LOGO_IMAGE = "bandaids-logo.png"

# --- STYLING --- #
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Abril+Fatface&display=swap');

    html, body, .stApp {
        background-color: #4e6d60;
        font-family: 'Abril Fatface', cursive;
        color: white;
        text-align: center;
    }

    section[data-testid="stSidebar"] > div:first-child {
        background-color: #fce0cf;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: #245444;
    }

    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] .css-1aumxhk,
    section[data-testid="stSidebar"] .stRadio > div,
    section[data-testid="stSidebar"] .stRadio label,
    section[data-testid="stSidebar"] .stRadio span {
        color: #245444 !important;
    }

    .css-1v3fvcr {
        background-color: #cbada7 !important;
    }

    .fade-in {
        animation: fadeIn ease 2s;
    }
    @keyframes fadeIn {
        0% {opacity:0;}
        100% {opacity:1;}
    }

    img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-width: 80%;
        border-radius: 10px;
    }

    .stTextInput, .stTextArea, .stButton {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 80%;
    }

    .sparkle {
        display: flex;
        justify-content: center;
        font-size: 2rem;
        animation: breathe 8s ease-in-out infinite;
        animation-delay: 1s;
    }

    @keyframes breathe {
        0%   { transform: scale(1); }
        25%  { transform: scale(4); }
        50%  { transform: scale(4); }
        75%  { transform: scale(1); }
        100% { transform: scale(1); }
    }

    .fade-slide {
        animation: fadeSlide 0.8s ease-in-out;
    }

    @keyframes fadeSlide {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    [data-testid="stDataFrame"] {
        background-color: #cbada7 !important;
        color: #245444 !important;
        font-family: 'Abril Fatface', cursive !important;
        border-radius: 10px;
    }
        [data-testid="stSidebar"] .stRadio > div > label {
        color: #245444 !important;
    }
    .flower {
        position: fixed;
        top: 0;
        font-size: 32px;
        animation: flowerRain 6s linear infinite;
        z-index: 9999;
        opacity: 0;
    }
    .flower:nth-child(1) { left: 5%; animation-delay: 0s; }
    .flower:nth-child(2) { left: 15%; animation-delay: 1s; }
    .flower:nth-child(3) { left: 25%; animation-delay: 2s; }
    .flower:nth-child(4) { left: 35%; animation-delay: 3s; }
    .flower:nth-child(5) { left: 45%; animation-delay: 4s; }
    .flower:nth-child(6) { left: 55%; animation-delay: 5s; }
    .flower:nth-child(7) { left: 65%; animation-delay: 6s; }
    .flower:nth-child(8) { left: 75%; animation-delay: 7s; }
    .flower:nth-child(9) { left: 85%; animation-delay: 8s; }
    .flower:nth-child(10) { left: 95%; animation-delay: 9s; }
    div[data-baseweb="slider"] .css-14v1g6z {
        background: linear-gradient(to right, #fbc3bc, #f8ad9d);
    }
    div[data-baseweb="slider"] .css-1ld3z1x {
        background-color: white !important;
        border: 3px solid #f8ad9d !important;
    }
    div[data-baseweb="slider"] .css-1ld3z1x:before {
        content: "🐢";
        position: absolute;
        top: -25px;
        left: -10px;
        font-size: 20px;
        transition: content 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR LOGO --- #
with st.sidebar:
    if os.path.exists(LOGO_IMAGE):
        st.image(LOGO_IMAGE, width=1000)

# --- TITLE + NAVIGATION --- #
st.title("Healing Bandaids 🩹✨")
mode = st.sidebar.selectbox("Choose mode ✨", [
    "🦋 Welcome",
    "🌈 Mood Meter",
    "✍️ Healing Journal",
    "📅 I Am Here Calendar",
    "🖼️ View All Bandaids",
    "🦋 About the Creator",
    "🌿 About the Creation"
])

# --- DEFAULT LANDING PAGE --- #
if mode == "🦋 Welcome":
    st.markdown("""
        <div class='sparkle'>🦋</div>
        <div style='margin-top: 30px; font-size: 22px; line-height: 1.6;'>
            <p>Welcome to your sanctuary of reflection and calm. 🩹💖</p>
            <ul style='text-align: left; max-width: 600px; margin: 20px auto; padding-left: 0;'>
                <li><b>🌈 Mood Meter</b> – Track how you're feeling from \"Surviving\" to \"Thriving\"</li>
                <li><b>✍️ Healing Journal</b> – Reflect with a new healing bandaid each time</li>
                <li><b>📅 I Am Here Calendar</b> – Be present and honor your journey</li>
                <li><b>🖼️ View All Bandaids</b> – Browse your healing collection</li>
            </ul>
            <p>Take a deep breath. You're in a safe space now. 🌿</p>
        </div>
    """, unsafe_allow_html=True)

# --- LOAD BANDAIDS --- #
bandaid_images = [img for img in os.listdir(BANDAID_FOLDER) if img.endswith(".png")]

# --- SESSION STATE --- #
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "show_next" not in st.session_state:
    st.session_state.show_next = False
if "chosen_bandaid" not in st.session_state:
    st.session_state.chosen_bandaid = random.choice(bandaid_images)
if "calendar_marked" not in st.session_state:
    st.session_state.calendar_marked = False

# --- HEALING JOURNAL --- #
if mode == "✍️ Healing Journal":
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
            # Reflection is not saved; reset every session
            st.success("Thank you for your vulnerability. You are doing beautiful work 🌟🪖")
            st.markdown("""
            <style>
            @keyframes flowerRain {
                0% { transform: translateY(-50px); opacity: 1; }
                100% { transform: translateY(100vh); opacity: 0; }
            }
            .flower {
                position: fixed;
                top: 0;
                font-size: 40px;
                animation: flowerRain 5s linear forwards;
                z-index: 9999;
                opacity: 0;
            }
            </style>
            <div class='flower' style='left: 10%; animation-delay: 0s;'>🌸</div>
            <div class='flower' style='left: 25%; animation-delay: 0.5s;'>🌼</div>
            <div class='flower' style='left: 40%; animation-delay: 1s;'>🌺</div>
            <div class='flower' style='left: 55%; animation-delay: 1.5s;'>💐</div>
            <div class='flower' style='left: 70%; animation-delay: 2s;'>🌷</div>
            <div class='flower' style='left: 85%; animation-delay: 2.5s;'>🌻</div>
            """, unsafe_allow_html=True)

    if st.session_state.show_next:
        if st.button("See next Healing Bandaid?"):
            st.session_state.chosen_bandaid = random.choice(bandaid_images)
            st.session_state.user_input = ""
            st.session_state.show_next = False

# --- ABOUT THE CREATOR --- #
elif mode == "🦋 About the Creator":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("fraffee-photo.png", width=200)
    st.markdown("""
    <div style='margin-top: 30px; font-size: 22px; line-height: 1.6;'>
        <p><strong>Fran</strong> (Artist name: <strong>Fraffee</strong>) is someone who vibe-codes in the way she writes poetry, and she writes poetry like the way she paints — with gentleness, intention, and love.</p>
        <p>A builder of soft digital spaces, Fran believes that reflection doesn’t have to be clinical or cold — it can be warm, whimsical, and wrapped in sparkles. ✨</p>
        <p>Whether it's choosing the perfect pastel for a slider, writing heart-hugging affirmations, or making butterflies pulse to the rhythm of a breath, her goal is simple: <br><strong>To create moments of stillness for those who need them.</strong></p>
    </div>
    """, unsafe_allow_html=True)

# --- ABOUT THE CREATION --- #
elif mode == "🌿 About the Creation":
    st.markdown("""
    <div style='margin-top: 30px; font-size: 22px; line-height: 1.6;'>
        <p>This app is not about metrics. It’s about meaning.</p>
        <p>No tracking. No pressure. Just healing — one soft step at a time. 🌿</p>
        <p style='margin-top: 3em; font-size: 18px;'>Made with love by <strong>Fraffee</strong> 🌱</p>
    </div>
    """, unsafe_allow_html=True)

# --- I AM HERE CALENDAR --- #
elif mode == "📅 I Am Here Calendar":
    st.header("I Am Here Calendar 🗓️")
    today = (datetime.utcnow() + timedelta(hours=8)).date()
    st.write(f"Today's date: **{today.strftime('%A, %B %d, %Y')}**")
    if not st.session_state.calendar_marked:
        if st.button("✨ I am here"):
            st.session_state.calendar_marked = True

    if st.session_state.calendar_marked:
        st.success("You are Here.")
        st.markdown('<div class="sparkle">✨</div>', unsafe_allow_html=True)
        st.caption("Breathe in… and out… 💫 Let this sparkle guide your presence.")





# --- MOOD METER --- #
elif mode == "🌈 Mood Meter":
    st.markdown('<div class="fade-slide">', unsafe_allow_html=True)
    st.header("Mood Meter 🌈")
    st.write("How are you feeling today?")
    mood = st.slider("", min_value=0, max_value=100, value=50, step=1,
                     format=None, label_visibility="collapsed")
    if "mood_history" not in st.session_state:
        st.session_state["mood_history"] = []
    if st.button("Log this mood"):
        st.session_state["mood_history"].append({"datetime": datetime.utcnow() + timedelta(hours=8), "mood": mood})

        if mood <= 33:
            st.success("Mood logged 🌈")
            st.markdown("#### 🌒 Even the moon has nights without light. Be still. Be held. Let softness meet your sorrow.")
        elif mood <= 66:
            st.success("Mood logged 🌈")
            st.markdown("#### 🌿 Your roots are reaching before your blooms show. Trust the quiet persistence of your becoming.")
        else:
            st.success("Mood logged 🌈")
            st.markdown("#### ✨ You’re radiant and rising. May your joy ripple beyond today — bold, bright, and beautifully yours.")
        st.markdown("""
        <style>
        @keyframes sparkleRain {
            0% { transform: translateY(-50px); opacity: 1; }
            100% { transform: translateY(100vh); opacity: 0; }
        }
        .sparkle-fall {
            position: fixed;
            top: 0;
            font-size: 40px;
            animation: sparkleRain 5s linear forwards;
            z-index: 9999;
            opacity: 0;
        }
        </style>
        <div class='sparkle-fall' style='left: 10%; animation-delay: 0s;'>✨</div>
        <div class='sparkle-fall' style='left: 25%; animation-delay: 0.5s;'>🌟</div>
        <div class='sparkle-fall' style='left: 40%; animation-delay: 1s;'>🌙</div>
        <div class='sparkle-fall' style='left: 55%; animation-delay: 1.5s;'>💫</div>
        <div class='sparkle-fall' style='left: 70%; animation-delay: 2s;'>✨</div>
        <div class='sparkle-fall' style='left: 85%; animation-delay: 2.5s;'>🌟</div>
        <div class='sparkle-fall' style='left: 15%; animation-delay: 3s;'>🌙</div>
        <div class='sparkle-fall' style='left: 35%; animation-delay: 3.5s;'>💫</div>
        """, unsafe_allow_html=True)
    if mood <= 33:
        st.markdown("### 🐢 Trying and Surviving")
    elif mood <= 66:
        st.markdown("### 🌱 In Progress… Growing")
    else:
        st.markdown("### 🦋 Thriving and Slaying")
    st.markdown('</div>', unsafe_allow_html=True)



elif mode == "🖼️ View All Bandaids":
    st.header("All Healing Bandaids 🖼️")
    st.markdown("<p style='font-size: 18px; margin-bottom: 2em;'>All artwork was made by <strong>Fraffee</strong> via the #The100DayProject and can be found on her Instagram at <a href='https://www.instagram.com/fraffee/' target='_blank' style='color: #fce0cf; text-decoration: underline;'>@fraffee</a></p>", unsafe_allow_html=True)
    for img in bandaid_images:
        img_path = os.path.join(BANDAID_FOLDER, img)
        st.image(img_path, caption="", use_container_width=True)
    st.info("When you're ready to reflect, go back to 'Healing Journal' on the sidebar ✍️")
