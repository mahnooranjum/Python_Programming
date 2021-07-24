import yfinance as yf
import streamlit as st

"""
    Reference: The Data Professor (http://youtube.com/dataprofessor)

"""

st.write("""
# Stock Price App

## Coinbase 

What's up with the billion dollar crytocurrency ecosystem? 

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'COIN'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2017-5-31', end='2021-7-15')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.area_chart(tickerDf.Volume)
