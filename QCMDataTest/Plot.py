import numpy as np
from matplotlib import pyplot as plt
time = np.genfromtxt('/Users/Matt/Desktop/testdata11.txt',delimiter=',',usecols=(1))
abs1 = np.genfromtxt('/Users/Matt/Desktop/testdata11.txt',delimiter=',',usecols=(2))
rel1 = np.genfromtxt('/Users/Matt/Desktop/testdata11.txt',delimiter=',',usecols=(3))
abs2 = np.genfromtxt('/Users/Matt/Desktop/testdata11.txt',delimiter=',',usecols=(4))
rel2 = np.genfromtxt('/Users/Matt/Desktop/testdata11.txt',delimiter=',',usecols=(5))
abs3 = np.genfromtxt('/Users/Matt/Desktop/testdata11.txt',delimiter=',',usecols=(6))
rel3 = np.genfromtxt('/Users/Matt/Desktop/testdata11.txt',delimiter=',',usecols=(7))

plt.plot(time,rel1,'b')
plt.plot(time,rel2,'r')
plt.plot(time,rel3,'g')
plt.title('Frequency Shift')
plt.xlabel('Time (s)')
plt.ylabel('Frequency Shift (Hz)')
plt.savefig('/Users/Matt/Desktop/testdata11.png')
plt.show()