# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import scipy.stats as stats

datos=pd.read_csv("Conjunto_datos_proyecto3.csv", delimiter=";")


#####################################################################################################################
#Comprobar que todas las configuraciones presentan un valor de rendimiento medio poblacional igual o mayor al 70%
#####################################################################################################################
mean1, std1 = stats.norm.fit(datos.iloc[0:89, 1])

print("Inicial")
print("Estimated Mean:", mean1)
print("Estimated Standard Deviation:", std1)

mean2, std2 = stats.norm.fit(datos.iloc[0:89, 2])

print("Primer cambio")
print("Estimated Mean:", mean2)
print("Estimated Standard Deviation:", std2)

mean, std = stats.norm.fit(datos.iloc[0:89, 3])

print("Segundo cambio")
print("Estimated Mean:", mean)
print("Estimated Standard Deviation:", std)

#####################################################################################################################
# Prueba de Hipótesis
#H0: u=70%
#H1: u>70%
#####################################################################################################################