import sys
from pyspark.sql.functions import col, to_timestamp
from pyspark.context import SparkContext
from awsglue.context import GlueContext

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

df = spark.read.parquet(
    "s3://banking-data-lake/bronze/transactions/"
)

clean_df = df.withColumn(
    "transaction_time",
    to_timestamp(col("transaction_time"))
)

clean_df = clean_df.filter(col("amount") > 0)

clean_df.write.mode("overwrite").parquet(
    "s3://banking-data-lake/silver/transactions/"
)
