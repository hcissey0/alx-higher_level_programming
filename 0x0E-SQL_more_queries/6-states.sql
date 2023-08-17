-- Creates a database and tables
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS state (
	id INT NOT NULL AUTO_INCREMENT PRIMARY,
	name VARCHAR(256) NOT NULL
);
