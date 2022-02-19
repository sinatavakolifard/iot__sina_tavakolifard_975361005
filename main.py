from node import node
from random import randint

# ex1 part1
nodes = []
for id in range(1, 21):
    nodes.append(node(id, randint(0, 100), randint(0, 100)))


# ex1 part2
for i in range((len(nodes))):
    temp_nodes = nodes[:]
    del temp_nodes[i]
    
    j = 0
    while j < 6:
        id = randint(0, 18)
        # print(id)
        if temp_nodes[id] not in nodes[i].neighbor_nodes:
            nodes[i].neighbor_nodes.append(temp_nodes[id])
            j += 1

