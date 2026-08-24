
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


# ---------------- UI ----------------

st.title("🚚 Delivery Time Prediction")

st.write(
    "Enter delivery information and the XGBoost model will estimate delivery time."
)


customer_age = st.number_input("Customer Age", 16, 100, 30)

city = st.selectbox(
    "City",
    [
        "City_A",
        "City_B",
        "City_C",
        "City_D"
    ]
)


area_options = {
    "City_A": [f"City_A_Area_{i}" for i in range(1, 11)],
    "City_B": [f"City_B_Area_{i}" for i in range(1, 11)],
    "City_C": [f"City_C_Area_{i}" for i in range(1, 11)],
    "City_D": [f"City_D_Area_{i}" for i in range(1, 11)],
}


delivery_area = st.selectbox(
    "Delivery Area",
    area_options[city]
)


distance_km = st.number_input(
    "Distance (KM)",
    0.1,
    100.0,
    5.0
)


restaurant_type = st.selectbox(
    "Restaurant Type",
    [
        "Fast Food",
        "Casual Dining",
        "Cafe",
        "Fine Dining"
    ]
)


restaurant_primary_category = st.selectbox(
    "Restaurant Category",
    [
        "Burger",
        "Pizza",
        "Asian",
        "Local",
        "Healthy",
        "Dessert"
    ]
)


restaurant_rating = st.number_input(
    "Restaurant Rating",
    1.0,
    5.0,
    4.2
)


items_count = st.number_input(
    "Items Count",
    1,
    100,
    3
)


order_hour = st.slider(
    "Order Hour",
    0,
    23,
    18
)


day_of_week = st.selectbox(
    "Day",
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


weather = st.selectbox(
    "Weather",
    [
        "Clear",
        "Cloudy",
        "Rain",
        "Storm"
    ]
)


traffic_level = st.selectbox(
    "Traffic",
    [
        "Low",
        "Medium",
        "High"
    ]
)


delivery_partner_experience_months = st.number_input(
    "Driver Experience (Months)",
    0,
    300,
    24
)


delivery_partner_rating = st.number_input(
    "Driver Rating",
    1.0,
    5.0,
    4.5
)


restaurant_preparation_time_minutes = st.number_input(
    "Preparation Time",
    1.0,
    120.0,
    20.0
)


estimated_delivery_time_minutes = st.number_input(
    "Estimated Delivery Time",
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
    "customer_age": customer_age,
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


if st.button("Predict Delivery Time ✨"):

    try:
        model = load_model()

        prediction = float(
            model.predict(input_data)[0]
        )

        status, icon = get_delivery_status(prediction)

        st.success(
            f"{icon} {status}: {prediction:.1f} Minutes"
        )

    except Exception as e:
        st.error(f"Prediction error: {e}")
