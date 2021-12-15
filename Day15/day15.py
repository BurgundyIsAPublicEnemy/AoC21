import numpy as np 
from networkx import grid_2d_graph, shortest_path_length, DiGraph
from itertools import product

matrix = np.loadtxt('output')

def find_shortest_path_distance(weights, source):
    G = grid_2d_graph(len(weights), len(weights), create_using=DiGraph)
    for u, v in G.edges:
        G[u][v]["weights"] = weights[v[1]][v[0]]
    print(shortest_path_length(G, source, (len(weights)-1,len(weights)-1), "weights"))

find_shortest_path_distance(matrix, (0,0))

bigboymatrix = np.zeros((matrix.shape[0] * 5, matrix.shape[1] * 5))

for x, y in product(range(matrix.shape[0] * 5), range(matrix.shape[1] * 5)):
    '''
        get corresponding matrix entry
        add it by what grid we are supposed to be on
    '''
    bigboymatrix[x][y] = matrix[y % len(matrix)][x % len(matrix)] + int(x /len(matrix)) + int ( y /len(matrix))

bigboymatrix[bigboymatrix > 9] -= 9
find_shortest_path_distance(bigboymatrix, (0,0))