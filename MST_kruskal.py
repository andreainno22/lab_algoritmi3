from Union_find import Set
from mergesort import merge_sort


def kruskal(g):
    a = []
    s = Set()
    for i in range(g.m_num_of_nodes):
        s.make_set(i)
    for i in merge_sort(g.get_edges()):
        if s.find_set(i[1]) != s.find_set(i[2]):
            a.append(i)
            s.union(i[1], i[2])
    return a
