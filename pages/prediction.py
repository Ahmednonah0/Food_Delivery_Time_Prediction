import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


st.set_page_config(
    page_title="Prediction",
    page_icon="🚚",
    layout="wide"
)


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "delivery_time_model.pkl"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


def get_delivery_status(prediction):
    if prediction <= 30:
        return "Fast Delivery", "⚡"
    elif prediction <= 50:
        return "Moderate Delivery", "🕒"
    else:
        return "Delayed Delivery", "🚨"


st.markdown("""
<style>
:root{
    --bg1:#071019;
    --bg2:#0d1724;
    --bg3:#111d2d;
    --card:rgba(255,255,255,0.05);
    --border:rgba(255,255,255,0.10);
    --text:#f5f7fb;
    --muted:#9aa8b8;
    --accent1:#ff8a00;
    --accent2:#ff5e3a;
    --accent3:#ffc76b;
    --blueGlow:rgba(77,129,255,.20);
    --orangeGlow:rgba(255,123,0,.20);
}

.stApp {
    background:
        radial-gradient(circle at 12% 15%, rgba(255,125,0,.16), transparent 22%),
        radial-gradient(circle at 88% 18%, rgba(61,114,255,.14), transparent 22%),
        radial-gradient(circle at 50% 100%, rgba(255,255,255,.03), transparent 32%),
        linear-gradient(135deg, var(--bg1), var(--bg2) 55%, var(--bg3));
    color: var(--text);
}

.block-container{
    max-width: 1400px;
    padding-top: 1.2rem;
    padding-bottom: 3rem;
}

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{background:transparent!important;}

section[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#09111c,#101927);
}

.hero-wrap{
    position: relative;
    overflow: hidden;
    border:1px solid rgba(255,255,255,.08);
    border-radius: 28px;
    padding: 34px 34px 28px 34px;
    background:
        linear-gradient(135deg, rgba(255,255,255,.06), rgba(255,255,255,.03)),
        radial-gradient(circle at 90% 20%, rgba(255,140,0,.20), transparent 25%),
        radial-gradient(circle at 12% 80%, rgba(77,129,255,.18), transparent 25%);
    box-shadow:
        0 10px 30px rgba(0,0,0,.18),
        inset 0 1px 0 rgba(255,255,255,.04);
    margin-bottom: 22px;
}

.hero-grid{
    display:grid;
    grid-template-columns: 1.35fr .65fr;
    gap: 22px;
    align-items:center;
}

.badge{
    display:inline-block;
    padding:8px 14px;
    border-radius:999px;
    font-size:12px;
    font-weight:800;
    letter-spacing:1.5px;
    color:#ffd5a0;
    background:rgba(255,140,0,.12);
    border:1px solid rgba(255,163,72,.18);
    margin-bottom:14px;
}

.hero-title{
    margin:0;
    font-size:52px;
    line-height:1.05;
    font-weight:950;
    color:white;
}

.hero-title .gradient{
    background:linear-gradient(90deg,var(--accent1),var(--accent3),var(--accent2));
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero-desc{
    margin-top:14px;
    max-width:760px;
    color:var(--muted);
    font-size:15px;
    line-height:1.8;
}

.hero-pills{
    display:flex;
    flex-wrap:wrap;
    gap:10px;
    margin-top:18px;
}

.pill{
    padding:10px 14px;
    border-radius:14px;
    font-size:13px;
    color:#eef3fb;
    background:rgba(255,255,255,.05);
    border:1px solid rgba(255,255,255,.08);
}

.hero-visual{
    min-height:220px;
    display:flex;
    align-items:center;
    justify-content:center;
    position:relative;
}

.glow-ring{
    width:180px;
    height:180px;
    border-radius:50%;
    background:
        radial-gradient(circle at 30% 30%, rgba(255,199,107,.55), rgba(255,94,58,.22) 50%, rgba(61,114,255,.08) 72%, transparent 74%);
    filter: blur(0.5px);
    box-shadow:
        0 0 50px rgba(255,140,0,.25),
        0 0 90px rgba(61,114,255,.16);
    display:flex;
    align-items:center;
    justify-content:center;
    animation:floaty 4s ease-in-out infinite;
}

.truck-badge{
    width:120px;
    height:120px;
    border-radius:28px;
    background:rgba(255,255,255,.07);
    border:1px solid rgba(255,255,255,.12);
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:56px;
    backdrop-filter: blur(14px);
    box-shadow: inset 0 1px 0 rgba(255,255,255,.05);
}

@keyframes floaty{
    0%{transform:translateY(0px);}
    50%{transform:translateY(-10px);}
    100%{transform:translateY(0px);}
}

.section-title{
    font-size:24px;
    font-weight:900;
    color:white;
    margin-top:16px;
    margin-bottom:4px;
}

.section-sub{
    color:var(--muted);
    font-size:13px;
    margin-bottom:12px;
}

.card-note{
    padding:14px 16px;
    border-radius:16px;
    background:rgba(255,255,255,.04);
    border:1px solid rgba(255,255,255,.08);
    color:var(--muted);
    font-size:13px;
    margin-bottom:18px;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input{
    background: rgba(255,255,255,.07)!important;
    color: white!important;
    border-radius: 14px!important;
    border: 1px solid rgba(255,255,255,.10)!important;
}

div[data-baseweb="select"] *{
    color:white!important;
}

label, .stMarkdown, .stText, .st-emotion-cache-16txtl3{
    color: white!important;
}

div.stButton > button{
    width:100%;
    min-height:58px;
    border:none;
    border-radius:16px;
    font-weight:900;
    font-size:16px;
    color:white;
    background:linear-gradient(90deg,var(--accent1),var(--accent2));
    box-shadow:0 10px 30px rgba(255,120,0,.25);
    transition:.25s ease;
}

div.stButton > button:hover{
    transform:translateY(-2px);
    box-shadow:0 12px 34px rgba(255,120,0,.33);
    color:white;
}

.result-card{
    margin-top:26px;
    padding:34px 28px;
    border-radius:28px;
    border:1px solid rgba(255,255,255,.10);
    background:
        linear-gradient(135deg, rgba(255,255,255,.06), rgba(255,255,255,.03)),
        radial-gradient(circle at top, rgba(255,123,0,.20), transparent 40%),
        radial-gradient(circle at bottom right, rgba(77,129,255,.16), transparent 35%);
    box-shadow: 0 18px 45px rgba(0,0,0,.20);
    text-align:center;
}

.result-kicker{
    color:#ffd4a6;
    font-size:12px;
    font-weight:900;
    letter-spacing:2px;
}

.result-number{
    font-size:86px;
    line-height:1;
    font-weight:950;
    margin-top:10px;
    color:#ffb35a;
}

.result-unit{
    color:white;
    font-size:20px;
    font-weight:800;
    margin-top:8px;
}

.result-status{
    display:inline-block;
    margin-top:16px;
    padding:10px 16px;
    border-radius:999px;
    color:white;
    font-size:14px;
    font-weight:800;
    background:rgba(255,255,255,.07);
    border:1px solid rgba(255,255,255,.10);
}

.result-range{
    color:var(--muted);
    margin-top:12px;
    font-size:14px;
}

.small-footer{
    margin-top:26px;
    text-align:center;
    color:#8090a0;
    font-size:12px;
}

.small-footer b{
    color:#ffb567;
}

div[data-testid="stSlider"] *{
    color:white!important;
}

hr{
    border:none;
    height:1px;
    background:rgba(255,255,255,.08);
    margin:1.2rem 0;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero-wrap">
    <div class="hero-grid">
        <div>
            <div class="badge">AI DELIVERY INTELLIGENCE</div>
            <h1 class="hero-title">
                Delivery Time <span class="gradient">Prediction</span>
            </h1>
            <div class="hero-desc">
                Estimate expected delivery duration using a trained XGBoost model.
                Fill in the order, restaurant, and environment details to get a
                real-time prediction with a clean premium dashboard experience.
            </div>
            <div class="hero-pills">
                <div class="pill">⚙️ XGBoost Model</div>
                <div class="pill">📊 18 Input Features</div>
                <div class="pill">⚡ Real-time Prediction</div>
            </div>
        </div>
        <div class="hero-visual">
            <div class="glow-ring">
                <div class="truck-badge">🚚</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


st.markdown('<div class="section-title">🧍 Customer & Location</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Basic customer and destination information</div>', unsafe_allow_html=True)

c2, c3 = st.columns(2)

with c2:
    city = st.selectbox("City", ["City_A", "City_B", "City_C", "City_D"])
     delivery_area = st.selectbox(
    "Delivery Area",
    [
        "Area_1",
        "Area_2",
        "Area_3",
        "Area_4",
        "Area_5"
    ]
)

with c3:
    distance_km = st.number_input("Distance (KM)", 0.1, 100.0, 5.0, 0.1)

st.markdown("<hr>", unsafe_allow_html=True)


st.markdown('<div class="section-title">🍽️ Restaurant</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Restaurant characteristics that affect preparation and service</div>', unsafe_allow_html=True)

r1, r2, r3 = st.columns(3)

with r1:
    restaurant_type = st.selectbox(
        "Restaurant Type",
        ["Fast Food", "Casual Dining", "Cafe", "Fine Dining"]
    )
    restaurant_primary_category = st.selectbox(
        "Restaurant Category",
        ["Burger", "Pizza", "Asian", "Local", "Healthy", "Dessert"]
    )

with r2:
    restaurant_rating = st.number_input("Restaurant Rating", 1.0, 5.0, 4.2, 0.1)

with r3:
    restaurant_preparation_time_minutes = st.number_input("Preparation Time", 1.0, 120.0, 20.0)

st.markdown("<hr>", unsafe_allow_html=True)


st.markdown('<div class="section-title">🧾 Order Details</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Order size information</div>', unsafe_allow_html=True)

o1 = st.columns(1)[0]

with o1:
    items_count = st.number_input("Items Count", 1, 100, 3)

st.markdown("<hr>", unsafe_allow_html=True)


st.markdown('<div class="section-title">🌦️ Environment</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Time, weather, traffic, and driver details</div>', unsafe_allow_html=True)

e1, e2, e3 = st.columns(3)

with e1:
    order_hour = st.slider("Order Hour", 0, 23, 18)
    day_of_week = st.selectbox(
        "Day",
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    )

with e2:
    weather = st.selectbox("Weather", ["Clear", "Cloudy", "Rain", "Storm"])
    traffic_level = st.selectbox("Traffic", ["Low", "Medium", "High"])

with e3:
    delivery_partner_experience_months = st.number_input("Driver Experience (Months)", 0, 300, 24)
    delivery_partner_rating = st.number_input("Driver Rating", 1.0, 5.0, 4.5, 0.1)

estimated_delivery_time_minutes = st.number_input(
    "Platform Estimated Delivery Time",
    1.0,
    300.0,
    35.0
)

is_weekend = 1 if day_of_week in ["Friday", "Saturday"] else 0

input_data = pd.DataFrame([{
    "order_hour": order_hour,
    "day_of_week": day_of_week,
    "is_weekend": is_weekend,
    "city": city,
    "delivery_area": delivery_area,
    "restaurant_type": restaurant_type,
    "restaurant_primary_category": restaurant_primary_category,
    "restaurant_rating": restaurant_rating,
    "items_count": items_count,
    "distance_km": distance_km,
    "weather": weather,
    "traffic_level": traffic_level,
    "delivery_partner_experience_months": delivery_partner_experience_months,
    "delivery_partner_rating": delivery_partner_rating,
    "restaurant_preparation_time_minutes": restaurant_preparation_time_minutes,
    "estimated_delivery_time_minutes": estimated_delivery_time_minutes
}])

st.write("")
_, mid, _ = st.columns([1.1, 1.4, 1.1])

with mid:
    predict = st.button("Predict Delivery Time ✨", use_container_width=True)

if predict:
    try:
        model = load_model()
        prediction = float(model.predict(input_data)[0])

        low = max(0, prediction - 3)
        high = prediction + 3
        status, icon = get_delivery_status(prediction)

        st.markdown(f"""
        <div class="result-card">
            <div class="result-kicker">PREDICTED DELIVERY TIME</div>
            <div class="result-number">{prediction:.1f}</div>
            <div class="result-unit">Minutes</div>
            <div class="result-status">{icon} {status}</div>
            <div class="result-range">Expected range: {low:.0f} – {high:.0f} minutes</div>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Prediction error: {e}")

st.markdown("""
<div class="small-footer">
    Food Delivery Time Prediction • Developed by <b>Eng. Ahmed Adel</b>
</div>
""", unsafe_allow_html=True)
