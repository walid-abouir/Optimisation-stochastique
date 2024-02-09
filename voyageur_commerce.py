# -*- coding: utf-8 -*-
"""
@author: aboui
"""
import numpy as np
import matplotlib.pyplot as plt
import random
from time import *


Nv=10
#Ici on travaille en coordonnées cartésiennes
M=np.random.uniform(0,1,(Nv,2))
plt.plot(M[:,0],M[:,1],"+")
plt.title('villes')
plt.show()

def plot_traj(S,M):

    M=M[S]
    MM=np.zeros((Nv+1,2))
    MM[0:Nv]=M
    MM[Nv]=M[0]
    plt.plot(M[:,0],M[:,1],'+')
    plt.plot(MM[:,0],MM[:,1],'r-')
    
traj_ini=np.arange(Nv)
plt.figure()
plot_traj(traj_ini,M)
plt.show()

#distance entre les villes. V étant la matrice des villes, et D la matrice des distances entre les villes.

def distance_matrix(M):
    D=np.zeros((Nv,Nv))
    for i in range(Nv):
        for j in range(Nv):
            D[i,j]=np.linalg.norm(M[i]-M[j])
    return D

D=distance_matrix(M)

def Length(S, D):
    
    L=D[S[0],S[-1]]
    for i in range(Nv-1):
        L+= D[S[i],S[i+1]]
    return L

#introduction de la notion de voisinage 
# 2 voyages sont voisins s'ils n'y qu'une seule permutation de 2 villes qui les diffère.
#Cette notion de voisinage nous permet d'obtenir la matrice de sélection

def permute(S):
    T=np.copy(S)
    t=random.sample(range(Nv),2)
    T[t[0]]=S[t[1]]
    T[t[1]]=S[t[0]]
    return T

S=np.arange(Nv)
T=permute(S)
print('S',S)
print('T',T)


#Nous ne devons pas oublier que le but du problème est que la distance totale du voyage soit la plus petite.



def delta(S0,S1,T):
    return (1/(1+np.exp(-(Length(S0,D)-Length(S1,D))/T)))


eps=0.07
nb_iter=2
S0=np.arange(Nv)#permutation de départ
h=1
T=h/np.log(nb_iter)
L=np.array([Length(S0,D)])

fig=plt.figure()
ax=fig.add_subplot(111)
plt.ion()
fig.show()

plot_traj(S0, M)
plt.title("tournée initiale")
fig.canvas.draw()
nb_itermax=10000

while T>eps and nb_iter<nb_itermax:
    S=permute(S0)
    u=np.random.uniform()
    if u< delta(S0,S,T):
        S0=S
    L=np.append(L, Length(S0,D))
    nb_iter+=1
    T=h/np.log(nb_iter)
    # if np.mod(nb_iter,1000)==0:
    #     ax.clear()
    #     ax.set(title=str(nb_iter)+'-ième trajectoire')
    #     plot_traj(S0,M)
    #     fig.canvas.draw()
    
plt.figure()
plot_traj(S0,M)
plt.show()

plt.figure()
plt.title('Longueur de la tournée au fil des itérations')
plt.plot(L)
plt.show()