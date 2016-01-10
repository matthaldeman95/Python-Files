timefile = open('/Users/Matt/Desktop/times.txt', 'w')
for i in range (0,2100000):
    time = str(i*1E-5)
    timefile.write(time)
    timefile.write('\n')

timefile.close()

