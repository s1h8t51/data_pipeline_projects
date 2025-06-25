
# 📊 Sales Analysis Dashboard

This project is based on a real-world dataset provided in a certification exam as part of the **Professional Data Analyst Certification** on DataCamp. The objective was to perform data loading, cleaning, exploratory analysis, feature exploration, and visualization. The final result is an interactive **Streamlit dashboard** that provides deep insights into sales trends by method, revenue distribution, customer segments, and web engagement.

## 🗂️ Project Structure
sales_analysis/
│
├── corrected_data.csv # Cleaned dataset used in analysis
├── streamlit_sales_dashboard_v2.py # Final Streamlit dashboard
├── requirements.txt # Python dependencies
└── README.md # Project overview

---

## 🚀 Features

### 🧼 Data Cleaning & Processing
- Loaded raw CSV using `pandas`
- Cleaned column inconsistencies and ensured data types
- Handled missing values and standardized `sales_method` entries

### 📈 Exploratory Data Analysis (EDA)
- Analyzed sales distribution across weeks and methods
- Investigated customer behavior by tenure and website visits
- Explored revenue contribution by customer segment and location

### 📊 Dashboard Components
The final dashboard (built using **Streamlit**, **Matplotlib**, and **Seaborn**) includes:

1. **KPI Cards**
   - Total Revenue
   - Units Sold
   - Avg. Website Visits
   - Unique Customers

2. **Visualizations**
   - Sales Method Types (bar plot)
   - Revenue Distribution by Customer Segment (histogram)
   - Total Revenue by Sales Method (bar plot)
   - Weekly Revenue Trend (line plot by method)
   - Website Visit Patterns by Sales Method (line plot)


## 🧰 Tools & Libraries

| Category        | Libraries Used                  |
|----------------|----------------------------------|
| Data Handling   | `pandas`                         |
| Visualization   | `matplotlib`, `seaborn`          |
| App Framework   | `streamlit`                      |
| Modeling Prep   | `scikit-learn` (EDA and prep)    |

---

## ▶️ How to Run the Dashboard
https://dataanalyticsprojects-fghdm2tinx8mrgfxvgpvut.streamlit.app/#key-performance-indicators

<img width="1409" alt="image" src="https://github.com/user-attachments/assets/f1cc056f-ddac-4ee8-a929-77c577cd459f" />


### 1. Clone the repository
```bash
git clone https://github.com/s1h8t51/data_analytics_projects.git
cd data_analytics_projects/sales_analysis


