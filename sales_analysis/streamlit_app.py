import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")  # Full-width layout

# Load your dataset
url = "https://raw.githubusercontent.com/s1h8t51/data_analytics_projects/main/sales_analysis/corrected_data.csv"
df = pd.read_csv(url)

st.title("📊 Sales Analysis Dashboard")

# KPIs on one row
st.markdown("### 🔑 Key Performance Indicators")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Revenue", f"${df['revenue'].sum():,.0f}")
kpi2.metric("Units Sold", f"{df['nb_sold'].sum():,}")
kpi3.metric("Avg. Site Visits", f"{df['nb_site_visits'].mean():.2f}")
kpi4.metric("Unique Customers", df['customer_id'].nunique())

# Row 1: Sales Method Types + Revenue Distribution
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🛒 Sales Method Types")
        sales_method_counts = df['sales_method'].value_counts().reset_index()
        sales_method_counts.columns = ['sales_method', 'count']
        fig1, ax1 = plt.subplots()
        sns.barplot(data=sales_method_counts, x='sales_method', y='count', ax=ax1)
        ax1.set_ylabel("Count")
        st.pyplot(fig1)

    with col2:
        st.markdown("### 💰 Revenue Distribution by Customer Segment")
        fig2, ax2 = plt.subplots()
        sns.histplot(data=df, x="revenue", hue="years_as_customer", multiple="stack", bins=20, ax=ax2)
        ax2.set_xlabel("Revenue")
        st.pyplot(fig2)

# Row 2: Revenue by Sales Method + Weekly Revenue
with st.container():
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### 📈 Total Revenue by Sales Method")
        revenue_sales_method = df.groupby("sales_method")["revenue"].sum().reset_index()
        fig3, ax3 = plt.subplots()
        sns.barplot(data=revenue_sales_method, x="sales_method", y="revenue", ax=ax3)
        st.pyplot(fig3)

    with col4:
        st.markdown("### 📊 Weekly Revenue by Sales Method")
        weekly_revenue = df.groupby(["week", "sales_method"])["revenue"].sum().reset_index()
        fig4, ax4 = plt.subplots()
        sns.lineplot(data=weekly_revenue, x="week", y="revenue", hue="sales_method", marker="o", ax=ax4)
        st.pyplot(fig4)

# Row 3: Site Visits by Sales Method
st.markdown("### 🌐 Website Visits Distribution by Sales Method")
site_visit_data = df.groupby(["week", "sales_method"])["nb_site_visits"].mean().reset_index()
fig5, ax5 = plt.subplots()
sns.lineplot(data=site_visit_data, x="week", y="nb_site_visits", hue="sales_method", marker="o", ax=ax5)
ax5.set_ylabel("Avg. Site Visits")
st.pyplot(fig5)
