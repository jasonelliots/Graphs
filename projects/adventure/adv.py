from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# will end up being total number of moves 
# traversal_path = ['n', 'n']
traversal_path = []

########################### START OF MY CODE ##################################

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


def bfs(current_room, visited):
      
        # queue to keep track of rooms to check out 
        queue = Queue()
    
        # enque current room - will need to leave this room off of final list 
        queue.enqueue([current_room])

        # while the queue is not empty:
        while queue.size() > 0: 
            # get the current vertex PATH (deque from queue)
            current_path = queue.dequeue()
            current_vertex = current_path[-1]

            # to keep track of unvisited directions of current_vertex
            unvisited_directions = []

            # loop through all the exits for the current room 
            for exit_direction in current_vertex.get_exits():
            # if the neighboring room in this direction (exit_direction) is not in visited, add that direction to unvisited_directions
                if current_vertex.get_room_in_direction(exit_direction) not in visited:
                    unvisited_directions.append(exit_direction)
            
            # if there are any moves to unvisited rooms 
            if len(unvisited_directions) > 0:
                # slicing off first room because that's where we already were 
                return current_path[1:] 

            # otherwise, there are still no moves to unvisited rooms, keep searching 
            else:
            # loop through the exit directions for the current_vertex (current_room) and tack the rooms at those directions on to the list of new paths 
                for exit_direction in current_vertex.get_exits():
                # Queue up NEW paths with each neighbor:
                    # append the neighbor to current path 
                    new_path = list(current_path)
                    new_path.append(current_vertex.get_room_in_direction(exit_direction))
                    # queue up NEW path    
                    queue.enqueue(new_path)


# dictionary for reverse directions 
reverse = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e',
}

def path_finder():
    # keeps track of the the step by step path we've made, allows us to backtrack when we hit a dead end 
    stack = Stack() 
    # keeps track of rooms that have been visited  
    visited = set()

    # loop until all rooms visited - stop once the number of total rooms is equal to the number of visited rooms 
    while len(visited) < len(world.rooms):

        # list to record unvisited directions from current room - possible moves to unvisited rooms 
        unvisited_directions = []

        # loop through all the exits for the current room 
        for exit_direction in player.current_room.get_exits():
            # if the neighboring room in this direction (exit_direction) is not in visited, add that direction to unvisited_directions
            if player.current_room.get_room_in_direction(exit_direction) not in visited:
                unvisited_directions.append(exit_direction)

        # add current room to visited 
        visited.add(player.current_room)

        # if there are possible moves to unvisited rooms 
        if len(unvisited_directions) > 0:
            # pick a random direction to go in 
            move = random.randint(0, len(unvisited_directions) - 1)
            # pushing chosen direction onto stack - comes into play for back tracking 
            stack.push(unvisited_directions[move])
            # actually move from current room to room at randomly chosen direction
            player.travel(unvisited_directions[move])
            # add to traversal_path - direction masterlist 
            traversal_path.append(unvisited_directions[move])

        # otherwise, there aren't any possible moves to unvisited rooms, we need to backtrack to most recent room with a possible move 
        else:
            # pop the last direction we took off the stack and store that value 
            last = stack.pop()
            # backtrack one move 
            player.travel(reverse[last])
            # add backtracking move to traversal_path - direction masterlist 
            traversal_path.append(reverse[last])
            
            # maybe more efficient alternative - send out the sonar for closest room with unexplored neighbors 

            # found path to closest room with an unexplored exit 
            # found_path = bfs(player.current_room, visited)
            # print(found_path[0])

            #  when this loop ends - the current room should be updated to a room with an unexplored exit - can restart with dft 
            # for room in found_path:
            #     # add room to visited rooms 
            #     visited.add(room)
            #     # print(visited)
            #     # loop through the exit directions of the current room 
            #     for exit_direction in player.current_room.get_exits():
            #         # if the room at this particular exit direction is the room in found path (room toward the closest unexplored room)
            #         if player.current_room.get_room_in_direction(exit_direction) == room:
            #             # add that direction to the traversal_path masterlist
            #             traversal_path.append(exit_direction)
            #             # make the player travel that way so current room is updated and loop can start over 
            #             player.travel(exit_direction)
            #             # print(player.current_room)
            

# call function to populate traversal_path 
path_finder()

########################### END OF MY CODE ##################################

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
