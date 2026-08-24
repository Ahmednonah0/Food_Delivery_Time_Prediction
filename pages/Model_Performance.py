import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)


# =========================================================
# DATA
# =========================================================

results = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Ridge",
        "Lasso",
        "KNN",
        "Decision Tree",
        "Random Forest",
        "XGBoost"
    ],

    "Train R2": [
        0.9506,
        0.9506,
        0.8987,
        0.8973,
        1.0000,
        0.9941,
        0.9770
    ],

    "Test R2": [
        0.9505,
        0.9505,
        0.8987,
        0.8464,
        0.9143,
        0.9590,
        0.9654
    ],

    "MAE": [
        2.4564,
        2.4562,
        3.4927,
        4.4671,
        3.3542,
        2.3346,
        2.1746
    ]
})


model_colors = {
    "Linear Regression": "#29B6F6",
    "Ridge": "#26C6DA",
    "Lasso": "#AB47BC",
    "KNN": "#FFA726",
    "Decision Tree": "#EF5350",
    "Random Forest": "#5C6BC0",
    "XGBoost": "#FFD54F"
}


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 10%,rgba(255,115,0,.10),transparent 25%),
        radial-gradient(circle at 90% 90%,rgba(80,110,255,.10),transparent 25%),
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

@keyframes fadeUp {
    from {opacity:0;transform:translateY(25px);}
    to {opacity:1;transform:translateY(0);}
}

@keyframes glow {
    0% {box-shadow:0 0 10px rgba(255,115,0,.08);}
    50% {box-shadow:0 0 38px rgba(255,115,0,.22);}
    100% {box-shadow:0 0 10px rgba(255,115,0,.08);}
}

