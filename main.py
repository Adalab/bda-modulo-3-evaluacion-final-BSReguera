#%%
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
#Funciones limpieza
merged_data = pd.merge(customer_loyalty_history, customer_flight_activity, on="Loyalty Number", how='inner')
merged_data
missing_data_series = eda.gestionar_nulos(merged_data)
lista_eliminar = ["Cancellation Year", "Cancellation Month"]
eda.eliminar_columnas(merged_data, lista_eliminar)
merged_data['Salary'] = merged_data['Salary'].apply(eda.transformacion_salary)

#%%
eda.plot_multiple_visualizaciones(merged_data)
#%%
eda.analisis_descriptivo(flight_education_data)
eda.ab_testing_flight_bookings(flight_education_data)
filtered_superior, filtered_basic = eda.filter_education_levels(flight_education_data)
# Calcular la media de vuelos reservados para cada grupo
mean_flights_superior = filtered_superior['Flights Booked'].mean()
mean_flights_basic = filtered_basic['Flights Booked'].mean()


#%%
#Creacion de bbdd y tablas
conexion.creacion_bbdd("root", "AlumnaAdalab")
conexion.creacion_tablas("root", "AlumnaAdalab", "raw_data")

# %%
df_empleado_unico = df_sin_duplicados.drop_duplicates(subset='EMPLOYEENUMBER')
# %%

datos_tabla_empleado = list(set(zip(df_empleado_unico["EMPLOYEENUMBER"].values, df_empleado_unico["AGE"].values, df_empleado_unico["EDUCATION"].values, df_empleado_unico["EDUCATIONFIELD"].values, df_empleado_unico["GENDER"].values, df_empleado_unico["MARITALSTATUS"].values, df_empleado_unico["WORKLIFEBALANCE"].values, df_empleado_unico["NUMCOMPANIESWORKED"].values, df_empleado_unico["RELATIONSHIPSATISFACTION"].values, df_empleado_unico["TOTALWORKINGYEARS"].values)))
datos_tabla_empleado_empresa = list(set(zip(df_empleado_unico["EMPLOYEENUMBER"].values, df_empleado_unico["DEPARTMENT"].values, df_empleado_unico["BUSINESSTRAVEL"].values, df_empleado_unico["JOBINVOLVEMENT"].values, df_empleado_unico["JOBROLE"].values, df_empleado_unico["JOBSATISFACTION"].values, df_empleado_unico["ATTRITION"].values, df_empleado_unico["YEARSATCOMPANY"].values, df_empleado_unico["MONTHLYRATE"].values, df_empleado_unico["PERCENTSALARYHIKE"].values, df_empleado_unico["STOCKOPTIONLEVEL"].values, df_empleado_unico["TRAININGTIMESLASTYEAR"].values, df_empleado_unico["YEARSSINCELASTPROMOTION"].values, df_empleado_unico["YEARSWITHCURRMANAGER"].values, df_empleado_unico["DAILYRATE"].values, df_empleado_unico["PERFORMANCERATING"].values)))
datos_tabla_registro = list(set(zip(df_sin_duplicados["EMPLOYEENUMBER"].values, df_sin_duplicados["DISTANCEFROMHOME"].values, df_sin_duplicados["REMOTEWORK"].values, df_sin_duplicados["MONTHLYINCOME"].values, df_sin_duplicados["HOURLYRATE"].values, df_sin_duplicados["OVERTIME"].values, df_sin_duplicados["ENVIRONMENTSATISFACTION"].values)))
#%%
datos_tabla_empleado1 = conexion.convertir_float(datos_tabla_empleado)
datos_tabla_empleado_empresa1 = conexion.convertir_float(datos_tabla_empleado_empresa)
datos_tabla_registro1 = conexion.convertir_float(datos_tabla_registro)

datos_tabla_empleado2 = conexion.convertir_int(datos_tabla_empleado1)
datos_tabla_empleado_empresa2 = conexion.convertir_int(datos_tabla_empleado_empresa1)
datos_tabla_registro2 = conexion.convertir_int(datos_tabla_registro1)

#%%

datos_tabla_empleado3 = conexion.cambio_unknown(datos_tabla_empleado2)
datos_tabla_empleado_empresa3 = conexion.cambio_unknown(datos_tabla_empleado_empresa2)
datos_tabla_registro3 = conexion.cambio_unknown(datos_tabla_registro2)

#%%
conexion.insertar_datos(conexion.query_insertar_empleado, "AlumnaAdalab", "raw_data", datos_tabla_empleado3)
#%%
conexion.insertar_datos(conexion.query_insertar_empleado_empresa, "AlumnaAdalab", "raw_data", datos_tabla_empleado_empresa3)
#%%
conexion.insertar_datos(conexion.query_insertar_registro, "AlumnaAdalab", "raw_data", datos_tabla_registro3)