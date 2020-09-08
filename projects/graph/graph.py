"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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
            # dont need to do this if passing in each direction individually to this function ie w {5,3} and {3,5}
            # self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def get_neighbors(self, vertex_id):
        # gets the neighbors of given vertex 
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # Create a queue to hold nodes to visit
        to_visit = Queue()

        # Create a set to hold visited nodes
        visited = set()

        # Initalize: add the starting node to the queue
        to_visit.enqueue(starting_vertex)

        # While queue not empty:
        while to_visit.size() > 0:
            # dequeue first entry
            v = to_visit.dequeue()

            # if not visited:
            if v not in visited:
                # Visit the node (print it out)
                print(v)

                # Add it to the visited set
                visited.add(v)

                # enqueue all its neighbors
                # how to access list of neighbors? - in the vertices dictionary as the value of the v index
                for n in self.vertices[v]:
                    #print(f"Adding: {n}")
                    to_visit.enqueue(n)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack to hold nodes to visit
        to_visit = Stack()

        # Create a set to hold visited nodes
        visited = set()

        # Initalize: add the starting node to the Stack
        to_visit.push(starting_vertex)

        # While queue not empty:
        while to_visit.size() > 0:
            # dequeue first entry
            v = to_visit.pop()

            # if not visited:
            if v not in visited:
                # Visit the node (print it out)
                print(v)

                # Add it to the visited set
                visited.add(v)

                # enqueue all its neighbors
                for n in self.vertices[v]:
                    #print(f"Adding: {n}")
                    to_visit.push(n)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Broken pseudocode
        # need base case 
        # for n in self.vertices[v]:
        #     dft_recursive(n)
        
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue the PATH TO starting_vertex
        queue = Queue()
        visited_vertices = set()
        # Create an empty set to track visited vertices 
        queue.enqueue({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })
        # same as this 
        # queue.enqueue([starting_vertex])

        # while the queue is not empty:
        while queue.size() > 0: 
            # get the current vertex PATH (deque from queue)
            current_obj = queue.dequeue()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']

            # set the current vertex to the LAST element of the PATH 

            # Check if the current vertex has not been visited:
            if current_vertex not in visited_vertices:

                # CHECK IF THE CURRENT VERTEX IS DESTINATION 
                #  IF IT IS, STOP AND RETURN
                if current_vertex == destination_vertex:
                    return current_path

                # Mark the current vertex as visited
                # Add the current vertex to a visited_set
                visited_vertices.add(current_vertex)
                    

                for neighbor_vertex in self.get_neighbors(current_vertex):
                # Queue up NEW paths with each neighbor:
                    # append the neighbor to current path 
                    # queue up NEW path
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)
                    queue.enqueue({
                        'current_vertex': neighbor_vertex,
                        'path': new_path
                    })

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
         # Create an empty queue and enqueue the PATH TO starting_vertex
        stack = Stack()
        visited_vertices = set()
        # Create an empty set to track visited vertices 
        stack.push({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })
        # same as this 
        # queue.enqueue([starting_vertex])

        # while the queue is not empty:
        while stack.size() > 0: 
            # get the current vertex PATH (deque from queue)
            current_obj = stack.pop()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']

            # set the current vertex to the LAST element of the PATH 

            # Check if the current vertex has not been visited:
            if current_vertex not in visited_vertices:

                # CHECK IF THE CURRENT VERTEX IS DESTINATION 
                #  IF IT IS, STOP AND RETURN
                if current_vertex == destination_vertex:
                    return current_path

                # Mark the current vertex as visited
                # Add the current vertex to a visited_set
                visited_vertices.add(current_vertex)
                    

                for neighbor_vertex in self.get_neighbors(current_vertex):
                # Queue up NEW paths with each neighbor:
                    # append the neighbor to current path 
                    # queue up NEW path
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)
                    stack.push({
                        'current_vertex': neighbor_vertex,
                        'path': new_path
                    })

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
