from matplotlib.pyplot import *
import numpy as np


GYW=np.loadtxt(open("20180129.csv","rb"),delimiter=",",dtype='float',skiprows=0)
#GYW1=np.loadtxt(open("1823_20180128_1.txt","rb"),dtype='float',skiprows=0)
#plot(GYW[:,0],GYW[:,1],label='Mercury Lamp')
#plot(GYW1[:,0],1.0002*GYW1[:,1],label='1800nm Filter')






l1 = len(GYW[:,0])
# lines of new matrix
print(l1)
result=np.zeros((1027,3))
l2 = len(result)

intensity_sum = 0

wave_ID = 0
temp = GYW[0,0]
for i in range(0,l1):
	if abs(GYW[i,0] - temp) > 1e-6:

		#i = i - 1
		result[wave_ID, 1] /= result[wave_ID, 2]
		print('%d %d %d' % (wave_ID, temp, result[wave_ID, 2]))
		wave_ID = wave_ID + 1
		temp = GYW[i,0]

	if wave_ID >= result.shape[0]:
        
		break

	result[wave_ID,0] = temp
	result[wave_ID,1] += GYW[i, 1]
	result[wave_ID,2] = result[wave_ID,2]+1

result[wave_ID, 1] /= result[wave_ID, 2]
print('%d %d %d' % (wave_ID, temp, result[wave_ID, 2]))

np.savetxt('002.txt',result,fmt="%d,%f,%d")




#xlabel('Wavelength(nm)')

#ylabel('Intensity')
#title(r'Wavelength Range' )
#plt.axis([1,115,40,90])

#grid()
#legend(loc='upper right')
#show()