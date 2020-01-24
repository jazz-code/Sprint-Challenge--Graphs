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

# queue = Queue()

# while queue.size() > 0:
#     starting_room = player.current_room.id
# stack = stack()
# rooms = {}
# exits = {}
# traversal_path = []
# unexplored = []
# init_graph = {0: {'n': '?', 's': '?','w': '?','e': '?'}}
# reverse_directions = { 'n': "s", 's': 'n', 'e': 'w', 'w': 'e' }
# starting_room = player.current_room.id
# rooms[0] = player.current_room.get_exits()
# exits[0] = player.current_room.get_exits()
# while len(rooms) < len(room_graph) -1:
#     if starting_room not in rooms:
#         rooms[starting_room] = player.current_room.get_exits()
#         exits[starting_room] = player.current_room.get_exits()

#         unexplored = path[-1]
#         exits[starting_room].remove(unexplored)

#     while len(exits[starting_room]) < 1:
#         loop_path = unexplored.pop()
#         traversal_path.append(loop_path)
#         player.travel(loop_path)

#     # find first exit in the room
#     new_exit = exits[starting_room].pop(0)
#     traversal_path.append(new_exit)
#     # loop back to reverse direction 
#     unexplored.append(reverse_directions[new_exit])
#     player.travel(new_exit)

#     # to get last room
#     if len(room_graph) - len(rooms) == 1:
#         rooms[player.current_room.id] = player.current_room.getExits()

# def dfs(starting_room):
"""
Return a list containing a path from
starting_vertex to destination_vertex in
depth-first order.
"""
init_graph = {0: {'n': '?', 's': '?','w': '?','e': '?'}}
reverse_directions = { 'n': "s", 's': 'n', 'e': 'w', 'w': 'e' }
traversal_path = []
# stack = Stack()
visited_rooms = set()
# Put starting room on the stack
room_id = player.current_room.id

def bfs(starting_room, destination_room):
        """
        Return a list of direction to follow to get from
        starting room to destination room
        """
        queue = Queue()
        paths = []
        visited = set()
        queue.enqueue([starting_room])

        while queue.size() > 0:
            path = queue.dequeue()
            room = path[-1]
            if room not in visited:
                if room == destination_room:
                    return
                visited.add(room)

                for next_room in list(traversal_graph[room].values()):
                    if next_room != '?':
                        new_path = list(path)
                        new_path.append(next_room)
                        queue.enqueue(new_path)

        for i in range(len(path) - 1):
            for path, room in traversal_graph[path[i]]:
                if room == path[i+1]:
                    paths.append(path)

        return print(f"Paths: ",{paths})

# print(traversal_path)
# #       For each edge in the item
    # for next_room in sel 
    # # self.get_neighbors(vertex):
    # # Copy path to avoid pass by reference bug
    #     traversal_path = list(path) # Make a copy of path rather than reference
    #     traversal_path.append(next_room)
    #     stack.push(traversal_path)



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
