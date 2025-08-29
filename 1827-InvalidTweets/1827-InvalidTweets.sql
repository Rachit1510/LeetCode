-- Last updated: 8/29/2025, 6:47:43 PM
# Write your MySQL query statement below
select tweet_id from Tweets 
where LENGTH(content)>15;