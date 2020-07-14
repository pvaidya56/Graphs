"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        # Create an empy Set to store visited vertices
        # While the queue is not empty...
            # Dequeue the first vertex
            # If that vertex has not been visited...
                # Mark as visited
                # Then add all of its neighbors to the back of the queue
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            current_node = q.dequeue()
            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                for neighbor in self.vertices[current_node]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #create a new stack
        s = Stack()
        #set for visited
        visited = set()
        #add start_node to the stack
        s.push(starting_vertex)
        #while stack is not empty
        while s.size() > 0:
            #assign node to stack.pop()
            current_node = s.pop()
            #if node is not in visited set
            if current_node not in visited:
                print(current_node)
                #add current node to visited set 
                visited.add(current_node)
                #for each child in current_node
                for next_node in self.vertices[current_node]:
                    #add each child to the stack
                    s.push(next_node)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #create empty queue
        q = Queue()
        #enqueue a path to starting_vertex
        q.enqueue([starting_vertex])
        #create a visited set
        visited = set()
        #while q is not empty
        while q.size() > 0:
            #dequeue first path
            path = q.dequeue()
            #grab vertex from last path
            vertex = path[-1]
            #if that vertex has not been visited
            if vertex not in visited:
                #check if that vertex is the target
                if vertex == destination_vertex:
                    return path
                #mark it as visited
                visited.add(vertex)
                #for each edge in item, add a oath to its neighbors to the back of the queue
                for neighbor in self.get_neighbors(vertex):
                    #copy path
                    new_path = list(path)
                    #append neighbor to the back of the queue
                    new_path.append(neighbor)
                    q.enqueue(new_path)
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #create an empty stack
        s = Stack()
        #add the starting point as the first path in the stack
        s.push([starting_vertex])
        #create set for visited
        visited = set()
        #while stack is not empty
        while s.size() > 0:
            #remove path at top of stack
            path = s.pop()
            #grab the last vertex of path
            vertex = path[-1]
            #if vertex not visited yet
            if vertex not in visited:
                #check if its the target, if so return path
                if vertex == destination_vertex:
                    return path
                #mark as visited
                visited.add(vertex)
                #get neighbors for each edge in item
                    #get this by adding a path to neighbors at top of stack
                for neighbors in self.get_neighbors(vertex):
                    #copy the path
                    new_path = list(path)
                    new_path.append(neighbors)
                    s.push(new_path)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if visited is None:
            #visited set
            visited = set()
        if path is None:
            #ordered array
            path = []
        #add starting vertex to visited and path
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        #if target, return path
        if starting_vertex == destination_vertex:
            return path
        #else, call dfs on each neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))