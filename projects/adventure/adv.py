from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

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

def opposite(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'w':
        return 'e'
    else:
        return 'w'

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
traversal_graph = {
    0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}


while len(traversal_graph) < len(room_graph):

    if '?' in traversal_graph[player.current_room.id].values():        
        valid_directions = []

        for x in player.current_room.get_exits():
            if traversal_graph[player.current_room.id][x] == '?':
                valid_directions.append(x)

        direction = random.choice(valid_directions)
        prev_room = player.current_room
        
        player.travel(direction)

        traversal_graph[prev_room.id][direction] = player.current_room.id
        if player.current_room.id not in traversal_graph:
            traversal_graph[player.current_room.id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
        traversal_graph[player.current_room.id][opposite(direction)] = prev_room.id
        traversal_path.append(direction)
    
    else:
        queue = Queue()
        path = [player.current_room.id]
        queue.enqueue(path)

        visited = set()

        while queue.size() > 0:
            path = queue.dequeue()
            current_room = path[-1]

            if current_room not in visited:
                visited.add(current_room)
                # print(current_room)

                if '?' in traversal_graph[current_room].values():
                    for room in range(len(path) - 1):
                        direction = ''
                        for key, value in traversal_graph[path[room]].items():
                            if value == path[room + 1]:                                
                                direction = key
                        player.travel(direction)
                        traversal_path.append(direction)
                    break
                
                else:
                    for exit in traversal_graph[current_room].values():                        
                        if exit is not None:
                            new_path = list(path)
                            new_path.append(exit)
                            queue.enqueue(new_path)




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
