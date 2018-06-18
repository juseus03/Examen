# Ejercicio 3 (20 puntos)

# A través de fotos aéreas se tienen medidas del alcance de un lanzador de proyectiles. 
# Se tienen cuatro valores (en metros): 61, 115, 31, 117. Todas las mediciones tienen una incertidumbre de 5 metros. 
# El lanzador siempre da la misma velocidad inicial (entre 15 m/s y 60 m/s). 
# Los valores diferentes del alcance se deben a diferentes ángulos de lanzamiento. 
# Utilice métodos montecarlo y el teorema de Bayes para encontrar la velocidad más probable del lanzador de proyectiles 
# a medida que se va incluyendo información nueva sobre los valores del alcance.
# Haga una grafica (bayes.png) que tenga la probabilidad de la velocidad inicial dados los datos observacionales.

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random
import numpy as np

alcance = [61,115,31,117]
incert = 5
Vmax=60
Vmin = 15
N=1000
resp = np.zeros(0)

for i in range(0,N):
    vel = random.uniform(Vmin, Vmax)
    theta = random.uniform(0, np.Pi()/2.0)
    dist = 0.2*vel**2*np.cos(theta)*np.sin(theta)
    for j in alcance:
        if (dist > j-5 and dist < j+5):
            resp = np.append(resp,vel)

plt.plot(resp)

plt.savefig("bayes.png")
        
