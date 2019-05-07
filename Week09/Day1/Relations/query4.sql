--gets all move titles with length less then that of Gone With the Wind
--shoud return an empty query
SELECT TITLE 
    FROM MOVIE
WHERE LENGTH > (SELECT LENGTH 
                    FROM MOVIE
                WHERE TITLE = 'Gone With the Wind');