

--Вывести: (если задание можно решить несколькими способами, указывай все)

--1. продукты, цена которых больше 80.00 и меньше или равно 150.00

SELECT product_title, price FROM Products WHERE price>80 AND price<=150;

--2. заказы совершенные после 01.10.2020 (поле created_at)

SELECT order_id FROM Order_ WHERE created_at>'2020-10-01';

SELECT order_id FROM Order_ 
INNER JOIN Order_status ON Order_status.order_status_id = Order_.order_status_order_status_id
WHERE Order_.created_at>'2020-10-01' AND Order_status.status_name='Finished';

--3. заказы полученные за первое полугодие 2020 года

SELECT order_id FROM Order_ 
INNER JOIN Order_status ON Order_status.order_status_id = Order_.order_status_order_status_id
WHERE created_at>'2020-01-01' AND created_at<'2020-06-01' AND status_name='Accepted';


--4. подукты следующих категорий Category 7, Category 11, Category 18

SELECT product_title FROM Products INNER JOIN categories ON categories.category_id = products.category_id
WHERE categories.category_title IN ('Category 7', 'Category 11', 'Category 18');

--5. незавершенные заказы по состоянию на 31.12.2020

SELECT order_id FROM order_ INNER JOIN order_status ON order_.order_status_order_status_id=order_status.order_status_id 
WHERE order_status.status_name='In progress'

-- верхній запрос не вірний, забув що потрібно до певного часу переглянути заказ

SELECT order_id FROM order_ INNER JOIN order_status ON order_.order_status_order_status_id=order_status.order_status_id 
WHERE order_status.status_name='In progress' AND order_.update_at<'2020-12-31'


--6. вывести все корзины, которые были созданы, но заказ так и не был оформлен.

SELECT carts.cart_id, Order_status.status_name FROM carts 
INNER JOIN Order_ ON carts.cart_id = Order_.carts_cart_id
INNER JOIN Order_status ON Order_status.order_status_id = Order_.order_status_order_status_id
WHERE Order_status.status_name='In progress'