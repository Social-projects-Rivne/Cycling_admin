-- To use it:
-- 1. login into MySQL as root
--      mysql -u root -p
-- 2. run this script
--      source <path to the file>/init_db.sql
-- 3. grant all rights on this DB for your work user
--      CREATE USER '<user_name>'@'localhost' IDENTIFIED BY '<password>';
--      GRANT ALL ON CYCLINGADMINDB.* TO '<user_name>'@'localhost';

-- create db. CHARACTER SET!!!
DROP DATABASE IF EXISTS CYCLINGADMINDB;
CREATE DATABASE IF NOT EXISTS CYCLINGADMINDB CHARACTER SET utf8;

-- switch to ur db
USE CYCLINGADMINDB;

-- table Users
CREATE TABLE `Users` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL UNIQUE,
  `password` VARCHAR(128) NOT NULL,
  `is_active` TINYINT NOT NULL,
  `avatar` VARCHAR(255),
  `role_id` TINYINT NOT NULL,
  PRIMARY KEY (`id`)
);

-- table Parking
CREATE TABLE `Parking` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `location` VARCHAR(255) NOT NULL,
  `security` TINYINT,
  `amount` INTEGER,
  `is_free` TINYINT,
  `owner_id` INTEGER NOT NULL,
  PRIMARY KEY (`id`)
);

-- table Attachments
CREATE TABLE `Attachments` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `image_url` VARCHAR(255) NOT NULL,
  `parking_id` INTEGER NOT NULL,
  `places_id` INTEGER,
  PRIMARY KEY (`id`)
);

-- table Places
CREATE TABLE `Places` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `location` VARCHAR(255) NOT NULL,
  `description` TINYTEXT,
  `work_period` VARCHAR(255),
  `category_id` INTEGER,
  `owner_id` INTEGER NOT NULL,
  PRIMARY KEY (`id`)
);

-- table Categories
CREATE TABLE `Categories` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`)
);

-- table Bicycles
CREATE TABLE `Bicycles` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TINYTEXT,
  `is_deleted` TINYINT NOT NULL DEFAULT 0,
  `user_id` INTEGER NOT NULL,
  PRIMARY KEY (`id`)
);

-- table Images
CREATE TABLE `Images` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `image_url` VARCHAR(255) NOT NULL,
  `bike_id` INTEGER NOT NULL,
  PRIMARY KEY (`id`)
);

-- table StolenBicycles
CREATE TABLE `StolenBicycles` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `bike_id` INTEGER NOT NULL,
  `description` TINYTEXT,
  `date` DATE NOT NULL,
  `location` VARCHAR(255) NOT NULL,
  `was_found` TINYINT DEFAULT 0,
  PRIMARY KEY (`id`)
);

-- create foreign keys
ALTER TABLE `Parking` ADD FOREIGN KEY (owner_id) REFERENCES `Users` (`id`);

ALTER TABLE `Attachments` ADD FOREIGN KEY (parking_id) REFERENCES `Parking` (`id`);
ALTER TABLE `Attachments` ADD FOREIGN KEY (places_id) REFERENCES `Places` (`id`);

ALTER TABLE `Places` ADD FOREIGN KEY (owner_id) REFERENCES `Users` (`id`);
ALTER TABLE `Places` ADD FOREIGN KEY (category_id) REFERENCES `Categories` (`id`);

ALTER TABLE `Bicycles` ADD FOREIGN KEY (user_id) REFERENCES `Users` (`id`);

ALTER TABLE `Images` ADD FOREIGN KEY (bike_id) REFERENCES `Bicycles` (`id`);

ALTER TABLE `StolenBicycles` ADD FOREIGN KEY (bike_id) REFERENCES `Bicycles` (`id`);

SHOW TABLES;
