from matplotlib.pyplot import *
import numpy as np

import initialization as init



def caculate_max_deflection_angle(p1,p2):

	peak1 = p1
	peak2 = p2
	

	# calculate the half-time between t1 and t2
	delta_t = (init.peak_2 - init.peak_1)*init.time_slot/2

	# caltulate the max deflection angle
	phi_max = init.phi_trig/(np.cos(2*np.pi*init.resonance_frequence*delta_t))

	# set the precision of float
	phi_max = float("%.3f" % phi_max)

	return phi_max



# set MAX Deflection Angle
max_deflection_angle = caculate_max_deflection_angle(init.peak_1,init.peak_2)
#max_deflection_angle = 3.864


# initialize points of linearization
points_of_linearization = 0


# initialize angle nolinear distribution
angle_nolinear_distribution = np.zeros((init.points_per_cycle,1))
distribution_temp=[]

l1 = len(angle_nolinear_distribution)

for i in range(0,l1):
	# calculate the angle corresponding to the sampling point
	angle_nolinear_distribution[i,0] = -1.0*max_deflection_angle*np.cos(2*np.pi*init.resonance_frequence*(i*init.time_slot))

# calculate points of linearization

#np.savetxt('cos.txt',angle_nolinear_distribution,fmt="%f")

temp = -1*max_deflection_angle
while temp  <= max_deflection_angle:
	points_of_linearization += 1
	temp = temp + init.angle_threshold
	distribution_temp.append(temp)

distribution = np.zeros((len(distribution_temp),2))
distribution[:,0] = distribution_temp

temp_1 = distribution[0,0]
wave_ID = 0



for i in range(0,l1):
    if angle_nolinear_distribution[i] > temp_1:

    	#print('%f %d' % (distribution[wave_ID,0], distribution[wave_ID,1]))
        wave_ID = wave_ID + 1
        temp_1 = distribution[wave_ID,0]
       

        

    if wave_ID >= distribution.shape[0]:

        break

    distribution[wave_ID,1] = distribution[wave_ID,1]+1
   


np.savetxt('distribution.txt',distribution,fmt="%f,%d")
#np.savetxt(serial_Number+'_distribution'+asr+rf+dv+'.txt',distribution,fmt="%f,%d")

