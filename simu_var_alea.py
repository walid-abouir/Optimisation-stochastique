# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:17:38 2023

@author: aboui
"""

#cas du graphe avec la loi de Rademacher (non circulaire)

import numpy  as np
import matplotlib.pyplot as plt

Mkv=[];


# Génération de X_0:
x=np.random.uniform(0,1)
if x <= 0.5 :
    Mkv.append(0)
elif x<= 5/6 :
    Mkv.append(1)
else: Mkv.append(2)

#matrice Q: en utilisant la loi de Rademacher
P = np.array([[0.5, 0.5, 0, 0, 0],
              [0.5, 0, 0.5, 0,0],
              [0, 0.5,0, 0.5,0],
              [0, 0, 0.5, 0,0.5],
              [0,0,0, 0.5, 0.5]])

for i in range(50):
    # On sélectionne la ligne de P correspondant à l'état dans lequel est la chaine
    State = Mkv[-1]
    x=np.random.uniform(0,1)
    proba= P[State]
    # On tire un nouvel état pour la chaine.
    if x <= proba[0] :
        Mkv.append(0)
    elif x<= proba[0]+proba[1] :
        Mkv.append(1)
    elif x<=proba[0]+proba[1]+proba[2] :
        Mkv.append(2)
    elif x<=proba[0]+proba[1]+proba[2]+proba[3] :
        Mkv.append(3)
    else: Mkv.append(4)
        

print(Mkv)

plt.plot(Mkv)
plt.title("Trajectoire de la chaîne en fonction du temps")
plt.show()
plt.hist(Mkv, range = (-0.5, 4.5), bins = 5,edgecolor = 'red')