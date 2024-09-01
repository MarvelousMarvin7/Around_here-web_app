-- Sets up mysql server for Around here database

CREATE DATABASE IF NOT EXISTS arh_dev_db;
CREATE USER IF NOT EXISTS 'arh_dev'@'localhost' IDENTIFIED BY 'arh_dev_pwd';
GRANT ALL PRIVILEGES ON `arh_dev_db`.* TO 'arh_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'arh_dev'@'localhost';

FLUSH PRIVILEGES;
