from timeit import default_timer as timer
import numpy as np
from MST_kruskal import kruskal
from MST_prim import prim
from random_graph import random_graph
import matplotlib.pyplot as plt


def main():
    # genera un grafo connesso con al massimo 15 nodi, con una probabilità crescente che vi sia un arco fra 2 nodi
    exe_times_k = []
    exe_times_p = []
    seq = np.arange(0, 1, 0.1)
    for i in range(10, 80, 5):
        for j in seq:
            graph = random_graph(i, j)
            start = timer()
            kruskal(graph)
            end = timer()
            exe_times_k.append(end - start)
            start = timer()
            prim(graph)
            end = timer()
            exe_times_p.append(end - start)
            # graph.print_adj_matrix()
    x = np.arange(10, 80, 5)
    xx = np.tile(x, 10)
    #print(xx)
    y = exe_times_k
    z = np.arange(0, 1, 0.1)
    zz = np.tile(z, 14)
    plt.plot(xx, y, zz, marker="o", color='red')
    plt.show()
    # plt.xlabel = "n nodi"
    # plt.ylabel = "t exe"

    """z = np.arange(10, 80, 5)
    t = exe_times_p
    w = np.arange(0, 1, 0.1)
    plt.plot(z, t, w, marker="o", color='blue')
    plt.show()"""

    # esegue l'algoritmo kruskal, che calcola l'MST di graph e stampa
    """start = timer()
    MST_kruskal = kruskal(graph)
    end = timer()

    print("\nkruskal: ", MST_kruskal, "\ntempo di esecuzione: ", end - start)

    # esegue l'algoritmo prim, che calcolo l'MST di graph e stampa
    start = timer()
    MST_prim = prim(graph)
    end = timer()
    print("\nprim: ", MST_prim, "\ntempo di esecuzione: ", end - start)"""


if __name__ == "__main__":
    main()
