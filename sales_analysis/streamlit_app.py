import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Full-width layout
st.set_page_config(layout="wide")

# Load the dataset
url = "https://raw.githubusercontent.com/s1h8t51/data_analytics_projects/main/sales_analysis/corrected_data.csv"
df = pd.read_csv(url)

st.title("📊  Sales Analysis Dashboard")

# 🔑 KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${df['revenue'].sum():,.0f}")
col2.metric("Units Sold", f"{df['nb_sold'].sum():,}")
col3.metric("Avg. Site Visits", f"{df['nb_site_visits'].mean():.2f}")
col4.metric("Unique Customers", df['customer_id'].nunique())

# 🛒 Sales Method Types & 💰 Revenue Distribution
col5, col6 = st.columns(2)
with col5:
    st.subheader("Sales Method Types")
    method_counts = df['sales_method'].value_counts().reset_index()
    method_counts.columns = ['sales_method', 'count']
    fig1, ax1 = plt.subplots(figsize=(5, 3))
    sns.barplot(data=method_counts, x='sales_method', y='count', ax=ax1)
    ax1.set_ylabel("Count")
    ax1.set_title("Sales Method Distribution")
    st.pyplot(fig1)

with col6:
    st.subheader("Revenue Distribution by Customer Segment")
    fig2 = plt.figure(figsize=(6, 4))
    sns.histplot(data=df, x='revenue', bins=30, kde=True, hue='sales_method', multiple='stack')
    plt.title("Revenue Distribution by Customer Segment")
    plt.xlabel("Revenue")
    plt.ylabel("Count")
    plt.tight_layout()
    st.pyplot(fig2)

# 📈 Revenue & 📉 Weekly Revenue by Sales Method
col7, col8 = st.columns(2)
with col7:
    st.subheader("Revenue by Sales Method")
    revenue_by_method = df.groupby("sales_method")["revenue"].sum().reset_index()
    fig3, ax3 = plt.subplots(figsize=5, 3))
    sns.barplot(data=revenue_by_method, x="sales_method", y="revenue", ax=ax3)
    ax3.set_title("Total Revenue by Sales Method")
    st.pyplot(fig3)

with col8:
    st.subheader("Weekly Revenue by Sales Method")
    weekly_revenue = df.groupby(["week", "sales_method"])["revenue"].sum().reset_index()
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    sns.lineplot(data=weekly_revenue, x="week", y="revenue", hue="sales_method", marker="o", ax=ax4)
    ax4.set_title("Weekly Revenue Trend")
    st.pyplot(fig4)

# 🌐 Website Visits Over Time
st.subheader("Website Visits by Sales Method (Weekly Average)")
site_visits = df.groupby(["week", "sales_method"])["nb_site_visits"].mean().reset_index()
fig5, ax5 = plt.subplots(figsize=(10, 4))
sns.lineplot(data=site_visits, x="week", y="nb_site_visits", hue="sales_method", marker="o", ax=ax5)
ax5.set_ylabel("Avg. Site Visits")
ax5.set_title("Weekly Site Visits by Sales Method")
st.pyplot(fig5)
