--Gets all actors who have played in movies produced by MGM during 1995
SELECT STARNAME FROM STARSIN
INNER JOIN MOVIE
ON MOVIETITLE = TITLE
WHERE MOVIE.YEAR = 1995 AND MOVIE.STUDIONAME = 'MGM';