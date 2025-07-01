import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Load data
df = pd.read_csv("customer_segmentation_analysis/final_credit_card_data.csv")

# (Re-do feature engineering here, as above, or save processed file)

st.title("Credit Card Customer Insights Dashboard")

# --- KPI cards ---
st.subheader("Customer Segmentation")
st.write(df['customer_segment'].value_counts())

# --- Feature selection ---
feature = st.selectbox(
    "Choose a feature to visualize:",
    [
        'credit_utilization', 'payment_ratio', 'purchase_frequncy',
        'average_transaction_value', 'oneoff_purchase_ratio', 'installments_purchase_ratio'
    ]
)

# Histogram
st.plotly_chart(px.histogram(df, x=feature, nbins=40, color='customer_segment', marginal="box",
                             title=f"Distribution of {feature}"))

# Scatter plot
st.subheader("Explore Feature Relationships")
col1, col2 = st.columns(2)
with col1:
    xcol = st.selectbox("X-axis", features, key='x')
with col2:
    ycol = st.selectbox("Y-axis", features, key='y')

st.plotly_chart(px.scatter(
    df, x=xcol, y=ycol, color='customer_segment',
    hover_data=['credit_utilization', 'payment_ratio', 'customer_segment'],
    title=f"{xcol} vs {ycol} by Segment"
))

# Segment filter
segment = st.selectbox("Filter by Customer Segment", ['All'] + df['customer_segment'].unique().tolist())
if segment != 'All':
    dff = df[df['customer_segment'] == segment]
else:
    dff = df

st.dataframe(dff.head(50))

st.write("Tip: Use the feature and segment filters to discover customer behavior patterns.")