.header {
    text-align:center;
    margin-bottom:38px;
    animation:fadeUp .7s ease-out;
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

.metric {
    min-height:140px;
    border-radius:20px;
    padding:22px;
    background:linear-gradient(145deg,rgba(255,255,255,.05),rgba(255,255,255,.015));
    border:1px solid rgba(255,255,255,.07);
    transition:.25s;
    animation:fadeUp .8s ease-out;
}

.metric:hover {
    transform:translateY(-5px);
    border-color:rgba(255,125,20,.35);
}

.metric-label {
    color:#7d8998;
    font-size:12px;
    letter-spacing:1px;
    font-weight:800;
}

.metric-value {
    font-size:35px;
    font-weight:950;
    margin-top:10px;
}

.orange {color:#ff8b2c;}
.blue {color:#42a5ff;}
.green {color:#00c78b;}
.purple {color:#b17cff;}

.winner {
    margin-top:28px;
    padding:30px;
    border-radius:24px;
    background:
        radial-gradient(circle at top,rgba(255,215,64,.14),rgba(255,255,255,.02));
    border:1px solid rgba(255,215,64,.22);
    animation:fadeUp .8s ease-out,glow 5s infinite;
}

.winner-label {
    color:#ffd54f;
    font-size:12px;
    font-weight:900;
    letter-spacing:2px;
}

.winner-title {
    color:white;
    font-size:30px;
    font-weight:950;
    margin-top:8px;
}

.winner-text {
    color:#8793a2;
    font-size:14px;
    line-height:1.7;
    margin-top:10px;
}

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

.info-card {
    min-height:165px;
    border-radius:20px;
    padding:22px;
    border:1px solid rgba(255,255,255,.07);
    background:linear-gradient(145deg,rgba(255,255,255,.045),rgba(255,255,255,.015));
    transition:.25s;
}

.info-card:hover {
    transform:translateY(-5px);
    border-color:rgba(255,125,20,.35);
}

.info-title {
    color:white;
    font-size:17px;
    font-weight:850;
}

.info-text {
    color:#83909f;
    font-size:13px;
    line-height:1.7;
    margin-top:8px;
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


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="header">
<div class="label">MACHINE LEARNING EVALUATION</div>
<div class="title">
Model <span class="gradient">Performance</span>
</div>
<div class="desc">
Compare the regression algorithms using Test R², MAE
and generalization performance.
</div>
</div>
""", unsafe_allow_html=True)


xgb = results[results["Model"] == "XGBoost"].iloc[0]
gap = xgb["Train R2"] - xgb["Test R2"]


# =========================================================
# KPI CARDS
# =========================================================

m1,m2,m3,m4 = st.columns(4)

with m1:
    st.markdown(f"""
<div class="metric">
<div class="metric-label">TEST R²</div>
<div class="metric-value orange">{xgb["Test R2"]:.4f}</div>
</div>
""", unsafe_allow_html=True)

with m2:
    st.markdown(f"""
<div class="metric">
<div class="metric-label">R² PERCENTAGE</div>
<div class="metric-value blue">{xgb["Test R2"]*100:.2f}%</div>
</div>
""", unsafe_allow_html=True)

with m3:
    st.markdown(f"""
<div class="metric">
<div class="metric-label">MAE</div>
<div class="metric-value green">{xgb["MAE"]:.2f} min</div>
</div>
""", unsafe_allow_html=True)

with m4:
    st.markdown(f"""
<div class="metric">
<div class="metric-label">TRAIN-TEST GAP</div>
<div class="metric-value purple">{gap:.3f}</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# WINNER
# =========================================================

st.markdown("""
<div class="winner">
<div class="winner-label">BEST PERFORMING MODEL</div>
<div class="winner-title">XGBoost Regressor</div>
<div class="winner-text">
XGBoost achieved the highest Test R² and the lowest
Mean Absolute Error, making it the strongest overall model.
</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# STYLE FUNCTION
# =========================================================

def style_chart(fig):

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#aab5c3"),
        title_font=dict(color="white", size=18),
        margin=dict(l=20, r=20, t=55, b=20),
        legend_title_text=""
    )

    fig.update_xaxes(
        gridcolor="rgba(255,255,255,.05)"
    )

    fig.update_yaxes(
        gridcolor="rgba(255,255,255,.05)"
    )

    return fig


# =========================================================
# TEST R2
# =========================================================

st.markdown('<div class="section">Test R² Comparison</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Higher values indicate stronger performance on unseen data.</div>', unsafe_allow_html=True)

r2_sorted = results.sort_values(
    "Test R2",
    ascending=True
)

fig1 = px.bar(
    r2_sorted,
    x="Test R2",
    y="Model",
    orientation="h",
    color="Model",
    color_discrete_map=model_colors,
    text="Test R2",
    title="Model Test R²"
)

fig1.update_traces(
    texttemplate="%{text:.4f}",
    textposition="outside"
)

fig1.update_xaxes(
    range=[0.80,1.0]
)

st.plotly_chart(
    style_chart(fig1),
    use_container_width=True
)


# =========================================================
# MAE
# =========================================================

st.markdown('<div class="section">Prediction Error</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Lower MAE means better average prediction accuracy.</div>', unsafe_allow_html=True)

mae_sorted = results.sort_values(
    "MAE",
    ascending=False
)

fig2 = px.bar(
    mae_sorted,
    x="MAE",
    y="Model",
    orientation="h",
    color="Model",
    color_discrete_map=model_colors,
    text="MAE",
    title="Mean Absolute Error"
)

fig2.update_traces(
    texttemplate="%{text:.2f} min",
    textposition="outside"
)

st.plotly_chart(
    style_chart(fig2),
    use_container_width=True
)


# =========================================================
# TRAIN VS TEST
# =========================================================

st.markdown('<div class="section">Train vs Test Performance</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Useful for identifying possible overfitting.</div>', unsafe_allow_html=True)

train_test = results.melt(
    id_vars="Model",
    value_vars=["Train R2","Test R2"],
    var_name="Dataset",
    value_name="R2"
)

fig3 = px.bar(
    train_test,
    x="Model",
    y="R2",
    color="Dataset",
    barmode="group",
    color_discrete_map={
        "Train R2":"#42a5ff",
        "Test R2":"#ff8b2c"
    },
    title="Train R² vs Test R²"
)

fig3.update_yaxes(
    range=[0.80,1.02]
)

st.plotly_chart(
    style_chart(fig3),
    use_container_width=True
)


# =========================================================
# GAP
# =========================================================

st.markdown('<div class="section">Overfitting Check</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Smaller train-test gaps generally indicate better generalization.</div>', unsafe_allow_html=True)

gap_df = results.copy()

gap_df["R2 Gap"] = (
    gap_df["Train R2"]
    -
    gap_df["Test R2"]
)

fig4 = px.bar(
    gap_df.sort_values(
        "R2 Gap",
        ascending=True
    ),
    x="R2 Gap",
    y="Model",
    orientation="h",
    color="R2 Gap",
    color_continuous_scale="Turbo",
    text="R2 Gap",
    title="Train-Test R² Gap"
)

fig4.update_traces(
    texttemplate="%{text:.4f}",
    textposition="outside"
)

st.plotly_chart(
    style_chart(fig4),
    use_container_width=True
)


# =========================================================
# WHY XGBOOST
# =========================================================

st.markdown('<div class="section">Why XGBoost?</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Why the final model was selected.</div>', unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
<div class="info-card">
<div class="info-title">Highest Test R²</div>
<div class="info-text">
XGBoost achieved the highest validation R² score
among the seven tested regression algorithms.
</div>
</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="info-card">
<div class="info-title">Lowest MAE</div>
<div class="info-text">
The average prediction error is approximately
2.17 minutes, the lowest among the compared models.
</div>
</div>
""", unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="info-card">
<div class="info-title">Strong Generalization</div>
<div class="info-text">
The train-test gap remains relatively small,
indicating good generalization performance.
</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# TABLE
# =========================================================

st.markdown('<div class="section">Complete Evaluation Results</div>', unsafe_allow_html=True)

display_results = results.copy()

display_results["Train R2"] = display_results["Train R2"].round(4)
display_results["Test R2"] = display_results["Test R2"].round(4)
display_results["MAE"] = display_results["MAE"].round(4)

st.dataframe(
    display_results,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
Food Delivery Time Prediction • Developed by <b>Eng. Ahmed Adel</b>
</div>
""", unsafe_allow_html=True)