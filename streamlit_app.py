import streamlit as st
import pandas as pd

# Load CSV from GitHub
url = "https://raw.githubusercontent.com/s1h8t51/data_analytics_projects/0870241b44736bcebd9720438a979da2fc517706/churn_predictions.csv"
df = pd.read_csv(url)

# Title
st.title("🔁 Customer Churn Prediction Dashboard")

# KPIs
total_customers = len(df)
churn_rate = df["Actual_Churn"].mean()
accuracy = (df["Actual_Churn"] == df["Predicted_Churn"]).mean()
high_risk_count = (df["Churn_Probability"] > 0.7).sum()

# Display KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", total_customers)
col2.metric("Churn Rate", f"{churn_rate:.2%}")
col3.metric("Model Accuracy", f"{accuracy:.2%}")
col4.metric("High-Risk Customers", high_risk_count)

# Bar Chart: Actual vs Predicted
st.subheader("📊 Actual vs Predicted Churn")
churn_matrix = df.groupby(["Actual_Churn", "Predicted_Churn"]).size().unstack(fill_value=0)
st.bar_chart(churn_matrix)

# High-Risk Customer Table
st.subheader("📋 High-Risk Customer Details")
threshold = st.slider("Churn Probability Threshold", 0.0, 1.0, 0.7)
filtered_df = df[df["Churn_Probability"] > threshold]
st.write(f"Showing {len(filtered_df)} high-risk customers (Churn Probability > {threshold}):")
st.dataframe(filtered_df.reset_index(drop=True))
