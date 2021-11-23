from GraphAlg import GraphAlg

#Create the graph from this dictionary by generating nodes
unewighted_nums = {
    0 : [1,4],
    1 : [0,6],
    2 : [0,1,6],
    3 : [7],
    4 : [0,6],
    5 : [6,7],
    6 : [1,4,5],
    7 : [5,3]  
}
unewighted_chars = {
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}
weighted_nums = {
        1:{2:2.0, 5:5.0}, 
        2:{1:2.0, 3:2.0}, 
        3:{2:2.0, 4:2.0}, 
        4:{3:2.0, 7:1.0}, 
        5:{1:1.0, 6:4.0}, 
        6:{5:4.0, 7:1.0}, 
        7:{4:1.0, 6:1.0}
    }
mst = {1:[2, 5], 2:[1, 3], 3:[2, 4], 4:[3, 7], 5:[1], 6:[7], 7:[4, 6]}

#DFS Test
g = GraphAlg(data=unewighted_nums,dir=False)
traversal = g.DFS(2,[])
GraphAlg.draw_graph_traversal(g.G, False, traversal)
print(unewighted_nums)
print("DFS traversal from 2: " + str(traversal))

#BFS Test
g = GraphAlg(data=unewighted_chars,dir=True)
traversal = g.BFS("3",[])
GraphAlg.draw_graph_traversal(g.G, False, traversal)
print(unewighted_chars)
print("BFS traversal from \'3\': " + str(traversal))

#Draw Multiple Graphs
wg = GraphAlg(data=weighted_nums,dir=False)
mst_wg = GraphAlg(data=mst,dir=False)
GraphAlg.draw_graphs([wg.G,mst_wg.G],False,['pink','yellow'])
