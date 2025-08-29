-- Last updated: 8/29/2025, 6:47:58 PM
# Write your MySQL query statement below
Select e.name,b.bonus 
From Employee as e
left join Bonus as b
on e.empId =b.empId
where bonus<1000 or bonus is null;