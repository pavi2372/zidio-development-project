# app.py

# 📦 Importing required libraries
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import numpy as np

# 🎨 Configure the Streamlit page layout and title
st.set_page_config(page_title="Stock Dashboard", layout="wide")
st.title("📈 Stock Price Dashboard")

# 📁 Load dataset (must be in the same directory as app.py)
# 'Date' is parsed as a datetime and set as index for time series plotting
df = pd.read_csv("nasdq.csv", parse_dates=["Date"], index_col="Date")

# 🧾 Display all column names in the sidebar for clarity
st.sidebar.header("Dataset Info")
st.sidebar.write("Columns available in the dataset:", df.columns.tolist())

# 🧠 Select correct column for closing price (case-insensitive handling)
col_name = "close" if "close" in df.columns else "Close"

# 📊 Initialize a Plotly figure to display stock closing price over time
fig = go.Figure()

# 🟢 Add actual closing prices to the plot
fig.add_trace(go.Scatter(
    x=df.index,
    y=df[col_name],
    mode='lines',
    name='Actual Close',
    line=dict(color='blue')
))

# 🛠️ Customize the layout for better visual interpretation
fig.update_layout(
    title="Stock Price Over Time",
    xaxis_title="Date",
    yaxis_title="Stock Price (Closing)",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    template="plotly_white"
)

# 📈 Render the Plotly chart inside the Streamlit app
st.plotly_chart(fig, use_container_width=True)

# 🧾 Optional: Show a snapshot of the data table for user reference
st.subheader("📋 Data Preview")
st.dataframe(df.head(10))

st.set_page_config(page_title="Commodity Price Dashboard", layout="wide")
st.title("📈 Commodity Price Dashboard: Gold & Oil")


# ✅ Button to visualize monthly close
if st.button("📅 Show Monthly Close for Gold and Oil"):

    # 🧠 Resample monthly using last available value (end of month close)
    monthly_df = df[["Gold", "Oil"]].resample("M").last()

    # 🟡 Plot for Gold
    fig_gold = go.Figure()
    fig_gold.add_trace(go.Scatter(
        x=monthly_df.index,
        y=monthly_df["Gold"],
        mode='lines+markers',
        name='Gold Monthly Close',
        line=dict(color='gold')
    ))
    fig_gold.update_layout(
        title="Gold Monthly Closing Price",
        xaxis_title="Month",
        yaxis_title="Price",
        template="plotly_white"
    )
    st.plotly_chart(fig_gold, use_container_width=True)

    # 🛢️ Plot for Oil
    fig_oil = go.Figure()
    fig_oil.add_trace(go.Scatter(
        x=monthly_df.index,
        y=monthly_df["Oil"],
        mode='lines+markers',
        name='Oil Monthly Close',
        line=dict(color='black')
    ))
    fig_oil.update_layout(
        title="Oil Monthly Closing Price",
        xaxis_title="Month",
        yaxis_title="Price",
        template="plotly_white"
    )
    st.plotly_chart(fig_oil, use_container_width=True)

else:
    st.info("Click the button above to visualize monthly Gold and Oil prices.")
