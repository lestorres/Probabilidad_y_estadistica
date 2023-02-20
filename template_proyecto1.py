# -*- coding: utf-8 -*-
"""
Curso Proabilidad y Estadística

Tarea #1

Template con lectura de datos en archivo csv

"""

# import numpy as np

#input_dir='C:/Users/PATH/' #PATH al archivo de datos, cambiar según cada computadora. Sirve para evitar 'File not found'
#filename=input_dir+'NOMBRE_de_ARCHIVO.csv'

# Esta línea lee la matriz de datos (sin titulos) para números solamente. Otro tipo de variable (texto por ejemplo) se leerá como nan
#datos=np.genfromtxt(filename,delimiter=',',skip_header=1)

#alternativamente, se pueden leer columnas específicas entre el rango [X,Y] de esta forma:
#datos=np.genfromtxt(filename,delimiter=',',skip_header=1, usecols = range(X,Y))

# Su código va aquí...

"""import pandas as pd
df = pd.read_csv('C:/Users/PATH/')
print(df.head(3))"""


import csv
"""
    https://parzibyte.me/blog
"""

nombre_archivo = "Datos.csv"
with open(nombre_archivo, "r") as archivo:
    lector = csv.reader(archivo, delimiter=";")
    # Omitir el encabezado
    next(lector, None)
    for fila in lector:
        
        date = fila[0]
        Appliances = fila[1]
        lights = fila[2]
        T1 = fila[3]
        RH1 = fila[4]
        T2 = (fila[5])
        RH2 = fila[6]
        #print(T2)

def mean(T2):
    return sum(T2) / len(T2)

print(mean(T2))




""" = fila[0]
        calificacion = int(fila[1])
        precio = float(fila[2])
        print({nombre},{calificacion},{precio})"""
