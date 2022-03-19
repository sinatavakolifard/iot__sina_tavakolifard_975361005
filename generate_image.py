from node import node
from random import randint
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from PIL import Image

def imageToRGB(imageAddress):
    img = Image.open(imageAddress)
    arr = np.array(img)
    return list(arr)

def setNeighborsToNodes(nodes, pixelNumbers):
    while True:
        try:
            neighborNumbers = int(input("How many neighbors each node can have? "))
            if neighborNumbers < 0 or neighborNumbers > pixelNumbers-1:
                print("It shoud be from 1 to " + str(pixelNumbers-1) + "!")
            else:
                break
        except:
            print("It shoud be a number!")

    tempNodes = nodes[1:]
    fatherNodeIds = [0]
    childNodeIds = []
    while len(tempNodes) > 0:
        for i in range(neighborNumbers):
            if len(tempNodes) > 0:
                randomNodeIndex = randint(0, len(tempNodes)-1)
                randomNode = tempNodes[randomNodeIndex]
                del tempNodes[randomNodeIndex]

                insertNeigbour(nodes, fatherNodeIds[0], randomNode)
                childNodeIds.append(randomNode.id)

        del fatherNodeIds[0]
        if len(fatherNodeIds) == 0:
            fatherNodeIds = childNodeIds[:]
            childNodeIds = []

def insertNeigbour(nodes, fatherNodeId, childNode):
    nodes[fatherNodeId].neighbor_nodes.append(childNode)

def printNodesInTerminal(nodes):
    for node in nodes:
        print("node id:", str(node.id) +",  X:", str(node.X) + ", Y:", node.Y, end=" ")

        try:
            print("- neighbour nodes:", node.neighbor_nodes[0].id, end=" ")
            i = 1
            while True:
                print(node.neighbor_nodes[i].id, end=" ")
                i += 1
        except:
            print()
    
def show_graph_of_nodes(nodes, imageRGB):
    pixelNumbers = len(imageRGB) * len(imageRGB[0])
    pixelNumbersY = len(imageRGB)
    pixelNumbersX = len(imageRGB[0])

    G = nx.Graph()
    edges = []
    pos = {}

    for node in nodes:
        G.add_node(node.id)

    for node in nodes:
        pos[node.id] = (node.X, -1* node.Y)
        for neighbor in node.neighbor_nodes:
            edges.append((node.id, neighbor.id))

    G.add_edges_from(edges)
    
    colors = ["white"] * pixelNumbers
    edge_colors = ["white"] * pixelNumbers

    setColorToNode(nodes[0], imageRGB, colors)       

    nx.draw_networkx(G, pos, node_color=colors, edge_color=edge_colors, node_size=40, with_labels = False)
    plt.title('Graph of nodes (' + str(pixelNumbersX) + " x " + str(pixelNumbersY) + ")")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def setColorToNode(destinationNode, imageRGB, colors):
    y = destinationNode.id // len(imageRGB)
    x = destinationNode.id % len(imageRGB)
    rgb = imageRGB[y][x]
    colors[destinationNode.id] = (rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)

    for neighbor in destinationNode.neighbor_nodes:
        setColorToNode(neighbor, imageRGB, colors)

imageAddress = input("Enter image address: ")
imageRGB = imageToRGB(imageAddress)
pixelNumbers = len(imageRGB) * len(imageRGB[0])

nodes = []
for id in range(0, pixelNumbers):
    x = id % len(imageRGB[0])
    y = id // len(imageRGB)
    nodes.append(node(id, x, y))


setNeighborsToNodes(nodes, pixelNumbers)
printNodesInTerminal(nodes)
show_graph_of_nodes(nodes, imageRGB)