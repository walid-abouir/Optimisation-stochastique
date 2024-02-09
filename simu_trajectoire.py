# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

Npas = 1000
Ntraj = 100
# Génération du processus discrétisé
U = np.random.normal(0, 1, (Ntraj,Npas))
X = np.cumsum(U, axis = 1)
# Représentation des trajectoires avec une enveloppe d'équation x=y2
#Ici on obtien un processus de Ornstein-Uhlenbeck
for i in range(Ntraj):
    plt.plot(X[i])
plt.plot(range(Npas), 2 * np.sqrt(range(Npas)), 'k', - 2 * np.sqrt(range(Npas)), 'k', label='Intervalle de largeur 4 sigma')
plt.title('Simulation de ' + str(Ntraj) + ' trajctoires de longueur ' +str(Npas))
plt.legend()
plt.show()

Ntarj=1000
Nmax=1000
theta=0.5
X0=0

U = np.random.normal(0,1,(Ntraj, Nmax))
X=np.zeros((Ntraj,Nmax))

X[:,0]= X0 * np.ones(Ntraj).T

for i in range (Nmax -1):
    X[:,i+1]= theta * X[:,i] + U[:,i]
    
for i in range(Ntraj):
    plt.plot(X[i])
    
