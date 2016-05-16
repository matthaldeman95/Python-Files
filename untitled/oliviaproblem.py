import simpy
import numpy as np
from random import randint
import re


#nodesfile = '/Users/Matt/Desktop/nodesedited.csv'                  #CSV file containing nodes
edgesfile = '/Users/Matt/Desktop/edges.csv'                  #CSV file containing edges
nodesfile = '/Users/Matt/Desktop/nodesedited.csv'

outfile = open('/Users/Matt/Desktop/edgesedited.csv','w')
outfile.write('edge_id, source, target, length, car, car_rev, hightime, lowtime')
outfile.write('\n')


nodes = np.genfromtxt(nodesfile,delimiter=',',usecols=0,skip_header=1)              #Array of all node names
long = np.genfromtxt(nodesfile,delimiter=',',usecols=1, skip_header=1)               #Array of latitudes
lat = np.genfromtxt(nodesfile,delimiter=',',usecols=2,skip_header=1)               #and longitudes

edge_id = np.genfromtxt(edgesfile,delimiter=',',usecols=0,skip_header=1)            #Array of edge names
edge_sn = np.genfromtxt(edgesfile,delimiter=',',usecols=1,skip_header=1)            #Start nodes for each edge
edge_dn = np.genfromtxt(edgesfile,delimiter=',',usecols=2,skip_header=1)            #and destination nodes
edge_length = np.genfromtxt(edgesfile,delimiter=',',usecols=3,skip_header=1)        #Length of edge in meters
edge_road = np.genfromtxt(edgesfile,delimiter=',',usecols=4,skip_header=1)          #
edge_oneway = np.genfromtxt(edgesfile,delimiter=',',usecols=5,skip_header=1)        #One way value



highspeed = [25,30,35,40,50,65]
lowspeed = [10,15,20,25,35,60]

for n in range(0,len(highspeed)):
    highspeed[n] = highspeed[n]*1609.34
    lowspeed[n] = lowspeed[n]*1609.34



for k in range(0,len(edge_id)):
    if edge_road[k] == 1:
        hspeed = highspeed[0]
        lspeed = lowspeed[0]
    elif edge_road[k] == 2:
        hspeed = highspeed[1]
        lspeed = lowspeed[1]
    elif edge_road[k] == 3:
        hspeed = highspeed[2]
        lspeed = lowspeed[2]
    elif edge_road[k] == 4:
        hspeed = highspeed[3]
        lspeed = lowspeed[3]
    elif edge_road[k] == 5:
        hspeed = highspeed[4]
        lspeed = lowspeed[4]
    elif edge_road[k] == 6:
        hspeed = highspeed[5]
        lspeed = lowspeed[5]


    hightime = edge_length[k] / hspeed
    lowtime = edge_length[k] / lspeed
    print edge_length[k],hightime,lowtime

    outfile.write('%s, %s, %s, %s,' % (int(edge_id[k]),int(edge_sn[k]),int(edge_dn[k]), int(edge_length[k]))),
    outfile.write('%s, %s, ' % (int(edge_road[k]),int(edge_oneway[k]))),
    outfile.write('%s, %s' % (hightime, lowtime))
    outfile.write('\n')





outfile.close()