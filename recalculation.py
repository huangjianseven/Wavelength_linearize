from matplotlib.pyplot import *
import numpy as np

#import calculate_distribution_pattern as cd

c=np.loadtxt(open("linearization883.txt","rb"),delimiter=",",dtype='float',skiprows=0)

def lrf(angle):
	wavelength = (angle+10.376)/0.00799
	return wavelength

d = np.zeros((len(c[:,0]),3))

d[:,1] = lrf(c[:,3])

d[:,0] = c[:,0]
d[:,2] = c[:,1]

print d



np.savetxt('recalculation883.txt',d,fmt="%d,%.1f,%.2f")
