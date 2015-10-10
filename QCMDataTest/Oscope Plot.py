import numpy as np
from matplotlib import pyplot as plt
time = np.genfromtxt('/Users/Matt/Desktop/oscopedata.csv',delimiter=',',usecols=(0))
amp = np.genfromtxt('/Users/Matt/Desktop/oscopedata.csv',delimiter=',',usecols=(1))

plt.plot(time,amp)
plt.show()