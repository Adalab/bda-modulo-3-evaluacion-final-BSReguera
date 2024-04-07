#%%
# Importar librería para la conexión con MySQL
import mysql.connector
from mysql.connector import errorcode


# Importar librerías para manipulación y análisis de datos
import pandas as pd
import numpy as np
# %%
def creacion_bbdd (usuario, contrasenya):
    """Esta funcion crea la bbdd fly en mysql

    Args:
    - usuario: usuario para la conexion al servidor
    - contraseña: contraseña para la conexión al servidor

    Returns:
    No devuelve ningún valor
    """
    
    cnx = mysql.connector.connect(user=usuario, password=contrasenya,
                                host='127.0.0.1')


    mycursor = cnx.cursor()
    query = "CREATE SCHEMA "

    try: 
        mycursor.execute(query) 
    
        print("BBDD creada")

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)


def creacion_tablas (usuario, contrasenya, bbdd):
    """Esta funcion crea las tablas Activity y History en mysql

    Args:
    - usuario: usuario para la conexion al servidor
    - contraseña: contraseña para la conexión al servidor
    - bbdd: nombre de la bbdd donde queremos crear las tablas

    Returns:
    No devuelve ningún valor
    """
    
    cnx = mysql.connector.connect(user=usuario, password=contrasenya,
                                host='127.0.0.1', database= bbdd)


    # Tabla Activity: 
    mycursor = cnx.cursor()
    query = "CREATE TABLE `Activity` (`Loyalty Number` INT NOT NULL, `Year` FLOAT NOT NULL, `Month` FLOAT NOT NULL, `Flights Booked` FLOAT NOT NULL, `Flights with Companies` FLOAT NOT NULL, `Total Flights` FLOAT NOT NULL, `Distance` FLOAT NOT NULL, `Points Accumulated` FLOAT NOT NULL, `Points Redeemed` FLOAT NOT NULL, `Dollar Cost Points Redeemed` FLOAT NOT NULL, PRIMARY KEY (`Loyalty Number`))"
    
    try: 
        mycursor.execute(query)
    
        print("Tabla Activity creada")

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)

    # Tabla History:
    mycursor = cnx.cursor()
    query = "CREATE TABLE `History` ( `Loyalty Number` INT NOT NULL, `Country` VARCHAR(45) NOT NULL, `Province` VARCHAR(45) NOT NULL, `City` VARCHAR(45) NOT NULL, `Postal Code` VARCHAR(45) NOT NULL, `Gender` VARCHAR(45) NOT NULL, `Education` VARCHAR(45) NOT NULL, `Salary` FLOAT NOT NULL, `Marital Status` VARCHAR(45) NOT NULL, `Loyalty Card` VARCHAR(45) NOT NULL, `CLV` DECIMAL NOT NULL, `Enrollment Type` VARCHAR(45) NOT NULL, `Enrollment Year` FLOAT NOT NULL, PRIMARY KEY (`Loyalty Number`))"
        
    try: 
        mycursor.execute(query)
    
        print("Tabla History creada")

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
 
    cnx.close()


#  QUERYS DE INSERCION DE DATOS

query_insertar_History = "INSERT INTO Activity (Loyalty Number, Year, Month, Flights Booked, Flights with Companies, Total Flights, Distance, Points Accumulated, Points Redeemed, Dollar Cost Points Redeemed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

query_insertar_Activity = "INSERT INTO History (Loyalty Number, Country, Province, City, Postal Code, Gender, Education, Salary, Marital Status, Loyalty Card, CLV, Enrollment Type, Enrollment Year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


def insertar_datos(query, contraseña, nombre_bbdd, lista_tuplas):
    """
    Inserta datos en una base de datos utilizando una consulta y una lista de tuplas como valores.

    Args:
    - query (str): Consulta SQL con placeholders para la inserción de datos.
    - contraseña (str): Contraseña para la conexión a la base de datos.
    - nombre_bbdd (str): Nombre de la base de datos a la que se conectará.

    Returns:
    No devuelve ningún valor, pero inserta los datos en la base de datos.

    """
    cnx = mysql.connector.connect(
        user="root", 
        password=contraseña, 
        host="127.0.0.1", database=nombre_bbdd
    )

    mycursor = cnx.cursor()

    try:
        mycursor.executemany(query, lista_tuplas)
        cnx.commit()
        print(mycursor.rowcount, "registro/s insertado/s.")
        cnx.close()

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        cnx.close()

# %%
