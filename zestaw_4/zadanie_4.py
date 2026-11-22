import sys

from zestaw_3.zadanie_2 import INF, dijkstra
from zestaw_4.digraph import print_weighted_adjacency_list
from zestaw_4.zadanie_3 import (add_s, bellman_ford, random_strongly_connected_digraph,
                                random_weights)


# algorytm 5: Johnson; zwraca macierz odległości D (INF = brak ścieżki)
# albo None, jeśli w digrafie jest cykl o ujemnej wadze
def johnson(g, w):
    n = len(g.adjacency_list)
    g0, w0 = add_s(g, w)
    ds, _, ok = bellman_ford(g0, w0, n)
    if not ok:
        return None
    h = ds
    # nowe, nieujemne wagi: wb[u][v] = w[u][v] + h[u] - h[v]
    wb = []
    for _ in range(n):
        wb.append([None] * n)
    for u, v in g.edges():
        wb[u][v] = w[u][v] + h[u] - h[v]
    d = []
    for u in range(n):
        bd, _ = dijkstra(g, wb, u)
        row = []
        for v in range(n):
            if bd[v] == INF:
                row.append(INF)
            else:
                row.append(bd[v] - h[u] + h[v])
        d.append(row)
    return d


def print_matrix(d):
    width = max(len(str(x)) for row in d for x in row)
    for row in d:
        print(" ".join(f"{x:>{width}}" for x in row))


# losuje silnie spójny digraf z wagami z [-5, 10], wypisuje go i macierz odległości (Johnson)
# np. python -m zestaw_4.zadanie_4 7 0.4
def main():
    if len(sys.argv) != 3:
        sys.exit("Podaj n i p.")
    try:
        g = random_strongly_connected_digraph(int(sys.argv[1]), float(sys.argv[2]))
    except ValueError as error:
        sys.exit(str(error))
    w = random_weights(g)

    print("Lista sąsiedztwa z wagami (v(waga)):")
    print_weighted_adjacency_list(g, w)
    print("\nMacierz odległości:")
    print_matrix(johnson(g, w))


if __name__ == "__main__":
    main()
