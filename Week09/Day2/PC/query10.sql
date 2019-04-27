--Gets the avg of the disk of those PCs whose manufacturers
--also ake printers
SELECT product.maker, AVG(hd) as DiskSpaceAvg FROM pc
    INNER JOIN product
       ON pc.model = product.model
GROUP BY maker
HAVING product.maker IN (SELECT maker FROM printer
                            INNER JOIN product
                                ON printer.model = product.model);

-- subquery: gets the names of the makers of printers
-- SELECT maker FROM printer
--     INNER JOIN product
--         on printer.model = product.model;
