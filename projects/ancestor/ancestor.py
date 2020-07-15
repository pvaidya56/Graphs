#Use a DFS to get to the end of the node to find earliest ancestor

##UPER
# Plan
## Graphs problem solving steps 
# Translate the problem
## Nodes: people
## Edges: when a child has a parent

## build our graph or justify get_neighbors
#### 
## Choose algorithm
### Either BFS OR DFS
#### DFS
#import deque from collections

from util import Stack 

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
    
    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)
    
    def get_neighbors(self, vertex):
        return self.vertices[vertex]

#Build a path like search
## But we don't know when to stop till we've visited every node

graph = Graph()
def build_graph(ancestors):
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    return graph

def earliest_ancestor(ancestors, starting_node):
    graph = build_graph(ancestors)

    s = Stack()
    visited = set()
    s.push([starting_node])
    longest_path = []
    aged_one = -1

    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]

        #if path is longer, or path is equal but the id is smaller
        if len(path) > len(longest_path) or (len(path) == len(longest_path) and current_node < aged_one):
            longest_path = path
            aged_one = longest_path[-1]

        if current_node not in visited:
            visited.add(current_node)
            parents = graph.get_neighbors(current_node)

            for parent in parents:
                new_path = path + [parent]
                s.push(new_path)
    if longest_path:
        return longest_path[-1]
    else:
         return -1