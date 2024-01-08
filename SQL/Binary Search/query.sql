WITH teste AS
  (SELECT CONCAT(n, ' Root') AS DATA
   FROM BST
   WHERE n NOT IN
       (SELECT n
        FROM BST
        WHERE p IS NOT NULL
        GROUP BY n)
   UNION 
   SELECT CONCAT(n, ' Leaf') AS DATA
   FROM BST
   WHERE n NOT IN
       (SELECT p
        FROM BST
        WHERE p IS NOT NULL )
   UNION 
   SELECT CONCAT(p, ' Inner') AS DATA
   FROM BST
   WHERE p IS NOT NULL
     AND p NOT IN
       (SELECT DISTINCT n
        FROM BST
        WHERE n NOT IN
            (SELECT n
             FROM BST
             WHERE p IS NOT NULL
             GROUP BY n)))

SELECT DATA
FROM teste
ORDER BY CONVERT(INT, replace(DATA, replace(translate(DATA, '0123456789', '##########'), '#', ''), ''));
