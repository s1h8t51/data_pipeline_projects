import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from prophet import Prophet
from sklearn.metrics import mean_squared_error
import numpy as np
import os
# Load data
st.set_page_config(layout="wide")

base_path = os.path.dirname(__file__)
df_path = os.path.join(base_path, "walmart_df.csv")
test_path = os.path.join(base_path, "test.csv")

walmart_df = pd.read_csv(df_path, parse_dates=["Date"])
test = pd.read_csv(test_path, parse_dates=["Date"])


st.title("📈 Walmart Weekly Sales Forecast Dashboard")
st.markdown("""
This dashboard shows time series forecasts of weekly sales using **Prophet** and **SARIMA** models. Select Store and Department to run the models and view results.
""")

# Sidebar filters
store_ids = sorted(walmart_df['Store'].unique())
dept_ids = sorted(walmart_df['Dept'].unique())

selected_store = st.sidebar.selectbox("🏬 Select Store ID", store_ids)
selected_dept = st.sidebar.selectbox("📦 Select Department ID", dept_ids)

run_forecast = st.sidebar.button("🔮 Run Forecast")

if run_forecast:
    # Filtered data
    train_sd = walmart_df[(walmart_df['Store'] == selected_store) & (walmart_df['Dept'] == selected_dept)].copy()
    test_sd = test[(test['Store'] == selected_store) & (test['Dept'] == selected_dept)].copy().sort_values('Date').reset_index(drop=True)

    if len(train_sd) < 30 or len(test_sd) == 0:
        st.warning("No forecast data available for this Store–Dept combination.")
    else:
        # --- Prophet Forecast ---
        prophet_model_df = train_sd[['Date', 'Weekly_Sales']].rename(columns={'Date': 'ds', 'Weekly_Sales': 'y'})
        model_prophet = Prophet()
        model_prophet.fit(prophet_model_df)
        future = model_prophet.make_future_dataframe(periods=len(test_sd), freq='W')
        prophet_forecast_full = model_prophet.predict(future)
        prophet_forecast = prophet_forecast_full[['ds', 'yhat']].tail(len(test_sd)).rename(columns={'ds': 'Date', 'yhat': 'Prophet'})

        # --- SARIMA Forecast ---
        train_sd['Date'] = pd.to_datetime(train_sd['Date']) 
        train_series = train_sd.set_index('Date')['Weekly_Sales'].asfreq('W-FRI').ffill()

        sarima_model = sm.tsa.SARIMAX(train_series,
                                      order=(1, 1, 1),
                                      seasonal_order=(0, 1, 0, 52),
                                      enforce_stationarity=False,
                                      enforce_invertibility=False)
        sarima_result = sarima_model.fit(disp=False)

        test_dates = test_sd['Date']
        start_date = test_dates.min()
        end_date = test_dates.max()
        pred_sarima = sarima_result.predict(start=start_date, end=end_date)

        sarima_forecast = test_sd[['Date']].copy()
        sarima_forecast['SARIMA'] = pred_sarima.values

        # --- Merge Forecasts ---
        comparison = test_sd[['Date']].copy()
        comparison['Prophet'] = prophet_forecast['Prophet'].values
        comparison['SARIMA'] = sarima_forecast['SARIMA'].values
        # --- Evaluation Section ---
        # Merge actual sales into comparison
        comparison = comparison.merge(test_sd[['Date', 'Weekly_Sales']], on='Date', how='left')
        
        # Evaluate model accuracy
        from sklearn.metrics import mean_absolute_error, mean_squared_error
        
        prophet_rmse = mean_squared_error(comparison['Weekly_Sales'], comparison['Prophet'], squared=False)
        sarima_rmse = mean_squared_error(comparison['Weekly_Sales'], comparison['SARIMA'], squared=False)
        
        prophet_mae = mean_absolute_error(comparison['Weekly_Sales'], comparison['Prophet'])
        sarima_mae = mean_absolute_error(comparison['Weekly_Sales'], comparison['SARIMA'])
        
        # Display metrics
        st.subheader("📊 Model Evaluation Metrics")
        st.write(f"**Prophet RMSE:** {prophet_rmse:,.2f} | **MAE:** {prophet_mae:,.2f}")
        st.write(f"**SARIMA RMSE:** {sarima_rmse:,.2f} | **MAE:** {sarima_mae:,.2f}")
        
        # Determine best model
        better_model = "Prophet" if prophet_rmse < sarima_rmse else "SARIMA"
        st.success(f"✅ Based on RMSE, **{better_model}** performs better for Store {selected_store}, Dept {selected_dept}.")
        
        # Optional: RMSE Bar Chart
        st.subheader("📊 RMSE Comparison")
        fig_rmse, ax_rmse = plt.subplots()
        ax_rmse.bar(["Prophet", "SARIMA"], [prophet_rmse, sarima_rmse], color=["red", "green"])
        ax_rmse.set_ylabel("RMSE")
        ax_rmse.set_title("Root Mean Squared Error by Model")
        st.pyplot(fig_rmse)


        # KPIs
        total_sales = comparison['Prophet'].sum()
        peak_date = comparison.loc[comparison['Prophet'].idxmax(), 'Date']
        st.metric(label="📊 Total Forecasted Sales (Prophet)", value=f"${total_sales:,.0f}")
        st.metric(label="📅 Peak Forecast Week", value=f"{peak_date.date()}")

        # Prophet Plot
        st.subheader("📈 Prophet Forecast")
        fig1, ax1 = plt.subplots(figsize=(10, 4))
        ax1.plot(train_sd['Date'], train_sd['Weekly_Sales'], label='Train Sales', color='blue')
        ax1.plot(comparison['Date'], comparison['Prophet'], label='Prophet Forecast', color='red', linestyle='--')
        ax1.axvline(x=train_sd['Date'].max(), color='gray', linestyle=':')
        ax1.legend()
        ax1.grid(True)
        st.pyplot(fig1)

        # Prophet Components
        st.subheader("🧩 Prophet Components")
        fig_comp = model_prophet.plot_components(prophet_forecast_full)
        st.pyplot(fig_comp)

        # SARIMA Plot
        st.subheader("📈 SARIMA Forecast")
        fig2, ax2 = plt.subplots(figsize=(10, 4))
        ax2.plot(train_sd['Date'], train_sd['Weekly_Sales'], label='Train Sales', color='blue')
        ax2.plot(sarima_forecast['Date'], sarima_forecast['SARIMA'], label='SARIMA Forecast', color='green', linestyle='--')
        ax2.axvline(x=train_sd['Date'].max(), color='gray', linestyle=':')
        ax2.legend()
        ax2.grid(True)
        st.pyplot(fig2)

        # Comparison Plot
        st.subheader("⚖️ Prophet vs SARIMA Forecast Comparison")
        fig3, ax3 = plt.subplots(figsize=(10, 4))
        ax3.plot(comparison['Date'], comparison['Prophet'], label='Prophet', color='red')
        ax3.plot(comparison['Date'], comparison['SARIMA'], label='SARIMA', color='green')
        ax3.set_title("Model Forecast Comparison")
        ax3.grid(True)
        ax3.legend()
        st.pyplot(fig3)

        # Forecast Table
        st.subheader("📋 Forecast Table")
        st.dataframe(comparison)

        # Download CSV
        csv = comparison.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Forecast CSV", data=csv, file_name=f"forecast_Store{selected_store}_Dept{selected_dept}.csv", mime='text/csv')
