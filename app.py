import streamlit as st
import random
import os
import json
from datetime import date, datetime, timedelta
import pandas as pd

# CONFIG
BANDAID_FOLDER = "bandaids"
REFLECTION_FILE = "reflection_history.json"
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
    section[data-testid="stSidebar"] .stRadio > div {
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
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR LOGO --- #
with st.sidebar:
    if os.path.exists(LOGO_IMAGE):
        st.image(LOGO_IMAGE, width=1000)

# --- TITLE + NAVIGATION --- #
st.title("Healing Bandaids 🩹✨")
mode = st.sidebar.radio("Choose mode ✨", ["Welcome 🦋",
    "Mood Meter",
    "Healing Journal",
    "I Am Here Calendar",
    "Goal Streak Tracker",
    "Reflection History",
    "View All Bandaids"
])

# --- DEFAULT LANDING PAGE --- #
if mode == "Welcome 🦋":
    st.markdown("""
        <div style='font-size: 60px; animation: breathe 4s ease-in-out infinite;'>🦋</div>
        <div style='margin-top: 30px; font-size: 22px; line-height: 1.6;'>
            Welcome to <strong>Healing Bandaids</strong> 🩹 – your space to reflect, breathe, and grow. 💖<br><br>
            Here’s what you can explore:
            <ul style='text-align: left; max-width: 600px; margin: 20px auto; padding-left: 0;'>
                <li><b>Mood Meter</b> 🌈 – Track how you're feeling from \"Surviving\" to \"Thriving\"</li>
                <li><b>Healing Journal</b> ✍️ – Reflect with a new healing bandaid each time</li>
                <li><b>I Am Here Calendar</b> 📅 – Be present and honor your journey</li>
                <li><b>Goal Streak Tracker</b> 📊 – Watch your reflection habits bloom</li>
                <li><b>Reflection History</b> 📓 – See everything you've journaled</li>
                <li><b>View All Bandaids</b> 🖼️ – Browse your healing collection</li>
            </ul>
            Take a deep breath. You're in a safe space now. 🌿
        </div>
        <style>
        @keyframes breathe {
            0% { transform: scale(1); opacity: 0.8; }
            50% { transform: scale(1.3); opacity: 1; }
            100% { transform: scale(1); opacity: 0.8; }
        }
        </style>
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

# --- INIT REFLECTION FILE --- #
if not os.path.exists(REFLECTION_FILE):
    with open(REFLECTION_FILE, "w") as f:
        json.dump([], f)

# --- HEALING JOURNAL --- #
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
            with open(REFLECTION_FILE, "r") as f:
                reflections = json.load(f)
            reflections.append({"datetime": datetime.now().isoformat(), "reflection": user_input})
            with open(REFLECTION_FILE, "w") as f:
                json.dump(reflections, f)
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

# --- I AM HERE CALENDAR --- #
elif mode == "I Am Here Calendar":
    st.header("I Am Here Calendar 🗓️")
    today = date.today()
    st.write(f"Today's date: **{today.strftime('%A, %B %d, %Y')}**")
    if not st.session_state.calendar_marked:
        if st.button("✨ I am here"):
            st.session_state.calendar_marked = True

    if st.session_state.calendar_marked:
        st.success("You are Here.")
        st.markdown('<div class="sparkle">✨</div>', unsafe_allow_html=True)
        st.caption("Breathe in… and out… 💫 Let this sparkle guide your presence.")

# --- GOAL STREAK TRACKER --- #
elif mode == "Goal Streak Tracker":
    st.markdown('<div class="css-1v3fvcr">', unsafe_allow_html=True)
    st.header("Reflection Streak Tracker 📊")
    with open(REFLECTION_FILE, "r") as f:
        data = json.load(f)
    if data:
        df = pd.DataFrame(data)
        df["date"] = pd.to_datetime(df["datetime"]).dt.date
        streak_dates = df["date"].sort_values().unique()
        streak_counts = list(range(1, len(streak_dates) + 1))
        st.line_chart(pd.Series(streak_counts, index=streak_dates))
        streak_today = date.today() in streak_dates
        streak_yesterday = (date.today() - timedelta(days=1)) in streak_dates
        streak = int(streak_today) + int(streak_yesterday)
        st.info(f"You're on a {streak}-day reflection streak! 🔥")
    else:
        st.warning("No reflections yet. Start journaling today!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- REFLECTION HISTORY --- #
elif mode == "Reflection History":
    st.header("Your Reflection History 📓")
    with open(REFLECTION_FILE, "r") as f:
        data = json.load(f)
    if data:
        df = pd.DataFrame(data)
        df["datetime"] = pd.to_datetime(df["datetime"])
        df["date"] = df["datetime"].dt.strftime("%Y-%m-%d %H:%M")
        df = df[["date", "reflection"]].sort_values("date", ascending=False)
        st.dataframe(df.rename(columns={"date": "Date", "reflection": "Reflection"}), use_container_width=True)
    else:
        st.info("No reflections yet. Start your first one today 💭")

# --- MOOD METER --- #
elif mode == "Mood Meter":
    st.markdown('<div class="fade-slide">', unsafe_allow_html=True)
    st.header("Mood Meter 🌈")
    st.write("How are you feeling today?")
    mood = st.slider("", min_value=0, max_value=100, value=50, step=1,
                     format=None, label_visibility="collapsed")
    if mood <= 33:
        st.markdown("### 🐢 Trying and Surviving")
    elif mood <= 66:
        st.markdown("### 🌱 In Progress… Growing")
    else:
        st.markdown("### 🦋 Thriving and Slaying")
    st.markdown('</div>', unsafe_allow_html=True)

elif mode == "View All Bandaids":
    st.header("All Healing Bandaids 🖼️")
    for img in bandaid_images:
        img_path = os.path.join(BANDAID_FOLDER, img)
        st.image(img_path, caption="", use_container_width=True)
    st.info("When you're ready to reflect, go back to 'Healing Journal' on the sidebar ✍️")

