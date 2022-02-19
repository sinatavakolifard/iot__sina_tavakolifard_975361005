from node import node
from random import randint
import matplotlib.pyplot as plt

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

# ex1 part3
x = []
y = []

for node in nodes:
    for neighbor in node.neighbor_nodes:
        x.append(node.X)
        y.append(node.Y)

        x.append(neighbor.X)
        y.append(neighbor.Y)
 
plt.plot(x, y, color='blue', markerfacecolor='red', marker='o', linewidth = 0.4)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(0,100)
plt.xlim(0,100)
plt.title('Graph of nodes')
plt.show()