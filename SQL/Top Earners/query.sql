SELECT MAX(months * salary), COUNT(*)
FROM Employee
GROUP BY salary 
HAVING MAX(months * salary) = (SELECT MAX(months * salary) FROM employee);
