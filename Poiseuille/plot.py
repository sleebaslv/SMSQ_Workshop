import numpy as np
import matplotlib.pyplot as plt

choice = input('(1) Velocity profile or (2) Density profile:')
if choice == 1:
	data1 = np.loadtxt('./vel_before.dat', skiprows=4)
	data2 = np.loadtxt('./vel_after.dat', skiprows=4)
	plt.plot(data1[:,1], data1[:,3], color='r', label='No field')
	plt.plot(data2[:,1], data2[:,3], color='b', label='field')
	plt.ylabel('Velocity')
	plt.xlabel('z-direction')
	plt.title('Velocity profile')
	plt.legend()
	plt.show()

elif choice == 2:
	data1 = np.loadtxt('./den.dat', skiprows=4)
	plt.plot(data1[:,1], data1[:,3], color='r')
	plt.ylabel('Density')
	plt.xlabel('z-direction')
	plt.title('Density profile')
	plt.show()

else:
	print('Please choose correct option.')

