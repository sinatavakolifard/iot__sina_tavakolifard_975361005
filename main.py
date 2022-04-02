from node import node
from random import randint
import matplotlib.pyplot as plt
import networkx as nx

nodes = []
for id in range(1, 21):
    nodes.append(node(id, randint(0, 100), randint(0, 100)))

for i in range((len(nodes))):
    temp_nodes = nodes[:]
    del temp_nodes[i]
    
    j = 0
    while j < 6:
        id = randint(0, 18)
        if temp_nodes[id] not in nodes[i].neighbor_nodes:
            nodes[i].neighbor_nodes.append(temp_nodes[id])
            j += 1

for node in nodes:
    print("node id:", str(node.id) +", X:", str(node.X) + ", Y:", node.Y,"- neighbour nodes: ", node.neighbor_nodes[0].id, node.neighbor_nodes[1].id, node.neighbor_nodes[2].id, node.neighbor_nodes[3].id, node.neighbor_nodes[4].id, node.neighbor_nodes[5].id)

def show_graph_of_nodes(nodes):
        G = nx.DiGraph()
        edges = []
        pos = {}
        for node in nodes:
            pos[node.id] = (node.X, node.Y)
            for i in range(6):
                edges.append((node.id, node.neighbor_nodes[i].id))
        G.add_edges_from(edges)
        nx.draw_networkx(G, pos)

        plt.title('Graph of nodes')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.ylim(-5,105)
        plt.xlim(-5,105)
        plt.show()

def find_path_between_2_nodes(nodes):
    node1 = 1
    node2 = 1

    while True:
        try:
            node1 = int(input("Enter id of first node (1-20): "))
            if node1 < 1 or node1 > 20:
                print("Entered id should be a number from 1 to 20!")
            else:
                break
        except:
            print("Entered id should be a number!")

    while True:
        try:
            node2 = int(input("Enter id of second node (1-20): "))
            if node2 < 1 or node2 > 20:
                print("Entered id should be a number from 1 to 20!")
            elif node2 == node1:
                print("Second node should be different from first node!")
            else:
                break
        except:
            print("Entered id should be a number!")
    
    paths = []
    visited_nodes = [node1]
    current_path = [node1]
    find_paths(node1, node2, nodes, visited_nodes, paths, current_path)

    print()
    if len(paths[0]) == 2:
        print("It has direct path.")
    else:
        print("It doesn't have direct path.")

    if (len(paths) > 1 and len(paths[0]) == 2) or (len(paths) > 0 and len(paths[0]) != 2):
        print("It has indirect path.")
    else:
        print("It doesn't have indirect path.")
    
    print()
    
    for i in range(len(paths)):
        print("Path " + str(i+1) + ": " + " ".join(str(x) for x in paths[i]))

    print()
    print("Nearest path: " + " ".join(str(x) for x in paths[0]))
    print()

    wanna_see = input("Wanna see results on graph? (y, n): ")
    if wanna_see == "y":
        see_paths(paths, nodes)


def find_paths(node1, node2, nodes, visited_nodes, paths, current_path):
    neighbor_ids = []
    for neighbor in nodes[node1-1].neighbor_nodes:
        neighbor_ids.append(neighbor.id)
    if set(neighbor_ids).issubset(visited_nodes):
        return
    elif nodes[node2-1] in nodes[node1-1].neighbor_nodes:
        paths.append(current_path[:] + [node2])
    for i in range(len(nodes[node1-1].neighbor_nodes)):
        neighbor_node = nodes[node1-1].neighbor_nodes[i]
        if neighbor_node.id != node2 and neighbor_node.id not in visited_nodes:
            visited_nodes.append(neighbor_node.id)
            find_paths(neighbor_node.id, node2, nodes, visited_nodes, paths, current_path[:] + [neighbor_node.id])
    
def see_paths(paths, nodes):
    for path_index in range(len(paths)):
        G = nx.DiGraph()
        pos = {}
        for node in nodes:
            G.add_node(node.id)
        
        for node in nodes:
            pos[node.id] = (node.X, node.Y)
        
        edges = []
        for j in range(len(paths[path_index])-1):
            edges.append((paths[path_index][j], paths[path_index][j+1]))

        G.add_edges_from(edges)
        nx.draw_networkx(G, pos)
        plt.title('Path ' + str(path_index+1))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.ylim(-5,105)
        plt.xlim(-5,105)
        plt.show()

while True:
    print("-------------------------------")
    print("Enter one of the options:")
    print("1- See graph")
    print("2- Find path between 2 nodes")
    print("3- Exit")
    choice = input()
    if choice == "1":
        show_graph_of_nodes(nodes)
        wanna_continue = input("Wanna continue? (y, n): ")
        if wanna_continue != "y":
            break
    elif choice == "2":
        find_path_between_2_nodes(nodes)
        wanna_continue = input("Wanna continue? (y, n): ")
        if wanna_continue != "y":
            break
    else:
        break

