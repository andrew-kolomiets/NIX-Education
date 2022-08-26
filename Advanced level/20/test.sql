----------------------------------------------------------
--Для выполнения задания воспользуйтесь БД, 
--созданной во время выполнения задач уровня Beginner. 

--Написать 2 любые хранимые процедуры.
----------------------------------------------------------
CREATE PROCEDURE procedure_1() 
LANGUAGE SQL
AS 
$$
	SELECT * FROM users;
$$;

CALL procedure_1();


----------------------------------------------------------
CREATE PROCEDURE procedure_2(var_1 varchar(255), var_2 varchar(255))
LANGUAGE SQL
AS 
$$
	SELECT order_.order_id,Order_status.status_name
	FROM order_
	INNER JOIN order_status
	ON Order_.order_status_order_status_id = Order_status.order_status_id 
	WHERE Order_status.status_name=var_1 OR Order_status.status_name=var_2; 
$$;

CALL procedure_2('Accepted','Paid');
----------------------------------------------------------
