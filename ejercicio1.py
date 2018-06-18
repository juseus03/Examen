# Ejercicio 1 (10 puntos)
# Calcule integral de exp(x) entre 0 y 1 con el método de trapecio y de Simpson.
# Haga una grafica (error.png) del error fraccional entre la solución numérica y 
# analítica como funcion del numero de puntos (desde N=10 hasta N=10^8). 
# Tanto el error como el numero de puntos deben variar en escala logaritmica.

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

#Funcion a integrar
def func(x):
    return np.exp(x)
#Solucion analitica
def analit(x):
    return func(1)-func(0)

#Metodo del Trapecio
def trapecio(a,b,np):
    ptos = np.linspace(a,b,np)
    area = 0
    for i in range(1,len(ptos)):
        area+=(ptos[i]-ptos[i-1])*(func(i-1)+func(i))/2.0
    return area

def simpson(a,b,np):
    ptos = np.linspace(a,b,np)
    area = 0
    for i in range(1,len(ptos)):
        p1=ptos[i-1]
        p2=ptos[i]
        k = (p1-p2)/6.0
        l = func(p1)+func(p2)+4*func((p1+p2)/2)
        area+=k*l
    return area  

#Parametros generales
a = 0
b = 1
Nmin=10
Nmax=10**8
np = np.linspace(Nmin,Nmax,100)
error_t = np.zeros(len(np))
error_s = np.zeros(len(np))

#Calcula el error
for i in range(0,len(np)):
    i_trap = trapecio(a,b,i)
    i_simp = simpson(a,b,i)
    error_t[i]= i_trap/analit(x)
    error_s[i]= i_simp/analit(x)

plt.loglog(error_t,np,'r--')
plt.loglog(error_s,np,'b-*')

plt.savefig("error.png")









