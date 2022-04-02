from node import node
from random import randint
import matplotlib.pyplot as plt
import networkx as nx

def generateNodes(nodes):
    n = int(input("Enter number of nodes: "))
    m = int(input("Enter number of neighbors for each node: "))

    for id in range(0, n):
        nodes.append(node(id, randint(0, 100), randint(0, 100)))

    for i in range(len(nodes)):
        temp_nodes = nodes[:]
        del temp_nodes[i]

        while len(nodes[i].neighbor_nodes) < m:
            id = randint(0, len(temp_nodes)-1)
            # if temp_nodes[id] not in nodes[i].neighbor_nodes and len(nodes[temp_nodes[id].id].neighbor_nodes) < m:
            if not any(d['name'] == temp_nodes[id] for d in nodes[i].neighbor_nodes):
                distance = randint(1, 25)
                nodes[i].neighbor_nodes.append({"name":temp_nodes[id], "distance":distance})
                nodes[temp_nodes[id].id].neighbor_nodes.append({"name":nodes[i], "distance":distance})

def printNodes(nodes):
    for node in nodes:
        print("node id:", str(node.id) +",  X:", str(node.X) + ", Y:", node.Y, end=" ")

        try:
            print("- neighbour nodes:", node.neighbor_nodes[0]["name"].id, end=" ")
            i = 1
            while True:
                print(node.neighbor_nodes[i]["name"].id, end=" ")
                i += 1
        except:
            print()

def DVRStep1(nodes):
    print("\nRouting tables at first:")
    for node in nodes:
        for i in range(len(nodes)):
            if i == node.id:
                node.routing_table[i] = (0, i)
            else:
                for neighborDict in node.neighbor_nodes:
                    if neighborDict["name"].id == i:
                        node.routing_table[i] = (neighborDict["distance"], i)
                        break
                    node.routing_table[i] = (10000000, "-")
        print(node.id)
        print(node.routing_table)
    print()

def DVRStep2(nodes):
    # Do everthing up to node lengths - 2
    for i in range(len(nodes) - 2):

        # sending routing_tables to neighbors.
        for node in nodes:
            for neighbor in node.neighbor_nodes:
                node.neighbor_tables[neighbor["name"].id] = nodes[neighbor["name"].id].routing_table.copy()

        # updating routing_tables based on neighbours' routing_tables
        for node in nodes:
            temp_routing_table = node.routing_table.copy()
            for destination in nodes:
                routes = []
                if node.id != destination.id:
                    routes.append(temp_routing_table[destination.id])
                    for (neighbourId, neighbour_table) in node.neighbor_tables.items():
                        if neighbourId != destination.id:
                            routes.append((temp_routing_table[neighbourId][0] + neighbour_table[destination.id][0] , neighbourId))
                    minLength = 10000000
                    nextHop = "-"
                    for route in routes:
                        if route[0] < minLength:
                            minLength = route[0]
                            nextHop = route[1]
                    if node.routing_table[destination.id][1] != destination.id and node.routing_table[destination.id][1] != "-":
                        nextHop = node.routing_table[destination.id][1]
                    node.routing_table[destination.id] = (minLength, nextHop)
                # print("Routes to " + str(destination.id) + ":", end=" ")
                # print(routes)

    print("Routing tables at last:")
    for node in nodes:
        print(node.id)
        print(node.routing_table)

def show_graph_of_nodes(nodes):
    G = nx.Graph()
    # pos = {}

    for node in nodes:
        G.add_node(node.id)

    for node in nodes:
        # pos[node.id] = (node.X, node.Y)
        for neighborDict in node.neighbor_nodes:
            G.add_edge(node.id, neighborDict["name"].id, title=neighborDict["distance"])

    edge_labels = nx.get_edge_attributes(G, 'title') 

    # set nodes' position automatically to circular form.
    pos = nx.circular_layout(G, scale=2, center=None, dim=2)
    
    nx.draw_networkx(G, pos, with_labels = True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title('Graph of nodes')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

nodes = []
generateNodes(nodes)
printNodes(nodes)
DVRStep1(nodes)
DVRStep2(nodes)
show_graph_of_nodes(nodes)
