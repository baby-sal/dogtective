--drop desert_menu database if it exists
DROP DATABASE IF EXISTS menu;

-- create a database called desert_menu
CREATE DATABASE menu;

-- create table called desert_menu
CREATE TABLE dessert_menu(
dessert_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(80) NOT NULL,
description VARCHAR(200) NOT NULL,
price DECIMAL(5, 2) NOT NULL
);

-- insert desert dta into desert_menu table
INSERT INTO DessertMenu (Name, Description, Price)
VALUES
('Carrot Cake','Rich and moist carrot cake with a creamy cream cheese filling.', 4.99),
('Strawberry Cheesecake','Creamy strawberry cheesecake with a graham cracker crust and a strawberry topping.', 5.99),
('Banoffie Pie', 'Classic banoffie pie with a banana and toffee filling.', 3.99),
('Salted caramel Ice cream', 'Three scoops of indulgent salted caramel ice cream.', 1.49);


--cursor.execute()