import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph
import matplotlib.animation as animation

class GraphAlg:
    def __init__(self,data:dict,dir:bool) -> None:
        self.G = nx.DiGraph(data) if dir else nx.Graph(data)
    @staticmethod
    def draw_graphs(graphs,animate,colors):
        '''Draw multiple graphs\n
        '''
        for i,G in enumerate(graphs):
            plt.figure(i)
            nx.draw_shell(G, node_color=colors[i], with_labels=True)
        if animate:
            plt.show(block=False)
            plt.pause(0.25)
            plt.close()
        else:
            plt.show(block=True)

    @staticmethod
    def draw_graph(G,color):
        nx.draw_shell(G, node_color=color, with_labels=True)
        plt.show(block=True)

    @staticmethod
    def draw_graph_traversal(G,animate,visited):
        '''Draw the graph using matplotlib\n
        '''
        nx.draw_shell(G, node_color=['orange' if node in visited else 'pink' for node in G], with_labels=True)
        if animate:
            plt.show(block=False)
            plt.pause(0.25)
            plt.close()
        else:
            plt.show(block=True)

    
    def DFS(self,source,visited):
        '''
            Depth first search\n
            Takes in a graph G\n
            A source Node\n
            And an empty list to which it will append the path taken and return
        ''' 
        if(source not in visited):
            visited.append(source)
            GraphAlg.draw_graph_traversal(self.G,True,visited)
            neighbors = sorted(self.G.neighbors(source))
            for neighbor in neighbors:
                visited = self.DFS(neighbor,visited) #Recursion used as a stack
        return visited

    
    def BFS(self,source,visited):
        
        queue = []
        queue.append(source)
        visited.append(source) #Visit source
        GraphAlg.draw_graph_traversal(self.G,True,visited) #Draw graph after visiting

        while (len(queue) != 0):
            current = queue.pop(0) #Popping from the front makes this a queue
            for neighbor in sorted(self.G.neighbors(current)):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.append(neighbor) #Visit unvisited neighbor
                    GraphAlg.draw_graph_traversal(self.G,True,visited) #Draw graph after visiting
        return visited

    
    
    
