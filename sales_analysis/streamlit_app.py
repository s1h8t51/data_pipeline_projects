import streamlit as st
import pandas as pd

# Use RAW GitHub URL
url = "https://raw.githubusercontent.com/s1h8t51/data_analytics_projects/main/churn_predictions.csv"
df = pd.read_csv(url)

st.title("🔁 Customer Churn Prediction Dashboard")
st.dataframe(df.head())
