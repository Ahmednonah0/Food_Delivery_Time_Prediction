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
    return "Delayed Delivery", "🚨"


# =========================
# Styling
# =========================

st.markdown("""
<style>

:root {
    --bg1: #071019;
    --bg2: #0d1724;
    --bg3: #121d2a;
    --orange1: #ff8a00;
    --orange2: #ff5a36;
    --orange3: #ffc56b;
    --text: #f4f7fb;
    --muted: #96a4b4;
}

.stApp {
    background:
        radial-gradient(circle at 8% 8%, rgba(255,130,0,.15), transparent 24%),
        radial-gradient(circle at 92% 90%, rgba(67,103,255,.13), transparent 27%),
        linear-gradient(135deg, var(--bg1), var(--bg2) 55%, var(--bg3));
}

.block-container {
    max-width: 1400px;
    padding-top: 1.2rem;
    padding-bottom: 4rem;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #080e17, #101927);
    border-right: 1px solid rgba(255,255,255,.06);
}


/* =========================
   Hero
   ========================= */

.hero {
    position: relative;
    overflow: hidden;
    padding: 38px;
    border-radius: 30px;

    background:
        radial-gradient(circle at 85% 30%, rgba(255,136,0,.20), transparent 25%),
        radial-gradient(circle at 15% 90%, rgba(65,105,255,.15), transparent 25%),
        linear-gradient(
            135deg,
            rgba(255,255,255,.065),
            rgba(255,255,255,.025)
        );

    border: 1px solid rgba(255,255,255,.09);

    box-shadow:
        0 20px 60px rgba(0,0,0,.28),
        inset 0 1px rgba(255,255,255,.04);

    margin-bottom: 28px;
}

.hero-grid {
    display: grid;
    grid-template-columns: 1.25fr .75fr;
    gap: 20px;
    align-items: center;
}

.hero-badge {
    display: inline-block;
    padding: 8px 15px;
    border-radius: 999px;

    background: rgba(255,135,0,.11);
    border: 1px solid rgba(255,160,65,.22);

    color: #ffd3a2;

    font-size: 12px;
    font-weight: 900;
    letter-spacing: 1.7px;

    margin-bottom: 18px;
}

.hero-title {
    color: white;
    font-size: 52px;
    line-height: 1.05;
    font-weight: 950;
    margin: 0;
}

.gradient-text {
    background:
        linear-gradient(
            90deg,
            var(--orange1),
            var(--orange3),
            var(--orange2)
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-desc {
    color: var(--muted);
    max-width: 760px;
    line-height: 1.8;
    font-size: 15px;
    margin-top: 15px;
}

.hero-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 20px;
}

.hero-pill {
    padding: 10px 14px;
    border-radius: 14px;

    background: rgba(255,255,255,.05);
    border: 1px solid rgba(255,255,255,.08);

    color: #eef3fb;
    font-size: 13px;
}

.hero-visual {
    display: flex;
    align-items: center;
    justify-content: center;
}

.delivery-orb {
    width: 190px;
    height: 190px;

    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    background:
        radial-gradient(
            circle at 30% 25%,
            #ffc469,
            #ff7d22 43%,
            #ff4f37 70%
        );

    box-shadow:
        0 0 55px rgba(255,125,0,.30),
        0 0 110px rgba(67,100,255,.13);

    animation: floating 4s ease-in-out infinite;
}

.delivery-box {
    width: 125px;
    height: 125px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 30px;

    background: rgba(8,15,24,.40);
    border: 1px solid rgba(255,255,255,.15);

    backdrop-filter: blur(10px);

    font-size: 60px;
}

@keyframes floating {
    0% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-10px);
    }

    100% {
        transform: translateY(0);
    }
}


/* =========================
   Section headings
   ========================= */

.section-head {
    margin-top: 32px;
    margin-bottom: 17px;

    padding: 18px 20px;

    border-left: 4px solid #ff8524;
    border-radius: 0 18px 18px 0;

    background:
        linear-gradient(
            90deg,
            rgba(255,130,0,.08),
            rgba(255,255,255,.02)
        );
}

.section-title {
    color: white;
    font-size: 23px;
    font-weight: 900;
}

.section-desc {
    color: #8492a2;
    font-size: 13px;
    margin-top: 4px;
}


/* =========================
   Inputs
   ========================= */

label {
    color: #f1f4f8 !important;
    font-weight: 700 !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
div[data-testid="stNumberInput"] input {
    background: rgba(255,255,255,.07) !important;

    border:
        1px solid rgba(255,255,255,.10) !important;

    border-radius: 14px !important;

    color: white !important;
}

div[data-baseweb="select"] * {
    color: white !important;
}

div[data-testid="stSlider"] * {
    color: white !important;
}


/* =========================
   Button
   ========================= */

div.stButton > button {
    width: 100%;
    min-height: 60px;

    border: none;
    border-radius: 17px;

    background:
        linear-gradient(
            90deg,
            #ff9700,
            #ff6833,
            #ff4e3b
        );

    color: white;

    font-size: 16px;
    font-weight: 900;

    box-shadow:
        0 12px 32px rgba(255,100,0,.25);

    transition: all .25s ease;
}

div.stButton > button:hover {
    transform: translateY(-3px);

    color: white;

    box-shadow:
        0 16px 38px rgba(255,100,0,.34);
}


/* =========================
   Result
   ========================= */

.result-card {
    margin-top: 35px;

    padding: 40px;

    border-radius: 30px;

    text-align: center;

    background:
        radial-gradient(
            circle at top,
            rgba(255,130,0,.20),
            transparent 40%
        ),
        radial-gradient(
            circle at bottom right,
            rgba(68,105,255,.16),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            rgba(255,255,255,.06),
            rgba(255,255,255,.025)
        );

    border:
        1px solid rgba(255,255,255,.10);

    box-shadow:
        0 20px 50px rgba(0,0,0,.25);
}

.result-label {
    color: #ffd2a1;

    font-size: 12px;
    font-weight: 900;
    letter-spacing: 2px;
}

.result-number {
    color: #ffb353;

    font-size: 88px;
    font-weight: 950;

    line-height: 1;

    margin-top: 15px;
}

.result-unit {
    color: white;

    font-size: 20px;
    font-weight: 800;

    margin-top: 8px;
}

.status-pill {
    display: inline-block;

    margin-top: 18px;

    padding: 10px 18px;

    border-radius: 999px;

    background: rgba(255,255,255,.07);

    border:
        1px solid rgba(255,255,255,.10);

    color: white;

    font-weight: 800;
}


/* =========================
   Footer
   ========================= */

.footer {
    margin-top: 60px;
    padding-top: 22px;

    border-top:
        1px solid rgba(255,255,255,.06);

    text-align: center;

    color: #718091;

    font-size: 12px;
}

.footer b {
    color: #ffad55;
}

</style>
""", unsafe_allow_html=True)


