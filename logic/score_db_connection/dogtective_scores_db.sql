DROP DATABASE IF exists dogtective;

CREATE DATABASE IF NOT EXISTS dogtective;
USE dogtective;

CREATE TABLE high_scores (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    score INT NOT NULL
);

-- sample used in game
INSERT INTO high_scores (date, score)
VALUES 
('2024-12-07', 4000),
('2024-12-06', 3000)
('2024-12-05', 2500),
('2024-12-04', 2100)
('2024-12-03', 2000),
('2024-12-02', 1600)
('2024-12-02', 1500),
('2024-12-01', 1200)
('2024-12-01', 1100),
('2024-12-01', 1000)
;