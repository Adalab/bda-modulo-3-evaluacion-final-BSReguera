-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema fly
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema fly
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `fly` DEFAULT CHARACTER SET utf8 ;
USE `fly` ;

-- -----------------------------------------------------
-- Table `fly`.`Activity`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fly`.`Activity` (
  `Loyalty Number` INT NOT NULL,
  `Year` FLOAT NOT NULL,
  `Month` FLOAT NOT NULL,
  `Flights Booked` FLOAT NOT NULL,
  `Flights with Companies` FLOAT NOT NULL,
  `Total Flights` FLOAT NOT NULL,
  `Distance` FLOAT NOT NULL,
  `Points Accumulated` FLOAT NOT NULL,
  `Points Redeemed` FLOAT NOT NULL,
  `Dollar Cost Points Redeemed` FLOAT NOT NULL,
  PRIMARY KEY (`Loyalty Number`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `fly`.`History`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fly`.`History` (
  `Loyalty Number` INT NOT NULL,
  `Country` VARCHAR(45) NOT NULL,
  `Province` VARCHAR(45) NOT NULL,
  `City` VARCHAR(45) NOT NULL,
  `Postal Code` VARCHAR(45) NOT NULL,
  `Gender` VARCHAR(45) NOT NULL,
  `Education` VARCHAR(45) NOT NULL,
  `Salary` FLOAT NOT NULL,
  `Marital Status` VARCHAR(45) NOT NULL,
  `Loyalty Card` VARCHAR(45) NOT NULL,
  `CLV` DECIMAL NOT NULL,
  `Enrollment Type` VARCHAR(45) NOT NULL,
  `Enrollment Year` FLOAT NOT NULL,
  PRIMARY KEY (`Loyalty Number`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
