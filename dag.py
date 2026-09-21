

from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

def start_task():
    print("AI Ops Pipeline Started")

def process_task():
    print("Processing the server data")

def finish_task():
    print("AI Ops Pipeline completed")

with DAG(
    dag_id="my_first_ai_ops_dag",
    start_date=datetime(2026,9,8),
    schedule=None,
    catchup=False
)as dag:
    start=PythonOperator(
        task_id="start_task",
        python_callable=start_task
    )
    process=PythonOperator(
        task_id="process_task",
        python_callable=process_task
    )
    finish=PythonOperator(
        task_id="finish_task",
        python_callable=finish_task
    )

    start >> process >> finish

    # ctrl+o
    # Enter
    # ctrl +x

# nano ~/airflow-class/dags/my_first_ai_ops_dag.py

# export AIRFLOW_HOME=~/airflow-class

# airflow standalone
