# data_analytics_projects
## Project Goal:

Predicting which customers are at risk of churning using historical behavior and account data. Deliver actionable insights through a predictive model and an executive dashboard

---

## Tech Stack

- **Python** – Data cleaning, EDA, modeling (`pandas`, `seaborn`, `scikit-learn`)
- **SQL** – Feature extraction and aggregation
- **Power BI / Tableau** – Visual dashboard to communicate business impact
- **Jupyter Notebook** – Exploratory data analysis and model development

---

## Key Steps

1. **Data Preprocessing**
   - Handle missing values
   - Encode categorical variables
   - Normalize continuous features

2. **Exploratory Data Analysis**
   - Churn breakdown by tenure, contract type, services
   - Correlation heatmaps and distribution plots

3. **Feature Engineering**
   - Created features: `TotalServices`, `AvgMonthlySpend`, `ContractCategory`

4. **Modeling**
   - Algorithms used: Logistic Regression, Decision Tree, Random Forest
   - Evaluation metrics: Accuracy, F1-score, ROC-AUC

5. **Business Dashboard**
   - Churn trends and risk factors
   - Filters by gender, contract type, senior citizen status

## 🔍 Insights

- Customers with short-term contracts and high monthly charges are more likely to churn.
- Tenure and number of services are strong indicators of customer loyalty.
- Paperless billing and electronic payments were also linked with higher churn risk.

## Dashboard Preview

> *(Insert a screenshot of your dashboard here)*

## Dataset

This project uses the [Telco Customer Churn]([https://www.kaggle.com/datasets/blastchar/telco-customer-churn](https://www.kaggle.com/datasets/abdallahwagih/telco-customer-churn?resource=download)) available publicly on Kaggle.


##  Contact

**Sahitya Gantala**  
 sahityagantalausa@gmail.com  
 [LinkedIn](https://linkedin.com/in/sahitya-gantala-7ab647113)

## Future Improvements

- Deploy the model as a REST API using Flask
- Add SHAP or LIME for model explainability
- Integrate streaming data with Apache Kafka + Spark
