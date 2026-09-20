from kafka import KafkaConsumer 
import json 
 
# Connect to Kafka 
consumer = KafkaConsumer( 
    'server_metrics', 
    bootstrap_servers='localhost:9092', 
    auto_offset_reset='earliest', 
    enable_auto_commit=True, 
    group_id='aiops-monitor', 
    value_deserializer=lambda x: json.loads(x.decode('utf-8')) 
) 
 
# Count anomalies 
anomaly_count = 0 
 
print("AIOps Monitoring System Started...") 
print("Waiting for server metrics...\n") 
 
# Continuously receive messages 
for message in consumer: 
 
    data = message.value 
 
    server_id = data["server_id"] 
    cpu_usage = float(data["cpu_usage"]) 
 
    print(f"Message received: {server_id} | CPU: {cpu_usage}%") 
 
    # Check CPU anomaly 
    if cpu_usage > 80: 
        anomaly_count += 1 
 
        print("ALERT: High CPU detected") 
        print(f"Total anomalies detected: {anomaly_count}") 
 
    else: 
        print("Normal") 
 
    print("-" * 40) 
 ------------------------------------------------------------------------------------
consumer .py:
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "server_metrics",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="aiops-monitor",
    value_deserializer=lambda value: json.loads(value.decode("utf-8"))
)

print("Waiting for messages...")

for message in consumer:

    data = message.value

    server = data["server_id"]
    cpu = data["cpu_usage"]
    memory = data["memory_usage"]

    print("\nReceived:")
    print("Server:", server)
    print("CPU:", cpu, "%")
    print("Memory:", memory, "%")

    if cpu > 80:
        print("ALERT: High CPU detected on", server)
