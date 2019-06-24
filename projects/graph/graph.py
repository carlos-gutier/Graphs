"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
        
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def bft(self, starting_vertex): # FIFO - using QUEUE
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty Queue and enqueu the starting vertex
        q = Queue()
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)                
        
    def dft(self, starting_vertex): # LIFO - using STACK
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty Queue and push the starting vertex
        s = Stack()
        s.push(starting_vertex)
        # Create an empty set to store visited vertices
        visited = set()
        # While the stack is not empty
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If that vertex has not been visited
            if v not in visited:
                print(v)
                visited.add(v)
                # Add all of its neighbors to the top of the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for neighbor in self.vertices[starting_vertex]:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty Queue and enqueue the starting vertex
        q = Queue()
        q.enqueue([starting_vertex]) # Creating list of lists with paths
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the FIRST PATH
            path = q.dequeue()
            # Gettig VERTEX at END of PATH
            v = path[-1]
            if v == destination_vertex:
                return path
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Make NEW PATHS with JUST NEIGHBORS of "v"
                # then we can go through each new path at the time
                # until we find "destination_vertex"
                for neighbor in self.vertices[v]:
                    # Make copy of "path"
                    path_copy = path.copy()
                    # Add v's neighbor to "path_copy"
                    path_copy.append(neighbor)
                    # Add "path_copy" with added neigbor to queue
                    q.enqueue(path_copy)


        
    def dfs(self, starting_vertex, destination_vertex): # LAST IN FIRST OUT
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty Stack and push the starting vertex AS A LIST (PATH)
        s = Stack()
        s.push([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the Stack is not empty
        while s.size() > 0:
            # Pop the FIRST PATH
            path = s.pop()
            # Get VERTEX at END of PATH
            v = path[-1]
            # If vertex is same as "destination_vertex"
            if v == destination_vertex:
                return path
            # If vertex not in visited
            if v not in visited:
                # Mark as visited
                visited.add(v)
            # Loop through neighbor for vertex
            for neighbor in self.vertices[v]:
                # make copy of path
                path_copy = path.copy()
                # add v's neighbor to path_copy
                path_copy.append(neighbor)
                # add path_copy with added neighbor to Stack
                s.push(path_copy)






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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

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
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
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