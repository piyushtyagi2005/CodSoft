import streamlit as st
import numpy as np
import joblib

# Load your model
model = joblib.load("churn_prediction.pkl")

# Page config
st.set_page_config(page_title="Bank Churn Prediction", layout="centered")
st.title("🏦 Customer Churn Prediction")
st.markdown("Provide customer details to predict churn risk.")

# Add custom background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: lightpink;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Input fields
customer_id = st.number_input("Customer ID", min_value=10000000, max_value=99999999, value=15634602)
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 18, 100, 40)
tenure = st.slider("Tenure (Years)", 0, 10, 3)
balance = st.number_input("Account Balance", min_value=0.0, value=50000.0)
products = st.selectbox("Number of Products", [1, 2, 3, 4])
has_card = st.selectbox("Has Credit Card?", ["Yes", "No"])
active_member = st.selectbox("Is Active Member?", ["Yes", "No"])
salary = st.number_input("Estimated Salary", min_value=0.0, value=100000.0)

# Encode categorical inputs
gender_encoded = 1 if gender == "Male" else 0
geography_encoded = {"France": 0, "Spain": 1, "Germany": 2}[geography]
has_card_encoded = 1 if has_card == "Yes" else 0
active_encoded = 1 if active_member == "Yes" else 0

# Final input (11 features)
input_data = np.array([[
    customer_id,
    credit_score,
    geography_encoded,
    gender_encoded,
    age,
    tenure,
    balance,
    products,
    has_card_encoded,
    active_encoded,
    salary
]])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error("⚠️ The customer is likely to **CHURN**.")
    else:
        st.success("✅ The customer is likely to **STAY**.")
    st.metric("Churn Probability", f"{probability:.2%}")

