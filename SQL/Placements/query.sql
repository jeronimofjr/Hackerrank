SELECT t.name
FROM
  (SELECT *
   FROM
     (SELECT s.id,
             s.name,
             p.salary AS my_salary,
             f.friend_id
      FROM students s
      INNER JOIN packages p ON s.id = p.id
      INNER JOIN friends f ON s.id = f.id) AS x
   INNER JOIN packages p ON x.friend_id = p.id) AS t
WHERE t.my_salary < t.salary
ORDER BY t.salary;
