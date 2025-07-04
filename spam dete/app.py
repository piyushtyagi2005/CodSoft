import streamlit as st
import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
st.set_page_config(page_title="SMS Spam Classifier")

st.title("SMS Spam Detection")
st.write("Enter an SMS message and find out it is spam or not.")

input = st.text_area("Type your message here", height=150)

# Add background image with CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://tse4.mm.bing.net/th/id/OIP.H7BqAyfUGtXNLurdesID9gHaEo?pid=Api&P=0&h=180");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("Predict"):
    if input.strip() == "":
        st.warning("Please enter a message.")
    else:
        vect_input = vectorizer.transform([input])
        prediction = model.predict(vect_input)[0]
        
        if prediction == 1:
            st.error("This message is SPAM.")
        else:
            st.success("This message is NOT SPAM (Ham).")
