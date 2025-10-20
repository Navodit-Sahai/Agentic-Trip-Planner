import streamlit as st
import requests
import datetime

BASE_URL = "https://agentic-trip-planner-gbfn.onrender.com/"

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------- DARK PROFESSIONAL THEME (UPDATED) ----------------
st.markdown("""
    <style>
    /* App Background */
    .stApp {
        background: linear-gradient(135deg, #0a0f2c 0%, #111b3f 50%, #1f2b55 100%);
        color: #e8e9ee;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Main Container */
    .main .block-container {
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        padding-top: 0rem !important;
        max-width: 100% !important;
    }

    /* Sidebar (About Section) */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0e1438 0%, #1c2257 100%);
        padding: 0rem 0rem;
        color: #e8e9ee !important;
        width: 100% !important;
        min-width: 1050px !important;
    }
    [data-testid="stSidebar"] * {
        color: #e8e9ee !important;
        font-size: 3.5rem !important;
        line-height: 1.5;
    }

    /* Sidebar Feature Cards */
    .feature-card {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 25px;
        padding: 2.0rem;
        margin: 2.3rem 0;
        border-left: 6px solid #6c63ff;
        box-shadow: 0 8px 22px rgba(0,0,0,0.4);
        transition: all 0.3s ease;
        font-size: 3.5rem;
    }
    .feature-card:hover {
        transform: translateX(15px);
        box-shadow: 0 12px 32px rgba(108,99,255,0.5);
    }
    
    /* About heading */
    [data-testid="stSidebar"] h1 {
        font-size: 5.7rem !important;
    }

    /* Feature titles */
    [data-testid="stSidebar"] [style*="font-weight:800"] {
        font-size: 4.0rem !important;
    }

    /* Header */
    .main-header {
        text-align: center;
        padding: 3rem 0 6rem 0;
        color: #e8e9ee;
    }
    .main-header h1 {
        font-size: 13rem;
        font-weight: 800;
        letter-spacing: 0.5px;
        color: #b3c7ff;
        text-shadow: 0 0 30px rgba(108,99,255,0.7);
    }
    .main-header p {
        font-size: 4.5rem;
        opacity: 0.9;
    }

    /* Input Field */
    div.stTextInput > div {
        height: 16rem !important;  
    }

    div.stTextInput > div > div > input {
        width: 100% !important;
        height: 100% !important; 
        font-size: 5rem !important;
        padding: 1.0rem 1rem !important;  
        border-radius: 12px !important;
        background: rgba(255,255,255,0.1) !important;
        border: 2px solid #6c63ff !important;
        color: #e8e9ee !important;
        transition: all 0.3s !important;
    }

    div.stTextInput > div > div > input::placeholder {
        font-size: 3.5rem !important;     
        color: #ccc !important;
    }

    div.stTextInput > div > div > input:focus {
        border-color: #6c63ff !important;
        box-shadow: 0 0 20px rgba(108,99,255,0.4) !important;
    }

    /* Form Submit Button */
    section[data-testid="stForm"] button,
    .stForm button,
    button[kind="primaryFormSubmit"],
    form button {
        width: 100% !important;
        height: 10rem !important;
        min-height: 10rem !important;
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        padding: 2rem 3rem !important;
        border-radius: 12px !important;
        line-height: 1.2 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        background: linear-gradient(135deg, #6c63ff 0%, #8f7cff 100%) !important;
        color: white !important;
        border: none !important;
        transition: all 0.3s ease !important;
    }

    section[data-testid="stForm"] button *,
    .stForm button *,
    button[kind="primaryFormSubmit"] *,
    form button * {
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        line-height: 1.2 !important;
    }

    section[data-testid="stForm"] button:hover,
    button[kind="primaryFormSubmit"]:hover {
        transform: translateY(-6px) !important;
        box-shadow: 0 12px 35px rgba(108,99,255,0.6) !important;
    }

    /* Section Titles */
    .section-title {
        font-size: 5.5rem;
        font-weight: 800;
        color: #b3c7ff;
        text-shadow: 0 0 15px rgba(108,99,255,0.6);
        text-align: center;
        margin-bottom: 1rem;
    }

    /* Example Section */
    .example-section {
        background: linear-gradient(135deg, #2a2e75 0%, #412b79 100%);
        border-radius: 28px;
        padding: 3.5rem;
        margin: 3rem auto;
        width: 100%;
        box-shadow: 0 12px 45px rgba(0,0,0,0.4);
    }
    
    .example-title {
        color: #f1f2ff;
        font-size: 5.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 1rem;
    }

    /* Example Buttons */
    div.stButton > button {
        width: 100% !important;
        height: 12rem !important; 
        font-size: 3.5rem !important;
        font-weight: 600 !important;
        background: rgba(255,255,255,0.07) !important;
        border-radius: 18px !important;
        padding: 2rem !important;
        color: #d0d4ff !important;
        border: 2px solid transparent !important;
        transition: all 0.3s !important;
    }
    
    div.stButton > button:hover {
        background: linear-gradient(135deg, #6c63ff, #8f7cff) !important;
        color: #fff !important;
        transform: translateY(-6px) !important;
        box-shadow: 0 10px 30px rgba(108,99,255,0.5) !important;
    }

    div.stButton > button > div {
        font-size: 3.5rem !important; 
    }

    /* Response Card */
    .response-card {
        max-width: 100% !important;
        width: 100% !important;
        font-size: 3.7rem !important;
        line-height: 1.5 !important;
        padding: 3rem !important;
        border-radius: 15px !important;
        background: linear-gradient(135deg, #0a0f2c 0%, #111b3f 50%, #1f2b55 100%) !important;
        color: #FAFAFA !important;
        margin: 2rem 0 !important;
        box-shadow: 0 12px 40px rgba(0,0,0,0.4) !important;
    }
    
    .response-card h1, .response-card h2, .response-card h3, 
    .response-card h4, .response-card h5, .response-card h6 {
        color: #FFD700 !important;
        font-weight: 700 !important;
    }
    
    .response-card h1 {
        font-size: 5.7rem !important;
        line-height: 1.2 !important;
        margin-top: 2rem !important;
        margin-bottom: 1rem !important;
        font-weight: 800 !important;
    }
    
    .response-card h2 {
        font-size: 4.9rem !important;
        line-height: 1.2 !important;
        margin-top: 1.5rem !important;
        margin-bottom: 0.8rem !important;
        font-weight: 700 !important;
    }
    
    .response-card h3 {
        font-size: 4.5rem !important;
        line-height: 1.3 !important;
        margin-top: 1.2rem !important;
        margin-bottom: 0.6rem !important;
        font-weight: 600 !important;
    }
    
    .response-card h4 {
        font-size: 4.0rem !important;
        line-height: 1.3 !important;
        margin-top: 1rem !important;
        margin-bottom: 0.5rem !important;
        font-weight: 600 !important;
    }
    
    .response-card p {
        font-size: 3.7rem !important;
        line-height: 1.5 !important;
        margin-bottom: 0.8rem !important;
    }
    
    .response-card ul, .response-card ol {
        font-size: 3.5rem !important;
        line-height: 1.4 !important;
        margin-bottom: 1rem !important;
        padding-left: 2rem !important;
    }
    
    .response-card li {
        margin-bottom: 0.5rem !important;
        line-height: 1.6 !important;
    }
    
    .response-card strong {
        font-weight: 700 !important;
        color: #a8b3ff !important;
        font-size: 3.9rem !important;
    }

    /* Download Button */
    .stDownloadButton button {
        height: 8rem !important;
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        padding: 2rem 3rem !important;
        margin-top: 2rem !important;
        background: linear-gradient(135deg, #6c63ff 0%, #5a52d5 100%) !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(108, 99, 255, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    
    .stDownloadButton button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(108, 99, 255, 0.6) !important;
    }
    
    .stDownloadButton button p {
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        margin: 0 !important;
    }

    /* Success message */
    .success-message {
        background: rgba(40, 167, 69, 0.15);
        border-left: 7px solid #28a745;
        color: #9ee6a1;
        border-radius: 14px;
        padding: 1.8rem;
        font-size: 3.5rem;
        margin: 2rem 0;
    }

    /* Info boxes */
    div[style*="background: rgba(255, 255, 255, 0.08)"] {
        font-size: 3.5rem !important;
        line-height: 2 !important;
    }

    /* Footer */
    footer {
        background: none;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
    <div class="main-header">
        <h1>✈️ AI Travel Planner</h1>
        <p>Your intelligent companion for planning unforgettable journeys</p>
    </div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR (ABOUT SECTION) ----------------
with st.sidebar:
    st.markdown("<h1 style='text-align:center;font-size:5.7rem;margin-bottom:2rem;'>🎯 About</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="feature-card">
        <strong style='font-size:4rem;'>Powered by AI</strong><br><br>
        <span style='font-size:3.5rem;'>Get personalized travel recommendations using advanced AI technology.</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center;font-size:5.7rem;margin:3rem 0 2rem 0;'>✨ Features</h1>", unsafe_allow_html=True)
    features = [
        ("🗺️", "Custom Itineraries", "Day-by-day travel plans"),
        ("🏨", "Hotel Recommendations", "Best stays within budget"),
        ("🍽️", "Restaurant Suggestions", "Local cuisine hotspots"),
        ("💰", "Budget Planning", "Detailed cost breakdown"),
        ("🌤️", "Weather Forecasts", "Real-time weather info"),
        ("🚗", "Transportation", "Best travel modes")
    ]
    for icon, title, desc in features:
        st.markdown(f"""
        <div class="feature-card">
            <div style="font-size:4.5rem;margin-bottom:1.3rem;">{icon}</div>
            <div style="font-weight:800;font-size:4.0rem;margin-bottom:0.8rem;">{title}</div>
            <div style="font-size:3.5rem;opacity:0.9;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ---------------- MAIN CONTENT ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "last_response" not in st.session_state:
    st.session_state.last_response = None

st.markdown('<h1  class="section-title">📝 Plan Your Perfect Journey</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center;font-size:4rem;color:#ccc;margin-bottom:3.5rem;'>Tell us where you'd like to go, and we'll create an amazing itinerary just for you!</p>", unsafe_allow_html=True)
st.markdown("""
<div style='background: rgba(255, 255, 255, 0.08); border-radius: 20px; padding: 1.5rem; margin: 2rem 0; font-size: 3.5rem; line-height: 2; color: #e8e9ee;'>
    <p style='text-align: center;'>
    🌍 Welcome to AI Travel Planner - Your ultimate travel companion powered by artificial intelligence! Tell us your travel dreams, destination, budget, and duration, and watch as our intelligent system crafts a personalized itinerary just for you.
    </p>
</div>
""", unsafe_allow_html=True)

# Input form
with st.form(key="query_form", clear_on_submit=True):
    user_input = st.text_input(
        "Your Travel Query",
        placeholder="e.g., Plan a 5-day romantic trip to Paris with a budget of $2000 for 2 people",
        label_visibility="collapsed"
    )
    submit_button = st.form_submit_button("✨ Generate My Perfect Plan ✨")

# ---------------- EXAMPLES ----------------
examples = [
    "🗽 Plan a 7-day adventure trip to New York City",
    "🏖️ Budget-friendly 3-day weekend in Barcelona",
    "🗼 Family vacation to Tokyo for 5 days with kids",
    "🌴 Romantic honeymoon in Maldives for a week",
    "⛰️ Solo backpacking trip across Thailand",
    "🏛️ Cultural tour of Rome for 4 days"
]

st.markdown("""<div class="example-section">
    <div class="example-title">💡 Try These Popular Destinations</div>
    <p style='text-align:center;color:#d0d4ff;font-size:3.6rem;opacity:0.9;margin-bottom:2.5rem;'>
        Click any destination to get started instantly!
    </p>
</div>""", unsafe_allow_html=True)

cols = st.columns(3)
for idx, example in enumerate(examples):
    with cols[idx % 3]:
        if st.button(example, key=f"example_{idx}", use_container_width=True):
            st.session_state.clicked_example = example

st.markdown("""
<div style='background: rgba(255, 255, 255, 0.08); border-radius: 20px; padding: 1.5rem; margin: 2rem 0 2rem 0; font-size: 3.5rem; line-height: 2; color: #e8e9ee;'>
    <p style='text-align: center;'>
    ✈️ Our AI analyzes thousands of travel options to bring you customized recommendations for hotels, restaurants, attractions, and transportation. Whether you're seeking adventure, relaxation, or cultural immersion, we create detailed day-by-day itineraries optimized for your budget and preferences!
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- QUERY RESPONSE ----------------
if submit_button and user_input.strip():
    with st.spinner("🔮 Creating your perfect travel plan..."):
        try:
            payload = {"question": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload, timeout=120)
            if response.status_code == 200:
                answer = response.json().get("answer", "No answer returned.")
                st.session_state.last_response = answer
                st.session_state.messages.append({
                    "query": user_input,
                    "response": answer,
                    "timestamp": datetime.datetime.now()
                })
                st.markdown("<div class='success-message'>✅ Awesome! Your personalized travel plan is ready below!</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ Error: {response.text}")
        except requests.exceptions.Timeout:
            st.error("⏱️ Request timed out. Please try again.")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# ---------------- RESPONSE DISPLAY ----------------
if st.session_state.last_response:
    st.markdown(
        f'<div class="response-card">{st.session_state.last_response}</div>',
        unsafe_allow_html=True
    )
    
    st.download_button(
        label="📥 Download My Travel Plan",
        data=st.session_state.last_response,
        file_name=f"travel_plan_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
        mime="text/markdown",
        use_container_width=True
    )

# ---------------- FOOTER ----------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
    <div style="text-align:center;color:#ccc;padding:2.5rem;">
        <p style="font-size:3.5rem;">Made with ❤️ by <b>Navodit Sahai</b> | Powered by AI Technology</p>
        <p style="font-size:3.0rem;opacity:0.8;">© 2025 AI Travel Planner. Plan smart, travel better.</p>
    </div>
""", unsafe_allow_html=True)