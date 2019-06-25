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

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


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
    
# DFS???
# Want to get all paths from starting node
# then get the longest
# if more than 1 path is max length
# then check last vertex in each path
# and return lowest numeric ID
def earliest_ancestor(ancestors, starting_node):
    # Build graph
    graph = Graph()
    # loop thorough tuple pairs from ancestors list
    for pair in ancestors:
        # add vertices and edges
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])     
    # Create an empty Stack
    print(graph)
    s = Stack()
    # Create a list of paths
    paths = []
    # Enqueue starting node/vertex
    s.push([starting_node])
    # Create empty visited set
    visited = set()
    # While the Queue is not empty
    while s.size() > 0:
        # Pop FIRST PATH
        path = s.pop()
        # Get VERTEX at END of PATH
        v = path[-1]
        # if vertex has not been visited
        if v not in visited:
            # add v to visited
            visited.add(v)
            # Loop through its ancestors
            # print(graph.vertices)
            for ancestor in graph.vertices[v]:
                # print(ancestor)
                # make a copy of path
                path_copy = path.copy()
                # add v's ancestor to path_copy
                path_copy.append(ancestor)
                # Push path_copy with added neighbor to paths
                s.push(path_copy)
                # add path_copy to paths to track all paths
                paths.append(path_copy)

    # Check for length of all paths
    print(paths)    
    path_lengths = [len(p) for p in paths]
    # print(path_lengths)
    # Get longest path(s) in "paths"
    max_paths = [p for p in paths if len(p) == max(path_lengths)]
    # print(max_paths)
    # if more than 1 path equal to max length
    if len(max_paths) > 1:
        # then check last vertex in each path
        # and return lowest numeric ID
        earliest = min([p[-1] for p in max_paths])
        return earliest
    else:
        earliest = max_paths[0][-1]
        return earliest
    # Earliest ancestor should be last vertex in longest_path
    # return paths


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 6))