query_creacion_bbdd = "CREATE SCHEMA IF NOT EXISTS `fly`;"

query_tabla_History = """CREATE TABLE IF NOT EXISTS `fly`.`History` (
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
  PRIMARY KEY (`Loyalty Number`));"""
  
query_tabla_Activity = """CREATE TABLE IF NOT EXISTS `fly`.`Activity` (
  `Loyalty Number` INT NOT NULL,L
  `Year` FLOAT NOT NULL,
  `Month` FLOAT NOT NULL,
  `Flights Booked` FLOAT NOT NULL,
  `Flights with Companies` FLOAT NOT NULL,
  `Total Flights` FLOAT NOT NULL,
  `Distance` FLOAT NOT NULL,
  `Points Accumulated` FLOAT NOT NULL,
  `Points Redeemed` FLOAT NOT NULL,
  `Dollar Cost Points Redeemed` FLOAT NOT NULL,
  PRIMARY KEY (`Loyalty Number`));"""  
  
query_insertar_History = "INSERT INTO Activity (Loyalty Number, Year, Month, Flights Booked, Flights with Companies, Total Flights, Distance, Points Accumulated, Points Redeemed, Dollar Cost Points Redeemed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

query_insertar_Activity = "INSERT INTO History (Loyalty Number, Country, Province, City, Postal Code, Gender, Education, Salary, Marital Status, Loyalty Card, CLV, Enrollment Type, Enrollment Year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
