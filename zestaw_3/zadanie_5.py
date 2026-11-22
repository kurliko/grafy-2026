import matplotlib.pyplot as plt

from zestaw_3.graf_wazony import INF, draw_weighted_graph, read_random_weighted_graph


# algorytm Prima od wierzchołka 0; zwraca listę krawędzi drzewa (u, v, waga)
def prim(g, w):
    n = len(g.adjacency_list)
    in_tree = [False] * n
    key = [INF] * n
    parent = [None] * n
    key[0] = 0
    tree = []
    for _ in range(n):
        u = None
        for x in range(n):
            if not in_tree[x] and (u is None or key[x] < key[u]):
                u = x
        in_tree[u] = True
        if parent[u] is not None:
            tree.append((parent[u], u, w[parent[u]][u]))
        for v in g.adjacency_list[u]:
            if not in_tree[v] and w[u][v] < key[v]:
                key[v] = w[u][v]
                parent[v] = u
    return tree


def print_tree(tree):
    for u, v, weight in sorted((min(u, v), max(u, v), x) for u, v, x in tree):
        print(f"{u + 1} - {v + 1} : {weight}")
    print(f"Waga drzewa: {sum(x for _, _, x in tree)}")


# wypisuje i rysuje minimalne drzewo rozpinające (krawędzie drzewa na niebiesko)
# np. python -m zestaw_3.zadanie_5 12 19
def main():
    g, w = read_random_weighted_graph()
    tree = prim(g, w)
    print_tree(tree)
    draw_weighted_graph(g, w, tree)
    plt.show()


if __name__ == "__main__":
    main()
