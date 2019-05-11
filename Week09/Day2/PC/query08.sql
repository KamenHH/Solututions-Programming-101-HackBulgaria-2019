--Gets those manufacturers who have made 
--more than 3 distinct pc models

SELECT maker
    FROM product
        WHERE type = 'PC'
    GROUP BY maker
        HAVING COUNT(model) >= 3;
