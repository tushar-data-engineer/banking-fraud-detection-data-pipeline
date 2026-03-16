import sys
from pyspark.sql.functions import col, when
from pyspark.context import SparkContext
from awsglue.context import GlueContext

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

df = spark.read.parquet(
    "s3://banking-data-lake/silver/transactions/"
)

fraud_df = df.withColumn(
    "fraud_flag",
    when(col("amount") > 10000, "YES").otherwise("NO")
)

fraud_df.write.mode("overwrite").parquet(
    "s3://banking-data-lake/gold/fraud_transactions/"
)
