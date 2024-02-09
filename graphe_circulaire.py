# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:31:59 2023

@author: aboui
"""

#cas du graphe circulaire

import numpy  as np
import matplotlib.pyplot as plt

Mkv=[];


# Génération de X_0:
# x=np.random.uniform(0,1)
# if x <= 0.5 :
#     Mkv.append(0)
# elif x<= 5/6 :
#     Mkv.append(1)
# else: Mkv.append(2)

p_inv=[1/8,2/8,2/8,2/8,1/8]
#p_inv=[1/5,1/5,1/5,1/5,1/5]

#matrice Q: c'est la matrice de sélection
Q = np.array([[2/3, 1/3, 0, 0, 0],
              [1/3, 0, 1/3,1/3,0],
              [0, 1/3,1/3, 1/3,0],
              [0, 1/3, 1/3, 0,1/3],
              [0,0 , 0, 1/3, 2/3]])

# Q = np.array([[1/2, 1/2, 0, 0, 0],
#               [1/2, 0, 1/2,0,0],
#               [0, 1/2,0, 1/2,0],
#               [0, 0, 1/2, 0,1/2],
#               [0,0 , 0, 1/2, 1/2]])

# Q = np.array([[0, 1/2, 0, 0, 1/2],
#               [1/2, 0, 1/2,0,0],
#               [0, 1/2,0, 1/2,0],
#               [0, 0, 1/2, 0,1/2],
#               [1/2,0 , 0, 1/2, 0]])

def delta(x,y):
    #Chi=np.zeros((5,5))
    #W=np.where(Q[int(x)][int(y)]>0)[0]
    if Q[x,y]==0:
        delta=0
    else:
        delta=min(1,p_inv[int(y)]/p_inv[int(x)])
    return delta

def P():
    P=np.zeros((5,5))
    for i in range (5):
        for j in range(5):
            if i != j :
                
                P[i,j]=delta(i,j)*Q[i,j]
    for i in range(5):
        P[i,i]= 1-sum(P[i,:])
    return P
        


# for i in range(10):
#     # On sélectionne la ligne de P correspondant à l'état dans lequel est la chaine
#     State = Mkv[-1]
#     x=np.random.uniform(0,1)
    
#     proba= P[State]#IL Y A UN PRBLEME ICI
    
#     # On tire un nouvel état pour la chaine.
#     if x <= proba[0].all() :
#         Mkv.append(0)
#     elif x<= proba[0].all()+proba[1].all() :
#         Mkv.append(1)
#     elif x<=proba[0].all()+proba[1].all()+proba[2].all() :
#         Mkv.append(2)
#     elif x<=proba[0].all()+proba[1].all()+proba[2].all()+proba[3].all() :
#         Mkv.append(3)
#     else: Mkv.append(4)
 
x=np.random.randint(0,5,1)       

for i in range(500):
    u = np.random.uniform(0,1)
    y=np.random.randint(0,5,1)
    if u< delta(x,y):
        x=y
        Mkv.append(y)
    else:
        Mkv.append(x)
P=P()
print(Mkv)
print(P)
plt.plot(Mkv,'+')
plt.title("Trajectoire de la chaîne en fonction du temps")
plt.show()
#plt.hist(Mkv, range = (-0.5, 4.5), bins = 5,edgecolor = 'red')