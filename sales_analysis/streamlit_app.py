import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV from GitHub raw link
url = "https://raw.githubusercontent.com/s1h8t51/data_analytics_projects/23a7804e005ac9aaae5fe945c34964a548b1a0f1/sales_analysis/corrected_data.csv"
df = pd.read_csv(url)

# Title and preview
st.title("📊 Customer Churn Prediction Dashboard")
st.write("Data Preview:")
st.dataframe(df.head())

# KPIs
total_customers = len(df)
churn_rate = df["Actual_Churn"].mean()
accuracy = (df["Actual_Churn"] == df["Predicted_Churn"]).mean()
high_risk_count = (df["Churn_Probability"] > 0.7).sum()

st.markdown("### 🔑 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", total_customers)
col2.metric("Churn Rate", f"{churn_rate:.2%}")
col3.metric("Accuracy", f"{accuracy:.2%}")
col4.metric("High-Risk Customers", high_risk_count)

# Bar Chart: Actual vs Predicted Churn
st.markdown("### 📉 Actual vs Predicted Churn")
churn_counts = df.groupby(["Actual_Churn", "Predicted_Churn"]).size().unstack(fill_value=0)
st.bar_chart(churn_counts)

# Distribution of Churn Probability
st.markdown("### 📈 Churn Probability Distribution")
fig, ax = plt.subplots()
sns.histplot(df["Churn_Probability"], bins=20, kde=True, color='orange', ax=ax)
st.pyplot(fig)

# High-risk filtering
st.markdown("### 🔍 High-Risk Customers Table")
threshold = st.slider("Churn Probability Threshold", 0.0, 1.0, 0.7)
high_risk_df = df[df["Churn_Probability"] > threshold]
st.write(f"Filtered to {len(high_risk_df)} customers above threshold:")
st.dataframe(high_risk_df.reset_index(drop=True))
