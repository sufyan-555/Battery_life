import streamlit as st
import numpy as np
import pickle
import random
from datetime import datetime

# Try to load the model
try:
    model = pickle.load(open('model.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="EV Battery Health Predictor",
    page_icon="🔋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a modern, visually appealing UI
st.markdown("""
    <style>
        /* Main layout and colors */
        .main {
            background-color: #121212;
            color: #f8f9fa;
            padding: 2rem;
            border-radius: 12px;
        }
        
        /* Header styling */
        h1 {
            color: #4fc3f7;
            font-weight: 700;
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            text-shadow: 0px 2px 4px rgba(0,0,0,0.2);
        }
        
        h2, h3, h4 {
            color: #81d4fa;
            font-weight: 600;
        }
        
        /* Card-like containers */
        .card {
            background-color: #1e1e1e;
            border-radius: 8px;
            padding: 1.2rem;
            margin-bottom: 1rem;
            border: 1px solid #333;
        }
        
        /* Button styling */
        .stButton>button {
            background: linear-gradient(90deg, #0288d1, #26c6da);
            color: white;
            font-weight: bold;
            padding: 0.8rem 1.5rem;
            border-radius: 10px;
            border: none;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            width: 100%;
            font-size: 1.1rem;
            margin-top: 10px;
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 10px rgba(0,0,0,0.15);
        }
        
        /* Input fields styling */
        .stNumberInput>div>div>input, .stSlider>div>div>div {
            background-color: #2c2c2c;
            color: white;
            border-radius: 8px;
            border: 1px solid #444;
        }
        
        /* Result section */
        .result-box {
            padding: 1.5rem;
            border-radius: 12px;
            margin-top: 1rem;
            text-align: center;
            background: #1e1e1e;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            border-left: 4px solid #4caf50;
        }
        
        .info-box {
            padding: 1.5rem;
            border-radius: 12px;
            margin-top: 1rem;
            text-align: center;
            background: #1e1e1e;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            border-left: 4px solid #ff9800;
        }
        
        /* Team members styling */
        .member {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
            padding: 8px;
            background-color: #2c2c2c;
            border-radius: 8px;
            transition: all 0.2s ease;
        }
        
        .member:hover {
            background-color: #3c3c3c;
            transform: translateX(3px);
        }
        
        .member img {
            border-radius: 50%;
            width: 32px;
            height: 32px;
            margin-right: 10px;
            border: 2px solid #0288d1;
        }
        
        /* Footer styling */
        .footer {
            font-size: 0.9rem;
            color: #aaa;
            margin-top: 3rem;
            padding: 1rem;
            border-top: 1px solid #333;
            text-align: center;
        }
        
        /* Gauge charts */
        .gauge-container {
            display: flex;
            justify-content: center;
        }
        
        /* Sidebar styling */
        .css-1d391kg {
            background-color: #1a1a1a;
        }
        
        /* Progress bar */
        .stProgress > div > div > div > div {
            background-color: #0288d1;
        }
    </style>
""", unsafe_allow_html=True)

# Functions for UI elements
def create_card(title, content):
    return f"""
    <div class="card">
        <h3>{title}</h3>
        {content}
    </div>
    """

# Sidebar content
with st.sidebar:
    st.markdown("## 🔋 EV Battery Health Predictor")
    
    st.markdown(create_card("📊 Project Info", """
    <ul>
        <li>Built with Python, Streamlit, and Scikit-learn</li>
        <li>Uses real-world EV battery data</li>
        <li>ML model with 94% accuracy</li>
        <li>Capstone project (Class of 2025 DS 3rd year)</li>
    </ul>
    """), unsafe_allow_html=True)
    
    # Team members with random avatars
    st.markdown("### 👨‍💻 Team Members")
    
    team_members = [
        "Debashi", "Ishan", "Subhanjan", 
        "Sawrnadeep","Jayant","Sufyan"
    ]
    
    
    for name in team_members:
        avatar_style = 'personas'
        avatar_seed = 's'.join(name.split())
        avatar_url = f"https://api.dicebear.com/7.x/{avatar_style}/svg?seed={avatar_seed}"
        
        st.markdown(
            f"""
            <div class="member">
                <img src="{avatar_url}" alt="{name}" />
                <span style="color: #f0f0f0;">{name}</span>
            </div>
            """, unsafe_allow_html=True
        )
    
    st.markdown("---")
    st.markdown("""📘 <i>This app provides an estimated battery health score and does not replace certified diagnostics.</i>""", unsafe_allow_html=True)
    
    current_date = datetime.now().strftime("%B %d, %Y")
    st.markdown(f"<div style='text-align: center; color: #888;'>Last updated: {current_date}</div>", unsafe_allow_html=True)

# Main content
st.markdown("<h1>🔋 EV Battery Health Predictor</h1>", unsafe_allow_html=True)

st.markdown("""
        Get an AI-powered estimate of your electric vehicle's battery health based on usage patterns and environmental factors.
        Fill in the form below and click "Predict" to see your results.
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<h2>Vehicle Details</h2>", unsafe_allow_html=True)
    
    left, right = st.columns(2)
    with left:
        age = st.number_input("Vehicle Age (years)", 
                             min_value=0.0, max_value=20.0, value=3.0, step=0.1,
                             help="How old is your vehicle?")
        
        mileage = st.number_input("Mileage (km)", 
                                 min_value=0.0, max_value=50000000.0, value=10000.0, step=100.0,
                                 help="Total distance traveled by your vehicle")
        
        charging_cycles = st.number_input("Charging Cycles", 
                                         min_value=0.0, max_value=3000.0, value=800.0, step=1.0,
                                         help="Number of full charge/discharge cycles")
    with right:
        avg_temp = st.number_input("Average Operating Temperature (°C)", 
                                  min_value=-50.0, max_value=100.0, value=25.0, step=0.5,
                                  help="The average temperature your battery operates in")
        
        battery_capacity = st.number_input("Battery Capacity (kWh)", 
                                          min_value=10.0, max_value=200.0, value=75.0, step=1.0,
                                          help="The total capacity of your battery")
        
        fast_charging = st.slider("Fast Charging Usage (%)", 
                                 min_value=0, max_value=100, value=30,
                                 help="Percentage of charges done with fast charging")
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("<h2>Analysis Results</h2>", unsafe_allow_html=True)
    
    predict = st.button("Generate Prediction")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Results area
    if predict:
        input_data = np.array([[age, mileage, charging_cycles, avg_temp, fast_charging, battery_capacity]])
        
        try:
            # Get prediction
            prediction = model.predict(input_data)[0]
            
            # Display the result
            st.markdown(f"""
                <div class="result-box">
                    <h2 style="color: #4caf50;">Battery Health Assessment</h2>
                    <div style="font-size: 3rem; font-weight: bold; color: {'#4caf50' if prediction > 80 else '#ff9800' if prediction > 60 else '#f44336'};">
                        {prediction:.1f}%
                    </div>
                    <div class="gauge-container">
                        <div style="width: 100%; background-color: #444; height: 20px; border-radius: 10px; margin-top: 10px;">
                            <div style="width: {prediction}%; background: linear-gradient(90deg, 
                            {'#f44336' if prediction < 40 else '#ff9800' if prediction < 70 else '#4caf50'}
                            {',' + '#ff9800' if prediction >= 40 and prediction < 70 else ',' + '#4caf50' if prediction >= 70 else ''});
                            height: 100%; border-radius: 10px;"></div>
                        </div>
                    </div>
                    <p style="margin-top: 15px;">
                        {'Critical - Consider replacement soon' if prediction < 40 else
                         'Fair - Monitor carefully' if prediction < 70 else
                         'Excellent - Battery in good condition'}
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### Insights")
            
            ideal_range = battery_capacity * 5  
            estimated_range = ideal_range * (prediction / 100)
            
            st.markdown(f"**Estimated Range**: About {estimated_range:.0f} km on a full charge")
            
            # Factors affecting battery health
            factors = []
            if age > 5:
                factors.append("Vehicle age above 5 years")
            if charging_cycles > 1000:
                factors.append("High number of charging cycles")
            if fast_charging > 50:
                factors.append("Frequent fast charging")
            if avg_temp < 10 or avg_temp > 30:
                factors.append("Non-optimal operating temperature")
            
            if factors:
                st.markdown("**Key factors affecting battery health:**")
                for factor in factors:
                    st.markdown(f"- {factor}")
            else:
                st.markdown("**Your usage patterns are optimal for battery longevity.**")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
        except Exception as e:
            st.markdown(f"""
                <div class="info-box" style="border-left: 4px solid #f44336;">
                    <h3 style="color: #f44336;">Prediction Failed</h3>
                    <p>There was an error processing your request: {e}</p>
                    <p>Please check your inputs and try again.</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="info-box">
                <h3>Ready for Your Analysis</h3>
                <p>Fill in the vehicle details on the left panel and click "Generate Prediction" to get your assessment.</p>
                <div style="text-align: center; margin-top: 1rem;">
                    <img src="https://api.dicebear.com/7.x/bottts/svg?seed=battery2" alt="Battery" width="100" />
                </div>
            </div>
        """, unsafe_allow_html=True)

# Tips section
st.markdown("<h2>💡 Battery Care Tips</h2>", unsafe_allow_html=True)
tips_col1, tips_col2, tips_col3 = st.columns(3)

with tips_col1:
    st.markdown("""
        <div class="card">
            <h4>Charging Habits</h4>
            <ul>
                <li>Keep battery between 20-80% when possible</li>
                <li>Limit fast charging to when necessary</li>
                <li>Avoid charging to 100% daily</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with tips_col2:
    st.markdown("""
        <div class="card">
            <h4>Temperature Management</h4>
            <ul>
                <li>Park in shade during hot weather</li>
                <li>Use preconditioning when available</li>
                <li>Avoid extreme temperatures</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with tips_col3:
    st.markdown("""
        <div class="card">
            <h4>Driving Style</h4>
            <ul>
                <li>Use regenerative braking</li>
                <li>Avoid frequent hard acceleration</li>
                <li>Plan routes with charging in mind</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>This prediction is a machine learning estimate and may not reflect actual battery condition. For accurate diagnostics, consult certified EV professionals.</p>
        <p>© 2025 EV Battery Health Predictor - Data Science Capstone Project</p>
    </div>
""", unsafe_allow_html=True)