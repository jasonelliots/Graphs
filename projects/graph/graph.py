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
                # Visit the node (print it out) (or whatever crazy stuff you might want to do with it)
                print(v)

                # Add it to the visited set
                visited.add(v)

                # enqueue all its neighbors
                for n in self.vertices[v]:
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
                    to_visit.push(n)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # initializes visited set on first pass 
        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        # visit current - base case 
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
        # Create an empty queue and enqueue the PATH TO starting_vertex
        queue = Queue()
        # Create an empty set to track visited vertices 
        visited_vertices = set()
    
        queue.enqueue([starting_vertex])

        # while the queue is not empty:
        while queue.size() > 0: 
            # get the current vertex PATH (deque from queue)
            current_path = queue.dequeue()
            # extra for search - set the current vertex to the LAST element of the PATH 
            current_vertex = current_path[-1]

            # Check if the current vertex has not been visited:
            if current_vertex not in visited_vertices:

                # CHECK IF THE CURRENT VERTEX IS DESTINATION 
                # IF IT IS, STOP AND RETURN
                # extra for search 
                if current_vertex == destination_vertex:
                    return current_path

                # Mark the current vertex as visited
                visited_vertices.add(current_vertex)

                for neighbor_vertex in self.get_neighbors(current_vertex):
                # Queue up NEW paths with each neighbor:
                    # append the neighbor to current path 
                    # extra for search 
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)
                    # queue up NEW path    
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
         # Create an empty stack and stackup the PATH TO starting_vertex
        stack = Stack()
         # Create an empty set to track visited vertices 
        visited_vertices = set()
       
        # add starting vertex as path top of stack 
        stack.push([starting_vertex])

        # while the stack is not empty:
        while stack.size() > 0: 
            # pop the current path of the top of the stack + get the current vertex
            current_path = stack.pop()
            current_vertex = current_path[-1]

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
                # stack NEW paths with each neighbor:
                    # append the neighbor to current path 
                    # stack NEW path
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        if visited is None:
            visited = set()

        if path is None:
            path = []

        visited.add(starting_vertex)

        path = path + [starting_vertex]

        if starting_vertex == destination_vertex: 
            return path
        
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path is not None:
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
    # print(graph.vertices)

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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
