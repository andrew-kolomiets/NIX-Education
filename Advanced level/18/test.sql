----------------------------------------------------------------------------
-- Для выполнения задания воспользуйтесь БД, созданной во время выполнения задач уровня Beginner.

-- Придумать 3 запроса, которые можно оптимизировать с помощью индекса 
-- (проверять стоит ли оптимизировать запрос оператором explain) и оптимизировать
-- их используя индекс. Результат проверять также оператором explain.

----------------------------------------------------------------------------
-- пошук кокретного аккаунта

EXPLAIN ANALYZE SELECT * FROM users WHERE email='email1231@gmail.com' AND password_='56542153800';

CREATE INDEX index_users on users (email, password_);

DROP INDEX index_users;

----------------------------------------------------------------------------
-- вывести максимальную сумму сделки за 3 квартал 2020

EXPLAIN ANALYZE SELECT MAX(total) FROM Order_ WHERE created_at>'2020-07-01' AND created_at<'2020-10-01';


CREATE INDEX index_order ON Order_ (created_at);

DROP INDEX index_order;
----------------------------------------------------------------------------
-- вывести продукты, которые ни разу не попадали в корзину. 

EXPLAIN ANALYZE SELECT product_id FROM products 
LEFT JOIN  cart_product ON cart_product.products_product_id = products.product_id
WHERE cart_product.products_product_id IS NULL;

CREATE INDEX index_cart_product ON  cart_product (products_product_id);

DROP INDEX index_cart_product;
----------------------------------------------------------------------------
