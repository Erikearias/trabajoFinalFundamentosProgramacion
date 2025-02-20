# resumen de cada columna
#column_translation
# "crim": "tasa_criminalidad"
# "zn": "proporcion_terrenos_residenciales"
# "indus": "proporcion_acres_comerciales"
# "chas": "rio_charles"
# "nox": "concentracion_oxidos_nitrogeno"
# "rm": "numero_habitaciones",
# "age": "proporcion_casas_antiguas",
# "dis": "distancia_centros_empleo",
# "rad": "accesibilidad_carreteras",
# "tax": "tasa_impuesto_propiedad",
# "ptratio": "ratio_alumnos_profesor",
# "b": "proporcion_poblacion_afroamericana",
# "lstat": "porcentaje_bajos_ingresos",
# "medv": "valor_medio_vivienda"

# se hace la importacion de pandas
import pandas as pd

#se carga el dataset
df = pd.read_csv("BostonHousing.csv")

#se identifican columnas y datos del dataset, solicitando los 5 primeros registros
df.head()
print(df.head())

#se identifica la informaicon que contiene cada columna y sus faltantes
df.info()

#identificamos que la columna "rm - Numero de habitaciones" le faltan 5 registros, sacamos promedio
#para rellenar los datos faltantes
promedio_rm = df["rm"].mean()
df["rm"].fillna(promedio_rm, inplace=True)
df.info()


#se identifica que todos los registros estan completos

promedio_rm = df["rm"].mean()
print(promedio_rm)




