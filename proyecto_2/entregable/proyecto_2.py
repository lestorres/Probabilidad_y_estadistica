# Integrantes: Lesmes Torres , Xavier Barrios, Jose Calderon

import matplotlib.pyplot as plt
import numpy as np


#_________________________________________CASO 1 (MONEDA NORMAL)_______________________________________

###########################################################################################################################

#Asignación clásica de la probabilidad de que salga corona en una tirada

s = 1           # Exito para que salga CORONA en una tirada
n = 2           # Numero de exitos posibles para que salga cara o escudo
p_1 = s/n       # Probabilidad de que salga CORONA en una tirada (Asignación clásica)

p_2 = 0.7       # Probabilidad de que salga CORONA en una tirada (MONEDA TRUCADA)

N = 10          # Cantidad total de tiradas de la distribución

#_________________________________________________Graficando distribución Geométrica (bastones)_____________________
def fmp_geometrica(n , p_a): 
   
   k = np.arange(1, n+1)          # Se define la probabilidad de éxito y se crea un array con los valores del 1 al N

   fmp= (1-p_a)**(k-1) * p_a      # Fórmula para calcular la probabilidad de obtener el primer éxito en el k-ésimo ensayo

   return k, fmp


def graficar_geometrica_sintruco():                                # graficar la distribución geométrica

    k_g, fmp_geo = fmp_geometrica(N, p_1)

    plt.stem(k_g, fmp_geo)                                         # Dibuja los bastones verticales en cada valor de k con una altura igual a la probabilidad (p)
    #plt.title('Distribución Geométrica sin truco')                # Agrega título al gráfico (NO ES NECESARIA EN INFORME)
    plt.xlabel('Número de lanzamientos de moneda (Lanzamientos)')  # Agrega etiqueta al eje x
    plt.ylabel('Probabilidad')                                     # Agrega etiqueta al eje y
    plt.show()                                                     # Mostrar el gráfico

#_________________________________________________Graficando distribución Binomial________________________________

def factorial(n):                                                       #calcular factorial
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
 
def combinatoria(comb_1, comb_2):                                       #calcular combinatoria
    return factorial(comb_1) / ( factorial(comb_2) * factorial(comb_1-comb_2) )


def fmp_binomial( n , p ):

    k_b = np.arange(0, n+1)                                             # Se define la probabilidad de éxito y se crea un array con los valores del 0 al N

    fmp_bino = [combinatoria(n, i) * p**i * (1-p)**(n-i) for i in k_b]  # Función de masa de probabilidad para la distribución binomial de 0 hasta N

    return k_b , fmp_bino

def graficar_binomial_sintruco():

    k_b, fmp_b = fmp_binomial(N, p_1)

    plt.stem(k_b , fmp_b )                                           # Dibuja los bastones verticales en cada valor de k con una altura igual a la probabilidad (p)
    #plt.title('Distribución Binomial sin truco')                    # Agrega título al gráfico (NO ES NECESARIA EN INFORME)
    plt.xlabel('Número de lanzamientos de moneda (Lanzamientos)')    # Agrega etiqueta al eje x
    plt.ylabel('Probabilidad')                                       # Agrega etiqueta al eje y
    plt.show()                                                       # Mostrarel gráfico



# Graficar las distribuciones graficos de bastones

graficar_geometrica_sintruco()
graficar_binomial_sintruco()


###############################################################################################################################
#_______________________________________________________Moneda trucada_________________________________________________________

#_______________________________________________________Geométrica_____________________________________________________________
def graficar_geometrica_truco():                                # graficar la distribución geométrica

    k_g, fmp_geo = fmp_geometrica(N, p_2)

    plt.stem(k_g, fmp_geo)                                         # Dibuja los bastones verticales en cada valor de k con una altura igual a la probabilidad (p)
    #plt.title('Distribución Geométrica con truco')                # Agrega título al gráfico (NO ES NECESARIA EN INFORME)
    plt.xlabel('Número de lanzamientos de moneda (Lanzamientos)')  # Agrega etiqueta al eje x
    plt.ylabel('Probabilidad')                                     # Agrega etiqueta al eje y
    plt.show()                                                     # Mostrar el gráfico

#_________________________________________________________Binomial________________________________________________________________

def graficar_binomial_truco():

    k_b, fmp_b = fmp_binomial(N, p_2)

    plt.stem(k_b , fmp_b )                                           # Dibuja los bastones verticales en cada valor de k con una altura igual a la probabilidad (p)
    #plt.title('Distribución Binomial con truco')                    # Agrega título al gráfico (NO ES NECESARIA EN INFORME)
    plt.xlabel('Número de lanzamientos de moneda (Lanzamientos)')    # Agrega etiqueta al eje x
    plt.ylabel('Probabilidad')                                       # Agrega etiqueta al eje y
    plt.show() 

graficar_geometrica_truco()
graficar_binomial_truco()
