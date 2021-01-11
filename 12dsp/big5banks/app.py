import yfinance as yf
import streamlit as st
import pandas as pd 
import altair as alt

st.write("""
    # Stock Price app - Big 5 Banks
    Shown are the closing stock prices and volume of the largest banks in Canada:


        -Bank of Montreal (BMO)
        -Bank of Nova Scotia (BNS)
        -CIBC (CM-PQ.TO)
        -Royal Bank (RBC)
        -Toronto Dominion (TD)

    Period: December 31, 2019 - December 31, 2020

""")

symbol_list = ['BMO.TO', 'BNS', 'RBC', 'CM-PQ.TO', 'TD']
start_date = '2019-12-31'
end_date = '2020-12-31'
ticker_dfs = []

for i, sym in enumerate(symbol_list):
    print(sym)
    
    tickerData = yf.Ticker(sym)
    ticker_df = tickerData.history(period='1d', start=start_date, end=end_date).reset_index()
    print("---")
    ticker_df['Symbol'] = sym
    ticker_dfs.append(ticker_df)

data = pd.concat(ticker_dfs)

close_chart = alt.Chart(data).mark_line().encode(
    x='Date',
    y='Close',
    color='Symbol',
).properties(
    width=725,
    height=300
)

vol_chart = alt.Chart(data).mark_line().encode(
    x='Date',
    y='Volume',
    color='Symbol',
).properties(
    width=725,
    height=300
)

combined_chart = alt.vconcat(close_chart, vol_chart)

st.altair_chart(combined_chart)
