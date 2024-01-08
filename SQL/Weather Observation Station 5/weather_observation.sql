(SELECT CITY,
          LENGTH(CITY) AS S
   FROM STATION
   ORDER BY S ASC, CITY
   LIMIT 1)
UNION
  (SELECT CITY,
          LENGTH(CITY) AS S
   FROM STATION
   ORDER BY S DESC, CITY
   LIMIT 1);
