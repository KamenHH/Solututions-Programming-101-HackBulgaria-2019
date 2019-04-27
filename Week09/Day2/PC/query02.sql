-- Gets the avg screen size of all laptops depending on the maker

SELECT product.maker,
AVG(laptop.screen) as screen_avg
    FROM laptop
    INNER JOIN product
        ON laptop.model = product.model
GROUP BY product.maker;