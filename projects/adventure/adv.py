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
# traversal_path = ['n', 'n']

# Initialise vert stack
traversal_path = [n, n, s, w,]
print(traversal_path)
visited_rooms = []

def add_to_map(direction, map):
    player.travel(direction)
    map += [player.current_room.id]
    for e in player.current_room.get_exits():
        if e.id == map[-2]:
            continue
        else:
            addendum = add_to_map(e.id, map)
            if(len(map + addendum) == 500):
                return map + addendum

final_map = add_to_map(player.current_room, [])
        



'Psuedocode'
# Get current room , if none , set to 0 , if 0 add to stack
def travel_directions():
    return player.current_room.id
'Current room is already 0 so add 0 to stack'
if player.current_room.id == 0:
    visited_rooms.append(player.current_room.id)
    print('visited: ', visited_rooms)
    
# Create list of verts adjacents(room exits)
# Add unvisited verts to top of a stack
# Move either n, s, e or w
# Log exit(vert) visited(put visited vert in a stack(visited list))
# move to any adjacent unvisited vert
# if cannot move further , backtrack and pick another unvisited vert
# repeat until all verts visited
travel_directions()

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
'''
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
'''
