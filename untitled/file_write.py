import numpy as np
import re

edgesfile = '/Users/Matt/Desktop/edges.csv'
outfile = open('/Users/Matt/Desktop/editededges.csv','w')
outfile.write('edge_id, source, target, length, car, car reverse, ')
outfile.write('\n')

nodesfile = '/Users/Matt/Desktop/nodesedited.csv'

edge_id = np.genfromtxt(edgesfile,delimiter=',',usecols=0,skip_header=1)
source = np.genfromtxt(edgesfile,delimiter=',',usecols=1,skip_header=1)
target = np.genfromtxt(edgesfile,delimiter=',',usecols=2,skip_header=1)
length = np.genfromtxt(edgesfile,delimiter=',',usecols=3,skip_header=1)
car = np.genfromtxt(edgesfile,delimiter=',',usecols=4,skip_header=1)
car_rev = np.genfromtxt(edgesfile,delimiter=',',usecols=5,skip_header=1)

newnodes = []
nodes = np.genfromtxt(nodesfile,delimiter=',',usecols=0,skip_header=1)
for node in nodes:
    newnodes.append(int(node))

#print newnodes
k = 0

for n in range (0,len(source)):
    #print source[n]

    if re.search(str(int(source[n])),str(newnodes)) or re.search(str(int(target[n])),str(newnodes)):
        outfile.write('%s, %s, %s, %s, %s, %s' % (k, source[n], target[n], length[n], car[n], car_rev[n]))
        outfile.write('\n')
        k = k + 1
outfile.close()
