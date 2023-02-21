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

#import numpy
import csv

nombre_archivo = "Datos.csv" # definis el csv
with open(nombre_archivo, "r") as archivo:  # se define define para abrir
    lector = csv.reader(archivo, delimiter=";") # Se separa cada elemento con ;
    # Omitir el encabezado
    next(lector, None) 

    for fila in lector: ## recorrido de 
        
        date = fila[0]
        Appliances = fila[1]
        lights = fila[2]
        T1 = fila[3]
        RH1 = fila[4]
        T2 = (fila[5]) ## La varible del equipo 
        RH2 = fila[6]
        #print(T2)

print(type(T2[15])) # sabemos que ha este punto es str
A=float(T2[16])

print(A)
print(A*2)