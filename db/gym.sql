DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS membership_types;
DROP TABLE IF EXISTS gym_classes;
DROP TABLE IF EXISTS class_types;
DROP TABLE IF EXISTS gym_info;

CREATE TABLE membership_types (
    type VARCHAR(255) PRIMARY KEY
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    type VARCHAR(255) REFERENCES membership_types(type) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    active_status BOOLEAN NOT NULL
);


CREATE TABLE class_types (
    class_type VARCHAR(255) PRIMARY KEY
);

CREATE TABLE gym_classes (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255) REFERENCES class_types(class_type) ON DELETE CASCADE,
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
    phone varchar(250),
    email VARCHAR(255)
)