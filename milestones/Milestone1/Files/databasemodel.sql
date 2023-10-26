-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Eco-Friendly-TransportationDB
-- -----------------------------------------------------
DROP DATABASE IF EXISTS `Eco-Friendly-TransportationDB`;

CREATE DATABASE IF NOT EXISTS `Eco-Friendly-TransportationDB`;

USE `Eco-Friendly-TransportationDB`;
-- -----------------------------------------------------
-- Table `Weather`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Weather` ;

CREATE TABLE IF NOT EXISTS `Weather` (
  `weather_id` INT NOT NULL,
  `humidity` INT NOT NULL,
  `temperature` DECIMAL(5,2) NOT NULL,
  `pollution_index` INT NOT NULL,
  `wind_speed` DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (`weather_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `User` ;

CREATE TABLE IF NOT EXISTS `User` (
  `User_id` INT NOT NULL AUTO_INCREMENT,
  `Username` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `Weather_weather_id` INT NOT NULL,
  PRIMARY KEY (`User_id`),
  UNIQUE INDEX `idUser_UNIQUE` (`User_id` ASC) VISIBLE,
  UNIQUE INDEX `Username_UNIQUE` (`Username` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  INDEX `fk_User_Weather1_idx` (`Weather_weather_id` ASC) VISIBLE,
  CONSTRAINT `fk_User_Weather1`
    FOREIGN KEY (`Weather_weather_id`)
    REFERENCES `Weather` (`weather_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Vehicle`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Vehicle` ;

CREATE TABLE IF NOT EXISTS `Vehicle` (
  `vehicle_id` INT NOT NULL AUTO_INCREMENT,
  `vehicle_type` VARCHAR(255) NOT NULL,
  `vehicle_company` VARCHAR(255) NOT NULL,
  `User_User_id` INT NOT NULL,
  UNIQUE INDEX `vehicle_id_UNIQUE` (`vehicle_id` ASC) VISIBLE,
  PRIMARY KEY (`vehicle_id`),
  CONSTRAINT `fk_Vehicle_User`
    FOREIGN KEY (`User_User_id`)
    REFERENCES `User` (`User_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Notifications`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Notifications` ;

CREATE TABLE IF NOT EXISTS `Notifications` (
  `notification_id` INT NOT NULL,
  `timestamp` DATETIME NOT NULL,
  `type` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`notification_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Mailing List Info`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mailing List Info` ;

CREATE TABLE IF NOT EXISTS `Mailing List Info` (
  `mailing_id` INT NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`mailing_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Route`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Route` ;

CREATE TABLE IF NOT EXISTS `Route` (
  `route_id` INT NOT NULL,
  `distance` DECIMAL(10,2) NOT NULL,
  `route_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`route_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Trip Sharing`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Trip Sharing` ;

CREATE TABLE IF NOT EXISTS `Trip Sharing` (
  `trip_sharing_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`trip_sharing_id`),
  UNIQUE INDEX `trip_sharing_id_UNIQUE` (`trip_sharing_id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Stations`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Stations` ;

CREATE TABLE IF NOT EXISTS `Stations` (
  `station_id` INT NOT NULL,
  `station_name` VARCHAR(255) NOT NULL,
  `station_location` VARCHAR(255) NOT NULL,
  `station type` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`station_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Charging Station`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Charging Station` ;

CREATE TABLE IF NOT EXISTS `Charging Station` (
  `station_name` INT NOT NULL,
  `station_location` VARCHAR(255) NOT NULL,
  `charging_units` INT NOT NULL,
  `Stations_station_id` INT NOT NULL,
  PRIMARY KEY (`Stations_station_id`),
  CONSTRAINT `fk_Charging Station_Stations1`
    FOREIGN KEY (`Stations_station_id`)
    REFERENCES `Stations` (`station_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Fueling Station`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Fueling Station` ;

CREATE TABLE IF NOT EXISTS `Fueling Station` (
  `station_name` VARCHAR(255) NOT NULL,
  `station_location` VARCHAR(255) NOT NULL,
  `Stations_station_id` INT NOT NULL,
  PRIMARY KEY (`Stations_station_id`),
  CONSTRAINT `fk_Fueling Station_Stations1`
    FOREIGN KEY (`Stations_station_id`)
    REFERENCES `Stations` (`station_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Regions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Regions` ;

CREATE TABLE IF NOT EXISTS `Regions` (
  `region_id` INT NOT NULL,
  `region_radius` DECIMAL(10,2) NOT NULL,
  `cooridnates` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`region_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Environmental Impact`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Environmental Impact` ;

CREATE TABLE IF NOT EXISTS `Environmental Impact` (
  `impact_id` INT NOT NULL AUTO_INCREMENT,
  `date` DATETIME NOT NULL,
  PRIMARY KEY (`impact_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `City`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `City` ;

CREATE TABLE IF NOT EXISTS `City` (
  `city_name` VARCHAR(255) NOT NULL,
  `city_area` DECIMAL(10,2) NOT NULL,
  `Regions_region_id` INT NOT NULL,
  `Environmental Impact_impact_id` INT NOT NULL,
  PRIMARY KEY (`Regions_region_id`),
  INDEX `fk_City_Environmental Impact1_idx` (`Environmental Impact_impact_id` ASC) VISIBLE,
  CONSTRAINT `fk_City_Regions1`
    FOREIGN KEY (`Regions_region_id`)
    REFERENCES `Regions` (`region_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_City_Environmental Impact1`
    FOREIGN KEY (`Environmental Impact_impact_id`)
    REFERENCES `Environmental Impact` (`impact_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `emission`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `emission` ;

CREATE TABLE IF NOT EXISTS `emission` (
  `emission_id` INT NOT NULL AUTO_INCREMENT,
  `fuel_tye` VARCHAR(255) NOT NULL,
  `carbon_emission` DECIMAL(10,2) NOT NULL,
  `pollution_index` DECIMAL(10,2) NOT NULL,
  `Vehicle_vehicle_id` INT NOT NULL,
  PRIMARY KEY (`emission_id`),
  INDEX `fk_emission_Vehicle1_idx` (`Vehicle_vehicle_id` ASC) VISIBLE,
  CONSTRAINT `fk_emission_Vehicle1`
    FOREIGN KEY (`Vehicle_vehicle_id`)
    REFERENCES `Vehicle` (`vehicle_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Campaign`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Campaign` ;

CREATE TABLE IF NOT EXISTS `Campaign` (
  `campaign` INT NOT NULL,
  `date` DATETIME NOT NULL,
  `campaign_type` VARCHAR(255) NOT NULL,
  `campaign_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`campaign`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `company`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `company` ;

CREATE TABLE IF NOT EXISTS `company` (
  `company_id` INT NOT NULL,
  `company_name` VARCHAR(255) NOT NULL,
  `vehicle_count` INT NOT NULL,
  `market_cap` DECIMAL(15,2) NOT NULL,
  PRIMARY KEY (`company_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Contracts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Contracts` ;

CREATE TABLE IF NOT EXISTS `Contracts` (
  `contract_id` INT NOT NULL AUTO_INCREMENT,
  `date` DATETIME NOT NULL,
  `contract_name` VARCHAR(255) NULL,
  `contract_type` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`contract_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Maintenence`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Maintenence` ;

CREATE TABLE IF NOT EXISTS `Maintenence` (
  `maintenance_id` INT NOT NULL AUTO_INCREMENT,
  `maintenance_name` VARCHAR(255) NOT NULL,
  `Vehicle_User_User_id` INT NOT NULL,
  PRIMARY KEY (`maintenance_id`),
  INDEX `fk_Maintenence_Vehicle1_idx` (`Vehicle_User_User_id` ASC) VISIBLE,
  CONSTRAINT `fk_Maintenence_Vehicle1`
    FOREIGN KEY (`Vehicle_User_User_id`)
    REFERENCES `Vehicle` (`User_User_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Account`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Account` ;

CREATE TABLE IF NOT EXISTS `Account` (
  `phone_number` INT NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `account_name` VARCHAR(255) NOT NULL,
  `User_User_id` INT NOT NULL,
  `company_company_id` INT NOT NULL,
  INDEX `fk_Account_User1_idx` (`User_User_id` ASC) VISIBLE,
  INDEX `fk_Account_company1_idx` (`company_company_id` ASC) VISIBLE,
  CONSTRAINT `fk_Account_User1`
    FOREIGN KEY (`User_User_id`)
    REFERENCES `User` (`User_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Account_company1`
    FOREIGN KEY (`company_company_id`)
    REFERENCES `company` (`company_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Payment Method`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Payment Method` ;

CREATE TABLE IF NOT EXISTS `Payment Method` (
  `payment_id` INT NOT NULL AUTO_INCREMENT,
  `payment_type` VARCHAR(255) NOT NULL,
  `payment_timestamp` DATETIME NOT NULL,
  `Stations_station_id` INT NOT NULL,
  `Maintenence_maintenance_id` INT NOT NULL,
  PRIMARY KEY (`payment_id`),
  INDEX `fk_Payment Method_Stations1_idx` (`Stations_station_id` ASC) VISIBLE,
  INDEX `fk_Payment Method_Maintenence1_idx` (`Maintenence_maintenance_id` ASC) VISIBLE,
  CONSTRAINT `fk_Payment Method_Stations1`
    FOREIGN KEY (`Stations_station_id`)
    REFERENCES `Stations` (`station_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Payment Method_Maintenence1`
    FOREIGN KEY (`Maintenence_maintenance_id`)
    REFERENCES `Maintenence` (`maintenance_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Bank Account`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Bank Account` ;

CREATE TABLE IF NOT EXISTS `Bank Account` (
  `account_number` VARCHAR(255) NOT NULL,
  `bank_name` VARCHAR(255) NOT NULL,
  `area_code` VARCHAR(255) NOT NULL,
  `Payment Method_payment_id` INT NOT NULL,
  PRIMARY KEY (`Payment Method_payment_id`),
  CONSTRAINT `fk_Bank Account_Payment Method1`
    FOREIGN KEY (`Payment Method_payment_id`)
    REFERENCES `Payment Method` (`payment_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Paypal`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Paypal` ;

CREATE TABLE IF NOT EXISTS `Paypal` (
  `paypal_account` VARCHAR(255) NOT NULL,
  `paypal_username` VARCHAR(255) NOT NULL,
  `timestamp` DATETIME NOT NULL,
  `Payment Method_payment_id` INT NOT NULL,
  PRIMARY KEY (`Payment Method_payment_id`),
  CONSTRAINT `fk_Paypal_Payment Method1`
    FOREIGN KEY (`Payment Method_payment_id`)
    REFERENCES `Payment Method` (`payment_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Crypto wallet`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Crypto wallet` ;

CREATE TABLE IF NOT EXISTS `Crypto wallet` (
  `wallet_address` INT NOT NULL,
  `amount` DECIMAL(15,2) NOT NULL,
  `crypto_type` VARCHAR(255) NOT NULL,
  `Payment Method_payment_id` INT NOT NULL,
  PRIMARY KEY (`Payment Method_payment_id`),
  CONSTRAINT `fk_Crypto wallet_Payment Method1`
    FOREIGN KEY (`Payment Method_payment_id`)
    REFERENCES `Payment Method` (`payment_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Credit card`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Credit card` ;

CREATE TABLE IF NOT EXISTS `Credit card` (
  `card_number` INT NOT NULL,
  `card_name` VARCHAR(255) NOT NULL,
  `bank_name` VARCHAR(255) NOT NULL,
  `Bank Account_Payment Method_payment_id` INT NOT NULL,
  PRIMARY KEY (`Bank Account_Payment Method_payment_id`),
  CONSTRAINT `fk_Credit card_Bank Account1`
    FOREIGN KEY (`Bank Account_Payment Method_payment_id`)
    REFERENCES `Bank Account` (`Payment Method_payment_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Debit card`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Debit card` ;

CREATE TABLE IF NOT EXISTS `Debit card` (
  `card_number` INT NOT NULL,
  `card_name` VARCHAR(255) NOT NULL,
  `bank_name` VARCHAR(45) NOT NULL,
  `payement_id` VARCHAR(45) NULL,
  `Bank Account_Payment Method_payment_id` INT NOT NULL,
  PRIMARY KEY (`Bank Account_Payment Method_payment_id`),
  CONSTRAINT `fk_Debit card_Bank Account1`
    FOREIGN KEY (`Bank Account_Payment Method_payment_id`)
    REFERENCES `Bank Account` (`Payment Method_payment_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Mailing List Info_has_User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mailing List Info_has_User` ;

CREATE TABLE IF NOT EXISTS `Mailing List Info_has_User` (
  `Mailing List Info_mailing_id` INT NOT NULL,
  `User_User_id` INT NOT NULL,
  PRIMARY KEY (`Mailing List Info_mailing_id`),
  INDEX `fk_Mailing List Info_has_User_User1_idx` (`User_User_id` ASC) VISIBLE,
  INDEX `fk_Mailing List Info_has_User_Mailing List Info1_idx` (`Mailing List Info_mailing_id` ASC) VISIBLE,
  CONSTRAINT `fk_Mailing List Info_has_User_Mailing List Info1`
    FOREIGN KEY (`Mailing List Info_mailing_id`)
    REFERENCES `Mailing List Info` (`mailing_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Mailing List Info_has_User_User1`
    FOREIGN KEY (`User_User_id`)
    REFERENCES `User` (`User_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `User_has_User_as_friends`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `User_has_User_as_friends` ;

CREATE TABLE IF NOT EXISTS `User_has_User_as_friends` (
  `User_User_id` INT NOT NULL,
  `User_User_id1` INT NOT NULL,
  PRIMARY KEY (`User_User_id`, `User_User_id1`),
  INDEX `fk_User_has_User_User2_idx` (`User_User_id1` ASC) VISIBLE,
  INDEX `fk_User_has_User_User1_idx` (`User_User_id` ASC) VISIBLE,
  CONSTRAINT `fk_User_has_User_User1`
    FOREIGN KEY (`User_User_id`)
    REFERENCES `User` (`User_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_has_User_User2`
    FOREIGN KEY (`User_User_id1`)
    REFERENCES `User` (`User_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `company_has_Campaign`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `company_has_Campaign` ;

CREATE TABLE IF NOT EXISTS `company_has_Campaign` (
  `company_company_id` INT NOT NULL,
  `Campaign_campaign` INT NOT NULL,
  INDEX `fk_company_has_Campaign_Campaign1_idx` (`Campaign_campaign` ASC) VISIBLE,
  INDEX `fk_company_has_Campaign_company1_idx` (`company_company_id` ASC) VISIBLE,
  CONSTRAINT `fk_company_has_Campaign_company1`
    FOREIGN KEY (`company_company_id`)
    REFERENCES `company` (`company_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_company_has_Campaign_Campaign1`
    FOREIGN KEY (`Campaign_campaign`)
    REFERENCES `Campaign` (`campaign`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Route_has_Vehicle`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Route_has_Vehicle` ;

CREATE TABLE IF NOT EXISTS `Route_has_Vehicle` (
  `Route_route_id` INT NOT NULL,
  `Vehicle_User_User_id` INT NOT NULL,
  INDEX `fk_Route_has_Vehicle_Vehicle1_idx` (`Vehicle_User_User_id` ASC) VISIBLE,
  INDEX `fk_Route_has_Vehicle_Route1_idx` (`Route_route_id` ASC) VISIBLE,
  CONSTRAINT `fk_Route_has_Vehicle_Route1`
    FOREIGN KEY (`Route_route_id`)
    REFERENCES `Route` (`route_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Route_has_Vehicle_Vehicle1`
    FOREIGN KEY (`Vehicle_User_User_id`)
    REFERENCES `Vehicle` (`User_User_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Notifications_has_User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Notifications_has_User` ;

CREATE TABLE IF NOT EXISTS `Notifications_has_User` (
  `Notifications_notification_id` INT NOT NULL,
  `User_User_id` INT NOT NULL,
  INDEX `fk_Notifications_has_User_User1_idx` (`User_User_id` ASC) VISIBLE,
  INDEX `fk_Notifications_has_User_Notifications1_idx` (`Notifications_notification_id` ASC) VISIBLE,
  CONSTRAINT `fk_Notifications_has_User_Notifications1`
    FOREIGN KEY (`Notifications_notification_id`)
    REFERENCES `Notifications` (`notification_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Notifications_has_User_User1`
    FOREIGN KEY (`User_User_id`)
    REFERENCES `User` (`User_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `emission_has_Environmental Impact`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `emission_has_Environmental Impact` ;

CREATE TABLE IF NOT EXISTS `emission_has_Environmental Impact` (
  `emission_emission_id` INT NOT NULL,
  `Environmental Impact_impact_id` INT NOT NULL,
  INDEX `fk_emission_has_Environmental Impact_Environmental Impact1_idx` (`Environmental Impact_impact_id` ASC) VISIBLE,
  INDEX `fk_emission_has_Environmental Impact_emission1_idx` (`emission_emission_id` ASC) VISIBLE,
  CONSTRAINT `fk_emission_has_Environmental Impact_emission1`
    FOREIGN KEY (`emission_emission_id`)
    REFERENCES `emission` (`emission_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_emission_has_Environmental Impact_Environmental Impact1`
    FOREIGN KEY (`Environmental Impact_impact_id`)
    REFERENCES `Environmental Impact` (`impact_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `User_has_Trip Sharing`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `User_has_Trip Sharing` ;

CREATE TABLE IF NOT EXISTS `User_has_Trip Sharing` (
  `User_User_id` INT NOT NULL,
  `Trip Sharing_trip_sharing_id` INT NOT NULL,
  PRIMARY KEY (`User_User_id`, `Trip Sharing_trip_sharing_id`),
  INDEX `fk_User_has_Trip Sharing_Trip Sharing1_idx` (`Trip Sharing_trip_sharing_id` ASC) VISIBLE,
  INDEX `fk_User_has_Trip Sharing_User1_idx` (`User_User_id` ASC) VISIBLE,
  CONSTRAINT `fk_User_has_Trip Sharing_User1`
    FOREIGN KEY (`User_User_id`)
    REFERENCES `User` (`User_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_has_Trip Sharing_Trip Sharing1`
    FOREIGN KEY (`Trip Sharing_trip_sharing_id`)
    REFERENCES `Trip Sharing` (`trip_sharing_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `company_has_Contracts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `company_has_Contracts` ;

CREATE TABLE IF NOT EXISTS `company_has_Contracts` (
  `company_company_id` INT NOT NULL,
  `Contracts_contract_id` INT NOT NULL,
  PRIMARY KEY (`company_company_id`, `Contracts_contract_id`),
  INDEX `fk_company_has_Contracts_Contracts1_idx` (`Contracts_contract_id` ASC) VISIBLE,
  INDEX `fk_company_has_Contracts_company1_idx` (`company_company_id` ASC) VISIBLE,
  CONSTRAINT `fk_company_has_Contracts_company1`
    FOREIGN KEY (`company_company_id`)
    REFERENCES `company` (`company_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_company_has_Contracts_Contracts1`
    FOREIGN KEY (`Contracts_contract_id`)
    REFERENCES `Contracts` (`contract_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
