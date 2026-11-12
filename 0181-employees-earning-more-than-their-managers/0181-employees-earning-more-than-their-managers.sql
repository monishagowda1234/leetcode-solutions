# Write your MySQL query statement below
#SELECT e.name AS Employee
#FROM employee e WHERE e.managerID ORDER BY e.salary ASC
#lIMIT 1;

#/* Write your PL/SQL query statement below */
SELECT EMP.name AS Employee FROM Employee EMP,Employee MGR
WHERE EMP.managerId=MGR.id AND EMP.salary>MGR.salary