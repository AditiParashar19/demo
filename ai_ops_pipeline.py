from datetime import datetime
from airflow import DAG
from airflow.providers.operators.python import PythonOperator

 # making the function to start task
"""
Data Collection -> 
Procesing the metrics -> 
Anomaly detection -> 
Saving the results
"""

def collect_data():
    print("Collecting the server data")
    print("CPU Usage: 92")
    print("Memory Usage: 78")
    print("Error logs: 12")

def process_data():
    print("Processing the server data")

def detect_anomaly():
    cpu=92
    if(cpu>80):
        print("ALERT: Anomaly detected in CPU Usage")
    else:
        print("CPU Usage is normal")

def save_results():
    print("Saving the results to the database ....")

# making the DAG
with DAG(
    dag_id="ai_ops_pipeline",
    start_date=datetime(2026,9,9),
    schedule=None,
    catchup=False
)as dag:
    collect=PythonOperator(
        task_id="collect_data",
        python_callable=collect_data
    )
    process=PythonOperator(
        task_id="process_data",
        python_callable=process_data
    )
    detect=PythonOperator(
        task_id="detect_anomaly",
        python_callable=detect_anomaly
    )
    save=PythonOperator(
        task_id="save_results",
        python_callable=save_results
    )
    collect >> process >> detect >> save