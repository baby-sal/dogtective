CREATE DATABASE dogtective;

USE dogtective;

CREATE TABLE high_scores (
user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
date DATE,
nickname VARCHAR(20),
score INT NOT NULL
);
