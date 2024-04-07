#%%
import pandas as pd
import numpy as np 
from word2number import w2n

# Imputación de nulos usando métodos avanzados estadísticos
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer

# Librerías de visualización
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display

# Configuración
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

# FUNCIÓN DE EXPLORACIÓN
def exploracion_general(dataframe):
    """Esta función proporciona una descripción personalizada de un DataFrame,
    incluyendo estadísticas descriptivas y tipos de datos de cada columna.
    
    Argumentos:
    dataframe : DataFrame de Pandas
        El DataFrame para el cual se generará la descripción
        
    La función no tiene return pero devuelve varios prints con la información necesaria:
    - describe separados por columnas numéricas y categóricas
    - dtypes por columna
    - shape
    - info
    - total de nulos
    - total de duplicados"""

    print(f"------EXPLORACIÓN DATAFRAME {dataframe}------")
    print("-------Descripción numéricas:---------")
    print(dataframe.describe())
    
    if any(dataframe.dtypes == 'object'):
        print("-------Descripción categóricas:---------")
        print(dataframe.describe(include="O"))
    else:
        print("No hay columnas categóricas en este DataFrame.")

    print("------Tipos:---------")
    print(dataframe.dtypes)
    print("------Forma del DataFrame:------")
    print(dataframe.shape)
    print("------Información:---------")
    print(dataframe.info())
    print("------Nulos:---------")
    print(dataframe.isnull().sum())
    print("------Duplicados:---------")
    print(dataframe.duplicated().sum())

def exploracion_columna(dataframe):
    """Realiza un análisis exploratorio de cada columna en un DataFrame dado.

    Parameters:
    dataframe (DataFrame): El DataFrame que se desea analizar."""
    # Iterar sobre cada columna en el DataFrame
    for columna in list(dataframe.columns):
        # Imprimir encabezado para la columna actual
        print(f" \n----------- ANALIZANDO LA COLUMNA: '{columna.upper()}' -----------\n")
        # Imprimir número de datos en la columna
        print(f"* Número de datos: {len(dataframe[columna].to_list())}")
        # Imprimir frecuencia de valores en la columna
        print(f"* Frecuencia de valores en la columna: \n {dataframe[columna].value_counts()}")
        # Imprimir cantidad de valores únicos en la columna
        print(f"* Datos únicos en la columna: {len(dataframe[columna].unique())}")
        # Imprimir tipo de datos de la columna
        print(f"* Los valores son de tipo: {dataframe[columna].dtype}")
        # Imprimir suma de datos nulos en la columna
        print(f"* La suma de datos nulos: {dataframe[columna].isnull().sum()}")
        # Imprimir lista de valores únicos en la columna
        print(f"* Valores únicos: {dataframe[columna].unique()}")

# FUNCIONES DE LIMPIEZA:
def gestionar_nulos(dataframe):
    """ Verifica la presencia de datos faltantes en un DataFrame y calcula el porcentaje de datos faltantes por columna.

    Parameters:
    dataframe (DataFrame): DataFrame a verificar.

    Returns:
    pandas.Series: Serie que contiene la cantidad de datos faltantes por columna. """
    
    # Verificar datos faltantes después de la unión
    print("Datos faltantes en el conjunto de datos:")
    merged_data = dataframe.isnull().sum()

    # Calcular el porcentaje de datos faltantes para cada columna
    missing_percentage = (merged_data / len(dataframe)) * 100

    # Imprimir el porcentaje de datos faltantes
    print("Porcentaje de datos faltantes en el conjunto de datos:")
    print(missing_percentage)

    return merged_data  # Devolver la cantidad de datos faltantes por columna como una Serie


def eliminar_columnas (merged_data, lista):
    """ Elimina las columnas indicadas

    Args:
    merged_data: el DF que queremos modificar
    lista: lista de columnas que queremos eliminar

    Returns:
    No tiene return, modifica el DF con "inplace=True"    """
    merged_data.drop(columns=["Cancellation Year", "Cancellation Month"], inplace=True)


