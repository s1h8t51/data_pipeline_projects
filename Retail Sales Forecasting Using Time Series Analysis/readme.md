# 📈 Sales Forecast Dashboard

This project is a dynamic **Streamlit-based web dashboard** that allows users to interactively explore **weekly sales forecasts** for different **Store** and **Department** combinations.

It supports three forecasting models:
- 🔮 **Prophet** (by Facebook)
- 📊 **SARIMA** (statistical model)
- 🤖 **XGBoost** (machine learning model)

---

## 🚀 Features

- 📌 **Interactive dropdowns** to select `Store ID` and `Dept ID`
- 📈 **Forecast comparison plots** across Prophet, SARIMA, and XGBoost
- 💾 **Downloadable CSV** for selected forecasts
- 📊 **Tabular data view** of weekly sales predictions

---

## 🖥️ Demo

https://user-streamlit-demo-link (replace this with your actual URL if deployed)

---

## 🧰 Tech Stack

| Tool        | Role                           |
|-------------|--------------------------------|
| Python      | Main programming language      |
| Streamlit   | Interactive web dashboard      |
| Pandas      | Data manipulation              |
| Matplotlib  | Plotting                       |
| Prophet     | Time series forecasting (trend + seasonality) |
| Statsmodels | SARIMA implementation          |
| XGBoost     | Machine learning predictions   |

---

## 📂 File Structure

```bash
.
├── streamlit_app.py        # Main Streamlit dashboard
├── final_forecast.csv      # Forecast data (Prophet, SARIMA, XGBoost)
├── sales_forecast.ipynb    # Jupyter notebook with modeling code
├── README.md               # This file
└── requirements.txt        # Dependencies
