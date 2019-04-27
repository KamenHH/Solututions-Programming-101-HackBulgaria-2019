--Gets the avg of all pc made by 'A'

SELECT AVG(price) FROM pc
    INNER JOIN product
        ON pc.model = product.model
WHERE product.maker = 'A';