def transformacion_salary(valor):
    """ Transforma un valor de salario en formato string en un entero después de limpiarlo.
    
    Parameters:
    valor (str): Valor de salario en formato string.
    
    Returns:
    int: Valor de salario limpiado y convertido a entero."""
    if valor != np.nan:
        valor = str(valor).replace('-', '')  # Elimina los guiones
        valor = valor.split('.')[0]  # Obtiene la parte entera antes del punto
        return int(valor)
    else:
        return np.nan

def preprocesar_salarios(dataframe, columna):
    """Preprocesa la columna de salarios de un DataFrame, imputando valores nulos y aplicando transformación.
    
    Parameters:
    dataframe (DataFrame): DataFrame que contiene los datos.
    columna (str): Nombre de la columna que contiene los salarios.
    
    Returns:
    DataFrame: DataFrame actualizado con la columna de salarios preprocesada."""
    # Imputar la media a los valores nulos en la columna 'Salary'
    salario_promedio = dataframe[columna].mean()
    dataframe[columna] = dataframe[columna].fillna(salario_promedio)

    # Aplicar la función de transformación a la columna 'Salary'
    dataframe[columna] = dataframe[columna].apply(transformacion_salary)

    return dataframe

# FUNCIÓN DE VISUALIZACIÓN

def plot_multiple_visualizaciones(data):
    """ Función para trazar múltiples visualizaciones de datos utilizando seaborn y matplotlib.

    Parameters:
    data (DataFrame): DataFrame que contiene los datos a visualizar."""
    # Visualización 1: Cantidad de vuelos reservados por mes durante el año (gráfico de barras)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x="Month", y="Flights Booked", hue="Year", palette="muted")
    plt.title("Cantidad de vuelos reservados por mes durante el año")
    plt.xlabel("Mes")
    plt.ylabel("Cantidad de vuelos reservados")
    plt.legend(title="Año")
    plt.show()

    # Visualización 2: Cantidad de vuelos reservados por mes durante el año (gráfico de líneas)
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x="Month", y="Flights Booked", hue="Year", palette="tab10")
    plt.title("Cantidad de vuelos reservados por mes durante el año")
    plt.xlabel("Mes")
    plt.ylabel("Cantidad de vuelos reservados")
    plt.xticks(range(1, 13))
    plt.legend(title="Año")
    plt.show()

    # Visualización 3: Relación entre la distancia de los vuelos y los puntos acumulados por los clientes
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x="Distance", y="Points Accumulated")
    plt.title("Relación entre distancia de vuelos y puntos acumulados")
    plt.xlabel("Distancia de vuelos")
    plt.ylabel("Puntos acumulados")
    plt.show()

    # Visualización 4: Distribución de los clientes por provincia o estado
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x="Province")
    plt.title("Distribución de los clientes por provincia o estado")
    plt.xlabel("Provincia")
    plt.ylabel("Cantidad de clientes")
    plt.xticks(rotation=45)
    plt.show()

    # Visualización 5: Comparación del salario promedio por nivel educativo
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x="Education", y="Salary", estimator=pd.np.mean, palette="muted")
    plt.title("Comparación del salario promedio por nivel educativo")
    plt.xlabel("Nivel educativo")
    plt.ylabel("Salario promedio")
    plt.xticks(rotation=45)
    plt.show()

    # Visualización 6: Proporción de clientes con diferentes tipos de tarjetas de fidelidad (gráfico de pastel)
    plt.figure(figsize=(8, 8))
    data["Loyalty Card"].value_counts().plot.pie(autopct="%1.1f%%", colors=sns.color_palette("pastel"), explode=(0.1, 0.1, 0.1))
    plt.title("Proporción de clientes con diferentes tipos de tarjetas de fidelidad")
    plt.axis("equal")
    plt.legend(labels=data["Loyalty Card"].value_counts().index, loc="upper right")
    plt.show()

    # Visualización 7: Distribución de los clientes por estado civil y género
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x="Marital Status", hue="Gender")
    plt.title("Distribución de los clientes por estado civil y género")
    plt.xlabel("Estado civil")
    plt.ylabel("Cantidad de clientes")
    plt.xticks(rotation=45)
    plt.legend(title="Género")
    plt.show()

    # Visualización 8: Relación entre salario y CLV (valor vitalicio del cliente)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x="Salary", y="CLV", hue="Gender", palette="pastel")
    plt.title("Relación entre salario y CLV")
    plt.xlabel("Salario")
    plt.ylabel("CLV")
    plt.show()

    # Visualización 9: Distribución del salario por nivel educativo y género (diagrama de caja)
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x="Education", y="Salary", hue="Gender", palette="pastel")
    plt.title("Distribución del salario por nivel educativo y género")
    plt.xlabel("Nivel educativo")
    plt.ylabel("Salario")
    plt.xticks(rotation=45)
    plt.legend(title="Género")
    plt.show()

