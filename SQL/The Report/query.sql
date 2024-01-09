SELECT (CASE WHEN grade < 8 THEN 'NULL' ELSE name END), grade, marks
FROM students, grades
WHERE marks >= min_mark AND marks <= max_mark
ORDER BY grade desc, name asc;
