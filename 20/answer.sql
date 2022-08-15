--Вывести наименование группы товаров, общее количество 
--по группе товаров в порядке убывания количества


--якщо мова іде про кількість загальна наявних одиниць кожного продукту загалом для кожної групи продуктів
SELECT categories.category_title, SUM(products.in_stock) AS _temp_ FROM products INNER JOIN categories ON categories.category_id = products.category_id
GROUP BY categories.category_title ORDER BY _temp_ DESC;

--якщо мається на увазі кількість продуктів в певній категорії
SELECT categories.category_title, COUNT(products.product_title) AS _temp_ 
FROM products INNER JOIN categories ON categories.category_id = products.category_id
GROUP BY categories.category_title ORDER BY _temp_ DESC;