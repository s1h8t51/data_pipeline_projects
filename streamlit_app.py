import streamlit as st
import pandas as pd

# Load your GitHub CSV
url = "https://raw.githubusercontent.com/s1h8t51/data_analytics_project/main/customer-churn-prediction-analytics/churn_predictions.csv"
df = pd.read_csv(url)

# Dashboard title
st.title("🔁 Customer Churn Prediction Dashboard")

# KPIs
total_customers = len(df)
churn_rate = df["Actual_Churn"].mean()
accuracy = (df["Actual_Churn"] == df["Predicted_Churn"]).mean()
high_risk_count = (df["Churn_Probability"] > 0.7).sum()

# KPI Display
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", total_customers)
col2.metric("Churn Rate", f"{churn_rate:.2%}")
col3.metric("Accuracy", f"{accuracy:.2%}")
col4.metric("High-Risk Customers", high_risk_count)

# Chart: Actual vs Predicted
st.subheader("📊 Actual vs Predicted Churn")
st.bar_chart(df[["Actual_Churn", "Predicted_Churn"]].value_counts().unstack(fill_value=0))

# Optional: Add filters and explore
st.subheader("🔍 Explore High-Risk Customers")
threshold = st.slider("Churn Probability Threshold", 0.0, 1.0, 0.7)
filtered = df[df["Churn_Probability"] > threshold]
st.dataframe(filtered)
