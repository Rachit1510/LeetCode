-- Last updated: 8/29/2025, 6:47:49 PM
# Write your MySQL query statement below
select p.product_name, s.year, s.price from Sales as s 
INNER JOIN Product as p ON s.product_id= p.product_id;