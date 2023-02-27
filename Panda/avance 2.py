# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 10:23:31 2023

@author: xbs20
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 13:43:39 2023

@author: xbs20
"""
#import math
import pandas as pd
import csv
import matplotlib.pyplot as plt
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
lecturas_sensores_temp_lista= creación_lista_datos_temp ()
data=pd.Series(lecturas_sensores_temp_lista)
#__________________histograma______________________
plt.title("Resultados de monitoreo de la temperatura en la sala")
plt.xlabel("Temperatura grados Celsius")
plt.ylabel("Frecuencia escala logarítmica")
bins=range(16,30) #limites del histograma
plt.hist(data, bins=bins, edgecolor='black', log=True)
plt.savefig('histograma',dpi=800)

#codigo tiene que calcular: promedio, mediana, varianza, desviacion estandar, cuartiles, coeficiente de variación, rango muestral e intercuartilico
mean=round(data.mean(),2)
size=data.size
mode=round(data.mode(),2).values[0]
var=round(data.var(),2)
std=round(data.std(),2)
cov=round((std/mean)*100,2)
minimo=round(data.min(),2)
maximo=round(data.max(),2)
q1=data.quantile(q=.25, interpolation="higher")
mediana=data.quantile(q=.5, interpolation="midpoint")
q3=data.quantile(q=.75,interpolation= "higher")

rangeq=q3-q1 #rango intercuartílico
rango=maximo-minimo
print("Resumen de las medidas de tendencia central y dispersión", "\nMínimo = " , minimo,"\nMáximo = ", maximo,"\nModa = ", mode,
      "\nPromedio = ", mean, "\nCuartil 1 = ", q1, "\nMediana = ", mediana, "\nCuartil 3 = ", q3, "\nVarianza = ",
      var, "\nDesviación estandar = ", std, "\nCoeficiente de variación = ", cov, "\nCantidad de datos = ", size)
