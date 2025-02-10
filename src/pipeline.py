from pyspark.sql import SparkSession

# Initialize PySpark
spark = SparkSession.builder.appName("DataPipeline").getOrCreate()

# Sample Data
data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Transformation
df = df.withColumnRenamed("Age", "User_Age")

# Display Output
df.show()
