import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# CONFIGURE YOUR DATABASE CONNECTION DETAILS
DB_NAME= 'churn_db'
DB_USER= 'postgres'
DB_PASS= 'postgres'
DB_HOST= 'localhost'
DB_PORT= '5432'


CSV_FILE = 'output/churn_predictions.csv'
TABLE_NAME = 'churn_predictions'

def load_csv_to_postgres():
    # Load CSV
    df = pd.read_csv(CSV_FILE)
    print(f" Loaded {len(df)} rows from {CSV_FILE}")

    # Clean column names to match PostgreSQL
    df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("(", "").str.replace(")", "").str.lower()

    # Connect using SQLAlchemy
    engine_str = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(engine_str)

    # Load to PostgreSQL
    df.to_sql(TABLE_NAME, engine, if_exists='replace', index=False)
    print(f" Data uploaded to table '{TABLE_NAME}' in database '{DB_NAME}'.")

if __name__ == "__main__":
    load_csv_to_postgres()
