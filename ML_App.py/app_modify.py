
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# ---------------- PAGE CONFIG ----------------

import streamlit as st

st.set_page_config(page_title="Streamlit Test", page_icon="❤️")

st.title("❤️ CardioCare Test")
st.success("Streamlit is working correctly!")
st.write("If you can see this page, the server and browser are communicating.")

age = st.slider("Select your age", 18, 100, 40)
st.write("Selected age:", age)


BASE_DIR = Path(__file__).resolve().parent

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_artifacts():
    model = joblib.load(BASE_DIR / "Logistic_Regression_heart.pkl")
    scaler = joblib.load(BASE_DIR / "scaler.pkl")
    columns = joblib.load(BASE_DIR / "columns.pkl")
    return model, scaler, columns


model, scaler, expected_columns = load_artifacts()

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: linear-gradient(145deg, #07111f 0%, #0b1830 55%, #101b32 100%);
    color: #f1f5f9;
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

h1, h2, h3, p, label {
    font-family: 'Inter', sans-serif !important;
}

.hero {
    padding: 34px;
    border: 1px solid rgba(91, 174, 255, 0.23);
    border-radius: 24px;
    background: linear-gradient(120deg, #102849, #102039 65%, #102d42);
    margin-bottom: 26px;
    box-shadow: 0 12px 40px rgba(0,0,0,0.18);
}

.hero-tag {
    color: #5eead4;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.hero h1 {
    color: #f8fafc;
    font-size: clamp(28px, 4vw, 43px);
    font-weight: 800;
    margin: 13px 0 10px;
    line-height: 1.2;
}

.hero p {
    color: #b8c9df;
    font-size: 15px;
    line-height: 1.8;
    margin-bottom: 0;
}

.section-card {
    padding: 19px 22px;
    border: 1px solid #243750;
    border-radius: 18px;
    background: rgba(15, 29, 49, 0.86);
    margin-bottom: 18px;
}

.section-heading {
    font-size: 19px;
    color: #e8f3ff;
    font-weight: 700;
    margin-bottom: 4px;
}

.section-subtitle {
    font-size: 12px;
    color: #8fa6c2;
    margin-bottom: 18px;
}

div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background-color: #14243a;
    border-color: #30445e;
    border-radius: 10px;
}

div[data-baseweb="select"] span,
div[data-baseweb="input"] input {
    color: #f1f5f9;
}

div[data-testid="stNumberInput"] button {
    background: #1c3552;
    color: #7dd3fc;
    border: none;
}

div[data-testid="stSlider"] [data-baseweb="slider"] {
    padding-top: 8px;
}

.stSlider [data-baseweb="slider"] div[role="slider"] {
    background-color: #38bdf8;
}

.stSlider [data-baseweb="slider"] div[data-testid="stTickBar"] {
    background-color: #29445f;
}

div.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    width: 100%;
    border: 0;
    border-radius: 12px;
    min-height: 52px;
    color: #061323;
    background: linear-gradient(100deg, #67e8f9, #38bdf8);
    font-weight: 800;
    font-size: 16px;
    transition: all 0.2s ease;
}

div.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    color: #061323;
    border: 0;
    box-shadow: 0 0 24px rgba(56,189,248,0.28);
    transform: translateY(-1px);
}

.result-card {
    padding: 25px;
    border-radius: 18px;
    margin: 22px 0;
    background: #10253b;
    border: 1px solid #2a4965;
}

.result-card h2 {
    margin-top: 8px;
    color: #f8fafc;
}

.result-card p {
    color: #b8c9df;
    line-height: 1.7;
}

.metric-card {
    background: #11243a;
    border: 1px solid #29425e;
    padding: 18px;
    border-radius: 15px;
    min-height: 100px;
}

.metric-label {
    font-size: 12px;
    color: #9bb1cb;
    margin-bottom: 9px;
}

.metric-value {
    font-size: 23px;
    color: #7dd3fc;
    font-weight: 800;
}

.footer {
    text-align: center;
    color: #8298b3;
    font-size: 12px;
    padding-top: 24px;
    line-height: 1.8;
}

hr {
    border-color: #243750;
}

