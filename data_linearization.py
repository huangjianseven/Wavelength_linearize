from matplotlib.pyplot import *
import numpy as np

import initialization as init

a=np.loadtxt(open("distribution.txt","rb"),delimiter=",",dtype='float',skiprows=0)

b=np.loadtxt(open("810.txt","rb"),dtype='float',skiprows=0)

real_data=b[init.fake_begin_point-1:init.fake_end_point,1]

raw_data_len = len(real_data)

raw_data = np.zeros((raw_data_len,2))

raw_data[:,0]= np.arange(1,raw_data_len+1,1)
raw_data[:,1] = real_data


#np.savetxt('raw_data_810.txt',raw_data,fmt="%d,%f")

linear_size = len(a)
raw_size = len(real_data)

redistribution = np.zeros((linear_size,4))
redistribution[:,3] = a[:,0]

redistribution[:,0] = np.arange(1,linear_size+1,1)
redistribution[:,2] = a[:,1]

row_ID = 0
flag = 1

flag = 1
sum = 0

for i in range(0,raw_size):
	
	sum = sum + real_data[i]
	flag += 1
	#When finilish one 
	if flag > redistribution[row_ID,2]:
		# Do average here
		redistribution[row_ID,1] = sum / redistribution[row_ID,2]
		row_ID += 1
		sum = 0
		flag = 1

	# if row_ID > redistribution.shape[0]:
	# 	break

np.savetxt('Linearization_810.txt',redistribution,fmt="%d,%f,%d,%f")
print redistribution
