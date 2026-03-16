CREATE TABLE fraud_transactions (

transaction_id INT,
customer_id INT,
transaction_time TIMESTAMP,
amount FLOAT,
merchant VARCHAR(100),
location VARCHAR(100),
fraud_flag VARCHAR(10)

);
