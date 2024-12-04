DROP DATABASE IF exists dogtective;

CREATE DATABASE IF NOT EXISTS dogtective;
USE dogtective;

CREATE TABLE high_scores (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    nickname VARCHAR(40),
    score INT NOT NULL
);

INSERT INTO high_scores (date, nickname, score)
VALUES 
('2024-12-03', 'player 1', 0),
('2024-12-03', 'player 1', 2)
;