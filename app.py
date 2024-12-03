import streamlit as st

# Define emission factors and country averages
EMISSION_FACTORS = {
    "India": {
        "Transportation": 0.14,
        "Electricity": 0.82,
        "Diet": 1.25,
        "Waste": 0.1,
        "Average_Emissions": 1.9
    },
    "United States": {
        "Transportation": 0.19,
        "Electricity": 0.43,
        "Diet": 1.5,
        "Waste": 0.2,
        "Average_Emissions": 13.7
    },
    "China": {
        "Transportation": 0.16,
        "Electricity": 0.73,
        "Diet": 1.3,
        "Waste": 0.15,
        "Average_Emissions": 7.4
    },
    "Brazil": {
        "Transportation": 0.12,
        "Electricity": 0.10,
        "Diet": 1.2,
        "Waste": 0.08,
        "Average_Emissions": 2.2
    },
    "Germany": {
        "Transportation": 0.15,
        "Electricity": 0.33,
        "Diet": 1.4,
        "Waste": 0.12,
        "Average_Emissions": 7.8
    },
    "United Kingdom": {
        "Transportation": 0.17,
        "Electricity": 0.23,
        "Diet": 1.3,
        "Waste": 0.11,
        "Average_Emissions": 4.7
    },
    "Japan": {
        "Transportation": 0.13,
        "Electricity": 0.50,
        "Diet": 1.6,
        "Waste": 0.17,
        "Average_Emissions": 8.7
    },
    "Canada": {
        "Transportation": 0.18,
        "Electricity": 0.16,
        "Diet": 1.4,
        "Waste": 0.16,
        "Average_Emissions": 15.4
    },
    "Australia": {
        "Transportation": 0.20,
        "Electricity": 0.62,
        "Diet": 1.7,
        "Waste": 0.22,
        "Average_Emissions": 15.4
    },
    "Russia": {
        "Transportation": 0.16,
        "Electricity": 0.45,
        "Diet": 1.2,
        "Waste": 0.13,
        "Average_Emissions": 11.4
    },
    "France": {
        "Transportation": 0.14,
        "Electricity": 0.06,
        "Diet": 1.3,
        "Waste": 0.10,
        "Average_Emissions": 4.3
    },
    "Mexico": {
        "Transportation": 0.15,
        "Electricity": 0.37,
        "Diet": 1.1,
        "Waste": 0.09,
        "Average_Emissions": 3.4
    },
    "South Africa": {
        "Transportation": 0.17,
        "Electricity": 0.89,
        "Diet": 1.2,
        "Waste": 0.14,
        "Average_Emissions": 6.2
    },
    "South Korea": {
        "Transportation": 0.14,
        "Electricity": 0.41,
        "Diet": 1.5,
        "Waste": 0.16,
        "Average_Emissions": 11.6
    },
    "Indonesia": {
        "Transportation": 0.13,
        "Electricity": 0.67,
        "Diet": 1.1,
        "Waste": 0.07,
        "Average_Emissions": 2.3
    }
}

# Custom CSS for theme
st.markdown("""
<style>
:root {
    --dark-background: #121212;
    --dark-surface: #1E1E1E;
    --primary-green: #4CAF50;
    --text-primary: #FFFFFF;
    --text-secondary: #B0B0B0;
}

.stApp {
    background-color: var(--dark-background);
    color: var(--text-primary);
    font-family: 'Roboto', 'Arial', sans-serif;
    max-width: 1200px;
    margin: 0 auto;
}

.main .block-container {
    background-color: var(--dark-surface);
    padding: 2rem;
    border-radius: 15px;
    color: var(--text-primary);
}

/* Headings */
h1, h2, h3, h4 {
    color: var(--primary-green);
    font-weight: 600;
    text-align: center;
}

/* Buttons */
.stButton>button {
    background-color: var(--primary-green);
    color: var(--text-primary);
    border: none;
    padding: 10px 24px;
    border-radius: 20px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}

.stButton>button:hover {
    background-color: #45a049;
    transform: translateY(-2px);
}

/* Inputs and Selectors */
.stSelectbox>div>div {
    background-color: var(--dark-surface);
    color: var(--text-primary);
    border-radius: 15px;
    border: 1px solid var(--primary-green);
}

.stSlider>div>div>div {
    background-color: var(--primary-green);
}

/* Information Boxes */
.stInfo, .stSuccess, .stWarning {
    border-radius: 15px;
    padding: 15px;
    margin-bottom: 15px;
    background-color: var(--dark-surface);
    color: var(--text-primary);
    border-left: 6px solid var(--primary-green);
}

.stInfo {
    border-color: #2196F3;
}

.stSuccess {
    border-color: var(--primary-green);
}

.stWarning {
    border-color: #FFC107;
}

/* Responsive Typography */
* {
    font-size: 16px;
    line-height: 1.6;
    color: var(--text-primary);
}

h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.75rem; }
</style>
""", unsafe_allow_html=True)

