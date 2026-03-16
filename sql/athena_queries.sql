SELECT location,
COUNT(*) AS fraud_count
FROM fraud_transactions
WHERE fraud_flag = 'YES'
GROUP BY location
ORDER BY fraud_count DESC;
