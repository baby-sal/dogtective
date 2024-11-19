--drop desert_menu database if it exists
DROP DATABASE IF EXISTS game_init;

-- create a database called desert_menu
CREATE DATABASE game_init;

-- create table called desert_menu
CREATE TABLE sprite(
sprite_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(80) NOT NULL,
damage INT(100) NOT NULL,
health INT(100) NOT NULL
);

-- insert desert dta into desert_menu table
INSERT INTO pygame_interface (Name, damage, health)
VALUES
('Car', 5, 100),
('Dog',5, 100),
('Bus', 20, 100),
('Van', 10, 100);


--cursor.execute()