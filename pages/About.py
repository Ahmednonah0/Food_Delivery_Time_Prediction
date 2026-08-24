import streamlit as st


st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)


st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 8% 10%,rgba(255,120,0,.10),transparent 25%),
        radial-gradient(circle at 92% 90%,rgba(75,110,255,.10),transparent 25%),
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
    0% {box-shadow:0 0 8px rgba(255,115,0,.08);}
    50% {box-shadow:0 0 38px rgba(255,115,0,.22);}
    100% {box-shadow:0 0 8px rgba(255,115,0,.08);}
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
    max-width:800px;
    margin:10px auto 0 auto;
    line-height:1.7;
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

.card {
    min-height:210px;
    padding:24px;
    border-radius:22px;
    border:1px solid rgba(255,255,255,.07);
    background:linear-gradient(145deg,rgba(255,255,255,.05),rgba(255,255,255,.015));
    transition:.25s;
    animation:fadeUp .8s ease-out;
}

.card:hover {
    transform:translateY(-6px);
    border-color:rgba(255,125,20,.35);
}

.icon {
    font-size:30px;
    margin-bottom:12px;
}

.card-title {
    color:white;
    font-size:18px;
    font-weight:850;
}

.card-text {
    color:#84909f;
    font-size:13px;
    line-height:1.7;
    margin-top:8px;
}

.step {
    min-height:160px;
    padding:22px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,.07);
    background:rgba(255,255,255,.03);
}

.step-number {
    color:#ff8d31;
    font-size:12px;
    font-weight:900;
    letter-spacing:1.5px;
}

.step-title {
    color:white;
    font-size:17px;
    font-weight:850;
    margin-top:7px;
}

.step-text {
    color:#84909f;
    font-size:13px;
    line-height:1.7;
    margin-top:7px;
}

.tech {
    min-height:140px;
    padding:20px;
    border-radius:20px;
    text-align:center;
    border:1px solid rgba(255,255,255,.07);
    background:linear-gradient(145deg,rgba(255,255,255,.045),rgba(255,255,255,.015));
    transition:.25s;
}

.tech:hover {
    transform:translateY(-5px);
    border-color:rgba(255,125,20,.35);
}

.tech-icon {
    font-size:30px;
}

.tech-name {
    color:white;
    font-size:17px;
    font-weight:850;
    margin-top:8px;
}

.tech-desc {
    color:#7f8c9b;
    font-size:12px;
    margin-top:6px;
}

.performance {
    min-height:175px;
    padding:25px;
    border-radius:22px;
    text-align:center;
    border:1px solid rgba(255,125,20,.15);
    background:
        radial-gradient(circle at top,rgba(255,115,0,.13),rgba(255,255,255,.02));
}

.performance-value {
    font-size:38px;
    font-weight:950;
    margin-top:10px;
}

