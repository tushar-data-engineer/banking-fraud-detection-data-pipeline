Banking Fraud Detection Data Pipeline

This project demonstrates an enterprise AWS data pipeline for detecting fraudulent banking transactions using AWS Glue and PySpark.

Architecture

Amazon S3 → AWS Glue ETL → Bronze → Silver → Gold → Redshift → Athena

Technologies

AWS Glue
PySpark
Amazon S3
Amazon Athena
Amazon Redshift

Features

Medallion Data Lake Architecture
Fraud detection pipeline
Glue workflow orchestration
Parquet optimized storage

## Deployment Steps

1. Create S3 Data Lake bucket
2. Upload dataset to raw layer
3. Create IAM role for Glue
4. Create Glue database
5. Run Glue crawler
6. Deploy Glue ETL jobs
7. Create Glue workflow orchestration
