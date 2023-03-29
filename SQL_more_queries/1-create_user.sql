-- Creates MYSQL server user 'user_0d_1
--- User should have all priviledges on MySQL server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *-* TO 'user_0d_1'@'localhost';
