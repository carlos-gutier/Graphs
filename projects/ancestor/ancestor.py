class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # dictionary of vertices as "keys" and
        # "set" of edges (vertices) as "values" (see add_vertex)
        self.vertices = {} 

    def add_vertex(self, ancestors_list):
        """
        Add a vertex to the graph.
        """
        # this is to add all vertices as keys first
        for v in ancestors_list:
            self.vertices[v] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # adding values (set) to keys already added
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            # cannot add edges if they are not vertices first
            raise IndexError("That vertex does not exist!")


    def bfs(self, starting_vertex, destination_vertex):
            """
            Return a list containing the SHORTEST PATH from
            starting_vertex to destination_vertex in
            breath-first order.
            """
            # Create an empty set to store visited nodes
            visited = set()
            # Create an empty Queue & enqueue A PATH TO the starting vertex
            q = Queue()
            q.enqueue( [starting_vertex] ) # "[]" to enqueue PATH
            # While the queue is not empty...
            while q.size() > 0:
                # Dequeue the first PATH
                path = q.dequeue()
                # GRAB THE VERTEX FORM THE END OF THE PATH
                v = path[-1]
                # IF VERTEX == TARGET, RETURN PATH
                if v == destination_vertex:
                    return path
                # if that vertex has not been visited...
                if v not in visited:
                    # Mark it as visited
                    visited.add(v)
                    # Then add a path to all of its neighbors to the back of the queue
                    for neighbor in self.vertices[v]:
                        # Copy the path
                        path_copy = list(path)
                        # Append neighbor to the back of the copy
                        path_copy.append(neighbor)
                        # Enqueue copy
                        q.enqueue(path_copy)




test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]