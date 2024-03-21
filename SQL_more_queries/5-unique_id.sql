-- create a table with unique

CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL,
    name VARCHAR(256),
    UNIQUE (id)
);