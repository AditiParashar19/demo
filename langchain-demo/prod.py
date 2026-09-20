Producer.py:
from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

for i in range(10):

    message = {
        "server_id": f"server{i+1}",
        "cpu_usage": 50 + i * 4,
        "memory_usage": 60 + i
    }

    producer.send(
        "server_metrics",
        value=message
    )

    print("Sent:", message)

    time.sleep(1)

producer.flush()
producer.close()

----------------------------------------------------------------------------------------------------------------------------
1. Generate uuid :
PS D:\kafka> .\bin\windows\kafka-storage.bat random-uuid
2. Temp folder: 
PS D:\kafka> .\bin\windows\kafka-storage.bat format -t BXMh8Pr1TTig-K-tOibYWQ -c .\config\server.properties –standalone
3. Start server
 	PS D:\kafka> .\bin\windows\kafka-server-start.bat .\config\server.properties

Now in a new tab
1. Create topic
PS D:\kafka> .\bin\windows\kafka-topics.bat --create --topic system-metric --bootstrap-server localhost:9092
2. Start producer
PS D:\kafka> .\bin\windows\kafka-console-producer.bat --topic system-metric --bootstrap-server localhost:9092
Now in another tab
PS D:\kafka> .\bin\windows\kafka-console-consumer.bat --topic system-metric --from- beginning --bootstrap-server localhost:9092
