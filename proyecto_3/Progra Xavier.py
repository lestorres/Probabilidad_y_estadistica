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
mean1, std1 = stats.norm.fit(datos.iloc[0:89, 1]) ##media y varianza con MLE
meanl1 = datos.iloc[0:89, 1].mean() ##Valor real de media
stdr1  = datos.iloc[0:89,1].std()
print("Inicial", )
print("Real mean", meanl1) ##BIEN
print("Real std", datos.iloc[0:89,1].std())
#print("Estimated Mean MLE:", mean1)
print("Estimated Standard Deviation MLE:", std1)
print("porcentaje de error desviacion estandar:", ((stdr1-std1)/stdr1)*100)

mean2, std2 = stats.norm.fit(datos.iloc[0:89, 2])##media y varianza con MLE
meanl2 = datos.iloc[0:89, 2].mean() ##Valor real de media
stdr2 = datos.iloc[0:89,2].std()
print("Primer cambio")
print("Real mean", meanl2) ##BIEN
print("Real std", stdr2 )
#print("Estimated Mean MLE:", mean2)
print("Estimated Standard Deviation MLE:", std2)
print("porcentaje de error desviacion estandar:", ((stdr2-std2)/stdr2)*100)

mean, std3 = stats.norm.fit(datos.iloc[0:89, 3])##media y varianza con MLE
meanl3 = datos.iloc[0:89, 3].mean() ##Valor real de media
stdr3 = datos.iloc[0:89,3].std()
print("Segundo cambio")
print("Real mean", meanl3) ##BIEN
print("Real std", stdr3)
#print("Estimated Mean MLE:", mean)
print("Estimated Standard Deviation MLE:", std3)
print("porcentaje de error desviacion estandar:", ((stdr3-std3)/stdr3)*100)

#####################################################################################################################
# Prueba de Hipótesis
#H0: u=70%
#H1: u>70%
#####################################################################################################################
datos.iloc[0:89, 3].hist()