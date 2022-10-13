from Union_find import Set


def connected_components(graph):
    s = Set()
    for i in range(graph.m_num_of_nodes):
        s.make_set(i)
    for i in graph.get_edges():
        s.union(i[1], i[2])

    new_matrix_dim = len(s.set_list[0].elements)
    connected_components_list = s.set_list[0].elements

    new_adj_matrix = [[0 for column in range(new_matrix_dim)]
                      for row in range(new_matrix_dim)]
    for i in range(new_matrix_dim):
        for j in range(new_matrix_dim):
            new_adj_matrix[i][j] = graph.m_adj_matrix[connected_components_list[i]][connected_components_list[j]]

    graph.m_adj_matrix = new_adj_matrix
    graph.m_num_of_nodes = new_matrix_dim
    return graph

