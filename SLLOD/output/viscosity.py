import numpy as np
import matplotlib.pyplot as plt

srate = [0.01, 0.02, 0.05, 0.08, 0.1, 0.2, 0.5, 0.8, 1, 1.2, 1.5, 1.8, 2, 2.2, 2.5] 
viscosity_mean = np.zeros(len(srate))
viscosity_upper = np.zeros(len(srate))
viscosity_lower = np.zeros(len(srate))
############ Main Body ################################### 
for i in range(len(srate)):
	input_fname = './pressure-' + str(srate[i]) + '.dat'
	data = np.loadtxt(input_fname, skiprows=2)

	time =data[:,0]
	pxy = data[:,4]	

	pxy_mean = np.mean(pxy)
	pxy_std = np.std(pxy, ddof=1)
	pxy_sterr = pxy_std/np.sqrt(len(pxy))

	viscosity_mean[i] = -pxy_mean/srate[i]
	viscosity_upper[i] = -(pxy_mean+pxy_sterr)/srate[i]
	viscosity_lower[i] = -(pxy_mean-pxy_sterr)/srate[i]

viscosity_error = (viscosity_upper-viscosity_lower)/2

#plt.plot(srate, viscosity_mean, marker='o', linestyle='none', color='r')
plt.errorbar(srate, viscosity_mean, yerr=viscosity_error, linestyle='none', color='r', marker='o', capsize=2)
plt.xscale('log')
plt.ylabel('Shear viscosity $(\eta)$')
plt.xlabel('Strain rate $(\dot \gamma$)')
plt.title('Shear viscosity (SLLOD) $vs$ Strain rate')
plt.show()
