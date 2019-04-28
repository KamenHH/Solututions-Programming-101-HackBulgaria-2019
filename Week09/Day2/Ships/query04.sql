--Gets the name of the ships for each country
--that have not participated in any battles.

SELECT CLASSES.COUNTRY, SHIPS.NAME FROM SHIPS
    JOIN CLASSES
        ON SHIPS.CLASS = CLASSES.CLASS
WHERE SHIPS.NAME NOT IN (SELECT SHIP FROM OUTCOMES)
ORDER BY CLASSES.COUNTRY;






