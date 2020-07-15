from util import Stack  

def earliest_ancestor(ancestors, starting_node):
    
    graph = get_graph(ancestors)

    s = Stack()
    s.push([starting_node])

    # keep track of [distance, node]
    earliest_node = [1, -1]

    while s.size() > 0:
        # print("stack", s)
        path = s.pop()
        last_node = path[-1]
        print("path", path)
        # print("ln", last_node)

        # the eldest nodes (nodes at top of graph)
        # are not in the dictionary, and are the end of the path
        if last_node not in graph:
            # check if path is longest and update our earliest_node tracker
            if len(path) > earliest_node[0]:
                earliest_node = [len(path), last_node]
            # "If there is more than one ancestor tied for "earliest", 
            # return the one with the lowest numeric ID."
            if len(path) == earliest_node[0] and last_node < earliest_node[1]:
                earliest_node = [len(path), last_node]
                # print("en", earliest_node)
        else:
            for n in graph[last_node]:
                s.push(path + [n])

    
    return earliest_node[1] 


def get_graph(ancestors):
    graph = {}
    for parent, child in ancestors:
        if child not in graph:
            graph[child] = []
        graph[child].append(parent)

    # print(graph)
    return graph

if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6),
                      (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    test2_ancestors = [(2, 3), (1, 3), (3, 6), (5, 6),
                      (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    # get_graph(test_ancestors)
    # {3: [1, 2], 6: [3, 5], 7: [5], 5: [4], 8: [4, 11], 9: [8], 1: [10]}
    print(earliest_ancestor(test_ancestors, 6))
    # print(earliest_ancestor(test2_ancestors, 6))


"""
Mando's recursive solution
def earliest_ancestor(ancestors, starting_node):
    # create a dictionary with earliest ancestor/ set key to depth and value to idx
    ancestor_history = {}
    # graph representation
    ancestor_adjacency = {}
    # loop through ancestors and store in dictionary with key being ancestor[1] and val being ancestor[0] 
    for ancestor in ancestors:
        if ancestor[1] not in ancestor_adjacency:
            ancestor_adjacency[ancestor[1]] = set()
        ancestor_adjacency[ancestor[1]].add(ancestor[0])
    # if starting node is not in ancestor_adjacency the node has no ancestors  
    if starting_node not in ancestor_adjacency:
        return -1
    # create helper function
    def earliest_ancestor_helper(current_vertex, count = 0):
        # base case - starting node is not in ancestor_adjacency list 
        if current_vertex not in ancestor_adjacency: 
                #if count is already in dictionary compare value and use lower value
                if count in ancestor_history:
                    ancestor_history[count] = ancestor_history[count] if ancestor_history[count] > current_vertex else current_vertex
                # else add to dictionary with count set as key and current vertex as value
                else:
                    ancestor_history[count] = current_vertex
                return
        # iterate through and recursively call on the current vertex ancestors
        for ancestor in ancestor_adjacency[current_vertex]:
            count += 1
            earliest_ancestor_helper(ancestor, count)
    earliest_ancestor_helper(starting_node)
    return ancestor_history[max(ancestor_history)]
"""