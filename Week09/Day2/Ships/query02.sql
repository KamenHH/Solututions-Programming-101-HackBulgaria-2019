--Might not be the desired query!
--Same as query01.sql but also gets the classes which do not have any ships,
--but they are ships with the same name as the class.

SELECT SHIPS.NAME, CLASSES.COUNTRY, CLASSES.NUMGUNS, SHIPS.LAUNCHED
    FROM SHIPS
    INNER JOIN CLASSES
        ON SHIPS.CLASS = CLASSES.CLASS
        AND SHIPS.NAME IN (SELECT CLASS
                            FROM CLASSES
                            WHERE CLASSES.CLASS NOT IN (SELECT CLASS 
                                                        FROM SHIPS));


--Subquery:
--Gets the classes which do not have any ships,
--but they are ships with the same name as the class.

-- SELECT CLASS FROM CLASSES
-- WHERE CLASSES.CLASS NOT IN (SELECT CLASS FROM SHIPS);

