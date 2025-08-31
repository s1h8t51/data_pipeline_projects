# Airflow: Local CSV ➜ Partitioned S3 Ingestion

This repo contains an Apache Airflow DAG that:
1) **Discovers** CSV files available on the local filesystem,
2) **Validates & optionally transforms** them,
3) **Partitions** the data (by column or by ingestion date),
4) **Uploads** partitioned files to Amazon S3 under a consistent path layout.

It’s designed to be production-minded but minimal, so you can extend it to larger pipelines.

---

## ✨ Key Features

- **Auto-discovery** of local CSVs (configurable folder)
- **Data validation** (file exists, non-empty; optional schema checks)
- **Partitioning strategies**
  - **By column** (e.g., `event_date`, `year`, `country`)
  - **By ingestion date** (fallback): `dt=YYYY-MM-DD`
- **Idempotent S3 paths**: `s3://<bucket>/<prefix>/<partitions>/filename.csv`
- **Retry & logging** baked into Airflow
- **Simple to run** via Docker Compose or local `pip`

---

## 🧱 Architecture (High Level)

Local CSV Folder
- └── discover_files
- └── validate_files
- └── optional_transform
- └── partition_and_stage (split CSV by partition key)
- └── upload_partitions_to_s3

## 📁 Repo Structure

├─ dags/
│ └─ partitioned_csv_to_s3.py
├─ include/
│ ├─ sample_data/ # put CSVs here
│ └─ schemas/ # (optional) schema definitions for validation
├─ docker-compose.yaml # optional: local Airflow stack
├─ requirements.txt
├─ .env.example
└─ README.md



---

## ✅ Prerequisites

- **Python 3.10+**
- **AWS credentials** with S3 write access:
  - `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and optionally `AWS_DEFAULT_REGION`
- **Docker** (recommended) or local Python installation
- **Airflow Providers**: `apache-airflow-providers-amazon`

---

## 🔐 Configuration

### 1) Environment (.env)
Copy `.env.example` ➜ `.env` and set values:

bash
# Airflow basics (Docker)
AIRFLOW_UID=50000
AIRFLOW_GID=0

# Local input
LOCAL_INPUT_DIR=/opt/airflow/include/sample_data
# Optional schema dir (if using schema checks)
LOCAL_SCHEMA_DIR=/opt/airflow/include/schemas

# AWS
AWS_DEFAULT_REGION=us-east-1
S3_BUCKET=my-bucket-name
S3_PREFIX=raw/sales                    # base prefix in S3

# Partitioning behavior
PARTITION_COLUMN=event_date            # falls back to ingestion date if empty or missing
DATE_FORMAT=%Y-%m-%d                   # used if partitioning by date strings



# Airflow Connections (UI → Admin → Connections)
AWS
- Conn ID: aws_default
- Conn Type: Amazon Web Services
- Login: AWS_ACCESS_KEY_ID
- Password: AWS_SECRET_ACCESS_KEY
- Extra (optional): {"region_name":"us-east-1"}

