import matplotlib.pyplot as plt
import numpy as np

# Definimos la probabilidad de éxito y creamos un array con los valores del 1 al 10
p = 0.5 # Probabilidad de éxito
k = np.arange(1, 11) # Valores de k del 1 al 10

# Calculamos la probabilidad de obtener el primer éxito en el k-ésimo ensayo
prob_geom = (1-p)**(k-1) * p

# Graficamos la distribución geométrica
plt.stem(k, prob_geom, use_line_collection=True) # Dibujamos líneas verticales en cada valor de k con una altura igual a la probabilidad calculada anteriormente
plt.title('Distribución geométrica') # Agregamos título al gráfico
plt.xlabel('Número de veces que se tira la moneda') # Agregamos etiqueta al eje x
plt.ylabel('Probabilidad') # Agregamos etiqueta al eje y
plt.show() # Mostramos el gráfico

###############################################################################################################################

# Graficando Geométrica


def Geometrica(x,p):
  funcion = ((1-p)**(x-1))*p
  #print (funcion)
  return funcion
x = 10 
p = 0.5
Xs = [k for k in range (1,x+1)]
Ys = [Geometrica(x,p) for x in range(1,x+1)]
#plt.plot(Xs, Ys, label =f'n = {x}')

plt.title('Distribución Geométrica')
plt.ylabel('probabilidad')
plt.xlabel('Número de veces que se tira la moneda')
plt.plot(Xs,Ys, "o")
plt.show()