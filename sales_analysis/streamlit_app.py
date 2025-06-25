import streamlit as st
import pandas as pd

# Load dataset from GitHub (raw URL)
url = "https://raw.githubusercontent.com/s1h8t51/data_analytics_projects/main/churn_predictions.csv"
df = pd.read_csv(url)

# Title and preview
st.title("🔁 Customer Churn Prediction Dashboard")
st.dataframe(df.head())

# KPIs
total_customers = len(df)
churn_rate = df["Actual_Churn"].mean()
accuracy = (df["Actual_Churn"] == df["Predicted_Churn"]).mean()
high_risk_count = (df["Churn_Probability"] > 0.7).sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", total_customers)
col2.metric("Churn Rate", f"{churn_rate:.2%}")
col3.metric("Accuracy", f"{accuracy:.2%}")
col4.metric("High Risk", high_risk_count)

# Chart
st.subheader("📊 Churn Rate by Prediction")
chart_df = df.groupby(["Actual_Churn", "Predicted_Churn"]).size().unstack(fill_value=0)
st.bar_chart(chart_df)

# High-risk filter
st.subheader("📋 High-Risk Customers (Churn Probability > Threshold)")
threshold = st.slider("Select Threshold", 0.0, 1.0, 0.7)
st.dataframe(df[df["Churn_Probability"] > threshold].reset_index(drop=True))
