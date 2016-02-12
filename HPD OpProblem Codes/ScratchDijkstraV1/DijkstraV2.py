from collections import defaultdict, deque
from matplotlib import pyplot as plt
import math
import networkx as nx

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):                              #Adds a value to the set of nodes
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):       #Adds an edge between from and to_nodes
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance     #Sets length of edge to specified distance
        self.distances[(to_node, from_node)] = distance

    def dijkstra(graph, initial):
        visited = {initial:0}                                   #create dictionary of visited nodes
        path = {}

        nodes = set(graph.nodes)

        while nodes:                                            #While there are nodes left in node set,
            min_node = None                                     #
            for node in nodes:                                  #Evaluate each node in set
                if node in visited:                             #
                    if min_node is None:                        #
                        min_node = node                         #Set current node
                    elif visited[node] < visited[min_node]:     #
                        min_node = node                         #
            if min_node is None:
                break

            nodes.remove(min_node)                              #remove current node from list of nodes
            current_weight = visited[min_node]

            for edge in graph.edges[min_node]:                                  #for all edges connected
                                                                                # to the current node:
                weight = current_weight + graph.distances[(min_node,edge)]      #add current weight to distance
                                                                                #between nodes, if already visited
                if edge not in visited or weight < visited[edge]:               #set weight to edge length if not
                                                                                # visited yet
                    visited[edge] = weight
                    path[edge] = min_node
        return visited, path



def shortest_path(graph, origin, destination):
    visited, paths = Graph.dijkstra(graph, origin)
    full_path = deque()
    #print(destination)
    _destination = paths[str(destination)]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)




if __name__ == '__main__':
    graph = Graph()
    plt.clf()
    x = []
    y = []

    nodes = []                                #list of nodes and --> connected nodes
    nodes.append((0,0,0))                     #node[0] = (0,0) (start node) --> node[1], node[2], node[3]
    nodes.append((2,2,1))                     #node[1] = (2,2)  --> node[2], node[3], node[4]
    nodes.append((4,1,2))                     #node[2] = (4,1)  --> node[5]
    nodes.append((1,5,3))                     #node[3] = (1,5)  --> node[4]
    nodes.append((5,7,4))                     #node[4] = (5,7)  --> node[5]
    nodes.append((8,4,5))                     #node[5] = (8,4) (end node)


    for node in range(0,len(nodes)):
        graph.add_node(str(nodes[node][2]))
        x.append(nodes[node][0])
        y.append(nodes[node][1])

    #for node in ['0','1','2','3','4','5']:
        #graph.add_node(node)


    dist01 = math.sqrt( (nodes[1][0]-nodes[0][0])**2 + (nodes[1][1]-nodes[0][1])**2 )
    dist02 = math.sqrt( (nodes[2][0]-nodes[0][0])**2 + (nodes[2][1]-nodes[0][1])**2 )
    dist03 = math.sqrt( (nodes[3][0]-nodes[0][0])**2 + (nodes[3][1]-nodes[0][1])**2 )
    dist12 = math.sqrt( (nodes[2][0]-nodes[1][0])**2 + (nodes[2][1]-nodes[1][1])**2 )
    dist13 = math.sqrt( (nodes[3][0]-nodes[1][0])**2 + (nodes[3][1]-nodes[1][1])**2 )
    dist14 = math.sqrt( (nodes[4][0]-nodes[1][0])**2 + (nodes[4][1]-nodes[1][1])**2 )
    dist25 = math.sqrt( (nodes[5][0]-nodes[2][0])**2 + (nodes[5][1]-nodes[2][1])**2 )
    dist34 = math.sqrt( (nodes[4][0]-nodes[3][0])**2 + (nodes[4][1]-nodes[3][1])**2 )
    dist45 = math.sqrt( (nodes[5][0]-nodes[4][0])**2 + (nodes[5][1]-nodes[4][1])**2 )

    graph.add_edge(str(nodes[0][2]),str(nodes[1][2]),dist01)
    graph.add_edge(str(nodes[0][2]),str(nodes[2][2]),dist02)
    graph.add_edge(str(nodes[0][2]),str(nodes[3][2]),dist03)
    graph.add_edge(str(nodes[1][2]),str(nodes[2][2]),dist12)
    graph.add_edge(str(nodes[1][2]),str(nodes[3][2]),dist13)
    graph.add_edge(str(nodes[1][2]),str(nodes[4][2]),dist14)
    graph.add_edge(str(nodes[2][2]),str(nodes[5][2]),dist25)
    graph.add_edge(str(nodes[3][2]),str(nodes[4][2]),dist34)
    graph.add_edge(str(nodes[4][2]),str(nodes[5][2]),dist45)

    plt.plot(nodes[0][0],nodes[0][1],nodes[1][0],nodes[1][1])




    result = shortest_path(graph, '0', '5')


    print(result)





    #Attempt to add in a graph of points / shortest route
    xmax = 0
    ymax = 0
    for value in range(0,len(nodes)):
        plt.plot(nodes[value][0],nodes[value][1],'or')
        plt.text((nodes[value][0]-0.25),(nodes[value][1]-0.25),nodes[value][2])
        if(x[value]>xmax):
            xmax = x[value]
        if(y[value]>ymax):
            ymax = y[value]
    plt.axis([0,xmax+3,0,ymax+3])
    #plt.plot(1,1)
    plt.show()
