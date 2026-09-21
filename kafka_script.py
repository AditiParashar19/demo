import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
# using json to parse data from kafka
import json 
# kafka consumer consume data from kafka
from kafka import KafkaConsumer

# connecting to kafka server and consuming data from the topic
consumer=KafkaConsumer(
    'system-metric', # topic name
    bootstrap_servers=['localhost:9092'], # kafka server address
    auto_offset_reset='earliest', # to read the data from beginning
    value_deserializer= lambda x: json.loads(x.decode('utf-8'))# to deserialize the data from kafka (json-> string)   
)

print("-------Kafka Consumer Anomaly Detection-----------")

# continously consuming the data from the kafka topic

for message in consumer:

    data=message.value # fetching data from message
    cpu=data.get("cpu_usage",0) # getting cpu usage from data
    service=data.get("service","unknown") # getservice name from data

    # threshold cpu usage- for anomaly detection
    if cpu>80:
        print(f"[ ALERT: Anomaly Detected, The CPU has spiked to {cpu}% for service {service} ]")
    else:
        print(f"[ NORMAL: CPU usage is {cpu}% for service {service} ]")

