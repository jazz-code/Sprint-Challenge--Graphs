from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

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

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
# print("id", player.current_room.id)                        # output = id 0
# print("room, get exits ", player.current_room.get_exits()) # output = ['n']
# print("travel direction",  player.travel('n'))             # output =
# print("id", player.current_room.id)                        # output = id 1
# print("room, get exits ", player.current_room.get_exits()) # output = ['n', 's']

# # Fill this out with directions to walk
# # traversal_path = ['n', 'n']
# traversal_path = []



# # TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

# def dfs(starting_room):
"""
Return a list containing a path from
starting_vertex to destination_vertex in
depth-first order.
"""
traversal_path = []
stack = Stack()
visited_rooms = set()
# print(player.current_room.id)
# player.current_room = starting_room
# Put starting room on the stack
# TODO implement random direction
stack.push(player.current_room.get_exits())
# While stuff in stack
while stack.size() > 0:
#   Pop the first item
    path = stack.pop()
    room = path[-1]
#    If not visited
    if room not in visited_rooms:
        visited_rooms.add(room)
        traversal_path.append(visited_rooms)
        print("test",list(traversal_path))
print(traversal_path)
# #       For each edge in the item
#     for next_room in sel 
#     # self.get_neighbors(vertex):
#     # Copy path to avoid pass by reference bug
#         traversal_path = list(path) # Make a copy of path rather than reference
#         traversal_path.append(next_room)
#         stack.push(traversal_path)



# visited_rooms.add(player.current_room) ????

# print("id", player.current_room.id)                        # output = id 0
# print("room, get exits ", player.current_room.get_exits()) # output = ['n']
# print("travel direction",  player.travel('n'))             # output =
# print("id", player.current_room.id)                        # output = id 1
# print("room, get exits ", player.current_room.get_exits()) # output = ['n', 's']

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# traversal_path = []

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

#### Plan ####

# Find Random unexplored direction from the player's current room

# Travels and logs that direction

# Hit dead-end collision (already explored path)

# Loops back to nearest room with unexplored path

# BFS shortest path
def dfs(self, starting_room, destination_vertex):
    """
    Return a list containing a path from
    starting_vertex to destination_vertex in
    depth-first order.
    """
    stack = Stack()
    visited_rooms = set()
    player.current_room = starting_room
    # Put starting room on the stack
    # TODO implement random room
    stack.push(starting_room)
    # While stuff in stack
    while stack.size() > 0:
    #   Pop the first item
        path = stack.pop()
        room = path[-1]
    #    If not visited
        if room not in visited_rooms:
            if room == destination_vertex:
                # Do the thing!
                return path
            visited_rooms.add(room)
    # visited_rooms.add(player.current_room) ????
#       For each edge in the item
        for next_vert in self.get_neighbors(vertex):
        # Copy path to avoid pass by reference bug
            new_path = list(path) # Make a copy of path rather than reference
            new_path.append(next_vert)
            stack.push(new_path)


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
