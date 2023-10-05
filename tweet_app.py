import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

#load the trained model
model = load_model('NLP_model.h5')

#load tokenizer
with open('tokenizer.pkl',"rb") as tk:
    tokenizer = pickle.load(tk)

# define function to preprocess text
def preprocess_text(texts):
    # tokenize the text
    tokens =tokenizer.texts_to_sequences([texts])

    # pad the sequence to a fixed lenght
    padded_tokens = pad_sequences(tokens, maxlen=100)

    return padded_tokens[0]

# Create title of the app
st.title("Sentiment Analysis APP")

# create text widget for user input
user_input  = st.text_area("Enter text for sentiment analysis", " ")

# create a button to trigger the sentiment analysis
if st.button("Predict Sentiment"):
    # preprocess the user input
    preprocessed_input = preprocess_text(user_input)

    # make prediction using the loaded model
    prediction = model.predict(np.array([preprocessed_input]))

    class_labels = {-1: "Negetive", 0: "Neutral", 1: "Positive"}

    # find the index of the highest prediction
    predicted_class_index = np.argmax(prediction)

    # get the corressponding class label
    predicted_class_label = class_labels[predicted_class_index]

    # display the result
    st.write(f"### Predicted Sentiment: {predicted_class_label}")