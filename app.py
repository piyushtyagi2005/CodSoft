import streamlit as st
import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
st.set_page_config(page_title="SMS Spam Classifier")
st.title("SMS Spam Detection App")
st.write("Enter an SMS message and find out if it's spam or not.")

input = st.text_area("Type your message here", height=150)

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
