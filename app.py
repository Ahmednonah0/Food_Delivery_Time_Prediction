import streamlit as st

st.set_page_config(
    page_title="Food Delivery Time Prediction",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 8% 10%, rgba(255, 122, 0, 0.12), transparent 25%),
        radial-gradient(circle at 92% 90%, rgba(82, 113, 255, 0.10), transparent 25%),
        linear-gradient(135deg, #070b12, #0d1520 55%, #111a27);
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {background: transparent !important;}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #080d15, #0d1520);
    border-right: 1px solid rgba(255,255,255,0.06);
}

@keyframes fadeUp {
    from {opacity:0; transform:translateY(30px);}
    to {opacity:1; transform:translateY(0);}
}

@keyframes float {
    0% {transform: translateY(0);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0);}
}

@keyframes glow {
    0% {box-shadow:0 0 10px rgba(255,110,0,.08);}
    50% {box-shadow:0 0 40px rgba(255,110,0,.25);}
    100% {box-shadow:0 0 10px rgba(255,110,0,.08);}
}

.hero {
    padding-top: 45px;
    animation: fadeUp .8s ease-out;
}

.badge {
    display:inline-block;
    color:#ff9b42;
    background:rgba(255,120,0,.10);
    border:1px solid rgba(255,120,0,.30);
    border-radius:30px;
    padding:8px 15px;
    font-size:12px;
    font-weight:800;
    letter-spacing:1.6px;
    margin-bottom:22px;
}

.hero-title {
    color:white;
    font-size:63px;
    line-height:1.04;
    font-weight:950;
    letter-spacing:-2px;
}

