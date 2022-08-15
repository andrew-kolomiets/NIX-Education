--Вывести:

--1. среднюю сумму всех завершенных сделок

SELECT AVG(Order_.total) FROM Order_ 
INNER JOIN order_status ON order_status.order_status_id = Order_.order_status_order_status_id
WHERE order_status.status_name='Finished'

--2. вывести максимальную сумму сделки за 3 квартал 2020

SELECT MAX(total) FROM Order_ WHERE created_at>'2020-07-01' AND created_at<'2020-10-01'

