import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("random_forest_heart_disease_model.pkl")

# App branding (logo optional)
# st.image("logo.png", width=100)  # Uncomment if you add a logo file
st.markdown("<h1 style='text-align: center; color: #FAFAFA;'>❤️ Heart Disease Risk Predictor</h1>", unsafe_allow_html=True)
st.markdown("---")

# Instructions
st.markdown("""
<style>
.big-font {
    font-size:18px !important;
    font-weight:500;
    color:#f0f0f0;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font">🔍 Enter patient information to assess their risk of heart disease.</p>', unsafe_allow_html=True)

# Inputs
age = st.slider("Age", 20, 100, 40)
sex = st.selectbox("Sex", ["M", "F"])
cp = st.selectbox("Chest Pain Type", ["TA", "ATA", "NAP", "ASY"])
rest_bp = st.slider("Resting Blood Pressure", 80, 200, 120)
chol = st.slider("Cholesterol (mg/dL)", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
rest_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.slider("Max Heart Rate Achieved", 60, 220, 150)
ex_angina = st.selectbox("Exercise-induced Angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak (ST depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

# Manual one-hot encoding
input_data = [
    age,
    rest_bp,
    chol,
    fbs,
    max_hr,
    oldpeak,
    1 if sex == "F" else 0,
    1 if sex == "M" else 0,
    int(cp == "ASY"),
    int(cp == "ATA"),
    int(cp == "NAP"),
    int(cp == "TA"),
    int(rest_ecg == "LVH"),
    int(rest_ecg == "Normal"),
    int(rest_ecg == "ST"),
    int(ex_angina == "N"),
    int(ex_angina == "Y"),
    int(st_slope == "Down"),
    int(st_slope == "Flat"),
    int(st_slope == "Up")
]

# Prediction button
if st.button("🧪 Predict"):
    pred = model.predict([input_data])[0]
    st.markdown("---")
    if pred == 1:
        st.error("🔴 **High Risk:** This patient is at high risk of heart disease. Immediate medical attention is recommended.")
    else:
        st.success("✅ **Low Risk:** This patient appears to be at low risk of heart disease.")

# Footer
st.markdown("---")
st.markdown("<center>🩺 Developed by UET Hospital | Built with ❤️ using Streamlit</center>", unsafe_allow_html=True)
