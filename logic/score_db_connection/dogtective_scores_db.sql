CREATE DATABASE if not exists dogtective; -- dogtective is an unknown word

USE dogtective;--dogtective is an unknown word

CREATE TABLE high_scores (
user_id INT auto_increment PRIMARY KEY,-- incorrect syntax near auto_increment
date DATE,
nickname VARCHAR(40),--incorrect syntax near (40) expected (, or SELECT
score INT NOT NULL
);