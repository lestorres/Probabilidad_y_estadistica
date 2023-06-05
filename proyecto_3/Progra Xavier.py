# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

datos=pd.read_csv("Conjunto_datos_proyecto3.csv", delimiter=";")


#####################################################################################################################
#Comprobar que todas las configuraciones presentan un valor de rendimiento medio poblacional igual o mayor al 70%
#####################################################################################################################
meanl1 = datos.iloc[0:89, 1].mean() ##Valor real de media
mean1, std1 = stats.norm.fit(datos.iloc[0:89, 1], loc=meanl1) ##media y varianza con MLE

stdr1  = datos.iloc[0:89,1].std()
print("Inicial", )
print("Real mean", meanl1) ##BIEN
print("Real std", datos.iloc[0:89,1].std())
#print("Estimated Mean MLE:", mean1)
print("Estimated Standard Deviation MLE:", std1)
print("porcentaje de error desviacion estandar:", ((stdr1-std1)/stdr1)*100)

meanl2 = datos.iloc[0:89, 2].mean() ##Valor real de media
stdr2 = datos.iloc[0:89,2].std()
mean2, std2 = stats.norm.fit(datos.iloc[0:89, 2], loc=meanl2)##media y varianza con MLE

print("Primer cambio")
print("Real mean", meanl2) ##BIEN
print("Real std", stdr2 )
#print("Estimated Mean MLE:", mean2)
print("Estimated Standard Deviation MLE:", std2)
print("porcentaje de error desviacion estandar:", ((stdr2-std2)/stdr2)*100)

meanl3 = datos.iloc[0:89, 3].mean() ##Valor real de media
stdr3 = datos.iloc[0:89,3].std()
mean, std3 = stats.norm.fit(datos.iloc[0:89, 3], loc=meanl3)##media y varianza con MLE

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
# alpha= P(x>70|u=70)
# valor critico se encuentra en 75%
#####################################################################################################################
##Error de tipo beta es alto debido a la muestra de tamaño pequeño.
#datos.iloc[0:89, 2].hist()

print("\nValores criticos para cada caso:\n")

x=1.65*stdr1+70
d=1.65*stdr2+70
e=1.65*stdr3+70

print("caso 1:", x)
print("caso 2:", d)
print("caso 3:", e)


print("\n\n Prubas t para valor p")

st1, pvalue1 = stats.ttest_1samp(datos.iloc[0:89,1], 70, alternative="greater")
print("Valor T = ", st1, "Valor p = ", pvalue1, "\n")

st2, pvalue2 = stats.ttest_1samp(datos.iloc[0:89,2], 70, alternative="greater")
print("Valor T = ", st2, "Valor p = ", pvalue2, "\n")

st3, pvalue3 = stats.ttest_1samp(datos.iloc[0:89,3], 70, alternative="greater")
print("Valor T = ", st3, "Valor p = ", pvalue3)


print("\n\n Comparación de datos")

stc1, pvaluec1 = stats.ttest_ind(datos.iloc[0:89,1], datos.iloc[0:89,2], equal_var = False, alternative = 'two-sided')
print("Valor T = ", stc1, "Valor p = ", pvaluec1, "\n")

stc2, pvaluec2 = stats.ttest_ind(datos.iloc[0:89,1], datos.iloc[0:89,3], equal_var = False, alternative = 'two-sided')
print("Valor T = ", stc2, "Valor p = ", pvaluec2, "\n")

stc3, pvaluec3 = stats.ttest_ind(datos.iloc[0:89,2], datos.iloc[0:89,3], equal_var = False, alternative = 'two-sided')
print("Valor T = ", stc3, "Valor p = ", pvaluec3)


# Generar datos para la distribución normal
x = np.linspace(datos.iloc[0:89, 1].min(), datos.iloc[0:89, 1].max(), 100)
y = stats.norm.pdf(x, loc=meanl1, scale=std1)

# Graficar histograma y distribución normal
plt.hist(datos.iloc[0:89, 1], bins=10, density=True, alpha=0.7, label='Histograma')
plt.plot(x, y, 'r', label='Distribución Normal')
plt.xlabel('Valores de muestra inicial')
plt.ylabel('Frecuencia absoluta')
plt.title('Histograma con Distribución Normal')
plt.legend()

# Mostrar el gráfico
plt.show()

x = np.linspace(datos.iloc[0:89, 2].min(), datos.iloc[0:89, 2].max(), 100)
y = stats.norm.pdf(x, loc=meanl2, scale=std2)

# Graficar histograma y distribución normal
plt.hist(datos.iloc[0:89, 1], bins=10, density=True, alpha=0.7, label='Histograma')
plt.plot(x, y, 'r', label='Distribución Normal')
plt.xlabel('Valores de muestra con primer cambio')
plt.ylabel('Frecuencia absoluta')
plt.title('Histograma con Distribución Normal')
plt.legend()

# Mostrar el gráfico
plt.show()

x = np.linspace(datos.iloc[0:89, 3].min(), datos.iloc[0:89, 3].max(), 100)
y = stats.norm.pdf(x, loc=meanl1, scale=std1)

# Graficar histograma y distribución normal
plt.hist(datos.iloc[0:89, 1], bins=10, density=True, alpha=0.7, label='Histograma')
plt.plot(x, y, 'r', label='Distribución Normal')
plt.xlabel('Valores de muestra con segundo cambio')
plt.ylabel('Frecuencia absoluta')
plt.title('Histograma con Distribución Normal')
plt.legend()

# Mostrar el gráfico
plt.show()




