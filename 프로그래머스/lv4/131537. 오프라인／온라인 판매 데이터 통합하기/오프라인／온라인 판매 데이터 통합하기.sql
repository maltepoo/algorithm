SELECT
DATE_FORMAT(sales_date, "%Y-%m-%d") as sales_date, product_id, user_id, sales_amount 
FROM 
(SELECT * FROM online_sale UNION ALL SELECT offline_sale_id, NULL AS user_id, product_id, sales_amount, sales_date FROM offline_sale GROUP BY sales_date, product_id) total
WHERE year(sales_date) = '2022' AND month(sales_date) = '3'
ORDER BY sales_date, product_id, user_id;