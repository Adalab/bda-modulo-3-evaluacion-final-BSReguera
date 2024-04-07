#%%
# Importaciones necesarias
import pandas as pd
from src import soporte_eda as eda
from src import soporte_conexion as conexion
 
# Apertura y carga de los conjuntos de datos en DataFrames
customer_loyalty_history = pd.read_csv("Customer Loyalty History.csv")
customer_flight_activity = pd.read_csv("Customer Flight Activity.csv")

#%%
# Funciones exploracion
eda.exploracion_general(customer_loyalty_history)
eda.exploracion_columna(customer_loyalty_history)
eda.exploracion_general(customer_flight_activity)
eda.exploracion_columna(customer_flight_activity)

#%%
# Funciones limpieza
merged_data = pd.merge(customer_loyalty_history, customer_flight_activity, on="Loyalty Number", how='inner')
merged_data
missing_data_series = eda.gestionar_nulos(merged_data)
lista_eliminar = ["Cancellation Year", "Cancellation Month"]
eda.eliminar_columnas(merged_data, lista_eliminar)
merged_data['Salary'] = merged_data['Salary'].apply(eda.transformacion_salary)

#%%
# Función visualización
eda.plot_multiple_visualizaciones(merged_data)

#%%
# Funciones ABTesting
# Filtrar el conjunto de datos
relevant_columns = ["Flights Booked", "Education"]
flight_education_data = merged_data[relevant_columns]
flight_education_data

eda.analisis_descriptivo(flight_education_data)
eda.ab_testing_flight_bookings(flight_education_data)
filtered_superior, filtered_basic = eda.filter_education_levels(flight_education_data)
# Calcular la media de vuelos reservados para cada grupo
mean_flights_superior = filtered_superior['Flights Booked'].mean()
mean_flights_basic = filtered_basic['Flights Booked'].mean()


eda.normalidad(filtered_superior, 'Flights Booked')
eda.normalidad(filtered_basic, 'Flights Booked')

eda.mann_whitney_test(filtered_superior['Flights Booked'], filtered_basic['Flights Booked'])

#%%
# Funciones de carga (Creacion de bbdd y tablas)
conexion.creacion_bbdd("root", "12345")
conexion.creacion_tablas("root", "12345", "fly")

#%%
# Datos tablas
datos_tabla_History = list(set(zip(merged_data["LOYALTYNUMBER"].values, merged_data["COUNTRY"].values, merged_data["PROVINCE"].values, merged_data["CITY"].values, merged_data["POSTALCODE"].values, merged_data["GENDER"].values, merged_data["EDUCATION"].values, merged_data["SALARY"].values, merged_data["MARITALSTATUS"].values, merged_data["LOYALTYCARD"].values, merged_data["CLV"].values, merged_data["ENROLLMENTTYPE"].values, merged_data["ENROLLMENTYEAR"].values)))
datos_tabla_Activity = list(set(zip(merged_data["LOYALTYNUMBER"].values, merged_data["YEAR"].values, merged_data["MONTH"].values, merged_data["FLIGHTSBOOKED"].values, merged_data["FLIGHTSWITHCOMPANIES"].values, merged_data["TOTALFLIGHTS"].values, merged_data["DISTANCE"].values, merged_data["POINTACCUMULATED"].values, merged_data["POINTSREDEEMED"].values, merged_data["DOLLARCOSTPOINTSREDEEMED"].values)))

#%%
#Funciones inserción
conexion.insertar_datos(conexion.query_insertar_History, "12345", "fly", datos_tabla_History)
conexion.insertar_datos(conexion.query_insertar_Activity, "12345", "fly", datos_tabla_Activity)
