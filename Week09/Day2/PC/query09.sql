--MIGHT NOT BE THE DESIRED QUERY
--Gets the maker, model, and price 
--of the most expensive PC models 

SELECT product.maker, pc.model, MAX(pc.price)
    FROM product
    INNER JOIN pc
        ON product.model = pc.model
    GROUP BY product.model
    ORDER BY -MAX(pc.price);