# =========================
# Hero
# =========================

st.markdown("""
<div class="hero">

<div class="hero-grid">

<div>

<div class="hero-badge">
AI DELIVERY INTELLIGENCE
</div>

<div class="hero-title">
Delivery Time
<span class="gradient-text">Prediction</span>
</div>

<div class="hero-desc">
Enter real delivery conditions and let the trained XGBoost
machine learning pipeline estimate the expected delivery duration.
</div>

<div class="hero-pills">

<div class="hero-pill">
🧠 XGBoost Model
</div>

<div class="hero-pill">
⚡ Real-Time Prediction
</div>

<div class="hero-pill">
📊 Data Driven
</div>

</div>

</div>


<div class="hero-visual">

<div class="delivery-orb">

<div class="delivery-box">
🛵
</div>

</div>

</div>

</div>

</div>
""", unsafe_allow_html=True)


# =========================
# Customer & Location
# =========================

st.markdown("""
<div class="section-head">

<div class="section-title">
📍 Customer & Location
</div>

<div class="section-desc">
Customer profile and delivery destination.
</div>

</div>
""", unsafe_allow_html=True)


c1, c2, c3 = st.columns(3)


with c1:

    customer_age = st.number_input(
        "👤 Customer Age",
        16,
        100,
        30
    )


with c2:

    city = st.selectbox(
        "🏙️ City",
        [
            "City_A",
            "City_B",
            "City_C",
            "City_D"
        ]
    )


with c3:

    distance_km = st.number_input(
        "📏 Distance (KM)",
        0.1,
        100.0,
        5.0
    )


area_options = {

    "City_A": [
        f"City_A_Area_{i}"
        for i in range(1, 11)
    ],

    "City_B": [
        f"City_B_Area_{i}"
        for i in range(1, 11)
    ],

    "City_C": [
        f"City_C_Area_{i}"
        for i in range(1, 11)
    ],

    "City_D": [
        f"City_D_Area_{i}"
        for i in range(1, 11)
    ],

}


delivery_area = st.selectbox(
    "🗺️ Delivery Area",
    area_options[city]
)


# =========================
# Restaurant
# =========================

st.markdown("""
<div class="section-head">

<div class="section-title">
🍽️ Restaurant Information
</div>

<div class="section-desc">
Restaurant type, category, rating and preparation time.
</div>

</div>
""", unsafe_allow_html=True)


