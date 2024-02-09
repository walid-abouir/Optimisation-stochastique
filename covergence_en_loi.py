
import numpy as np
import matplotlib.pyplot as plt

Nmax = 1000000 
X0 = 1
theta=0.5
U = np.random.normal(0, 1, Nmax)
X = np.zeros(Nmax)
X[0] = X0 
for i in range(Nmax-1):
    X[i+1] = theta * X[i] + U[i]

plt.hist(X, bins = 50, density = True, label = 'Distribution empirique')
tt = np.linspace(min(X), max(X))
plt.plot(tt, np.exp(-tt**2*(1-theta**2)/2) * np.sqrt(1-theta**2)/np.sqrt(2*np.pi), label = 'Distribution théorique')
plt.legend()
plt.title('Convergence du processus vers la mesure invariante')
plt.show()
