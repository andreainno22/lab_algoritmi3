from random import random, randint
from Graph import Graph
from connected_components import connected_components


def random_graph(n, p):
    g = Graph(n)
    for u in range(0, n):
        for v in range(u, n):
            x = random()
            if 0 < x <= p:
                a = randint(1, 20)
                g.add_edge(u, v, a)
                g.add_edge(v, u, a)
    g = connected_components(g)
    return g
