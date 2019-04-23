--Gets all stars who are male and have played in 'Terms of Endearment'
SELECT STARNAME FROM STARSIN
INNER JOIN MOVIESTAR
ON STARNAME = NAME
WHERE GENDER == 'M' AND MOVIETITLE == 'Terms of Endearment';
