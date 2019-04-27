--Gets the avg speed of all laptops with price > 1000

SELECT AVG(speed) as LaptopAvgSpeedWithPriceGreaterThen1000
    FROM laptop
WHERE price > 1000;