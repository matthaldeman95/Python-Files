import numpy as np
from matplotlib import pyplot as plt

time = np.genfromtxt('/Volumes/NO NAME/FlexQCM/Pierce/BJT/oscsample_times.csv', delimiter=',',usecols=(0))
amp = np.genfromtxt('/Volumes/NO NAME/FlexQCM/Pierce/BJT/oscsample_times.csv', delimiter=',',usecols=(1))

plt.plot(time,amp)
plt.show()





