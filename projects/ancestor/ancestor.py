from util import Stack, Queue  



def earliest_ancestor(ancestors, starting_node):
    
    graph = get_graph(ancestors)

    # s = Stack()
    # s.push([starting_node])

    # visited = set()

    # while s.size() > 0:
    #     path = s.pop()
    #     last_vertex = path[-1]
    #     if last_vertex not in visited:
    #         if last_vertex == destination_vertex:
    #             return path
    #         visited.add(last_vertex)
          
    #         for n in self.get_neighbors(last_vertex):
    #             new_path = list(path)  # copy the list
    #             new_path.append(n)
    #             s.push(new_path)
    
    # return -1


def get_graph(ancestors):
    graph = {}
    for parent, child in ancestors:
        if child not in graph:
            graph[child] = []
        graph[child].append(parent)

    print(graph)
    return graph


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6),
                  (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# get_graph(test_ancestors)
print(earliest_ancestor(test_ancestors, 6))
