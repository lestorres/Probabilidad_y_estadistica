import matplotlib.pyplot as plt
import numpy as np

p_1  = 0.5
N=10


def fmp_geometrica(n , p_a): # Fórmula para calcular la probabilidad de obtener el primer éxito en el k-ésimo ensayo
   
   k = np.arange(1, n+1)

   fmp= (1-p_a)**(k-1) * p_a

   return k, fmp

# graficar la distribución geométrica
def graficar_geometrica():

    k_g, fmp_geo = fmp_geometrica(N, p_1)

    plt.stem(k_g, fmp_geo) # Dibujamos líneas verticales en cada valor de k con una altura igual a la probabilidad (p)
    plt.title('Distribución Geométrica') # Agregamos título al gráfico (NO ES NECESARIA EN INFORME)
    plt.xlabel('Numero de lanzamientos de moneda (Lanzamientos)') # Agregamos etiqueta al eje x
    plt.ylabel('Probabilidad') # Agregamos etiqueta al eje y
    plt.show() # Mostramos el gráfico


graficar_geometrica()

'''

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
 
def combinatoria(comb_1, comb_2):
    return factorial(comb_1) / ( factorial(comb_2) * factorial(comb_1-comb_2) )

def fmp_binomial( n , p ):

    k_b = np.arange(0, n+1)

    fmp_bino = [combinatoria(n, i) * p**i * (1-p)**(n-i) for i in k_b]

    return k_b , fmp_bino
       
   
k_b, fmp_b = fmp_binomial(N, p_1)


plt.stem(k_b , fmp_b ) # Dibujamos líneas verticales en cada valor de k con una altura igual a la probabilidad (p)
plt.title('Distribución Binomial') # Agregamos título al gráfico (NO ES NECESARIA EN INFORME)
plt.xlabel('Numero de lanzamientos de moneda (Lanzamientos)') # Agregamos etiqueta al eje x
plt.ylabel('Probabilidad') # Agregamos etiqueta al eje y
plt.show() # Mostramos el gráfico

'''