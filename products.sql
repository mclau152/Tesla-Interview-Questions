SELECT product_id, product_name, price, stock
FROM products
WHERE stock > 50
AND price < 100;
ORDER BY price DESC