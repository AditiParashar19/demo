from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def check_system():
    print("System check started")
    print("System is healthy")


def process_data():
    print("Data processing started")
    print("Data processing completed")


def generate_report():
    print("Report generation started")
    print("Report generated successfully")


with DAG(
    dag_id="data_pipeline",
    start_date=datetime(2026, 9, 14),
    schedule=None,
    catchup=False,
) as dag:

    check = PythonOperator(
        task_id="check_system",
        python_callable=check_system,
    )

    process = PythonOperator(
        task_id="process_data",
        python_callable=process_data,
    )

    report = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,
    )

    check >> process >> report