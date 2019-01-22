#!/bin/python

CREATE DATABASE mydb;
USE mydb;
CREATE TABLE mytable (id INT PRIMARY KEY, name VARCHAR(20));
INSERT INTO mytable VALUES(1, 'WILL');
INSERT INTO mytable VALUES(2,'MARRY');
INSERT INTO mytable VALUES(3,'DEAN');
SELECT id, name FROM mytable WHERE id=1;
UPDATE mytable SET name = 'willy' WHERE id = 1;
SELECT id, name FROM mytable;
DELETE FROM mytable WHERE id = 1;
SELECT id, name FROM mytable;
DROP DATABASE mydb;
SELECT count (1) from mytable; gives the number of records in the table











