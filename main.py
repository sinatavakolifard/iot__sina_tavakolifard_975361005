from node import node
from random import randint

# ex1 part1
nodes = []
for id in range(1, 21):
    nodes.append(node(id, randint(0, 100), randint(0, 100)))
