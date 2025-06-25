import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
url = "https://raw.githubusercontent.com/s1h8t51/data_analytics_projects/main/sales_analysis/corrected_data.csv"
df = pd.read_csv(url)

st.title("📊 Enhanced Sales Method Analysis Dashboard")

# KPI Section
st.markdown("### 🔑 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${df['revenue'].sum():,.0f}")
col2.metric("Units Sold", f"{df['nb_sold'].sum():,}")
col3.metric("Avg. Site Visits", f"{df['nb_site_visits'].mean():.2f}")
col4.metric("Unique Customers", df['customer_id'].nunique())

# 1. Sales Methods Overview
st.markdown("### 🛒 Sales Method Types")
sales_method_counts = df['sales_method'].value_counts().reset_index()
sales_method_counts.columns = ['sales_method', 'count']
fig1, ax1 = plt.subplots()
sns.barplot(data=sales_method_counts, x='sales_method', y='count', ax=ax1)
ax1.set_title("Sales Method Distribution")
ax1.set_ylabel("Count")
st.pyplot(fig1)

# 2. Revenue Distribution by Customer Segment (Years as Customer)
st.markdown("### 💰 Revenue Distribution by Customer Segment")
fig2, ax2 = plt.subplots()
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='revenue', bins=50, kde=True, hue='sales_method', multiple='stack')
plt.xlabel("Revenue")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
st.pyplot(fig2)

# 3. Revenue by Sales Method
st.markdown("### 📈 Total Revenue by Sales Method")
revenue_sales_method = df.groupby("sales_method")["revenue"].sum().reset_index()
fig3, ax3 = plt.subplots()
sns.boxplot(x='sales_method', y='revenue', data=df,hue="sales_method")
#plt.title("Revenue by Sales Method")
plt.show()
st.pyplot(fig3)

# 4. Weekly Revenue Trend by Sales Method
st.markdown("### 📊 Weekly Revenue by Sales Method")
weekly_revenue = df.groupby(["week", "sales_method"])["revenue"].sum().reset_index()
fig4, ax4 = plt.subplots()
plt.figure(figsize=(10, 6))
sns.violinplot(x='sales_method', y='years_as_customer', data=df, inner='quartile')
plt.title('Distribution of Customer Tenure by Sales Method')
plt.xlabel('Sales Method')
plt.ylabel('Years as Customer')
plt.tight_layout()
plt.show()
st.pyplot(fig4)

# 5. Site Visits Distribution by Sales Method
st.markdown("### 🌐 Website Visits Distribution by Sales Method")
site_visit_data = df.groupby(["week", "sales_method"])["nb_site_visits"].mean().reset_index()
fig5, ax5 = plt.subplots()
sns.boxplot(x='sales_method', y='nb_site_visits', data=df,hue="sales_method")
plt.title("Website Visits by Sales Method")
plt.show()
st.pyplot(fig5)
