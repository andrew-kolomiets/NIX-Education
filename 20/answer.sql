--Вывести наименование группы товаров, общее количество 
--по группе товаров в порядке убывания количества

SELECT categories.category_title, COUNT(products.in_stock) AS _temp_ FROM products INNER JOIN categories ON categories.category_id = products.category_id
GROUP BY categories.category_title ORDER BY _temp_ DESC;
