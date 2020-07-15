from util import Stack, Queue


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


def build(bois):
    graph = Graph()
    for x, y in bois:
        graph.add_vertex(x)
        graph.add_vertex(y)
        graph.add_edge(y, x)
    return graph


def earliest_ancestor(ancestors, starting_node):
    graph = build(ancestors)
    stack = Stack()
    # create a set
    been = set()
    stack.push([starting_node])
    # make two lists
    lon = []
    aged = -1
    # while loop
    while stack.size() > 0:
        line = stack.pop()
        current = path[-1]
        if (len(line) >= len(lon) and current < aged):
            lon = line
            aged = lon[-1]
        if current not in been:
            been.add(current)
            carers = graph.get_neighbors(current)
            for carer in carers:
                new = line+[carer]
                stack.push(new)
    return lon[-1]
    # loop through starting at starting node
    # find starting nodes ancestors
    # append to the ancestors list
    # find all the ancestors of ancestors list
    #put in temp
    # map through temp


if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6),
                      (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    earliest_ancestor(test_ancestors, 1)
