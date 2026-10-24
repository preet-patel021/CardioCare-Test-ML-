import streamlit as st 
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "Logistic_Regression_heart.pkl")
scaler = joblib.load(BASE_DIR / "scaler.pkl")
expected_columns = joblib.load(BASE_DIR / "columns.pkl")

st.title("Heart Disease Prediction App")
st.markdown("Enter your health details below.")

age = st.slider("Age", 18,100,40)
sex = st.selectbox("Sex", ["Male","Female"])
chest_pain_type =st.selectbox("Chest Pain Type", ["ATA","NAP","ASY","TA"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input(
    "Cholesterol (mg/dL)", 100, 600, 200,
    key="cholesterol"
)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
resting_bp = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    min_value=80,
    max_value=200,
    value=120,
    key="resting_bp"
)
resting_ecg = st.selectbox("Resting ECG", ["Normal","ST","LVH"])
max_hr = st.number_input(
    "Maximum Heart Rate", 60, 220, 150,
    key="max_hr"
)
exercise_angina = st.selectbox("Exercise-Induced Angina",["Y", "N"])
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope =st.selectbox("ST Slope", ["Up", "Flat", "Down"])


if st.button("Predict"):
    raw_input = {
        'Age': age,
        'Sex_' + sex: 1,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'ChestPainType_' + chest_pain_type: 1,
        'RestingECG_' + resting_ecg: 1,
        'MaxHR': max_hr,
        'ExerciseAngina_' + exercise_angina: 1,
        'Oldpeak': oldpeak,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error("High risk of heart disease")
    else:
        st.success("Low risk of heart disease")
