pip install plotly
import streamlit as st
import pickle
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

# Define a function to load the model and apply the st.cache decorator
@st.cache(allow_output_mutation=True)
def load_model():
    with open('stock_prediction(2).pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Function to get stock data
def get_stock_data(symbol):
    # You need to implement this function to retrieve stock data for the given symbol
    # Replace this with your code to fetch stock data
    return stock_data

# Function to create candlestick chart
def create_candlestick_chart(stock_data):
    fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                         open=stock_data['Open'],
                                         high=stock_data['High'],
                                         low=stock_data['Low'],
                                         close=stock_data['Close'])])
    fig.update_layout(xaxis_rangeslider_visible=False,
                      title=f'Candlestick Chart for {symbol}',
                      xaxis_title='Date',
                      yaxis_title='Price')
    return fig

# Load the pickled model using the cached function
model = load_model()

# Main application title
st.title('Stock Time Series and Sentiment Analysis')

# User input for ticker symbol
symbol = st.text_input("Enter a ticker symbol", "")

# Main area for displaying output
if symbol:
    try:
        # Get stock data
        stock_data = get_stock_data(symbol)

        # Create candlestick chart
        fig_candlestick = create_candlestick_chart(stock_data)
        st.plotly_chart(fig_candlestick)

        # Use the model to predict based on user input
        # You need to replace this with your actual prediction logic
        prediction_result = model.predict(symbol)

        # Display the prediction result
        st.write("Recommended stocks for investment:")
        for result in prediction_result:
            st.write(f"Symbol: {result['symbol']}, Sentiment: {result['sentiment']:.2f}, Latest Close Price: ${result['latest_close_price']:.2f}")

    except Exception as e:
        st.error(f"An error occurred: {e}")
