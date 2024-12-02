## SQL - 'Median'

- HackerRank

```mysql
WITH rownumtable AS
(SELECT row_number() OVER(ORDER BY lat_n asc) rowasc, row_number() OVER(ORDER BY lat_n desc) rowdesc,lat_n
FROM station) -- create two helper columns with asc and desc order to match the middle row/row in the WHERE clause

SELECT CAST(ROUND(AVG(lat_n), 4) AS decimal(6,4))  --Use AVG() for the case with even rows, use CAST() to output four decimal places of six total digits
FROM rownumtable
WHERE rowasc=rowdesc --If uneven number of rows
    OR (rowasc = rowdesc +1) OR (rowasc = rowdesc - 1) --If even number of rows
```

아직 진행중

---

