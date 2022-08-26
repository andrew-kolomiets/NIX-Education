----------------------------------

-- Для выполнения задания воспользуйтесь БД, созданной 
-- во время выполнения задач уровня Beginner.
-- Использовать транзакции для insert, update, delete на 3х таблицах. 

----------------------------------
-- update
----------------------------------


BEGIN TRANSACTION;
  
UPDATE users
SET is_staff=2
WHERE user_id=3;

COMMIT;

----------------------------------

BEGIN TRANSACTION;
  
UPDATE order_
SET total=total/2

ROLLBACK;

----------------------------------


BEGIN TRANSACTION;

SAVEPOINT SP1;

UPDATE carts
SET total=total*2

ROLLBACK TO SP1;

----------------------------------
--insert
----------------------------------

BEGIN WORK;
  
INSERT INTO users(user_id,email,password_,first_name,last_name,middle_name,is_staff,country,city,address_, phone_number)
VALUES(0,'andrew.kolomiets@gmail.com', '380678723728', 'andrew', 'kolomiets', 'yurievich',3,'Ukraine','Kiev', 'Borchagivska','');

SELECT * FROM users WHERE user_id=0;

ROLLBACK;

COMMIT;

----------------------------------
BEGIN WORK;
  
INSERT INTO products(product_id,product_title,product_description,in_stock,price,slug,category_id)
VALUES(0,'My unique','Product description unique',21,500,'Product-0',3);

SELECT * FROM products WHERE product_id=0;

ROLLBACK;

COMMIT;
----------------------------------
BEGIN TRANSACTION;

SAVEPOINT SP1;

INSERT INTO cart_product(carts_cart_id, products_product_id) VALUES(1,100);

SELECT * FROM cart_product WHERE carts_cart_id=1 AND products_product_id=100;

ROLLBACK TO SP1;
----------------------------------
--delete
----------------------------------
BEGIN WORK;
  
INSERT INTO users(user_id,email,password_,first_name,last_name,middle_name,is_staff,country,city,address_, phone_number)
VALUES(0,'andrew.kolomiets@gmail.com', '380678723728', 'andrew', 'kolomiets', 'yurievich',3,'Ukraine','Kiev', 'Borchagivska','');

SELECT * FROM users WHERE user_id=0;

COMMIT;

BEGIN WORK;

DELETE FROM users
WHERE user_id = 0;

SELECT * FROM users WHERE user_id=0;

ROLLBACK;


----------------------------------
BEGIN WORK;
  
INSERT INTO products(product_id,product_title,product_description,in_stock,price,slug,category_id)
VALUES(0,'My unique','Product description unique',21,500,'Product-0',3);

SELECT * FROM products WHERE product_id=0;

COMMIT;

BEGIN WORK;

DELETE FROM products
WHERE product_id = 0;

SELECT * FROM products WHERE product_id=0;

ROLLBACK;

----------------------------------
BEGIN TRANSACTION;

SAVEPOINT SP1;

INSERT INTO cart_product(carts_cart_id, products_product_id) VALUES(1,100);

SELECT * FROM cart_product WHERE carts_cart_id=1 AND products_product_id=100;

DELETE FROM  cart_product;

SELECT * FROM cart_product;

ROLLBACK TO SP1;
----------------------------------