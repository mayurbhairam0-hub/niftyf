import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# App title
st.title("📈 NSE Stock Price Viewer")

# Load data
df = pd.read_csv('../yfinance_Project/stock_nse.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Show raw data (optional)
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Stock selection dropdown
stock_list = df['Stock'].unique()
st.sidebar.header("Select Stock")
st_name = st.sidebar.selectbox("Stock Name", stock_list)

# Filter data
r = df[df['Stock'] == st_name]

# Plot
st.subheader(f"Closing Price Trend for {st_name}")

fig, ax = plt.subplots()
sb.lineplot(x=r['Date'], y=r['Close'], ax=ax)
ax.set_xlabel("Date")
ax.set_ylabel("Close Price")

st.pyplot(fig)
