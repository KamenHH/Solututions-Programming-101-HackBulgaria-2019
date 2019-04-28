--Gets the name of each ship that took part in
--a battle during 1942.

SELECT SHIP, DATE FROM OUTCOMES
    INNER JOIN BATTLES
        ON OUTCOMES.BATTLE = BATTLES.NAME
WHERE BATTLES.DATE LIKE '1942%'