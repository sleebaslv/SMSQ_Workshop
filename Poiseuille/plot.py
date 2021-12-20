import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('./vel1.dat', skiprows=4)
data2 = np.loadtxt('./vel2.dat', skiprows=4)

plt.plot(data1[:,1], data1[:,3], color='r', label='No field')
plt.plot(data2[:,1], data2[:,3], color='b', label='field')
plt.legend()
plt.show()
