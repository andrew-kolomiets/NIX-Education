
BEGIN TRANSACTION;

UPDATE order_ 
SET temp_.shipping_total = IF(users.country='country 2',0.0,temp_.shipping_total )
FROM order_ AS temp_
INNER JOIN carts ON carts.cart_id = temp_.carts_cart_id
INNER JOIN users ON users.user_id = carts.users_user_id;


ROLLBACK;