.orange {color:#ff8b2c;}
.blue {color:#42a5ff;}
.green {color:#00c78b;}

.performance-label {
    color:#7f8c9b;
    font-size:12px;
    letter-spacing:1px;
}

.performance-text {
    color:#84909f;
    font-size:13px;
    line-height:1.6;
    margin-top:8px;
}

.developer {
    margin-top:25px;
    padding:48px 25px;
    border-radius:28px;
    text-align:center;
    border:1px solid rgba(255,125,20,.18);
    background:
        radial-gradient(circle,rgba(255,115,0,.15),rgba(255,255,255,.02));
    animation:glow 5s infinite;
}

.developer-label {
    color:#ff8d31;
    font-size:12px;
    font-weight:900;
    letter-spacing:2px;
}

.developer-name {
    color:white;
    font-size:36px;
    font-weight:950;
    margin-top:10px;
}

.developer-role {
    color:#84909f;
    font-size:14px;
    margin-top:7px;
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
<div class="label">PROJECT INFORMATION</div>
<div class="title">
About The <span class="gradient">Project</span>
</div>
<div class="desc">
Food Delivery Time Prediction is a machine learning system
designed to estimate delivery duration using operational,
customer, restaurant and environmental information.
</div>
</div>
""", unsafe_allow_html=True)


c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
<div class="card">
<div class="icon">🎯</div>
<div class="card-title">Project Goal</div>
<div class="card-text">
Build a regression system capable of estimating
food delivery duration from real-world delivery features.
</div>
</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="card">
<div class="icon">🧠</div>
<div class="card-title">Model Development</div>
<div class="card-text">
Seven regression algorithms were compared using
cross-validation and multiple evaluation metrics.
</div>
</div>
""", unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="card">
<div class="icon">🚀</div>
<div class="card-title">Final System</div>
<div class="card-text">
The selected XGBoost pipeline was integrated into
an interactive Streamlit application.
</div>
</div>
""", unsafe_allow_html=True)


st.markdown('<div class="section">Project Workflow</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">The complete lifecycle of the project.</div>', unsafe_allow_html=True)

w1,w2,w3,w4 = st.columns(4)

with w1:
    st.markdown("""
<div class="step">
<div class="step-number">STEP 01</div>
<div class="step-title">Data Collection</div>
<div class="step-text">
Historical delivery records provide the foundation
for the machine learning project.
</div>
</div>
""", unsafe_allow_html=True)

with w2:
    st.markdown("""
<div class="step">
<div class="step-number">STEP 02</div>
<div class="step-title">Preprocessing</div>
<div class="step-text">
Numerical and categorical variables are prepared
and transformed for machine learning.
</div>
</div>
""", unsafe_allow_html=True)

with w3:
    st.markdown("""
<div class="step">
<div class="step-number">STEP 03</div>
<div class="step-title">Model Training</div>
<div class="step-text">
Multiple regression models are trained and
evaluated using cross-validation.
</div>
</div>
""", unsafe_allow_html=True)

with w4:
    st.markdown("""
<div class="step">
<div class="step-number">STEP 04</div>
<div class="step-title">Deployment</div>
<div class="step-text">
The final model is deployed through an interactive
Streamlit web interface.
</div>
</div>
""", unsafe_allow_html=True)


st.markdown('<div class="section">Technologies Used</div>', unsafe_allow_html=True)

t1,t2,t3,t4,t5 = st.columns(5)

techs = [
    ("🐍","Python","Core Language"),
    ("📊","Pandas","Data Processing"),
    ("🤖","Scikit-learn","ML Pipeline"),
    ("🌲","XGBoost","Final Model"),
    ("🌐","Streamlit","Web App")
]

for col, (icon, name, desc) in zip([t1,t2,t3,t4,t5], techs):
    with col:
        st.markdown(f"""
<div class="tech">
<div class="tech-icon">{icon}</div>
<div class="tech-name">{name}</div>
<div class="tech-desc">{desc}</div>
</div>
""", unsafe_allow_html=True)


st.markdown('<div class="section">Final Model Performance</div>', unsafe_allow_html=True)

p1,p2,p3 = st.columns(3)

with p1:
    st.markdown("""
<div class="performance">
<div class="performance-label">TEST R²</div>
<div class="performance-value orange">96.54%</div>
<div class="performance-text">
Strong validation performance on unseen data.
</div>
</div>
""", unsafe_allow_html=True)

with p2:
    st.markdown("""
<div class="performance">
<div class="performance-label">MEAN ABSOLUTE ERROR</div>
<div class="performance-value blue">2.17</div>
<div class="performance-text">
Average prediction error of approximately 2.17 minutes.
</div>
</div>
""", unsafe_allow_html=True)

with p3:
    st.markdown("""
<div class="performance">
<div class="performance-label">FINAL MODEL</div>
<div class="performance-value green">XGBoost</div>
<div class="performance-text">
Selected after comparing seven regression algorithms.
</div>
</div>
""", unsafe_allow_html=True)


st.markdown('<div class="section">Developer</div>', unsafe_allow_html=True)

st.markdown("""
<div class="developer">
<div class="developer-label">PROJECT DEVELOPER</div>
<div class="developer-name">Eng. Ahmed Adel</div>
<div class="developer-role">
Data Analysis • Machine Learning • Streamlit Development
</div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="footer">
Food Delivery Time Prediction • Developed by <b>Eng. Ahmed Adel</b>
</div>
""", unsafe_allow_html=True)