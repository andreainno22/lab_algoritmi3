from cmath import inf
from random import randint
from Heap import Heap


class Vertex:
    def __init__(self, node, key, pi):
        self.node = node
        self.key = key
        self.pi = pi


def prim(graph):
    a = []
    q = Heap(a)
    u_list = []
    for i in range(graph.m_num_of_nodes):
        q.min_heap_insert(Vertex(i, inf, None))
    q.heap_decrease_key(randint(0, graph.m_num_of_nodes - 1), 0)

    while q.size != 0:

        # estrae il vertex con la key più piccola
        u = q.heap_extract_min()
        u_list.append(u)

        # itera su tutti i nodi
        adj_u = graph.adj(u.node)
        for v in adj_u:
            v_index_in_heap = q.find_node(v)
            w_uv = graph.m_adj_matrix[u.node][v]

            # se il peso dell'arco (u,v) è minore della chiave di u e maggiore di 0 (altrimenti l'arco non esiste)
            if type(v_index_in_heap) == int:
                if w_uv < q.heap[v_index_in_heap].key:
                    q.heap[v_index_in_heap].pi = u.node
                    q.heap_decrease_key(v_index_in_heap, w_uv)

    MST_prim = []
    u_list = u_list[1:len(u_list)]

    for i in u_list:
        MST_prim.append([i.key, i.node, i.pi])
    return MST_prim
