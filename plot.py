from matplotlib.pyplot import *
import numpy as np

dataset=np.loadtxt(open("002.txt","rb"),delimiter=",",dtype='float',skiprows=0)

wavelength = dataset[:,0]
distribution = dataset[:,2]

plot(wavelength,distribution)

xlabel('Wavelength (nm)')
ylabel('Sampling Points (a.u.)')

grid()
show()