# starting a spark session for application
from pyspark.sql import SparkSession
import os 
import sys

# os.environ["PYSPARK_PYTHON"] = sys.executable
# os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
# os.environ["SPARK_LOCAL_IP"]="127.0.0.1"

# creating spark session
spark = SparkSession.builder\
.appName("MyApp")\
.master("local[*]")\
.getOrCreate()

# Read Dataframe , header - loads header, inferSchema- assign datatypes
df=spark.read.csv("server.csv", header=True, inferSchema=True)

df.printSchema() # print column datatype

df.select("server","errors").show() # show selected columns 

spark.stop()
