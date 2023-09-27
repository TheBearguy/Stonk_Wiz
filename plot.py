import streamlit as st
import yfinance as yf
import pandas as pd

all_stocks = yf.Ticker("SPY").constituents

st.set_page_config(layout="wide")
st.title("Stock Dashboard")


stock_symbol = st.sidebar.selectbox("Select a stock:", all_stocks)


stock_data = yf.download(stock_symbol, period="1d")

st.header(stock_symbol)
st.write(stock_data.head()
