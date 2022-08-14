--Создайте новую таблицу potential_customers с полями id, email, name, surname, second_name, city
--Заполните данными таблицу.
--Выведите имена и электронную почту потеницальных и существующих пользователей из города city 17

drop table if exists  potential_customers

CREATE TABLE potential_customers
(
	potential_customers_id INT PRIMARY KEY, 
	email VARCHAR(255), 
	name_potential_customers VARCHAR(255), 
	surname VARCHAR(255), 
	second_name VARCHAR(255), 
	city VARCHAR(255) 
);

INSERT INTO potential_customers (potential_customers_id, email, name_potential_customers,surname,second_name,city)
SELECT user_id,email,first_name,last_name,middle_name,city
FROM Users
--WHERE users.is_staff=1;

Select * from potential_customers where city='city 17'

