--1. Вывести продукты, которые ни разу не попадали в корзину. +

SELECT product_id FROM products 
LEFT JOIN  cart_product ON cart_product.products_product_id = products.product_id
WHERE cart_product.products_product_id IS NULL;


--2. Вывести все продукты, которые так и не попали ни в 1 заказ. (но в корзину попасть могли). -
SELECT DISTINCT products.product_id, products.product_title, order_.carts_cart_id FROM products 
INNER JOIN cart_product ON cart_product.products_product_id = products.product_id 
INNER JOIN carts ON carts.cart_id = cart_product.carts_cart_id
LEFT JOIN order_ ON order_.carts_cart_id = carts.cart_id
WHERE order_.carts_cart_id IS NULL AND cart_product.products_product_id NOT IN (SELECT DISTINCT products.product_id FROM products 
INNER JOIN cart_product ON cart_product.products_product_id = products.product_id 
INNER JOIN carts ON carts.cart_id = cart_product.carts_cart_id
LEFT JOIN order_ ON order_.carts_cart_id = carts.cart_id
WHERE order_.carts_cart_id IS NULL ) 

SELECT DISTINCT products.product_id, products.product_title, order_.carts_cart_id FROM products 
INNER JOIN cart_product ON cart_product.products_product_id = products.product_id 
INNER JOIN carts ON carts.cart_id = cart_product.carts_cart_id
INNER JOIN order_ ON order_.carts_cart_id = carts.cart_id
WHERE products.product_id NOT IN 

--3. Вывести топ 10 продуктов, которые добавляли в корзины чаще всего.+
SELECT COUNT(cart_product.products_product_id) AS _temp_, products.product_title FROM cart_product INNER JOIN products ON cart_product.products_product_id = products.product_id
GROUP BY products.product_title ORDER BY _temp_ DESC LIMIT 10;

--4. Вывести топ 10 продуктов, которые не только добавляли в корзины, но и оформляли заказы чаще всего.(не знаю як перевірити але приблизно так) +
SELECT COUNT(order_.order_id),COUNT(cart_product.products_product_id) AS _temp_, products.product_title FROM order_ INNER JOIN carts ON carts.cart_id = order_.carts_cart_id
INNER JOIN cart_product ON cart_product.carts_cart_id = carts.cart_id 
INNER JOIN products ON products.product_id = cart_product.products_product_id
GROUP BY  order_.order_id, products.product_title ORDER BY _temp_ DESC LIMIT 10;

--5. Вывести топ 5 юзеров, которые потратили больше всего денег (total в заказе). +

SELECT users.user_id, users.first_name,users.last_name, users.middle_name , order_.total FROM order_ INNER JOIN carts ON carts.cart_id = order_.carts_cart_id
INNER JOIN users ON carts.users_user_id = users.user_id
ORDER BY total DESC LIMIT 5;

--6. Вывести топ 5 юзеров, которые сделали больше всего заказов (кол-во заказов).+

--кількість заказів

SELECT Users.user_id, COUNT(Order_.order_id) AS _temp_ FROM Users INNER JOIN Carts ON carts.users_user_id= users.user_id
INNER JOIN Order_ ON Order_.carts_cart_id = Carts.cart_id
GROUP BY Users.user_id ORDER BY _temp_ DESC LIMIT 5

--кількість продуктів
SELECT Users.user_id, COUNT(Cart_product.products_product_id) AS _temp_ FROM Users INNER JOIN Carts ON carts.users_user_id= users.user_id
INNER JOIN Cart_product ON Cart_product.carts_cart_id = Carts.cart_id
GROUP BY Users.user_id ORDER BY _temp_ DESC LIMIT 5



--7. Вывести топ 5 юзеров, которые создали корзины, но так и не сделали заказы.+
SELECT users.user_id, users.first_name,users.last_name, users.middle_name,order_.carts_cart_id, carts.users_user_id FROM users
INNER JOIN carts ON carts.users_user_id = users.user_id
LEFT JOIN order_ ON carts.cart_id = order_.carts_cart_id
WHERE order_.carts_cart_id IS NULL
LIMIT 5;
