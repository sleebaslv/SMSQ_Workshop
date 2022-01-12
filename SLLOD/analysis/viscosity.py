#Python script for calculating correlation using scipy
# Arguments nrun: array slicing no., endtime: prod run end time, starttime: prod run start time, skip: timesteps skipped
import numpy as np
import matplotlib.pyplot as plt

strain_rate = 2.5 

############ Main Body ################################### 
#fname1 = './correlation/r' + str(int(i+1)) + '-corr.data'
input_fname = './pressure-2.dat'

data = np.loadtxt(input_fname, skiprows=2)

time =data[:,0]
pxy = data[:,4]	

pxy_mean = np.mean(pxy)
pxy_std = np.std(pxy, ddof=1)
pxy_sterr = pxy_std/np.sqrt(len(pxy))

viscosity_mean = -pxy_mean/strain_rate
viscosity_upper = -(pxy_mean+pxy_sterr)/strain_rate
viscosity_lower = -(pxy_mean-pxy_sterr)/strain_rate

print(viscosity_mean, viscosity_upper, viscosity_lower)
plt.plot(time, pxy, linestyle='--', color='r')
plt.axhline(y=pxy_mean, linestyle='--', color='k')
plt.show()
