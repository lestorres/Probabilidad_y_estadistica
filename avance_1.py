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
import math
import csv
from statistics import mode

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
#print("primero: ", lecturas_sensores_temp_lista[0])
#print("ultimo: ", lecturas_sensores_temp_lista[-1])

    
##___________________ORDENAR LA LISTA ______________________________________
lecturas_sensores_temp_ordenada = sorted(lecturas_sensores_temp_lista) ## La lista que contiene todos los elementos ordenada
#print("primero: ", lecturas_sensores_temp_ordenada[0])
#print("ultimo: ", lecturas_sensores_temp_ordenada[-1])





     



##_________________Promedio_______________________________________________________

def promedio(lecturas_sensores_temp_ordenada): # se crea una funcion para determinar el promedio
    return sum(lecturas_sensores_temp_ordenada) / len(lecturas_sensores_temp_ordenada) # se utiliza la funcion sum para sumar cada valor en la lista

    



##____________Mediana___________________________________________________________________
from statistics import median # se importa la libreria statistics para poder averiguar la mediana

def mediana(lecturas_sensores_temp_ordenada): # funcion para determinar la mediana
    return (median(lecturas_sensores_temp_ordenada))
    




##_____________Varianza__________________________________________________________________

def varianza(lecturas_sensores_temp_ordenada): # funcion para calcular la varianza
    promedio(lecturas_sensores_temp_ordenada) #para la varianza debemos utilizar el promedio por eso llamamos la funcion promedio
    diff = [(v-promedio(lecturas_sensores_temp_ordenada)) for v in lecturas_sensores_temp_ordenada] # a cada valor de la lista se le resta el promedio
    sqr_diff = [d**2 for d in diff] # a cada resultado de la resta anterior se eleva al cuadrado
    sum_sqr_diff = sum(sqr_diff) # se suma cada valor luego de que hayan sido elevados al cuadrado
    varianza = sum_sqr_diff/ (len(lecturas_sensores_temp_ordenada)-1) # los valores sumados son divididos por la cantidad de valores en la lista menos 1 debido a que es una muestra
    return varianza




'''

"""Ejemplo"""
edades = [5,6,6,7,8]
promedio(edades)
print ("Ejemplo Promedio de edades:", promedio(edades))
varianza(edades)
print ("Ejemplo Varianza de edades: ", varianza(edades))
'''

##___________Desviacion Estandar_________________

def des (lecturas_sensores_temp_ordenada):
    desviacion = varianza(lecturas_sensores_temp_ordenada)**(1/2)
    return desviacion




##___________________Cuartiles___________________
def Cuartil (lecturas_sensores_temp_ordenada):
    cuartiles=[]
    cuartil1=lecturas_sensores_temp_ordenada [math.ceil(len(lecturas_sensores_temp_ordenada)/4)]
    cuartiles.append(cuartil1)
    cuartiles.append(mediana(lecturas_sensores_temp_ordenada)) # mediana
    cuartil3=lecturas_sensores_temp_ordenada [math.ceil(3*len(lecturas_sensores_temp_ordenada)/4)]
    cuartiles.append(cuartil3)
    return (cuartiles)

## _______________ coeficiente de variación_________________
def coeficiente_de_variacion():
    c_v=  des (lecturas_sensores_temp_ordenada) / promedio(lecturas_sensores_temp_ordenada)
    c_v_cien= c_v * 100
    return(c_v_cien)

##_________________Rango Muestral_________
def rango_muestral():
    r= lecturas_sensores_temp_ordenada[-1]-lecturas_sensores_temp_ordenada[0]
    return(r)

def rango_intercuartilico():
    r=Cuartil(lecturas_sensores_temp_ordenada)

    a=r[-1]-r[0]

    return(a)

    


## Resultados 

print("\nMedidas de tendencia central: \n")
print("La cantidad de elementos en la muestra: ", len(lecturas_sensores_temp_lista))## Aprox 19735 mediciones
print("El promedio de la muestra es: ", (promedio(lecturas_sensores_temp_ordenada)))
print("La moda de la muestra: ", mode(lecturas_sensores_temp_ordenada))
print("La mediana de la muestra es: ",(mediana(lecturas_sensores_temp_ordenada)))
print("Los cuartiles 1, 2 y 3 son: ",Cuartil(lecturas_sensores_temp_ordenada))

print("\nMedidas de dispersión o variabilidad: \n")
print ("La varianza de la muestra es: ", varianza(lecturas_sensores_temp_ordenada))
print ("La desviacion estandar de la muestra es: ", des(lecturas_sensores_temp_ordenada))
print("El coeficiente de variación de la muestra es: ", coeficiente_de_variacion(), "%" )
print("El rango muestral es: ", rango_muestral())
print("El rango intercuatílico de la muestra es: ", rango_intercuartilico())
