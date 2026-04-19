import streamlit as st
import random
import time
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

system_prompt = """
You are SmartCar AI assistant.

You diagnose car problems clearly and shortly.
You help with repair, maintenance, costs, and safety.
""" 

def ai(msg):
    try:
        prompt = f"""
        {system_prompt}
        
        User request: {msg}
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return str(e)


# ===================== EXTRA AI =====================
def sound_ai():
    return ai("Analyze engine sound and detect issues")

def predict_failure():
    return ai("Predict possible car failures in 30 days")

def maintenance_tips():
    return ai("Give simple DIY car maintenance tips")

def finance_summary():
    return ai("Monthly car expense breakdown")

def route_suggestion():
    return ai("Suggest smart route optimization")


# ===================== UI =====================
st.set_page_config(page_title="SmartCar AI", layout="wide")

st.markdown("""
<style>

/* BACKGROUND */
body {
    background: #f4f7fb;
}

/* TITLE */
h1, h2, h3 {
    color: #1f3b73;
    font-family: Arial;
}

/* CARD DESIGN */
.card {
    background: white;
    padding: 18px;
    border-radius: 18px;
    border: 1px solid #e6eaf0;
    box-shadow: 0 6px 20px rgba(0,0,0,0.05);
    margin-bottom: 12px;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
}

/* BUTTONS */
.stButton button {
    background: linear-gradient(135deg, #2f80ed, #56ccf2);
    color: white;
    border-radius: 10px;
    padding: 8px 14px;
    border: none;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.05);
}

/* METRICS */
[data-testid="metric-container"] {
    background: white;
    border-radius: 12px;
    padding: 10px;
    border: 1px solid #e6eaf0;
}

</style>
""", unsafe_allow_html=True)


# ===================== SESSION =====================
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ===================== HEADER =====================
st.title("🚗 SmartCar AI System")
st.caption("AI-powered vehicle intelligence & diagnostics")


# ===================== NAV =====================
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Dashboard"):
        st.session_state.page = "Dashboard"

with col2:
    if st.button("📊 Diagnostics"):
        st.session_state.page = "Diagnostics"

with col3:
    if st.button("💬 AI Chat"):
        st.session_state.page = "Chat"

with col4:
    if st.button("⚙ Smart Center"):
        st.session_state.page = "Smart"

page = st.session_state.page


# ===================== 1. DASHBOARD =====================
if page == "Dashboard":

    st.header("🚘 Dashboard Overview")

    st.markdown("""
    <div class="card">
        <h3>🚗 Toyota Camry XLE 2022</h3>
        <p style="color:gray;">Smart Connected Vehicle System</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("⛽ Fuel", "72%")

    with col2:
        st.metric("🔧 Engine", "91%")

    with col3:
        st.metric("🛞 Tires", "Good")

    st.markdown("""
    <div class="card">
        ⚠ Brake wear detected<br>
        🛢 Oil change recommended soon<br>
        ✔ System stable
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔮 Predict Issues"):
        st.warning(predict_failure())


# ===================== 2. DIAGNOSTICS =====================
elif page == "Diagnostics":

    st.header("📊 Live Diagnostics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("RPM", random.randint(1500, 3500))

    with col2:
        st.metric("Speed km/h", random.randint(20, 120))

    with col3:
        st.metric("Engine Temp °C", random.randint(70, 110))

    st.markdown("---")

    if st.button("🎤 Engine Sound AI"):
        st.success(sound_ai())


# ===================== 3. CHAT =====================
elif page == "Chat":

    st.header("💬 AI Mechanic Chat")

    msg = st.text_input("Describe your car problem:")

    if st.button("Send"):
        if msg:
            st.session_state.chat_history.append(("You", msg))
            response = ai(msg)
            st.session_state.chat_history.append(("AI", response))

    for role, text in st.session_state.chat_history:
        if role == "You":
            st.markdown(f"<div class='card'>👤 {text}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='card'>🤖 {text}</div>", unsafe_allow_html=True)


# ===================== 4. SMART CENTER =====================
elif page == "Smart":

    st.header("⚙ Smart Center")

    st.subheader("🎤 Voice Command")
    voice = st.text_input("Say command (e.g. check engine)")

    if st.button("Run Voice Command"):
        st.success(ai(voice))

    st.markdown("---")

    if st.button("🛠 DIY Maintenance Tips"):
        st.info(maintenance_tips())

    st.markdown("---")

    if st.button("🚨 Emergency SOS"):
        st.error("🚨 SOS SENT (SIMULATION MODE)")

    st.markdown("---")

    if st.button("💰 Monthly Expenses"):
        st.success(finance_summary())

    st.markdown("---")

    if st.button("🗺 Smart Route Optimization"):
        st.info(route_suggestion())
