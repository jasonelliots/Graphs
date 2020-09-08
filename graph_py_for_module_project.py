class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        # adds a vertex (point) as an key with a value set to an empty set (where the edges (pathways) will go)
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        # if the two passed in vertices (points) are in the dictionary, add v2 to the value of the key for v1. (directed aka one way)
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def get_neighbors(self, vertex_id):
        # gets the neighbors of given vertex 
        return self.vertices[vertex_id]