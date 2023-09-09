import streamlit as st
import requests
import plotly.express as px
import pandas as pd
import numpy as np
from JSONToDF import JSONToDF



API_KEY = "ZRRO9VW6CVON92DZ"

# App title
st.title('Stonks')

symbol = st.text_input('Enter your stonk: eg: APPL for Apple Stonk')

if st.button('Predict'):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}.BSE&outputsize=full&apikey={API_KEY}"
    response = requests.get(url)
    json_data = response.json()
    print(json_data)







    #Print(data)
    #st.write(data)
    #print(data)
    # if data['status'] == 'OK':
    #     result  = data["results"][0]
    #     st.write(f"**{symbol}** Stock Price Prediction:")
    #     st.write(f"Open: ${result['o']}")
    #     st.write(f"Close: ${result['c']}")
    #     st.write(f"High: ${result['h']}")
    #     st.write(f"Low: ${result['l']}")
    # else:
    #     st.write("Invalid symbol or an error occurred.")

