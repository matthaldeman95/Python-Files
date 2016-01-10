import numpy as np
from matplotlib import pyplot as plt
#time = np.genfromtxt('/Volumes/NO NAME/FlexQCM/Miller/C1/0pc/0pc_f.csv', delimiter=',',usecols=(0))
amp = np.genfromtxt('/Volumes/NO NAME/FlexQCM/Pierce/BJT/oscsample.csv', delimiter=',',usecols=(0))

file1 = open('/Volumes/NO NAME/FlexQCM/Pierce/BJT/oscsample_times.csv','w')

for x in range(0,10000):
    file1.write(str(x*1E-10)),
    file1.write(', '),
    file1.write(str(amp[x])),
    file1.write('\n')

file1.close()