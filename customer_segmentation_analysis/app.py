import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

# Load data (adjust path as needed)
df = pd.read_csv("customer_segmentation_analysis/final_credit_card_data.csv")

st.title("Credit Card Customer Insights Dashboard")

# --- KPI cards ---
st.subheader("Customer Segmentation")
if 'customer_segment' in df.columns:
    st.write(df['customer_segment'].value_counts())
else:
    st.warning("customer_segment column not found. Please add customer segmentation to your data.")

# --- Feature selection for histogram (fixed list, or you can use dynamic list) ---
feature_list = [
    'credit_utilization', 'payment_ratio', 'purchase_frequncy',
    'average_transaction_value', 'oneoff_purchase_ratio', 'installments_purchase_ratio'
]
available_features = [f for f in feature_list if f in df.columns]
if not available_features:
    st.error("No engineered features found in data.")
else:
    feature = st.selectbox(
        "Choose a feature to visualize:",
        available_features
    )

    # Histogram
    st.plotly_chart(px.histogram(df, x=feature, nbins=40, color='customer_segment' if 'customer_segment' in df.columns else None, marginal="box",
                                 title=f"Distribution of {feature}"))

# --- Scatter plot: auto-detect all numeric columns except 'ID' or similar ---
numeric_cols = [col for col in df.select_dtypes(include=np.number).columns if col.lower() not in ['id', 'accountno']]
if len(numeric_cols) >= 2:
    st.subheader("Explore Feature Relationships")
    col1, col2 = st.columns(2)
    with col1:
        xcol = st.selectbox("X-axis", numeric_cols, key='x')
    with col2:
        ycol = st.selectbox("Y-axis", numeric_cols, key='y')

    st.plotly_chart(px.scatter(
        df, x=xcol, y=ycol, color='customer_segment' if 'customer_segment' in df.columns else None,
        hover_data=['credit_utilization', 'payment_ratio', 'customer_segment'] if 'customer_segment' in df.columns else None,
        title=f"{xcol} vs {ycol} by Segment"
    ))
else:
    st.warning("Not enough numeric columns for scatter plot.")

# --- Segment filter and data table ---
if 'customer_segment' in df.columns:
    segment = st.selectbox("Filter by Customer Segment", ['All'] + sorted(df['customer_segment'].unique().tolist()))
    if segment != 'All':
        dff = df[df['customer_segment'] == segment]
    else:
        dff = df
    st.dataframe(dff.head(50))
else:
    st.dataframe(df.head(50))

st.write("Tip: Use the feature and segment filters to discover customer behavior patterns.")
