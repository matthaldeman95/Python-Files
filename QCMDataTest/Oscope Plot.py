import numpy as np
from matplotlib import pyplot as plt
amp = np.genfromtxt('/Users/Matt/Documents/ORNL Internship/2015-11-10 QCMD Test/water 2.txt',delimiter=',',usecols=(0))
time = np.genfromtxt('/Users/Matt/Documents/ORNL Internship/2015-11-10 QCMD Test/times.txt',delimiter=',',usecols=(0))



plt.plot(amp)
#plt.title('1 Drop Water')
#plt.xlabel('Time (ms)')
#plt.ylabel('Amplitude (V)')
#plt.savefig('/Users/Matt/Desktop/2DWater.bmp')
plt.show()