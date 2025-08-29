-- Last updated: 8/29/2025, 6:48:09 PM
# Write your MySQL query statement below

WITH helper (Employee, Salary, Department, ranks) AS (
    SELECT 
        E.name AS Employee, 
        E.salary AS Salary,
        D.name AS Department,
        DENSE_RANK() OVER (PARTITION BY D.id ORDER BY E.salary DESC) AS ranks
    FROM Employee E 
    JOIN Department D
        ON D.id = E.departmentId
)
SELECT 
    Employee, 
    Salary,
    Department
FROM helper
WHERE ranks < 4;
