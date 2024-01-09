SELECT CT.CONTINENT, AVG(C.POPULATION)
FROM COUNTRY CT, CITY C
WHERE C.COUNTRYCODE = CT.CODE
GROUP BY CONTINENT;