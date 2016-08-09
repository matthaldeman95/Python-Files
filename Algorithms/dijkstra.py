from collections import defaultdict
import math

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.weight = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.weight[(from_node,to_node)] = weight


def distance(x1,y1,x2,y2):

    return math.sqrt((x2-x1)**2 + (y2-y1)**2)



def dijkstra(graph,start):
    nodes = set(graph.nodes)
    visited = {}
    path = {}
    for node in nodes:

        if node == start:
            visited[node] = 0
            path[node] = [start]
        else:
            visited[node] = float('inf')
    currentnode = start

    while nodes:
        for connnode in graph.edges[currentnode]:
            newdist = graph.weight[currentnode,connnode] + visited[currentnode]
            if newdist < visited[connnode]:
                visited[connnode] = newdist
                path[connnode] = path[currentnode] + [connnode]

        nodes.remove(currentnode)
        currentnode += 1

    return visited, path

def shortest_path(graph, start, end):
    visited, path = dijkstra(graph, start)
    return visited[end], path[end]


if __name__ == '__main__':
    graph = Graph()
    nodes = [{'nodeid': 0, 'coord': (0, 0), 'connnodes': [1,3]},
             {'nodeid': 1, 'coord': (1, 0), 'connnodes': [0,2]},
             {'nodeid': 2, 'coord': (2, 0), 'connnodes': [1,4]},
             {'nodeid': 3, 'coord': (0, 1), 'connnodes': [0,4,5]},
             {'nodeid': 4, 'coord': (2, 1), 'connnodes': [2,3,6,7]},
             {'nodeid': 5, 'coord': (1, 2), 'connnodes': [3,8]},
             {'nodeid': 6, 'coord': (3, 2), 'connnodes': [4,7]},
             {'nodeid': 7, 'coord': (2, 3), 'connnodes': [4,6,8,9]},
             {'nodeid': 8, 'coord': (1, 4), 'connnodes': [5,7,9]},
             {'nodeid': 9, 'coord': (2, 4), 'connnodes': [7,8]}
             ]
    for node in nodes:
        graph.add_node(node['nodeid'])
        for connnode in node['connnodes']:
            coord1 = node['coord']
            coord2 = nodes[connnode]['coord']
            dist = distance(coord1[0],coord1[1],coord2[0],coord2[1])
            graph.add_edge(node['nodeid'], connnode, dist)
    print shortest_path(graph,0,7)