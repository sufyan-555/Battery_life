import streamlit as st
import numpy as np
import pickle

# Load the pre-trained model
try:
    model = pickle.load(open('model.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Page configuration
st.set_page_config(page_title="EV Battery Health Predictor", layout="centered")
st.title("🔋 EV Battery Health Predictor")
st.markdown("Enter your vehicle's details below:")

# --- Input Fields ---
age = st.number_input("Vehicle Age (years)", min_value=0.0, max_value=20.0, value=3.0, step=0.1)
mileage = st.number_input("Mileage (km)", min_value=0.0, max_value=500000.0, value=50000.0, step=100.0)
charging_cycles = st.number_input("Charging Cycles", min_value=0.0, max_value=3000.0, value=800.0, step=1.0)
avg_temp = st.number_input("Average Operating Temperature (°C)", min_value=-50.0, max_value=100.0, value=25.0, step=0.5)
fast_charging = st.slider("Fast Charging Usage (%)", min_value=0, max_value=100, value=30)
battery_capacity = st.number_input("Battery Capacity (kWh)", min_value=10.0, max_value=200.0, value=75.0, step=1.0)

# --- Prediction Button ---
if st.button("Predict"):
    input_data = np.array([[age, mileage, charging_cycles, avg_temp, fast_charging, battery_capacity]])
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"🔋 Estimated Battery Health: **{prediction:.2f}%**")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

# --- Footer ---
st.markdown("---")
st.markdown("💡 *Note: This is an estimate based on historical data and machine learning. Actual battery health may vary.*")