# FUNCIONES A/B Testing
def analisis_descriptivo(flight_data):
    """
    Realiza un análisis descriptivo y un gráfico de barras para comparar el promedio de vuelos reservados
    por nivel educativo en un DataFrame de datos de vuelos.

    Parámetros:
        flight_data (DataFrame): DataFrame que contiene los datos de vuelos y niveles educativos.

    Retorna:
        None: Muestra un gráfico de barras y estadísticas descriptivas por nivel educativo.
    """
    # Filtrar el conjunto de datos
    relevant_columns = ["Flights Booked", "Education"]
    flight_education_data = merged_data[relevant_columns]
    flight_education_data
    
    # Calcular estadísticas descriptivas por nivel educativo
    education_group = flight_data.groupby("Education")["Flights Booked"].describe()

    # Mostrar el gráfico de barras
    plt.figure(figsize=(10, 6))  # Establece el tamaño de la figura
    sns.barplot(x=education_group.index, y=education_group["mean"], palette="viridis")  # Crear el gráfico de barras
    plt.title("Promedio de vuelos reservados por nivel educativo")  # Título del gráfico
    plt.xlabel("Nivel educativo")  # Etiqueta del eje x
    plt.ylabel("Promedio de vuelos reservados")  # Etiqueta del eje y
    plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para una mejor visualización

    # Agregar etiquetas numéricas en la parte superior de cada barra
    for index, value in enumerate(education_group["mean"]):
        plt.text(index, value + 0.1, f"{value:.2f}", ha='center', va='bottom', fontsize=10)

    plt.show()  # Mostrar el gráfico

    # Calcular estadísticas descriptivas básicas de forma individual
    # Agrupar los datos por nivel educativo
    education_groups = flight_data.groupby("Education")["Flights Booked"]

    # Calcular el promedio para cada grupo
    average_flights = education_groups.mean()
    print("Promedio de vuelos reservados por nivel educativo:\n", average_flights)

    # Calcular la desviación estándar para cada grupo
    std_dev_flights = education_groups.std()
    print("\nDesviación estándar de vuelos reservados por nivel educativo:\n", std_dev_flights)

    # Calcular percentiles para cada grupo (25%, 50%, 75%)
    percentiles_flights = education_groups.quantile([0.25, 0.5, 0.75])
    print("\nPercentiles de vuelos reservados por nivel educativo:\n", percentiles_flights)

    # Calcular la mediana para cada grupo
    median_flights = education_groups.median()
    print("\nMediana de vuelos reservados por nivel educativo:\n", median_flights)

# Llamada a la función
analisis_descriptivo(flight_education_data)


def ab_testing_flight_bookings(data):
    """
    Realiza un análisis de A/B testing para determinar si existen diferencias significativas en el número de vuelos
    reservados entre diferentes niveles educativos.

    Parámetros:
        data (DataFrame): DataFrame que contiene los datos de vuelos y niveles educativos.

    Retorna:
        dict: Un diccionario que contiene el resultado del análisis.
            - 'H0': Hipótesis nula.
            - 'H1': Hipótesis alternativa.
    """
    # Filtrar columnas relevantes
    flight_education_data = data[['Flights Booked', 'Education']]

    # Formular hipótesis
    H0 = "No hay diferencias significativas en el número de vuelos reservados entre los diferentes niveles educativos."
    H1 = "Existen diferencias significativas en el número de vuelos reservados entre los diferentes niveles educativos."

    # Definir niveles educativos para educación superior y educación básica
    levels_superior_education = ['College', 'Doctor', 'Master']
    levels_basic_education = ['High School or Below', 'Bachelor']

    # Filtrar datos por niveles educativos
    superior_data = flight_education_data[flight_education_data['Education'].isin(levels_superior_education)]
    basic_data = flight_education_data[flight_education_data['Education'].isin(levels_basic_education)]

    # Guardar resultados en un diccionario
    result = {
        'H0': H0,
        'H1': H1,    }

    return result

