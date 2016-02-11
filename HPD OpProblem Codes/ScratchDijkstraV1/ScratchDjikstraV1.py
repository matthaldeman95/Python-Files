from collections import defaultdict, deque
from matplotlib import pyplot as plt
import math

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):                              #Adds a value to the set of noes
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):       #Adds an edge between from and to_nodes
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance     #Sets length of edge to specified distance
        self.distances[(to_node, from_node)] = distance

    def dijkstra(graph, initial):
        visited = {initial:0}
        path = {}

        nodes = set(graph.nodes)

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node
            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in graph.edges[min_node]:
                weight = current_weight + graph.distances[(min_node,edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node
        return visited, path



def shortest_path(graph, origin, destination):
    visited, paths = Graph.dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)




if __name__ == '__main__':
    graph = Graph()

    node1 = {'x': 0, 'y':0}
    node2 = {'x': 2, 'y':2}
    node3 = {'x': 4, 'y':1}
    node4 = {'x': 1, 'y':5}
    node5 = {'x': 5, 'y':7}
    node6 = {'x': 8, 'y':4}

    for node in ['1','2','3','4','5','6']:
        graph.add_node(node)

    dist12 = math.sqrt( (node2['x']-node1['x'])**2 + (node2['y']-node1['y'])**2 )
    dist13 = math.sqrt( (node3['x']-node1['x'])**2 + (node3['y']-node1['y'])**2 )
    dist14 = math.sqrt( (node4['x']-node1['x'])**2 + (node4['y']-node1['y'])**2 )
    dist23 = math.sqrt( (node3['x']-node2['x'])**2 + (node3['y']-node2['y'])**2 )
    dist24 = math.sqrt( (node4['x']-node2['x'])**2 + (node4['y']-node2['y'])**2 )
    dist25 = math.sqrt( (node5['x']-node2['x'])**2 + (node5['y']-node2['y'])**2 )
    dist36 = math.sqrt( (node6['x']-node3['x'])**2 + (node6['y']-node3['y'])**2 )
    dist45 = math.sqrt( (node5['x']-node4['x'])**2 + (node5['y']-node4['y'])**2 )
    dist56 = math.sqrt( (node6['x']-node5['x'])**2 + (node6['y']-node5['y'])**2 )

    graph.add_edge('1','2',dist12)
    graph.add_edge('1','3',dist13)
    graph.add_edge('1','4',dist14)
    graph.add_edge('2','3',dist23)
    graph.add_edge('2','4',dist24)
    graph.add_edge('2','5',dist25)
    graph.add_edge('3','6',dist36)
    graph.add_edge('4','5',dist45)
    graph.add_edge('5','6',dist56)
    


    print(shortest_path(graph, '1', '6'))
