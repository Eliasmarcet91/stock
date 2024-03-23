import streamlit as st
import pickle
import matplotlib.pyplot as plt
import numpy as np

# Define a function to load the model and apply the st.cache decorator
@st.cache(allow_output_mutation=True)
def load_model():
    with open('stock_prediction(2).pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Load the pickled model using the cached function
model = load_model()

# Main application title
st.title('Stock Time Series and Sentiment Analysis')

# User input for word or sentence
user_input = st.text_input("Enter a word or sentence from the movie American Psycho to get its vector:", "")
