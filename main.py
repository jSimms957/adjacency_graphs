#from stack import stack
from queue import ListQueue


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



# Breadth first traversal
#-----------------------------
queue_obj = ListQueue()

current_node = 'J'
visited_nodes = [current_node]

# adds starting node to the queue
queue_obj.enqueue(current_node)



# loop continues until queue is empty
while queue_obj.get_size() > 0:
    # empties the queue
    current_node = queue_obj.dequeue()

    # loop through all current node neighbours
    for neighbour in sorted(graph[current_node]):
        # if neighbour hasn't been visited add it to queue
        if neighbour not in visited_nodes:
            visited_nodes.append(neighbour)
            queue_obj.enqueue(neighbour)


print(visited_nodes)










# stack_obj = stack()
#
# current_node = 'J'
# visited_nodes = [current_node]
#
# stack_obj.push(current_node)



# # loop continues until stack is empty
# while stack_obj.get_size() > 0:
#     # temporary node to save the current node
#     temp_current = current_node
#
#
#     # loop through all current node neighbours
#     for neighbour in sorted(graph[current_node]):
#         # if neighbour hasn't been visited, set current node to the neighbour, push it to the
#         #the stack, append it to visited list, and break loop
#         if neighbour not in visited_nodes:
#             current_node = neighbour
#             stack_obj.push(current_node)
#             visited_nodes.append(current_node)
#             break
#
#
#     # after loop has exited, if there has been no change to the current node (no unvisited
#     #neighbour found) pop the stack and set current node to be the returned node
#     if temp_current == current_node:
#         current_node = stack_obj.pop()
#
# print(visited_nodes)








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