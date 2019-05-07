--Gets all the titles of the movies which have a networth
--greater than that of producer Merv Griffin.

SELECT TITLE, NETWORTH FROM MOVIE
    JOIN MOVIEEXEC
        ON MOVIE.PRODUCER = MOVIEEXEC.CERT
WHERE NETWORTH > (SELECT NETWORTH
                    FROM MOVIEEXEC
                 WHERE NAME = 'Merv Griffin');