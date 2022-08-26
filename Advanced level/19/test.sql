-----------------------------------------------------------
--Для выполнения задания воспользуйтесь БД, созданной 
--во время выполнения задач уровня Beginner. 
--Написать представление для таблицы products, для таблиц 
--order_status и order , для таблиц products и category
-----------------------------------------------------------

CREATE VIEW products_v AS 
SELECT product_title, price FROM Products WHERE price>80 AND price<=150;

SELECT * FROM products_v;

-----------------------------------------------------------

CREATE VIEW order_statu_order_v AS 
SELECT order_.order_id,Order_status.status_name
FROM order_
INNER JOIN order_status
ON Order_.order_status_order_status_id = Order_status.order_status_id;

SELECT * FROM order_statu_order_v;

-----------------------------------------------------------

CREATE VIEW products_category_v AS 
SELECT categories.category_title, COUNT(products.product_title) AS _temp_ 
FROM products INNER JOIN categories ON categories.category_id = products.category_id
GROUP BY categories.category_title ORDER BY _temp_ DESC;

SELECT * FROM products_category_v;

-----------------------------------------------------------
