import numpy as np
from matplotlib import pyplot as plt
time = np.genfromtxt('/Volumes/NO NAME/FlexQCM/Miller/C1/0pc_new/d1_w_times.csv',delimiter=',',usecols=(0))
amp = np.genfromtxt('/Volumes/NO NAME/FlexQCM/Miller/C1/0pc_new/d1_w_times.csv',delimiter=',',usecols=(1))

file1 = open('/Volumes/NO NAME/FlexQCM/Miller/C1/0pc_new/d1_short.csv','w')

for x in range(125000,1700000):
    file1.write(str(time[x]-0.011)),
    file1.write(', '),
    file1.write(str(amp[x])),
    file1.write('\n')

file1.close()

