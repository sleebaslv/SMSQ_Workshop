import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit

def Line_Fit(x,m):
	return m*x
########## Input data ##########
choice = raw_input('msd or rdf:')

if choice == 'msd':
	data1 = np.loadtxt('./msd.dat', skiprows=2)
	
	time = data1[:,0]
	msd = data1[:,4]
	popt, pcov = curve_fit(Line_Fit, time, msd)
	slope = popt[0]
	diff_coeff = slope/6
	msd_fit = Line_Fit(time, slope)
	plt.plot(time, msd, linestyle = '-', color='r', label='MSD')
	plt.plot(time, msd_fit, linestyle = '--', color='k', label='MSD Fit')
	text_str = 'D = ' + str(np.around(float(diff_coeff*pow(10,4)),4)) + '$\\times 10^{-9}$' + '$m^{2} s^{-1}$'
	plt.text(1.0, 60.0, text_str)
	plt.legend()
	plt.xlabel('Time (fs)')
	plt.ylabel('MSD ($\\AA^{2}$)')
	plt.title('Mean Square Displacement')
	plt.show()

elif choice == 'rdf':
	data1 = np.loadtxt('./rdf.dat', skiprows=4)
	r = data1[:,1]
	rdf_choice = raw_input('ghh or goh or goo:')
	if rdf_choice == 'ghh':
		gor = data1[:,2]
		plt.plot(r, gor, color='r', label='$g_{H-H}$')	

	elif rdf_choice == 'goh':
		gor = data1[:,4]
		plt.plot(r, gor, color='r', label='$g_{O-H}$')
		r_choice = float(input('Enter value for r:'))
		gor_choice = float(input('Enter value for g(r):'))
		plt.plot(r_choice, gor_choice, linestyle='None', color='k', marker='o', label='Mark and Nilsson')
#		plt.axvline(x=r_choice, linestyle='--', color='k')
#		plt.axhline(y=gor_choice, linestyle='--', color='k')	

	elif rdf_choice == 'goo':
		gor = data1[:,6]
		plt.plot(r, gor, color='r', label='$g_{O-O}$')	
	
	else:
		print('Please enter correct option')

	plt.axhline(y=1, linestyle='--', color='r')
	plt.legend()
	plt.xlabel('$r/\\sigma$')
	plt.ylabel('$g(r)$')
	plt.title('Radial Distribution Function')
	plt.show()



else:
	print('Please enter correct option')


