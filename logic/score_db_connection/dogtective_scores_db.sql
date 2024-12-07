DROP DATABASE IF exists dogtective;

CREATE DATABASE IF NOT EXISTS dogtective;
USE dogtective;

CREATE TABLE high_scores (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    score INT NOT NULL
);

INSERT INTO high_scores (date, score)
VALUES 
('2024-12-04', 500),
('2024-12-03', 1000)
;