import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# -----------------------------------------
# Load trained model and scaler
# -----------------------------------------
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler

model, scaler = load_model()

# -----------------------------------------
# Streamlit UI
# -----------------------------------------
st.set_page_config(page_title="Maternal Mortality Predictor", layout="centered")
st.title("🤰 Maternal Mortality Rate Predictor")
st.markdown("""
This AI tool predicts the **maternal mortality rate (per 1000 births)** based on hospital features.
""")

st.header("🏥 Hospital Characteristics")

beds = st.slider("Number of Beds", 50, 1000, 350)
doctors_per_patient = st.slider("Doctors per Patient", 0.05, 0.3, 0.15)
nurses_per_patient = st.slider("Nurses per Patient", 0.1, 0.8, 0.4)
equipment_quality = st.slider("Equipment Quality (1 = Poor, 10 = Excellent)", 1.0, 10.0, 7.5)
rural_location = st.selectbox("Is the hospital in a rural location?", ["No", "Yes"])
avg_patient_age = st.slider("Average Patient Age", 18, 45, 28)
avg_pregnancies = st.slider("Average Pregnancies per Patient", 0.5, 5.0, 2.0)
has_nicu = st.selectbox("Has NICU?", ["No", "Yes"])
hospital_years = st.slider("Hospital Age (Years)", 1, 100, 25)

# -----------------------------------------
# Prepare Input Data
# -----------------------------------------
rural_location_val = 1 if rural_location == "Yes" else 0
has_nicu_val = 1 if has_nicu == "Yes" else 0

input_data = {
    'beds': beds,
    'doctors_per_patient': doctors_per_patient,
    'nurses_per_patient': nurses_per_patient,
    'equipment_quality': equipment_quality,
    'rural_location': rural_location_val,
    'avg_patient_age': avg_patient_age,
    'avg_pregnancies_per_patient': avg_pregnancies,
    'has_nicu': has_nicu_val,
    'hospital_years': hospital_years
}

input_df = pd.DataFrame([input_data])

# -----------------------------------------
# Predict
# -----------------------------------------
if st.button("📊 Predict Mortality Rate"):
    # Scale input
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]

    st.success(f"🩺 Predicted Maternal Mortality Rate: **{prediction:.2f} per 1000 births**")

    # Insights
    if prediction > 4:
        st.warning("⚠️ High predicted mortality. Consider increasing equipment quality or NICU access.")
    elif prediction > 2:
        st.info("ℹ️ Moderate risk. Target improvements in doctor/nurse ratios.")
    else:
        st.balloons()
        st.success("✅ Low predicted mortality rate. Keep up the good practices!")

# -----------------------------------------
# Footer
# -----------------------------------------
st.markdown("---")
st.caption("Developed as part of the Power Learn Project – AI for Software Engineering")
