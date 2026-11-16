-- Write your query below
SELECT distinct(customer_id)
FROM customers
WHERE year=2020 AND revenue>0;