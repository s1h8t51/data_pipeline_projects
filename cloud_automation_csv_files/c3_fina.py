# /opt/airflow/dags/sales_year_to_s3.py
from __future__ import annotations
import os, csv, tempfile
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils import timezone
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

# ---- CONFIG ----
LOCAL_FILES_PATH = "/opt/airflow/sample_data"
INPUT_FILENAME   = "sales_data.csv"         # columns: product_id, product_name, date
S3_CONN_ID       = "aws_default"
S3_BUCKET        = "my-first-bucket-2025-12345"
S3_PREFIX        = "sales"
# ----------------

def _get_year(val: str) -> str:
    """Parse year from the date string."""
    v = val.strip()
    if len(v) >= 4 and v[:4].isdigit():
        return v[:4]
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y", "%Y/%m/%d"):
        try:
            return str(datetime.strptime(v, fmt).year)
        except Exception:
            pass
    raise ValueError(f"Cannot parse year from date value: {val!r}")

def split_by_year_and_upload():
    src = os.path.join(LOCAL_FILES_PATH, INPUT_FILENAME)
    by_year = {}

    # --- Read CSV and group rows by year ---
    with open(src, "r", newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        header = next(r)  # product_id, product_name, date
        for row in r:
            year = _get_year(row[2])   # 3rd column is "date"
            by_year.setdefault(year, []).append(row)

    # --- Write each year's rows into its own file and upload ---
    hook = S3Hook(aws_conn_id=S3_CONN_ID)
    uploaded = []
    for y in sorted(by_year.keys()):
        fd, tmp = tempfile.mkstemp(suffix=f"_sales_{y}.csv")
        os.close(fd)
        with open(tmp, "w", newline="", encoding="utf-8") as out:
            w = csv.writer(out)
            w.writerow(header)
            w.writerows(by_year[y])

        key = f"{S3_PREFIX}/year={y}/sales_data_{y}.csv"
        hook.load_file(filename=tmp, key=key, bucket_name=S3_BUCKET, replace=True)
        os.remove(tmp)
        uploaded.append(f"s3://{S3_BUCKET}/{key}")

    print("Uploaded:", uploaded)

with DAG(
    dag_id="sales_year_to_s3",
    start_date=timezone.datetime(2025, 8, 30),
    schedule=None,   # run manually
    catchup=False,
    tags=["aws","s3","year-split"],
) as dag:
    PythonOperator(
        task_id="split_and_upload_by_year",
        python_callable=split_by_year_and_upload,
    )
