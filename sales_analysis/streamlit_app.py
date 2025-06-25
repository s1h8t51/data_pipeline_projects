import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use full-width layout
st.set_page_config(layout="wide")

# Dashboard title
st.markdown("<h1 style='text-align: center;'>📊 Sales Insights Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# Load the dataset
url = "https://raw.githubusercontent.com/s1h8t51/data_analytics_projects/main/sales_analysis/corrected_data.csv"
df = pd.read_csv(url)

# KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Revenue", f"${df['revenue'].sum():,.0f}")
col2.metric("📦 Units Sold", f"{df['nb_sold'].sum():,}")
col3.metric("🌐 Avg. Site Visits", f"{df['nb_site_visits'].mean():.2f}")
col4.metric("👤 Unique Customers", df['customer_id'].nunique())

st.markdown("---")

# Row 1: Sales Method Types + Revenue Distribution
col1, col2 = st.columns(2)

with col1:
    st.subheader("🛍️ Sales Method Types")
    fig1, ax1 = plt.subplots(figsize=(5, 3))
    sns.barplot(x=df['sales_method'].value_counts().index,
                y=df['sales_method'].value_counts().values, ax=ax1)
    ax1.set_title("Sales Method Distribution", fontsize=10)
    ax1.set_xlabel("")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)

with col2:
    st.subheader("💸 Revenue Distribution by Sales Method")
    fig2 = plt.figure(figsize=(5, 3))
    sns.histplot(data=df, x='revenue', bins=30, kde=True, hue='sales_method', multiple='stack')
    plt.title("Revenue Distribution", fontsize=10)
    plt.xlabel("Revenue")
    plt.ylabel("Count")
    plt.tight_layout()
    st.pyplot(fig2)

# Row 2: Revenue by Method + Weekly Revenue Trend
col3, col4 = st.columns(2)

with col3:
    st.subheader("📊 Revenue by Sales Method")
    rev_by_method = df.groupby("sales_method")["revenue"].sum().reset_index()
    fig3, ax3 = plt.subplots(figsize=(5, 3))
    sns.barplot(data=rev_by_method, x="sales_method", y="revenue", ax=ax3)
    ax3.set_title("Total Revenue", fontsize=10)
    st.pyplot(fig3)

with col4:
    st.subheader("📈 Weekly Revenue Trend")
    weekly_rev = df.groupby(["week", "sales_method"])["revenue"].sum().reset_index()
    fig4, ax4 = plt.subplots(figsize=(5, 3))
    sns.lineplot(data=weekly_rev, x="week", y="revenue", hue="sales_method", marker="o", ax=ax4)
    ax4.set_title("Weekly Revenue", fontsize=10)
    st.pyplot(fig4)

# Row 3: Full-width Website Visits Chart
st.subheader("🌐 Website Visits Weekly (by Sales Method)")
weekly_visits = df.groupby(["week", "sales_method"])["nb_site_visits"].mean().reset_index()
fig5, ax5 = plt.subplots(figsize=(10, 3))
sns.lineplot(data=weekly_visits, x="week", y="nb_site_visits", hue="sales_method", marker="o", ax=ax5)
ax5.set_title("Website Visits Over Time", fontsize=10)
ax5.set_ylabel("Avg. Visits")
st.pyplot(fig5)
