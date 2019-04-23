--adds 'PRESIDENT' row to STUDIO table
ALTER TABLE STUDIO ADD COLUMN PRESIDENT VARCHAR(15)

--updates PRESIDENT value of Disney to ...
UPDATE STUDIO
SET PRESIDENT = 'Bob Iger'
WHERE NAME = 'Disney';

--updates PRESIDENT value of Fox to ...
UPDATE STUDIO
SET PRESIDENT = 'Roger Ailes'
WHERE NAME = 'Fox';

--updates PRESIDENT value of MGM to ...
UPDATE STUDIO
SET PRESIDENT = 'Jonathan Glickman'
WHERE NAME = 'MGM';

--updates PRESIDENT value of Paramount to ...
UPDATE STUDIO
SET PRESIDENT = 'Jim Gianopulos'
WHERE NAME = 'Paramount';

--updates PRESIDENT value of USA Entertainm. to ...
UPDATE STUDIO
SET PRESIDENT = 'Someone'
WHERE NAME = 'USA Entertainm.';

--updates PRESIDENT value of Warner Bros to ...
UPDATE STUDIO
SET PRESIDENT = 'Toby Emmerich'
WHERE NAME = 'Warner Bros';

--gets the name of the president of MGM studio
SELECT PRESIDENT FROM STUDIO
WHERE NAME = 'MGM';
