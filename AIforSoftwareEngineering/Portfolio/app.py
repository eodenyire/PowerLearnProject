import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained model and scaler
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler

model, scaler = load_model()

# Set up the app
st.set_page_config(page_title="Maternal Mortality Predictor", layout="centered")
st.title("🤰 Maternal Mortality Rate Predictor")
st.markdown("""
Predict the **maternal mortality rate** (per 1000 births) based on hospital infrastructure and resources.
""")

# Input fields
st.header("🏥 Hospital Profile")

beds = st.slider("Number of Beds", 50, 1000, 350)
doctors_per_patient = st.slider("Doctors per Patient", 0.05, 0.3, 0.15)
nurses_per_patient = st.slider("Nurses per Patient", 0.1, 0.8, 0.4)
equipment_quality = st.slider("Equipment Quality (1 = Poor, 10 = Excellent)", 1.0, 10.0, 7.5)
rural_location = st.selectbox("Rural Location?", ["No", "Yes"])
avg_patient_age = st.slider("Average Patient Age", 18, 45, 28)
avg_pregnancies = st.slider("Average Pregnancies per Patient", 0.5, 5.0, 2.0)
has_nicu = st.selectbox("Has NICU?", ["No", "Yes"])
hospital_years = st.slider("Hospital Age (Years)", 1, 100, 25)

# Convert categorical inputs to numeric
rural_val = 1 if rural_location == "Yes" else 0
nicu_val = 1 if has_nicu == "Yes" else 0

# Format input for model
input_data = pd.DataFrame([{
    'beds': beds,
    'doctors_per_patient': doctors_per_patient,
    'nurses_per_patient': nurses_per_patient,
    'equipment_quality': equipment_quality,
    'rural_location': rural_val,
    'avg_patient_age': avg_patient_age,
    'avg_pregnancies_per_patient': avg_pregnancies,
    'has_nicu': nicu_val,
    'hospital_years': hospital_years
}])

# Predict
if st.button("📊 Predict Mortality Rate"):
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]
    
    st.success(f"Predicted Maternal Mortality Rate: **{prediction:.2f} per 1000 births**")

    if prediction > 4:
        st.error("⚠️ High mortality rate. Consider reviewing staff ratios or NICU availability.")
    elif prediction > 2:
        st.warning("🟡 Moderate mortality rate. Improvements may reduce risks.")
    else:
        st.balloons()
        st.info("✅ Low risk. Hospital profile is favorable.")

st.markdown("---")
st.caption("Developed by Emmanuel Odenyire Anyira | AI for Software Engineering Final Project")
