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

def creación_lista_datos_temp(): ##Funcion que crea la lista de los datos
    lecturas_sensores_temp= []
    nombre_archivo = "Datos.csv" # define el csv
    with open(nombre_archivo, "r") as archivo:  # se define define para abrir el csv
        lector = csv.reader(archivo, delimiter=";") # Se separa cada elemento con ;
        next(lector, None) # Omitir el encabezado        
        for columna in lector: ## recorrido del csv para crear la lista de datos
            T2 = (columna[5])
            lecturas_sensores_temp.append(float(T2)) ## La lista que contiene todos los elementos
            #print(T2) 
    return (lecturas_sensores_temp)      

##___________________LA LISTA (sin ordenar) __________________________________
lecturas_sensores_temp_lista= creación_lista_datos_temp ()
print("primero: ", lecturas_sensores_temp_lista[0])
print("ultimo: ", lecturas_sensores_temp_lista[-1])

    
##___________________ORDENAR LA LISTA ______________________________________
lecturas_sensores_temp_ordenada = sorted(lecturas_sensores_temp_lista) ## La lista que contiene todos los elementos ordenada
print("primero: ", lecturas_sensores_temp_ordenada[0])
print("ultimo: ", lecturas_sensores_temp_ordenada[-1])




## Resultados 
print("La cantidad de elementos en la muestra: ", len(lecturas_sensores_temp_lista))## Aprox 19735 mediciones
print(lecturas_sensores_temp_ordenada[:10]) ##primeros 10 elementos de la lista ordenada
     
#print(type(T2[15])) # sabemos que ha este punto es str
