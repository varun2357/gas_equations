CREATE TABLE conversion_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    input1 VARCHAR(255) NOT NULL,
    input2 VARCHAR(255) NOT NULL,
    input3 FLOAT NOT NULL,
    result FLOAT NOT NULL,
    category VARCHAR(255) NOT NULL
);
