-- Churn rate by contract type
SELECT contract_one_year, contract_two_year,
       AVG(predicted_churn::FLOAT) AS avg_churn
FROM churn_predictions
GROUP BY 1, 2;

-- Top 10 churn risk
SELECT * FROM churn_predictions
ORDER BY churn_probability DESC
LIMIT 10;
