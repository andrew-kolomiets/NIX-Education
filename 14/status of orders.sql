
SELECT status_name FROM Order_status, Order_ WHERE order_status_order_status_id=order_status_id;

SELECT order_.order_id,Order_status.status_name
FROM order_
INNER JOIN order_status
ON Order_.order_status_order_status_id = Order_status.order_status_id;
