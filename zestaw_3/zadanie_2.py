import sys
from zestaw_3.graf_wazony import INF, print_weighted_graph, read_random_weighted_graph, draw_weighted_graph
import matplotlib.pyplot as plt

# algorytm 1: wartości początkowe
def init(g, s):
    n = len(g.adjacency_list)
    ds = [INF] * n #tablica odległości
    ps = [None] * n #znaczenia poprzednie
    ds[s] = 0
    return ds, ps


# algorytm 2: relaksacja krawędzi (u, v)
def relax(u, v, w, ds, ps):
    if ds[v] > ds[u] + w[u][v]:
        ds[v] = ds[u] + w[u][v]
        ps[v] = u


# algorytm 3: Dijkstra; zwraca długości ds i poprzedników ps
def dijkstra(g, w, s):
    n = len(g.adjacency_list)
    ds, ps = init(g, s)
    done = [False] * n
    for _ in range(n):
        u = None
        for x in range(n):
            if not done[x] and (u is None or ds[x] < ds[u]):
                u = x
        done[u] = True
        for v in g.adjacency_list[u]:
            if not done[v]:
                relax(u, v, w, ds, ps)
    return ds, ps


# ścieżka s -> v odtworzona z tablicy poprzedników
def path_to(ps, s, v):
    path = [v]
    while v != s:
        v = ps[v]
        path.append(v)
    path.reverse()
    return path


def print_shortest_paths(g, w, s):
    ds, ps = dijkstra(g, w, s)
    width = len(str(len(ds)))
    print(f"START: s = {s + 1}")
    for v in range(len(ds)):
        path = " - ".join(str(x + 1) for x in path_to(ps, s, v))
        print(f"d({v + 1:>{width}}) = {ds[v]:>3} ==> [{path}]")


# np. python -m zestaw_3.zadanie_2 12 19 [s]
def main():
    g, w = read_random_weighted_graph(extra=1)
    s = 0
    if len(sys.argv) == 4:
        try:
            s = int(sys.argv[3]) - 1
        except ValueError:
            sys.exit("s musi być liczbą całkowitą.")
        if not 0 <= s < len(g.adjacency_list):
            sys.exit(f"s musi być od 1 do {len(g.adjacency_list)}.")
    print("Graf (sąsiad(waga)):")
    print_weighted_graph(g, w)
    draw_weighted_graph(g, w)
    print()
    print_shortest_paths(g, w, s)
    plt.show()


if __name__ == "__main__":
    main()
