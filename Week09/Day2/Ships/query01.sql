--Gets the name, country, number of guns 
--and year of launching of each ship.

SELECT SHIPS.NAME, CLASSES.COUNTRY, CLASSES.NUMGUNS, SHIPS.LAUNCHED
    FROM SHIPS
    INNER JOIN CLASSES
        ON SHIPS.CLASS = CLASSES.CLASS;