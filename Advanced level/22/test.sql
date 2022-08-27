-----------------------------------------------------------------
--Для выполнения задания воспользуйтесь БД, созданной 
--во время выполнения задач уровня Beginner.

-- Сравнить цену каждого продукта n с средней ценой продуктов в 
-- категории продукта n. Использовать window function.
-- Таблица результата должна содержать такие колонки: 
-- category_title, product_title, price, avg. 
-- Пример для решения можно найти в теории.
-----------------------------------------------------------------

BEGIN TRANSACTION;

SELECT categories.category_title, products.product_title, products.price, avg(price) 
OVER(PARTITION BY categories.category_title) AS avarage_price
FROM products 
INNER JOIN categories ON categories.category_id = products.category_id
WHERE categories.category_title='Category 1'

ROLLBACK;

-----------------------------------------------------------------