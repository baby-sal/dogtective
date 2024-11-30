CREATE DATABASE IF NOT EXISTS dogtective;
USE dogtective;

CREATE TABLE high_scores (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    nickname VARCHAR(40),
    score INT NOT NULL
);
