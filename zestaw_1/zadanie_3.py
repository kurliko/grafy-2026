import random
import sys

import matplotlib.pyplot as plt

from zestaw_1.graph import Graph
from zestaw_1.zadanie_2 import draw_graph


def possible_edges(n):
    if n < 0:
        raise ValueError("n nie może być ujemne")
    edges = []
    for u in range(n):
        for v in range(u + 1, n):
            edges.append((u, v))
    return edges


# krawędzie -> lista sąsiedztwa
def graph_from_edges(n, edges):
    adjacency_list = []
    for _ in range(n):
        adjacency_list.append([])
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    return Graph(adjacency_list)


# G(n, l): dokładnie l krawędzi wybranych losowo
def random_gnl(n, l):
    edges = possible_edges(n)
    if not 0 <= l <= len(edges):
        raise ValueError(f"l musi być od 0 do {len(edges)}")
    # sorted: sąsiedzi na liście rosnąco
    return graph_from_edges(n, sorted(random.sample(edges, l)))


# G(n, p): każda krawędź osobno, z prawdopodobieństwem p
def random_gnp(n, p):
    if not 0 <= p <= 1:
        raise ValueError("p musi być od 0 do 1")
    edges = []
    for edge in possible_edges(n):
        if random.random() < p:
            edges.append(edge)
    return graph_from_edges(n, edges)


# losuje graf, wypisuje jego listę sąsiedztwa i pokazuje go w oknie
# np. python -m zestaw_1.zadanie_3 gnl 6 7
# albo python -m zestaw_1.zadanie_3 gnp 6 0.5
def main():
    if len(sys.argv) != 4:
        sys.exit("Podaj trzy argumenty: model (gnl albo gnp), n oraz l (dla gnl) albo p (dla gnp).")

    model = sys.argv[1]
    if model != "gnl" and model != "gnp":
        sys.exit("Model musi być gnl albo gnp.")

    try:
        n = int(sys.argv[2])
        if model == "gnl":
            g = random_gnl(n, int(sys.argv[3]))
        else:
            g = random_gnp(n, float(sys.argv[3]))
    except ValueError as error:
        sys.exit(str(error))

    print("Lista sąsiedztwa:")
    for u in range(len(g.adjacency_list)):
        print(f"{u}: {g.adjacency_list[u]}")
    draw_graph(g)
    plt.show()


if __name__ == "__main__":
    main()