@media (max-width: 640px) {
    .block-container {
        padding: 1rem 1rem 2rem;
    }

    .hero {
        padding: 22px;
        border-radius: 17px;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown("""
<div class="hero">
    <div class="hero-tag">❤️ &nbsp; CARDIOCARE · HEALTH INTELLIGENCE</div>
    <h1>Your Heart. Your Health.<br>Know Your Numbers.</h1>
    <p>
        Enter your health measurements below to receive a machine-learning
        estimate based on your trained heart disease prediction model.
        Simple insights, designed around you.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- QUICK INTRO ----------------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">01 · PERSONAL</div>
        <div class="metric-value">Your Profile</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">02 · HEALTH</div>
        <div class="metric-value">Your Metrics</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">03 · INSIGHTS</div>
        <div class="metric-value">ML Prediction</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown("## Let's get to know your heart")
st.caption("Complete the fields below. Use your actual measurements where available.")

# ---------------- HEALTH INPUT FORM ----------------
with st.form("heart_health_form"):

    st.markdown("""
    <div class="section-heading">👤 Personal information</div>
    <div class="section-subtitle">Basic details for your assessment</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age (years)", 18, 100, 40)

    with col2:
        sex = st.selectbox("Sex", ["Male", "Female"])

    st.markdown("---")
    st.markdown("""
    <div class="section-heading">🩺 Clinical measurements</div>
    <div class="section-subtitle">Enter your recorded health values</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        resting_bp = st.number_input(
            "Resting Blood Pressure (mm Hg)",
            min_value=80, max_value=200, value=120, step=1
        )

        cholesterol = st.number_input(
            "Cholesterol (mg/dL)",
            min_value=100, max_value=600, value=200, step=1
        )

        fasting_bs = st.selectbox(
            "Fasting Blood Sugar above 120 mg/dL",
            [0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No"
        )

        resting_ecg = st.selectbox(
            "Resting ECG",
            ["Normal", "ST", "LVH"]
        )

    with col2:
        max_hr = st.number_input(
            "Maximum Heart Rate (bpm)",
            min_value=60, max_value=220, value=150, step=1
        )

        chest_pain_type = st.selectbox(
            "Chest Pain Type",
            ["ATA", "NAP", "ASY", "TA"],
            format_func=lambda x: {
                "ATA": "Atypical Angina (ATA)",
                "NAP": "Non-Anginal Pain (NAP)",
                "ASY": "Asymptomatic (ASY)",
                "TA": "Typical Angina (TA)"
            }[x]
        )

        exercise_angina = st.selectbox(
            "Exercise-Induced Angina",
            ["N", "Y"],
            format_func=lambda x: "Yes" if x == "Y" else "No"
        )

    st.markdown("---")
    st.markdown("""
    <div class="section-heading">📈 Heart performance indicators</div>
    <div class="section-subtitle">Additional ECG-related measurements</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        oldpeak = st.slider(
            "Oldpeak (ST Depression)",
            min_value=0.0,
            max_value=6.0,
            value=1.0,
            step=0.1
        )

    with col2:
        st_slope = st.selectbox(
            "ST Slope",
            ["Up", "Flat", "Down"]
        )

    st.write("")
    submitted = st.form_submit_button(
        "❤️  Analyze My Heart Health",
        use_container_width=True
    )

# ---------------- PREDICTION ----------------
if submitted:
    raw_input = {
        "Age": age,
        "Sex_" + sex: 1,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "ChestPainType_" + chest_pain_type: 1,
        "RestingECG_" + resting_ecg: 1,
        "MaxHR": max_hr,
        "ExerciseAngina_" + exercise_angina: 1,
        "Oldpeak": oldpeak,
        "ST_Slope_" + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    # Match the exact feature columns used during training.
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    try:
        scaled_input = scaler.transform(input_df)
        prediction = int(model.predict(scaled_input)[0])

        st.markdown("---")
        st.markdown("## Your assessment result")

        if prediction == 1:
            st.markdown(f"""
            <div class="result-card" style="border-color:#fb7185;">
                <div style="font-size:13px;color:#fda4af;font-weight:700;">
                    ASSESSMENT COMPLETE
                </div>
                <h2>⚠️ Elevated predicted risk</h2>
                <p>
                    Your entered measurements were classified into the
                    heart-disease-positive category by the trained model.
                    This is not a diagnosis. Please discuss your results
                    with a qualified healthcare professional.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-card" style="border-color:#34d399;">
                <div style="font-size:13px;color:#6ee7b7;font-weight:700;">
                    ASSESSMENT COMPLETE
                </div>
                <h2>💚 Lower predicted risk category</h2>
                <p>
                    Your entered measurements were classified into the
                    heart-disease-negative category by the trained model.
                    This does not rule out heart disease or guarantee
                    that your heart is healthy.
                </p>
            </div>
            """, unsafe_allow_html=True)

        # Show the positive-class probability only if supported.
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(scaled_input)[0]
            classes = list(model.classes_)

            if 1 in classes:
                risk_probability = float(probabilities[classes.index(1)])

                st.markdown("### Model probability")
                st.progress(risk_probability)
                st.markdown(
                    f"**Positive-class probability: {risk_probability:.1%}**"
                )
                st.caption(
                    "This is the model's estimated probability for its "
                    "positive class, not your clinically established "
                    "probability of having heart disease."
                )

        st.info(
            "This educational tool cannot diagnose, treat, or rule out "
            "heart disease. Seek medical advice for personal interpretation. "
            "If you have chest pain, severe breathlessness, or other "
            "emergency symptoms, seek urgent medical care."
        )

    except Exception as e:
        st.error(
            "Prediction could not be completed. Check that your model, "
            "scaler, and feature columns match the data used during training."
        )
        st.exception(e)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    ❤️ CardioCare · Machine Learning Health Project<br>
    Built with Python & Streamlit<br>
    For educational purposes only · Not a substitute for professional medical advice
</div>
""", unsafe_allow_html=True)
