
DROP TABLE IF EXISTS Order_status, Carts, Order_, Users, Categories, Products, Cart_product;

CREATE TABLE Order_status
(
    order_status_id INT PRIMARY KEY, 
    status_name VARCHAR(255)
);

CREATE TABLE Users
(
    user_id INT PRIMARY KEY,
    email VARCHAR(255),
    password_ VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    middle_name VARCHAR(255),
    is_staff SMALLINT,
    country VARCHAR(255),
    city VARCHAR(255),
    address_ TEXT
);

CREATE TABLE Carts
(
    cart_id INT PRIMARY KEY, 
    Users_user_id INT,
    subtotal DECIMAL,
    total DECIMAL,
    time_stamp TIMESTAMP(2),
    FOREIGN KEY(Users_user_id) REFERENCES Users(user_id) 
    
);

CREATE TABLE Order_
(
    order_id INT PRIMARY KEY,
    Carts_cart_id INT,
    Order_status_order_status_id INT,
    shipping_total DECIMAL,
    total DECIMAL,
    created_at TIMESTAMP(2),
    update_at TIMESTAMP(2),
    FOREIGN KEY(Carts_cart_id) REFERENCES Carts(cart_id),
    FOREIGN KEY(Order_status_order_status_id) REFERENCES Order_status(order_status_id)
    
);

CREATE TABLE Categories
(
    category_id INT PRIMARY KEY,
    category_title VARCHAR(255),
    category_description TEXT
);

CREATE TABLE Products
(
    product_id INT PRIMARY KEY,
    product_title VARCHAR(255),
    product_description TEXT,
    in_stock INT,
    price FLOAT,
    slug VARCHAR(45),
    category_id INT,
    FOREIGN KEY(category_id) REFERENCES Categories(category_id)
);

CREATE TABLE Cart_product
(
    carts_cart_id INT,
    products_product_id INT,
    FOREIGN KEY(carts_cart_id) REFERENCES Carts(cart_id),
    FOREIGN KEY(products_product_id) REFERENCES Products(product_id)
);

