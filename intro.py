# starting a spark session for application
from pyspark.sql import SparkSession
import os 
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
os.environ["SPARK_LOCAL_IP"]="127.0.0.1"

# creating spark session
spark = SparkSession.builder\
.appName("MyApp")\
.master("local[*]")\
.getOrCreate()

# column and data
column=["Server Name","CPU Usage"]
data=[
    ("Server 1",67),
    ("Server 2",76),
    ("Server 3",89),
    ("Server 4",92),
    ("Server 5",56),
    ("Server 6",43),
    ("Server 7",77)
]

# Dataframe 
df = spark.createDataFrame(data,column)

# Show the dataframe in tabular format 
df.show()

# Stopping the spark session 
spark.stop()
