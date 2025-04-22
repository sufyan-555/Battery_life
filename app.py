import streamlit as st
import numpy as np
import pickle


try:
    model = pickle.load(open('model.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.set_page_config(page_title="EV Battery Health Predictor", layout="wide")


st.markdown("""
    <style>
        .main {
            background-color: #1e1e1e;
            color: #f0f0f0;
            padding: 2rem;
            border-radius: 10px;
        }
        h1, h2, h3, h4 {
            color: #4fc3f7;
        }
        .stButton>button {
            background-color: #0288d1;
            color: white;
            font-weight: bold;
            padding: 0.6rem 1.2rem;
            border-radius: 8px;
            margin-top: 10px;
        }
        .stNumberInput>div>div>input {
            background-color: #2c2c2c;
            color: white;
        }
        .footer {
            font-size: 0.9rem;
            color: #aaa;
            margin-top: 3rem;
        }
        .member {
            display: flex;
            align-items: center;
            margin-bottom: 6px;
        }
        .member img {
            border-radius: 50%;
            width: 26px;
            height: 26px;
            margin-right: 8px;
        }
        .sidebar-section {
            margin-bottom: 16px;
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## EV Battery Health Predictor")
st.sidebar.markdown("A machine learning-powered web app that estimates the current health of an EV's battery based on key usage parameters.")

st.sidebar.markdown("### 📁 Project Info")
st.sidebar.markdown("""
-  Built with Python, Streamlit, and Scikit-learn  
-  Uses real-world EV battery data  
-  Capstone project (Class of 2025 DS 3rd year)
""")

st.sidebar.markdown("### 👨‍💻 Team Members")
team_members = [
    "Alice", "Bob", "Charlie", "Diana", "Ethan", "Fay"
]
icon_url = "https://cdn-icons-png.flaticon.com/512/9131/9131529.png"  # Simple user icon

for name in team_members:
    st.sidebar.markdown(
        f"""
        <div class="member">
            <img src="{icon_url}" alt="{name}" />
            <span style="color: #f0f0f0;">{name}</span>
        </div>
        """, unsafe_allow_html=True
    )

st.sidebar.markdown("---")
st.sidebar.markdown("📘 *This app provides an estimated battery health score and does not replace certified diagnostics.*")

st.title("EV Battery Health Predictor")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Enter Vehicle Details")

    left , right = st.columns(2)
    with left:
        age = st.number_input("Vehicle Age (years)", min_value=0.0, max_value=20.0, value=3.0, step=0.1)
        mileage = st.number_input("Mileage (km)", min_value=0.0, max_value=500000.0, value=50000.0, step=100.0)
        charging_cycles = st.number_input("Charging Cycles", min_value=0.0, max_value=3000.0, value=800.0, step=1.0)
    with right:
        avg_temp = st.number_input("Average Operating Temperature (°C)", min_value=-50.0, max_value=100.0, value=25.0, step=0.5)
        battery_capacity = st.number_input("Battery Capacity (kWh)", min_value=10.0, max_value=200.0, value=75.0, step=1.0)
        fast_charging = st.slider("Enter the fast charging percentage (%)", min_value=0, max_value=100, value=30)



with col2:
    top_left, top_right = st.columns([4,1])
    with top_right:
        predict = st.button("Predict")
    with top_left:
        st.subheader("Prediction Result")
        if predict:
            input_data = np.array([[age, mileage, charging_cycles, avg_temp, fast_charging, battery_capacity]])
            try:
                prediction = model.predict(input_data)[0]
                st.success(f"Estimated Battery Health: {prediction:.2f}%")
            except Exception as e:
                st.error(f"Prediction failed: {e}")
        else:
            st.info("Fill in the inputs on the left and click Predict.")
    

# Footer
st.markdown("<div class='footer'>This prediction is a machine learning estimate and may not reflect actual battery condition. For accurate diagnostics, consult certified EV professionals.</div>", unsafe_allow_html=True)