.gradient-text {
    background:linear-gradient(90deg,#ff7600,#ffae3d,#ff4e31);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero-desc {
    color:#9aa6b5;
    font-size:17px;
    max-width:690px;
    line-height:1.8;
    margin-top:20px;
}

.dev {
    color:#738091;
    font-size:14px;
    margin-top:18px;
}

.dev b {color:white;}

.visual {
    height:490px;
    border-radius:32px;
    border:1px solid rgba(255,255,255,.08);
    background:
        radial-gradient(circle at 50% 35%,rgba(255,120,0,.28),transparent 32%),
        linear-gradient(145deg,#151f2b,#090f18);
    display:flex;
    align-items:center;
    justify-content:center;
    flex-direction:column;
    animation:fadeUp .9s ease-out,float 5s ease-in-out 1s infinite;
    box-shadow:0 30px 75px rgba(0,0,0,.4);
}

.visual-circle {
    width:230px;
    height:230px;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:105px;
    background:linear-gradient(145deg,#ff9a23,#ff4d32);
    box-shadow:0 0 80px rgba(255,110,0,.35);
}

.visual-title {
    color:white;
    font-size:22px;
    font-weight:900;
    margin-top:28px;
}

.visual-sub {
    color:#8290a0;
    font-size:13px;
    margin-top:7px;
}

.section-label {
    text-align:center;
    color:#ff9138;
    font-size:12px;
    font-weight:850;
    letter-spacing:2px;
    margin-top:75px;
}

.section-title {
    text-align:center;
    color:white;
    font-size:37px;
    font-weight:950;
    margin-top:7px;
}

.section-desc {
    text-align:center;
    color:#7f8c9b;
    max-width:730px;
    margin:10px auto 35px auto;
    line-height:1.7;
}

.card {
    min-height:215px;
    border-radius:22px;
    padding:25px;
    border:1px solid rgba(255,255,255,.07);
    background:linear-gradient(145deg,rgba(255,255,255,.05),rgba(255,255,255,.015));
    transition:.25s;
    animation:fadeUp .8s ease-out;
}

.card:hover {
    transform:translateY(-7px);
    border-color:rgba(255,125,20,.4);
    box-shadow:0 20px 48px rgba(0,0,0,.25);
}

.icon {
    width:50px;
    height:50px;
    border-radius:15px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    margin-bottom:17px;
}

.icon-orange {background:rgba(255,125,20,.12);}
.icon-blue {background:rgba(65,120,255,.14);}
.icon-purple {background:rgba(150,80,255,.14);}
.icon-green {background:rgba(0,190,125,.14);}

.card-title {
    color:white;
    font-size:18px;
    font-weight:850;
}

.card-text {
    color:#82909e;
    font-size:13px;
    line-height:1.7;
    margin-top:8px;
}

.stat {
    text-align:center;
    padding:27px 15px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,.07);
    background:rgba(255,255,255,.03);
}

.stat-value {
    font-size:34px;
    font-weight:950;
}

.orange {color:#ff8a27;}
.blue {color:#42a5ff;}
.green {color:#00c78b;}
.purple {color:#b17cff;}

.stat-label {
    color:#748090;
    font-size:12px;
    margin-top:6px;
}

.cta {
    margin-top:70px;
    padding:47px 20px;
    border-radius:28px;
    text-align:center;
    border:1px solid rgba(255,125,20,.16);
    background:radial-gradient(circle,rgba(255,115,0,.13),rgba(255,255,255,.015));
    animation:glow 5s infinite;
}

.cta-title {
    color:white;
    font-size:30px;
    font-weight:950;
}

.cta-text {
    color:#84909f;
    margin-top:8px;
}

div.stButton > button {
    background:linear-gradient(90deg,#ff7700,#ff4d30);
    color:white;
    border:none;
    border-radius:14px;
    min-height:54px;
    font-weight:850;
    transition:.25s;
    box-shadow:0 12px 30px rgba(255,95,0,.25);
}

div.stButton > button:hover {
    transform:translateY(-3px);
    color:white;
    border:none;
}

.footer {
    text-align:center;
    color:#647181;
    border-top:1px solid rgba(255,255,255,.06);
    padding-top:25px;
    margin-top:65px;
    font-size:12px;
}

.footer b {color:#ff8b2c;}

</style>
""", unsafe_allow_html=True)

left, right = st.columns([1.1, .9], gap="large")

with left:
    st.markdown("""
<div class="hero">
<div class="badge">MACHINE LEARNING PROJECT</div>

<div class="hero-title">
Food Delivery Time<br>
<span class="gradient-text">Prediction System</span>
</div>

<div class="hero-desc">
An intelligent machine learning application that predicts
food delivery duration using customer, restaurant, order,
traffic, weather, distance and delivery partner information.
</div>

<div class="dev">
Designed & Developed by <b>Eng. Ahmed Adel</b>
</div>
</div>
""", unsafe_allow_html=True)

    st.write("")

    if st.button("Start Prediction →"):
        st.switch_page("pages/prediction.py")


with right:
    st.markdown("""
<div class="visual">
<div class="visual-circle">🛵</div>
<div class="visual-title">AI Delivery Intelligence</div>
<div class="visual-sub">Fast • Smart • Data Driven</div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="section-label">CORE FEATURES</div>
<div class="section-title">Explore the Complete ML System</div>
<div class="section-desc">
Predict delivery time, explore data patterns and evaluate
the machine learning models from one interactive dashboard.
</div>
""", unsafe_allow_html=True)


c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
<div class="card">
<div class="icon icon-orange">⚡</div>
<div class="card-title">Prediction</div>
<div class="card-text">
Generate instant delivery-time predictions using the trained XGBoost pipeline.
</div>
</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="card">
<div class="icon icon-blue">📊</div>
<div class="card-title">Data Insights</div>
<div class="card-text">
Explore delivery data through interactive and colorful visualizations.
</div>
</div>
""", unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="card">
<div class="icon icon-purple">🧠</div>
<div class="card-title">Model Analysis</div>
<div class="card-text">
Compare regression models using R², MAE and generalization performance.
</div>
</div>
""", unsafe_allow_html=True)

with c4:
    st.markdown("""
<div class="card">
<div class="icon icon-green">🚀</div>
<div class="card-title">Deployment</div>
<div class="card-text">
A complete Streamlit web application built around the final ML pipeline.
</div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="section-label">MODEL RESULTS</div>
<div class="section-title">Strong Validation Performance</div>
<div class="section-desc">
XGBoost achieved the strongest overall performance among
the regression models evaluated in the project.
</div>
""", unsafe_allow_html=True)


s1,s2,s3,s4 = st.columns(4)

with s1:
    st.markdown("""
<div class="stat">
<div class="stat-value orange">96.54%</div>
<div class="stat-label">TEST R²</div>
</div>
""", unsafe_allow_html=True)

with s2:
    st.markdown("""
<div class="stat">
<div class="stat-value blue">2.17</div>
<div class="stat-label">MAE MINUTES</div>
</div>
""", unsafe_allow_html=True)

with s3:
    st.markdown("""
<div class="stat">
<div class="stat-value purple">7</div>
<div class="stat-label">MODELS TESTED</div>
</div>
""", unsafe_allow_html=True)

with s4:
    st.markdown("""
<div class="stat">
<div class="stat-value green">XGBoost</div>
<div class="stat-label">BEST MODEL</div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="cta">
<div class="cta-title">Ready to Make a Prediction?</div>
<div class="cta-text">
Enter the delivery information and let the model estimate the expected duration.
</div>
</div>
""", unsafe_allow_html=True)

st.write("")

a,b,c = st.columns([1.3,1,1.3])

with b:
    if st.button("Make Prediction", use_container_width=True):
        st.switch_page("pages/prediction.py")


st.markdown("""
<div class="footer">
Food Delivery Time Prediction • Developed by <b>Eng. Ahmed Adel</b>
</div>
""", unsafe_allow_html=True)
st.markdown(
    '<div class="section-title">🧍 Customer & Location</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-sub">Customer and destination information</div>',
    unsafe_allow_html=True
)


c1, c2, c3 = st.columns(3)


with c1:

    customer_age = st.number_input(
        "Customer Age",
        16,
        100,
        30
    )


with c2:

    city = st.selectbox(
        "City",
        sorted(
            df["city"]
            .dropna()
            .unique()
            .tolist()
        )
    )


    delivery_area = st.selectbox(
        "Delivery Area",
        sorted(
            df["delivery_area"]
            .dropna()
            .unique()
            .tolist()
        )
    )


with c3:

    distance_km = st.number_input(
        "Distance (KM)",
        0.1,
        100.0,
        5.0,
        0.1
    )



st.markdown("<hr>", unsafe_allow_html=True)



# Restaurant Section

st.markdown(
    '<div class="section-title">🍽️ Restaurant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-sub">Restaurant characteristics</div>',
    unsafe_allow_html=True
)



r1, r2, r3 = st.columns(3)



with r1:

    restaurant_type = st.selectbox(
        "Restaurant Type",
        sorted(
            df["restaurant_type"]
            .dropna()
            .unique()
            .tolist()
        )
    )


    restaurant_primary_category = st.selectbox(
        "Restaurant Category",
        sorted(
            df["restaurant_primary_category"]
            .dropna()
            .unique()
            .tolist()
        )
    )



with r2:

    restaurant_rating = st.number_input(
        "Restaurant Rating",
        1.0,
        5.0,
        4.2,
        0.1
    )



with r3:

    restaurant_preparation_time_minutes = st.number_input(
        "Preparation Time (Minutes)",
        1.0,
        120.0,
        20.0
    )



st.markdown("<hr>", unsafe_allow_html=True)



# Order Details

st.markdown(
    '<div class="section-title">🧾 Order Details</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-sub">Order information</div>',
    unsafe_allow_html=True
)



items_count = st.number_input(
    "Items Count",
    1,
    100,
    3
)



st.markdown("<hr>", unsafe_allow_html=True)




# Environment

st.markdown(
    '<div class="section-title">🌦️ Environment</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="section-sub">Time, weather, traffic and driver information</div>',
    unsafe_allow_html=True
)



e1, e2, e3 = st.columns(3)



with e1:

    order_hour = st.slider(
        "Order Hour",
        0,
        23,
        18
    )


    day_of_week = st.selectbox(
        "Day",
        sorted(
            df["day_of_week"]
            .dropna()
            .unique()
            .tolist()
        )
    )



with e2:

    weather = st.selectbox(
        "Weather",
        sorted(
            df["weather"]
            .dropna()
            .unique()
            .tolist()
        )
    )


    traffic_level = st.selectbox(
        "Traffic Level",
        sorted(
            df["traffic_level"]
            .dropna()
            .unique()
            .tolist()
        )
    )



with e3:

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
        4.5,
        0.1
    )



estimated_delivery_time_minutes = st.number_input(
    "Platform Estimated Delivery Time",
    1.0,
    300.0,
    35.0
)



is_weekend = 1 if day_of_week in [
    "Friday",
    "Saturday"
] else 0
# Prepare input data

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

    "delivery_partner_experience_months":
        delivery_partner_experience_months,

    "delivery_partner_rating":
        delivery_partner_rating,

    "restaurant_preparation_time_minutes":
        restaurant_preparation_time_minutes,

    "estimated_delivery_time_minutes":
        estimated_delivery_time_minutes

}])



st.write("")


left, mid, right = st.columns(
    [1.2, 1.5, 1.2]
)



with mid:

    predict = st.button(
        "Predict Delivery Time ✨",
        use_container_width=True
    )



if predict:

    try:

        model = load_model()


        prediction = float(
            model.predict(input_data)[0]
        )


        low = max(
            0,
            prediction - 3
        )


        high = prediction + 3


        status, icon = get_delivery_status(
            prediction
        )



        st.markdown(
        f"""

<div class="result-card">


<div style="
color:#ffd4a6;
font-size:12px;
font-weight:900;
letter-spacing:2px;
">

PREDICTED DELIVERY TIME

</div>



<div class="result-number">

{prediction:.1f}

</div>



<div style="
color:white;
font-size:20px;
font-weight:800;
">

Minutes

</div>



<div style="
display:inline-block;
margin-top:16px;
padding:10px 18px;
border-radius:999px;
background:rgba(255,255,255,.07);
border:1px solid rgba(255,255,255,.10);
color:white;
font-weight:800;
">

{icon} {status}

</div>



<div style="
color:#9aa8b8;
margin-top:14px;
font-size:14px;
">

Expected Range:
{low:.0f} - {high:.0f} Minutes

</div>


</div>

""",
        unsafe_allow_html=True
        )



    except Exception as e:

        st.error(
            f"Prediction Error: {e}"
        )



st.markdown(
"""
<div style="
text-align:center;
margin-top:60px;
padding-top:25px;
border-top:1px solid rgba(255,255,255,.06);
color:#8090a0;
font-size:12px;
">

Food Delivery Time Prediction • Developed by

<b style="color:#ffb567;">
Eng. Ahmed Adel
</b>

</div>
""",
unsafe_allow_html=True
)
