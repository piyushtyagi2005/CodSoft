🏦 Customer Churn Prediction Web App

This Streamlit-based web application predicts whether a customer is likely to churn (leave) or stay based on various input features like credit score, geography, age, balance, etc.

📌 Features

Clean, user-friendly Streamlit interface

Background color customization

Predicts churn using a pre-trained ML model (churn_prediction.pkl)

Displays results with confidence and visual cues (✅ stay / ⚠️ churn)

🚀 How to Run the App Locally
1. Clone or Download This Repository
bash
Copy
Edit
git clone https://github.com/your-username/churn-prediction-app.git
cd churn-prediction-app

2. Install Dependencies
Make sure you have Python installed (3.7+ recommended), then install:

bash
Copy
Edit
pip install streamlit numpy joblib

3. Run the App
bash
Copy
Edit
streamlit run app.py
The app will open in your default browser at http://localhost:8501.

📂 Files in This Project
File Name	Description
app.py	Main Streamlit app code
churn_prediction.pkl	Trained machine learning model
CHURN_PREDICTION.ipynb	Jupyter notebook used for training the model (optional)

📥 Input Fields
Customer ID

Credit Score

Geography

Gender

Age

Tenure

Balance

Number of Products

Has Credit Card

Is Active Member

Estimated Salary

📊 Model Output
✅ The customer is likely to STAY.

⚠️ The customer is likely to CHURN.

Prediction is also supported by a probability score (optional to show).

🧠 Model Info
Loaded using joblib

Trained on bank customer data

Uses logistic regression, decision tree, or other classifier (based on your notebook)

✨ Custom Styling
The app uses custom CSS to set a light blue background for better user experience.