graph = {
    'A':['B','C'],
    'B':['A','K'],
    'C':['A','D','F'],
    'D':['C','E','G','H'],
    'E':['D'],
    'F':['C','G','J'],
    'G':['D','F'],
    'H':['D','J'],
    'J':['F','H'],
    'K':['B']
}


def print_neighbours(node):
    print(graph[node])



print_neighbours('A')