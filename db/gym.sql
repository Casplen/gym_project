DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS gym_classes;
DROP TABLE IF EXISTS gym_info;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    type VARCHAR(10) NOT NULL,
    start_date DATE NOT NULL,
    active_status BOOLEAN NOT NULL
);

CREATE TABLE gym_classes (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    capacity INT,
    duration INT NOT NULL
);

CREATE TABLE bookings (
   id SERIAL PRIMARY KEY,
   member_id INT REFERENCES members(id) ON DELETE CASCADE,
   gym_class_id INT REFERENCES gym_classes(id) ON DELETE CASCADE 
);

CREATE TABLE gym_info (
    name VARCHAR(255),
    address TEXT,
    phone INT,
    email VARCHAR(255)
)