''' Your task is to determine if two nodes are adjacent in a graph when 
    given the adjacency matrix and the two nodes.'''

def is_adjacent(matrix, node1, node2):
    return matrix([node1][node2]) == 0


matrix = [[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]]
# print(is_adjacent(matrix, 0, 1))
# print(is_adjacent(matrix, 0, 2))
print(is_adjacent(matrix, 2, 1))