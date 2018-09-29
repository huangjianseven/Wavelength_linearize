from matplotlib.pyplot import *
import numpy as np

# set A/D Sample rate
ad_sample_rate = 3000000
asr = "_"+('%d' % ad_sample_rate)+'Hz'

#set Mirror Resonance Frequence
resonance_frequence =  621.07
rf = '_'+('%.2f'%resonance_frequence)+'Hz'

#set Mirror serial Number
serial_Number = 'TJ_16P0004'
#set driver voltage mV
driver_voltage = 590
dv = '_'+('%d'%driver_voltage)+'mV'

# set 2 Peak position points of Interference Band-Pass Filter
peak_1 = 1848
peak_2 = 3000

# set the Wavelength of Interference Band-Pass Filter
Filter_wavelength = 1650


# set Angle Threshold (Deg)
angle_threshold = 0.008

# define linear regression equation
def lre(wavelength):
	angle = 0.00799*wavelength - 10.376
	return angle

# calculate the half cycle time of Mirror
half_cycle_time = 1/(2*resonance_frequence)

# calculate the Design deflection angle of Interference Band-Pass Filter
phi_trig = lre(Filter_wavelength)

#ZEMAX result
#phi_trig = 2.808 
phi_trig_rad = np.deg2rad(phi_trig)



# calculate the points per spectral cycle,temp special
points_per_cycle = int(ad_sample_rate * half_cycle_time)

# calculate time slot between one point and next one
time_slot = half_cycle_time/points_per_cycle

# calculate the FAKE End point of Mirror cycle
fake_end_point = (peak_2 - peak_1)/2 + peak_1
fake_begin_point = fake_end_point - points_per_cycle + 1

print fake_begin_point
print fake_end_point