# Llamada a la función
results = ab_testing_flight_bookings(flight_education_data)

# Imprimir los resultados del análisis
print("Hipótesis Nula (H0):", results['H0'])
print("Hipótesis Alternativa (H1):", results['H1'])

def filter_education_levels(dataframe):
    """
    Filtra los datos para niveles educativos superiores y básicos en un DataFrame dado.
    
    Parámetros:
        dataframe (DataFrame): El DataFrame que contiene los datos de educación.
    
    Returns:
        DataFrame, DataFrame: Dos DataFrames filtrados, uno para niveles educativos superiores y otro para básicos.
    """
    # Filtrar datos para niveles educativos superiores
    levels_superior_education = dataframe[dataframe['Education'].isin(['College', 'Doctor', 'Master'])]
    
    # Filtrar datos para niveles educativos básicos
    levels_basic_education = dataframe[dataframe['Education'].isin(['High School or Below', 'Bachelor'])]
    
    return levels_superior_education, levels_basic_education

# Llamar a la función para filtrar niveles educativos
filtered_superior, filtered_basic = filter_education_levels(flight_education_data)

# Mostrar las primeras filas de los DataFrames filtrados
print("Niveles educativos superiores:", filtered_superior.head())
print("\nNiveles educativos básicos:", filtered_basic.head())
# %%
# Calcular la media de vuelos reservados para cada grupo
mean_flights_superior = filtered_superior['Flights Booked'].mean()
mean_flights_basic = filtered_basic['Flights Booked'].mean()

# Imprimir resultados
print(f"Media de vuelos reservados para niveles educativos superiores: {mean_flights_superior}")
print(f"Media de vuelos reservados para niveles educativos básicos: {mean_flights_basic}")

def normalidad(dataframe, columna):
    """
    Evalúa la normalidad de una columna de datos de un DataFrame utilizando la prueba de Shapiro-Wilk.
    Parámetros:
        dataframe (DataFrame): El DataFrame que contiene los datos.
        columna (str): El nombre de la columna en el DataFrame que se va a evaluar para la normalidad.
    Returns:
        None: Imprime un mensaje indicando si los datos siguen o no una distribución normal.
    """
    # Calcular la normalidad utilizando la prueba de Shapiro-Wilk para la columna especificada
    statistic, p_value = stats.shapiro(dataframe[columna])
    print(f'Prueba Shapiro-Wilk para la columna {columna}:')
    print(f'Estadística = {statistic}, p-valor = {p_value}')
    if p_value < 0.05:
        print("Los datos no siguen una distribución normal (p-valor < 0.05). Considera utilizar pruebas no paramétricas.")
    else:
        print("No hay suficiente evidencia para rechazar la hipótesis nula de normalidad (p-valor >= 0.05).")

# Calcular la normalidad para levels_superior_education
normalidad(filtered_superior, 'Flights Booked')

# Calcular la normalidad para levels_basic_education
normalidad(filtered_basic, 'Flights Booked')

def mann_whitney_test(group1, group2):
    stat, p_value = mannwhitneyu(group1, group2)
    print(f'Prueba de Mann-Whitney U:')
    print(f'Estadística = {stat}, p-valor = {p_value}')
    if p_value < 0.05:
        print("Existe una diferencia significativa entre los grupos.")
    else:
        print("No hay evidencia suficiente para afirmar una diferencia significativa entre los grupos.")
        
mann_whitney_test(filtered_superior['Flights Booked'], filtered_basic['Flights Booked'])       