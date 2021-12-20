import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('./rdf.dat', skiprows=4)

plt.plot(data1[:,1], data1[:,2], color='r', label='rdf')
plt.legend()
plt.show()
