import random
import sys

from zestaw_3.zadanie_2 import INF, init, path_to, relax
from zestaw_4.digraph import (Digraph, print_weighted_adjacency_list, random_digraph,
                              read_start)
from zestaw_4.zadanie_2 import is_strongly_connected


# losuje G(n, p) tak długo, aż digraf jest silnie spójny (Kosaraju z zadania 2)
def random_strongly_connected_digraph(n, p, max_tries=100000):
    for _ in range(max_tries):
        g = random_digraph(n, p)
        if is_strongly_connected(g):
            return g
    raise ValueError("nie udało się wylosować silnie spójnego digrafu, podaj większe p")


# algorytm 6: dodatkowy wierzchołek s = n z łukami (s, v) o wadze 0 do wszystkich v
def add_s(g, w):
    n = len(g.adjacency_list)
    adjacency_list = []
    for neighbors in g.adjacency_list:
        adjacency_list.append(list(neighbors))
    adjacency_list.append(list(range(n)))
    w0 = []
    for row in w:
        w0.append(list(row) + [None])
    w0.append([0] * n + [None])
    return Digraph(adjacency_list), w0


# algorytm 4: Bellman-Ford; zwraca (ds, ps, True) albo (ds, ps, False) przy ujemnym cyklu
def bellman_ford(g, w, s):
    n = len(g.adjacency_list)
    ds, ps = init(g, s)
    edges = g.edges()
    for _ in range(n - 1):
        for u, v in edges:
            relax(u, v, w, ds, ps)
    for u, v in edges:
        if ds[v] > ds[u] + w[u][v]:
            return ds, ps, False
    return ds, ps, True


# czy w digrafie z wagami w jest cykl o ujemnej sumie wag (Bellman-Ford z dodatkowego wierzchołka)
def has_negative_cycle(g, w):
    g0, w0 = add_s(g, w)
    return not bellman_ford(g0, w0, len(g.adjacency_list))[2]


# losowe wagi z [low, high]; jeśli powstał ujemny cykl, ujemne wagi (w losowej kolejności)
# zamieniamy na losowe nieujemne tak długo, aż cykl zniknie (sam rozkład wag nie zawsze to daje)
def random_weights(g, low=-5, high=10):
    n = len(g.adjacency_list)
    w = []
    for _ in range(n):
        w.append([None] * n)
    for u, v in g.edges():
        w[u][v] = random.randint(low, high)
    negative = []
    for u, v in g.edges():
        if w[u][v] < 0:
            negative.append((u, v))
    random.shuffle(negative)
    while has_negative_cycle(g, w):
        u, v = negative.pop()
        w[u][v] = random.randint(0, high)
    return w


def print_paths(ds, ps, s):
    width = len(str(len(ds)))
    print(f"START: s = {s + 1}")
    for v in range(len(ds)):
        if ds[v] == INF:
            print(f"d({v + 1:>{width}}) = brak ścieżki")
            continue
        path = " - ".join(str(x + 1) for x in path_to(ps, s, v))
        print(f"d({v + 1:>{width}}) = {ds[v]:>3} ==> [{path}]")


# losuje silnie spójny digraf z wagami z [-5, 10] i wypisuje najkrótsze ścieżki
# Bellmana-Forda od wierzchołka s (domyślnie 1)
# np. python -m zestaw_4.zadanie_3 7 0.4 [s]
def main():
    if not 3 <= len(sys.argv) <= 4:
        sys.exit("Podaj n, p i opcjonalnie s (wierzchołek startowy).")
    try:
        g = random_strongly_connected_digraph(int(sys.argv[1]), float(sys.argv[2]))
    except ValueError as error:
        sys.exit(str(error))
    w = random_weights(g)
    s = read_start(3, len(g.adjacency_list))

    print("Lista sąsiedztwa z wagami (v(waga)):")
    print_weighted_adjacency_list(g, w)
    print()
    ds, ps, ok = bellman_ford(g, w, s)
    print_paths(ds, ps, s)


if __name__ == "__main__":
    main()