r1, r2, r3, r4 = st.columns(4)


with r1:

    restaurant_type = st.selectbox(
        "🏪 Restaurant Type",
        [
            "Fast Food",
            "Casual Dining",
            "Cafe",
            "Fine Dining"
        ]
    )


with r2:

    restaurant_primary_category = st.selectbox(
        "🍔 Restaurant Category",
        [
            "Burger",
            "Pizza",
            "Asian",
            "Local",
            "Healthy",
            "Dessert"
        ]
    )


with r3:

    restaurant_rating = st.number_input(
        "⭐ Restaurant Rating",
        1.0,
        5.0,
        4.2
    )


with r4:

    restaurant_preparation_time_minutes = st.number_input(
        "⏱️ Preparation Time",
        1.0,
        120.0,
        20.0
    )


# =========================
# Order Details
# =========================

st.markdown("""
<div class="section-head">

<div class="section-title">
🛍️ Order Details
</div>

<div class="section-desc">
Information related to the current customer order.
</div>

</div>
""", unsafe_allow_html=True)


items_count = st.number_input(
    "📦 Items Count",
    1,
    100,
    3
)


# =========================
# Environment
# =========================

st.markdown("""
<div class="section-head">

<div class="section-title">
🌦️ Delivery Environment
</div>

<div class="section-desc">
Time, traffic, weather and delivery partner conditions.
</div>

</div>
""", unsafe_allow_html=True)


e1, e2, e3 = st.columns(3)


with e1:

    order_hour = st.slider(
        "🕐 Order Hour",
        0,
        23,
        18
    )


    day_of_week = st.selectbox(
        "📅 Day",
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
    )


with e2:

    weather = st.selectbox(
        "🌤️ Weather",
        [
            "Clear",
            "Cloudy",
            "Rain",
            "Storm"
        ]
    )


    traffic_level = st.selectbox(
        "🚦 Traffic",
        [
            "Low",
            "Medium",
            "High"
        ]
    )


with e3:

    delivery_partner_experience_months = st.number_input(
        "🛵 Driver Experience (Months)",
        0,
        300,
        24
    )


    delivery_partner_rating = st.number_input(
        "⭐ Driver Rating",
        1.0,
        5.0,
        4.5
    )


estimated_delivery_time_minutes = st.number_input(
    "📱 Platform Estimated Delivery Time",
    1.0,
    300.0,
    35.0
)


# =========================
# Prepare model input
# =========================

is_weekend = (
    1
    if day_of_week in ["Friday", "Saturday"]
    else 0
)


input_data = pd.DataFrame([{

    "order_hour": order_hour,

    "day_of_week": day_of_week,

    "is_weekend": is_weekend,

    "city": city,

    "delivery_area": delivery_area,

    "customer_age": customer_age,

    "restaurant_type": restaurant_type,

    "restaurant_primary_category":
        restaurant_primary_category,

    "restaurant_rating":
        restaurant_rating,

    "items_count":
        items_count,

    "distance_km":
        distance_km,

    "weather":
        weather,

    "traffic_level":
        traffic_level,

    "delivery_partner_experience_months":
        delivery_partner_experience_months,

    "delivery_partner_rating":
        delivery_partner_rating,

    "restaurant_preparation_time_minutes":
        restaurant_preparation_time_minutes,

    "estimated_delivery_time_minutes":
        estimated_delivery_time_minutes

}])


# =========================
# Prediction Button
# =========================

st.write("")
st.write("")


left, middle, right = st.columns(
    [1.15, 1.5, 1.15]
)


with middle:

    predict = st.button(
        "🚀 Predict Delivery Time",
        use_container_width=True
    )


# =========================
# Prediction
# =========================

if predict:

    try:

        model = load_model()

        prediction = float(
            model.predict(input_data)[0]
        )

        status, icon = get_delivery_status(
            prediction
        )


        st.markdown(
            f"""
<div class="result-card">

<div class="result-label">
AI PREDICTION RESULT
</div>

<div class="result-number">
{prediction:.1f}
</div>

<div class="result-unit">
Minutes
</div>

<div class="status-pill">
{icon} {status}
</div>

</div>
""",
            unsafe_allow_html=True
        )


    except Exception as e:

        st.error(
            f"Prediction error: {e}"
        )


# =========================
# Footer
# =========================

st.markdown("""
<div class="footer">

Food Delivery Time Prediction
•
Developed by
<b>Eng. Ahmed Adel</b>

</div>
""", unsafe_allow_html=True)
