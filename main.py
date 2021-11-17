from typing import Set
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import traversal
from networkx.classes.function import neighbors
from networkx.classes.graph import Graph
import matplotlib.animation as animation

def draw_graph(G,animate,visited):
    '''Draw the graph using matplotlib\n
    '''
    nx.draw_shell(G, node_color=['orange' if node in visited else 'pink' for node in G], with_labels=True)
    if animate:
        plt.show(block=False)
        plt.pause(0.25)
        plt.close()
    else:
        plt.show(block=True)
    


def DFS(G,source,visited):
    '''
        Depth first search\n
        Takes in a graph G\n
        A source Node\n
        And an empty list to which it will append the path taken and return
    '''
    if(source not in visited):
        visited.append(source)
        draw_graph(G,True,visited)
        neighbors = sorted(G.neighbors(source))
        for neighbor in neighbors:
            visited = DFS(G,neighbor,visited) #Recursion used as a stack
    return visited


def BFS(G,source,visited):
    queue = []
    queue.append(source)
    visited.append(source) #Visit source
    draw_graph(G,True,visited) #Draw graph after visiting

    while (len(queue) != 0):
        current = queue.pop(0) #Popping from the front makes this a queue
        for neighbor in sorted(G.neighbors(current)):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor) #Visit unvisited neighbor
                draw_graph(G,True,visited) #Draw graph after visiting
    return visited

if __name__ == '__main__':
    #Create the graph from this dictionary by generating nodes
    d1 = {
        0 : [1,4],
        1 : [0,6],
        2 : [0,1,6],
        3 : [7],
        4 : [0,6],
        5 : [6,7],
        6 : [1,4,5],
        7 : [5,3]  
    }
    d2 = {
        '5' : ['3','7'],
        '3' : ['2', '4'],
        '7' : ['8'],
        '2' : [],
        '4' : ['8'],
        '8' : []
    }
    
    #DFS Test
    G = nx.DiGraph(d2)
    traversal = DFS(G,'5',[])
    #draw_graph(G,False,traversal)
    print("DFS: " + traversal.__str__())

    #BFS Test
    G = nx.DiGraph(d1)
    traversal = BFS(G,2,[])
    #draw_graph(G,False,traversal)
    print("BFS: " + traversal.__str__())
    
