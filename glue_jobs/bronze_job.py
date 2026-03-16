import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

raw_path = "s3://banking-data-lake/raw/transactions/"

df = spark.read.csv(
    raw_path,
    header=True,
    inferSchema=True
)

df.write.mode("overwrite").parquet(
    "s3://banking-data-lake/bronze/transactions/"
)
