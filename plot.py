
import streamlit as st
import plotly.graph_objects as go
import requests
import pandas as pd

crypto_api_url = "https://api.example.com/cryptostocks"


st.title("Crypto Stock Visualization App")


response = requests.get(crypto_api_url)
crypto_data = response.json()


df = pd.DataFrame(crypto_data)


st.sidebar.header("Select Cryptocurrency")

selected_crypto = st.sidebar.selectbox("Select a cryptocurrency",)
selected_data = df[df["Symbol"] == selected_crypto]

# Display candlestick chart
st.subheader("Candlestick Chart")
fig = go.Figure(data=[go.Candlestick(
    x=selected_data['Date'],
    open=selected_data['Open'],
    high=selected_data['High'],
    low=selected_data['Low'],
    close=selected_data['Close']
)])
st.plotly_chart(fig)

# Display line chart
st.subheader("Line Chart")
fig_line = go.Figure()
fig_line.add_trace(go.Scatter(x=selected_data['Date'], y=selected_data['Close'], mode='lines', name='Close Price'))
st.plotly_chart(fig_line)

# Display the selected data
st.subheader(f"Selected {selected_crypto} Data")
st.write(selected_data)
