CREATE DATABASE IF NOT EXISTS office;

USE office;

CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    role VARCHAR(40)
);

INSERT INTO employees (name, role) VALUES
('Michael', 'Regional Manager'),
('Jim', 'Sales Representative'),
('Dwight', 'Assistant to Regional Manager'),
('Toby', 'HR');
