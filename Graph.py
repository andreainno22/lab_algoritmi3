class Graph:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)]
                             for row in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight=1):
        if node1 != node2:
            self.m_adj_matrix[node1][node2] = weight
            self.m_adj_matrix[node2][node1] = weight

    def get_edges(self):
        edges = []
        for i in range(0, self.m_num_of_nodes):
            for j in range(0, self.m_num_of_nodes):
                if self.m_adj_matrix[i][j] != 0:
                    edges.append([self.m_adj_matrix[i][j], i, j])
        return edges

    def adj(self, node):
        adj_nodes = []
        for i in range(self.m_num_of_nodes):
            adj_node = self.m_adj_matrix[node][i]
            if adj_node != 0:
                adj_nodes.append(i)
        return adj_nodes

    def print_adj_matrix(self):
        print("grafo: ", self.m_adj_matrix)








