from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

def collect_metrics():
    cpu = 87
    memory = 65
    response_time=420
    print("metrics collected")
def process_metrics():
    cpu = 87
    memory = 65
    response_time=420
    print("Processing metrics")
    print("CPU: ",cpu)
    print("memory: ",memory)
    print("Response Time: ",response_time)
def detect_anamoly():
    print("detecting anamoly")
    cpu = 87
    if(cpu>80):
        print("Anomaly detected: High CPU usage")
    else:
        print("No anamoly detected!!")
def generate_report():
    print("=====AIOPS REPORT======")
    print("metrics collected successfully")
    print("Metrics processed successfully")
    print("Anamoly detection completed!! ")
    print("============================")
with DAG(
    dag_id="dag1",
    start_date=datetime(2026,9,20),
    schedule=None,
    catchup=False
)as dag:
    collect_metrics = PythonOperator(
        task_id="collect_metrics",
        python_callable=collect_metrics
    )
    process_metrics = PythonOperator(
        task_id="process_metrics",
        python_callable=process_metrics
    )
    detect_anamoly =PythonOperator(
        task_id="detect_anamoly",
        python_callable=detect_anamoly
    )
    generate_report=PythonOperator(
        task_id="generate_report",
        python_callable=generate_report
    )
    collect_metrics >> process_metrics >> detect_anamoly >> generate_report
