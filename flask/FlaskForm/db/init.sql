CREATE DATABASE if not exists detail;
use detail;
CREATE TABLE if NOT exists information (
  name VARCHAR(100) NOT NULL PRIMARY KEY,
  book_name VARCHAR(100) NOT NULL,
  author VARCHAR(100) NOT NULL
);

