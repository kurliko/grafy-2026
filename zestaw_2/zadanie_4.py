import random
import sys

import matplotlib.pyplot as plt

from zestaw_1.graph import Graph
from zestaw_1.wypisywanie import print_adjacency_list
from zestaw_1.zadanie_2 import draw_graph
from zestaw_2.zadanie_1 import graph_from_degree_sequence
from zestaw_2.zadanie_2 import add_edge, randomize, remove_edge
from zestaw_2.zadanie_3 import components


def random_euler_graph(n):
    if n < 3:
        raise ValueError("n musi być co najmniej 3")
    max_degree = n - 1
    if max_degree % 2 == 1:
        max_degree = n - 2

    while True:
        degrees = []
        for _ in range(n):
            degrees.append(random.randrange(2, max_degree + 1, 2))
        g = graph_from_degree_sequence(degrees)
        if g is None:
            continue
        randomize(g, 100)

        connected = True
        for nr in components(g):
            if nr != 1:
                connected = False
        if connected:
            return g, degrees


def is_bridge(g, u, v):
    remove_edge(g, u, v)
    comp = components(g)
    add_edge(g, u, v)
    return comp[u] != comp[v]


def copy_graph(g):
    adjacency_list = []
    for neighbors in g.adjacency_list:
        adjacency_list.append(list(neighbors))
    return Graph(adjacency_list)


def euler_cycle(g):
    work = copy_graph(g)
    u = 0
    cycle = [u]
    while len(work.adjacency_list[u]) > 0:
        next_vertex = work.adjacency_list[u][0]
        if len(work.adjacency_list[u]) > 1:
            for v in list(work.adjacency_list[u]):
                if not is_bridge(work, u, v):
                    next_vertex = v
                    break
        remove_edge(work, u, next_vertex)
        cycle.append(next_vertex)
        u = next_vertex
    return cycle


def format_path(path):
    text = "[" + str(path[0] + 1)
    for v in path[1:]:
        text = text + " - " + str(v + 1)
    return text + "]"


# losuje graf eulerowski, wypisuje go razem z cyklem Eulera i rysuje 
def main():
    if len(sys.argv) > 2:
        sys.exit("Podaj jeden argument: liczbę wierzchołków n.")
    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
        except ValueError as error:
            sys.exit(str(error))
    else:
        n = random.randint(5, 10)

    try:
        g, degrees = random_euler_graph(n)
    except ValueError as error:
        sys.exit(str(error))

    print(f"n = {n}")
    print(f"Wylosowane stopnie: {degrees}")
    print("Lista sąsiedztwa:")
    print_adjacency_list(g)
    print(f"Cykl Eulera: {format_path(euler_cycle(g))}")
    draw_graph(g)
    plt.show()


if __name__ == "__main__":
    main()
