from stack import stack


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


stack_obj = stack()

current_node = 'J'
visited_nodes = [current_node]

stack_obj.push(current_node)



while





# def print_neighbours(node):
#     print(graph[node])
#
#
# def check_if_connected(node1, node2):
#     if node1 in graph[node2]:
#         print(True)
#     else:
#         print(False)
#
#
#
# print_neighbours('A')
# check_if_connected('A', 'B')