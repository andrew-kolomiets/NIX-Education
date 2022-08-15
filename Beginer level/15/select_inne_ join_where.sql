
SELECT order_.order_id,Order_status.status_name
FROM order_
INNER JOIN order_status
ON Order_.order_status_order_status_id = Order_status.order_status_id 
WHERE Order_status.status_name='Accepted' OR Order_status.status_name='Paid'; 