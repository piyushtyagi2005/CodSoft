📱 Spam SMS Detection using Naive Bayes


This project is a machine learning application that classifies SMS messages as spam or ham (not spam) using the Naive Bayes algorithm. The model is trained on a labeled dataset and uses TF-IDF vectorization to convert text data into numerical features.


🔍 Project Overview
Goal: Automatically detect spam SMS messages.


Algorithm: Multinomial Naive Bayes

Tech stack: Python, Scikit-learn, Pandas, Streamlit

Dataset: SMS Spam Collection Dataset (Kaggle)


⚙️ How It Works

Data Cleaning: Remove stopwords, punctuation, and lowercase all words.

Feature Extraction: Convert text to numeric using TF-IDF vectorization.

Model Training: Train a Naive Bayes classifier.

Prediction: Input a new SMS message to classify it as spam or ham.


🚀 Getting Started

Prerequisites
Make sure you have Python installed. Then install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
Running the App
To launch the Streamlit web app:

bash
Copy
Edit
streamlit run app.py
🧪 Example
Input:

"You have won ?1,000 cash or a ?2,000 prize! To claim, call09050000327"

Output:

Spam


🧠 Model Used


TF-IDF Vectorizer: Converts text into numerical format based on term importance.

Multinomial Naive Bayes: A probabilistic classifier best suited for text classification.


📊 Evaluation
Accuracy: ~98%

Precision/Recall/F1: Evaluated using test set.


##How to run


-Open app.py file on vs code
-open terminal
-write streamlit run app.py
-output will come with beautiful interface
