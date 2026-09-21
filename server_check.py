from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time


def check_server():
    print("Checking Server")
    time.sleep(2)
    print("Server is up and running....")
   
def collect_metrics():
    print("Collecting Metrics...")
    time.sleep(2)
    print("CPU: 72")
    print("Memory: 65")
    print("Error logs: 5")

def analysing():
    print("Analyzing")
    time.sleep(2)
    cpu_usage=72
    if(cpu_usage>90):
        print("[ALERT] : High CPU usage detected")
        raise Exception("High CPU usage")
    print("Server metrics are normal")

def generate_report():
    print("Generating Report")
    time.sleep(2)
    print("Report Generated successfully")


with DAG(
    dag_id="server_check",
    start_date=datetime(2026, 9, 15),
    schedule=None,
    catchup=False,
) as dag:
    check = PythonOperator(
        task_id="check_server",
        python_callable=check_server,
    )
    collect = PythonOperator(
        task_id="collect_metrics",
        python_callable=collect_metrics,
    )
    analyze=PythonOperator(
        task_id="analysing",
        python_callable=analysing,
        retries=2,  # retry 2 times
        retry_delay=10 # retry after 10 sec
    )
    report = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,
    )

    check >> collect >> analyze >> report