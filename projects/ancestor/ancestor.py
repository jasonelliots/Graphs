
# Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.

# Could use either DFS or BFS for this - both 0(n)
# We don't know when to stop until we've seen everyone - we need to visit every node

# When is DFS better choice?
    # want to find maze, one solution  
    # if you want to use recursion 

# When is BFS a better choice?
    # better for shortest path 

# ancestors are pased in as list of tuples (parent, child)

# U 
    # find a child's earliest ancestor
# P 
    # What is the Graph?
        # nodes are people, edges are relationships - when child has a parent 
        # one directional - directed 
    # Build our graph, or just define get_neighbors 
        #    
    # Which algorithm to use? BFS or DFS 
        # Either works, try DFS first

# try without instantiating classes - just building out define get_neighbors, use guided project dictionary problem as reference 
# try using bfs 

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
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
    
    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex):
        return self.vertices[vertex]

def build_graph(ancestors):
    graph = Graph()

    # unpacking the tuple 
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    
    return graph 

def get_parents(child):

    parents = []
    

# using BFS

def earliest_ancestor(ancestors, starting_node):
    graph = build_graph(ancestors)

    q = Queue()

    visited = set()

    ### base case if starting_node has no parents
    if len(graph.get_neighbors(starting_node)) == 0:
        return -1 
    ###

    q.enqueue([starting_node])

    longest_path = []

    while q.size() > 0:
        path = q.dequeue()
        current_node = path[-1]
        
        ### logic for updating longest path 
        if (len(path) > len(longest_path)) or (len(path) == len(longest_path) and current_node < longest_path[-1]):
            longest_path = path 
        ###

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.get_neighbors(current_node)

            for parent in parents:
                new_path = path + [parent]
                q.enqueue(new_path)
    
    return longest_path[-1]


# using DFS 

# def earliest_ancestor(ancestors, starting_node):
#     graph = build_graph(ancestors)

#     s = Stack()

#     visited = set()

#     # base case if starting_node has no parents
#     if len(graph.get_neighbors(starting_node)) == 0:
#         return -1 
#     ###

#     s.push([starting_node])

#     longest_path = []

#     while s.size() > 0:
#         path = s.pop()
#         current_node = path[-1]
        
#         ### logic for updating longest path 
#         if (len(path) > len(longest_path)) or (len(path) == len(longest_path) and current_node < longest_path[-1]):
#             longest_path = path 
#         ###

#         if current_node not in visited:
#             visited.add(current_node)

#             parents = graph.get_neighbors(current_node)

#             for parent in parents:
#                 new_path = path + [parent]
#                 s.push(new_path)
    
#     return longest_path[-1]