# Set wide layout and page name
# st.set_page_config(layout="wide", page_title="🌍 Carbon Footprint Calculator", page_icon="🌿")

# Streamlit app code
st.title("🌿 Personal Carbon Footprint Calculator")
st.subheader("Understand and Minimize Your Environmental Impact")

# User inputs
st.markdown("## 🌍 Select Your Country")
country = st.selectbox("Choose your country", list(EMISSION_FACTORS.keys()), 
                       help="Select the country you're calculating emissions for")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🚗 Daily Commute")
    distance = st.slider("Daily travel distance (km)", 0.0, 100.0, key="distance_input", 
                         help="How many kilometers do you travel daily?")
    
    st.markdown("### 💡 Electricity Consumption")
    electricity = st.slider("Monthly electricity usage (kWh)", 0.0, 1000.0, key="electricity_input", 
                            help="How much electricity do you consume monthly?")

with col2:
    st.markdown("### 🗑️ Weekly Waste")
    waste = st.slider("Waste generated per week (kg)", 0.0, 100.0, key="waste_input", 
                      help="How many kilograms of waste do you produce weekly?")
    
    st.markdown("### 🍽️ Daily Meals")
    meals = st.number_input("Number of meals per day", 0, 10, key="meals_input", 
                            help="How many meals do you have daily?")

# Normalize inputs
distance = distance * 365 if distance > 0 else 0
electricity = electricity * 12 if electricity > 0 else 0
meals = meals * 365 if meals > 0 else 0
waste = waste * 52 if waste > 0 else 0

# Calculate carbon emissions
transportation_emissions = round(EMISSION_FACTORS[country]["Transportation"] * distance / 1000, 2)
electricity_emissions = round(EMISSION_FACTORS[country]["Electricity"] * electricity / 1000, 2)
diet_emissions = round(EMISSION_FACTORS[country]["Diet"] * meals / 1000, 2)
waste_emissions = round(EMISSION_FACTORS[country]["Waste"] * waste / 1000, 2)

# Calculate total emissions
total_emissions = round(
    transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
)

if st.button("🔍 Calculate My Carbon Footprint"):
    # Results section
    st.header("🌍 Your Carbon Footprint Analysis")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("### 📊 Emissions Breakdown")
        st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2/year")
        st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2/year")
        st.info(f"🍽️ Diet: {diet_emissions} tonnes CO2/year")
        st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2/year")
    
    with col4:
        st.markdown("### 🌐 Total Impact")
        st.success(f"Total Carbon Footprint: {total_emissions} tonnes CO2/year")
        
        # Compare with country average
        country_avg = EMISSION_FACTORS[country]["Average_Emissions"]
        difference = round(abs(total_emissions - country_avg), 2)
        
        if total_emissions > country_avg:
            st.warning(f"Your footprint is {difference} tonnes above the country average of {country_avg} tonnes CO2/year.")
        elif total_emissions < country_avg:
            st.success(f"Your footprint is {difference} tonnes below the country average of {country_avg} tonnes CO2/year.")
        else:
            st.info(f"Your footprint matches the country average of {country_avg} tonnes CO2/year.")
        
        # Reduction Strategies
        st.header("🌱 Reduction Strategies")
        st.markdown("""
        #### Quick Tips to Lower Your Carbon Footprint
        - 🚲 **Transportation**: Use public transit, carpool, bike
        - 💡 **Energy**: Switch to LED, unplug unused devices
        - 🥗 **Diet**: Eat more plant-based, local foods
        - ♻️ **Waste**: Reduce, reuse, recycle
        """)