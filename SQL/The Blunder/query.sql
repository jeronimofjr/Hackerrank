SELECT CAST(CEILING(AVG(CAST(salary as float)) - AVG(CAST(REPLACE(salary,0,'') as float))) as int) from employees;

