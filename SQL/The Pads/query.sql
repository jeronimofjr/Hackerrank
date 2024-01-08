(SELECT CONCAT(Name, '(', SUBSTRING(Occupation, 1, 1), ')') 
FROM OCCUPATIONS)
UNION
(SELECT CONCAT('There are a total of ', COUNT(Occupation), ' ', LOWER(Occupation), 's.')
FROM OCCUPATIONS
GROUP BY Occupation
