--gets the avg price of all PCs for all hd sizes

SELECT hd, AVG(price) FROM pc
GROUP BY hd;
