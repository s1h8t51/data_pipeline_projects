# Credit Card Customer Analytics Dashboard

This project analyzes credit card customer data to extract actionable business insights and explore customer behavior through interactive visualization.

## Features
- Custom features: credit utilization, payment ratio, purchase behavior ratios, and more
- Automated customer segmentation based on financial behavior
- Interactive dashboard (built in Streamlit) for business users

## Data source 
- https://www.kaggle.com/datasets/arjunbhasin2013/ccdata

## Getting Started

1. Clone this repo
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Place your data file in the `data/` directory (or edit `app.py` to point to the correct location)
4. Run the dashboard:
    ```
    streamlit run app.py
    ```

## Key Insights and Business Recommendations

### 1. Credit Utilization
- **Insight:** Most customers use a high share (0.5–1.0) of their available credit, with some maxing out.
- **Recommendation:** Closely monitor these accounts for risk but reward responsible high utilizers. Consider limit increases or loyalty bonuses for those who repay on time.

### 2. Payment Ratio
- **Insight:** Most pay only the minimum, creating risk and interest revenue opportunities.
- **Recommendation:** Incentivize full payment, target minimum-payers with educational nudges, and flag high-utilization, low-repayment customers for proactive risk review.

### 3. Purchase and Installment Behavior
- **Insight:** Customers are polarized between installment-only and one-off-only purchasing styles, with few mixing both.
- **Recommendation:** Tailor campaigns (e.g., EMI offers vs. full-pay rewards) based on segment.

### 4. Average Transaction Value
- **Insight:** Most customers make small transactions, but a few “big spenders” exist in both the one-off and installment segments.
- **Recommendation:** Offer premium services to “big spenders,” and create micro-offers for low-value users.

### 5. Segmentation
- **Insight:** Segments reveal clear behavioral groups, enabling targeted risk, marketing, and loyalty actions.
- **Recommendation:** Assign segment-based relationship managers and customize product offerings.


*These insights and strategies can directly improve credit card portfolio performance, retention, and risk management.*


## Screenshots
![newplot-3](https://github.com/user-attachments/assets/84b29b7b-157a-467e-a033-69e259df1d9e)
![newplot](https://github.com/user-attachments/assets/eb439a1e-fef1-4e71-9281-be42cfb32cca)
![newplot-2](https://github.com/user-attachments/assets/0793c90f-102d-4613-aa0f-ad456bfa991d)

