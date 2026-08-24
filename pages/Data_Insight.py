import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


st.set_page_config(
    page_title="Data Insights",
    page_icon="📊",
    layout="wide"
)


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "food_delivery_orders_dataset.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df.columns = df.columns.str.strip().str.lower()
    return df


df = load_data()


st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 10%,rgba(255,115,0,.10),transparent 25%),
        radial-gradient(circle at 90% 90%,rgba(70,110,255,.09),transparent 25%),
        linear-gradient(135deg,#070b12,#0d1520 60%,#111a27);
}

.block-container {
    max-width:1450px;
    padding-top:2rem;
    padding-bottom:4rem;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {background:transparent!important;}

section[data-testid="stSidebar"] {
    background:linear-gradient(180deg,#080d15,#0d1520);
}

.header {
    text-align:center;
    margin-bottom:38px;
}

.label {
    color:#ff9138;
    font-size:12px;
    font-weight:850;
    letter-spacing:2px;
}

.title {
    color:white;
    font-size:48px;
    font-weight:950;
    margin-top:8px;
}

.gradient {
    background:linear-gradient(90deg,#ff7600,#ffac3d,#ff4e31);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.desc {
    color:#84909f;
    font-size:14px;
    line-height:1.7;
    max-width:760px;
    margin:10px auto 0 auto;
}

.kpi {
    border-radius:20px;
    padding:22px;
    min-height:135px;
    border:1px solid rgba(255,255,255,.07);
    background:linear-gradient(145deg,rgba(255,255,255,.05),rgba(255,255,255,.015));
}

.kpi-label {
    color:#7d8998;
    font-size:12px;
    letter-spacing:1px;
    font-weight:800;
}

.kpi-value {
    font-size:35px;
    font-weight:950;
    margin-top:10px;
}

.orange {color:#ff8b2c;}
.blue {color:#42a5ff;}
.green {color:#00c78b;}
.purple {color:#b17cff;}

.section {
    color:white;
    font-size:24px;
    font-weight:900;
    margin-top:42px;
}

.section-sub {
    color:#7f8c9b;
    font-size:13px;
    margin-bottom:15px;
}

.footer {
    text-align:center;
    margin-top:65px;
    padding-top:25px;
    border-top:1px solid rgba(255,255,255,.06);
    color:#657181;
    font-size:12px;
}

.footer b {color:#ff8b2c;}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="header">
<div class="label">EXPLORATORY DATA ANALYSIS</div>
<div class="title">
Delivery Data <span class="gradient">Insights</span>
</div>
<div class="desc">
Explore patterns and relationships affecting actual food delivery duration.
</div>
</div>
""", unsafe_allow_html=True)


df = df.dropna(subset=["actual_delivery_time_minutes"])


total_orders = len(df)
avg_delivery = df["actual_delivery_time_minutes"].mean()
avg_distance = df["distance_km"].mean()
avg_rating = df["restaurant_rating"].mean()


k1,k2,k3,k4 = st.columns(4)

with k1:
    st.markdown(f"""
<div class="kpi">
<div class="kpi-label">TOTAL ORDERS</div>
<div class="kpi-value orange">{total_orders:,}</div>
</div>
""", unsafe_allow_html=True)

with k2:
    st.markdown(f"""
<div class="kpi">
<div class="kpi-label">AVG DELIVERY</div>
<div class="kpi-value blue">{avg_delivery:.1f} min</div>
</div>
""", unsafe_allow_html=True)

with k3:
    st.markdown(f"""
<div class="kpi">
<div class="kpi-label">AVG DISTANCE</div>
<div class="kpi-value green">{avg_distance:.1f} km</div>
</div>
""", unsafe_allow_html=True)

with k4:
    st.markdown(f"""
<div class="kpi">
<div class="kpi-label">AVG RATING</div>
<div class="kpi-value purple">{avg_rating:.2f}</div>
</div>
""", unsafe_allow_html=True)


def style_chart(fig):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#aab5c3"),
        title_font=dict(color="white",size=18),
        margin=dict(l=20,r=20,t=55,b=20)
    )

    fig.update_xaxes(
        gridcolor="rgba(255,255,255,.05)"
    )

    fig.update_yaxes(
        gridcolor="rgba(255,255,255,.05)"
    )

    return fig


st.markdown('<div class="section">Delivery Distribution</div>',unsafe_allow_html=True)
st.markdown('<div class="section-sub">Distribution of actual delivery duration</div>',unsafe_allow_html=True)

fig1 = px.histogram(
    df,
    x="actual_delivery_time_minutes",
    nbins=35,
    color_discrete_sequence=["#ff7a00"],
    title="Delivery Time Distribution"
)

st.plotly_chart(
    style_chart(fig1),
    use_container_width=True
)


st.markdown('<div class="section">Distance Impact</div>',unsafe_allow_html=True)
st.markdown('<div class="section-sub">Distance vs actual delivery duration</div>',unsafe_allow_html=True)

fig2 = px.scatter(
    df,
    x="distance_km",
    y="actual_delivery_time_minutes",
    color="traffic_level",
    color_discrete_map={
        "Low":"#00c78b",
        "Medium":"#ffb020",
        "High":"#ff4d4f"
    },
    opacity=.55,
    title="Distance vs Delivery Time"
)

st.plotly_chart(
    style_chart(fig2),
    use_container_width=True
)


c1,c2 = st.columns(2)

with c1:

    traffic = (
        df.groupby("traffic_level",as_index=False)
        ["actual_delivery_time_minutes"]
        .mean()
    )

    fig3 = px.bar(
        traffic,
        x="traffic_level",
        y="actual_delivery_time_minutes",
        color="traffic_level",
        color_discrete_map={
            "Low":"#00c78b",
            "Medium":"#ffb020",
            "High":"#ff4d4f"
        },
        title="Average Delivery Time by Traffic"
    )

    st.plotly_chart(
        style_chart(fig3),
        use_container_width=True
    )


with c2:

    weather = (
        df.groupby("weather",as_index=False)
        ["actual_delivery_time_minutes"]
        .mean()
    )

    fig4 = px.bar(
        weather,
        x="weather",
        y="actual_delivery_time_minutes",
        color="weather",
        color_discrete_sequence=[
            "#42a5ff",
            "#7e57c2",
            "#26c6da",
            "#ef5350"
        ],
        title="Average Delivery Time by Weather"
    )

    st.plotly_chart(
        style_chart(fig4),
        use_container_width=True
    )


st.markdown('<div class="section">Restaurant Preparation</div>',unsafe_allow_html=True)

fig5 = px.scatter(
    df,
    x="restaurant_preparation_time_minutes",
    y="actual_delivery_time_minutes",
    color="restaurant_type",
    color_discrete_sequence=[
        "#ff7043",
        "#42a5f5",
        "#ab47bc",
        "#26a69a",
        "#ffa726"
    ],
    opacity=.55,
    title="Preparation Time vs Delivery Time"
)

st.plotly_chart(
    style_chart(fig5),
    use_container_width=True
)


st.markdown('<div class="section">Driver Experience</div>',unsafe_allow_html=True)

fig6 = px.scatter(
    df,
    x="delivery_partner_experience_months",
    y="actual_delivery_time_minutes",
    color="delivery_partner_rating",
    color_continuous_scale="Turbo",
    opacity=.55,
    title="Driver Experience vs Delivery Time"
)

st.plotly_chart(
    style_chart(fig6),
    use_container_width=True
)


st.markdown('<div class="section">Delivery by City</div>',unsafe_allow_html=True)

city_data = (
    df.groupby("city",as_index=False)
    ["actual_delivery_time_minutes"]
    .mean()
)

fig7 = px.bar(
    city_data,
    x="city",
    y="actual_delivery_time_minutes",
    color="city",
    color_discrete_sequence=[
        "#ff7043",
        "#42a5f5",
        "#ab47bc",
        "#26a69a",
        "#ffee58",
        "#ec407a"
    ],
    title="Average Delivery Time by City"
)

st.plotly_chart(
    style_chart(fig7),
    use_container_width=True
)


st.markdown('<div class="section">Dataset Preview</div>',unsafe_allow_html=True)

st.dataframe(
    df.head(20),
    use_container_width=True,
    hide_index=True
)


st.markdown("""
<div class="footer">
Food Delivery Time Prediction • Developed by <b>Eng. Ahmed Adel</b>
</div>
""", unsafe_allow_html=True)