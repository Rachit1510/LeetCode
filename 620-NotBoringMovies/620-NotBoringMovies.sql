-- Last updated: 8/29/2025, 6:47:55 PM
# Write your MySQL query statement below
select id,movie,description,rating
from Cinema
where id%2 != 0 AND description != "boring"
order by rating desc;
