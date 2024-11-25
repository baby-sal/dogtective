CREATE DATABASE if not exists dogtective;

USE dogtective;

CREATE TABLE high_scores (
user_id INT auto_increment PRIMARY KEY,
date DATE,
nickname VARCHAR(40),
score INT NOT NULL
);