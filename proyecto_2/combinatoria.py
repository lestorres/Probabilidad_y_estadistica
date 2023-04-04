import matplotlib.pyplot as plt
import numpy as np

def factorial_p(n):
    dev = 1
    while True:
        if n < 2:
            return dev
        dev *= n
        n -= 1
def factorial_b(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
 
def combinaciones_p(m, n):
    return factorial(m)/(factorial(n)*factorial(m-n))

#print(combinaciones(10 , 6))

# Graficando Binomial
N, p = 30, 0.4 # parametros de forma 
binomial = stats.binom(N, p) # Distribución
x = np.arange(binomial.ppf(0.01),
              binomial.ppf(0.99))
fmp = binomial.pmf(x) # Función de Masa de Probabilidad
plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Binomial')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()