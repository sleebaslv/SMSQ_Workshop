import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('./rdf.dat', skiprows=4)
data2 = np.loadtxt('./allen.csv')

plt.plot(data1[:,1], data1[:,2], color='r', label='Atomic system')
plt.plot(data2[:,0], data2[:,1], linestyle='None', color='k', marker='o', markersize=4, label='Allen and Tildesley')
plt.axhline(y=1, linestyle='--', color='r')
plt.legend()
plt.xlabel('$r/\\sigma$')
plt.ylabel('$g(r)$')
plt.title('Radial Distribution Function')
plt.show()
