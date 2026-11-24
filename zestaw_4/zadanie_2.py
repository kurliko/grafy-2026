import sys
import matplotlib.pyplot as plt
from zestaw_4.digraph import Digraph, print_adjacency_list, read_random_digraph, draw_digraph


# transpozycja: łuki mają odwrócone zwroty
def transpose(g):
    n = len(g.adjacency_list)
    adjacency_list = []
    for _ in range(n):
        adjacency_list.append([])
    for u in range(n):
        for v in g.adjacency_list[u]:
            adjacency_list[v].append(u)
    return Digraph(adjacency_list)


# algorytm 2: DFS_visit; czas t trzymamy w liście jednoelementowej, żeby rekurencja mogła go zmieniać
def dfs_visit(v, g, d, f, t, order):
    t[0] += 1
    d[v] = t[0]
    for u in g.adjacency_list[v]:
        if d[u] == -1:
            dfs_visit(u, g, d, f, t, order)
    t[0] += 1
    f[v] = t[0]
    order.append(v)  # kolejność kończenia przetwarzania (stos)


# algorytm 3: oznacza wszystko, co osiągalne z v w GT i jeszcze bez składowej
def components_r(nr, v, gt, comp):
    for u in gt.adjacency_list[v]:
        if comp[u] == -1:
            comp[u] = nr
            components_r(nr, u, gt, comp)


# algorytm 1: Kosaraju; zwraca comp[v] = numer silnie spójnej składowej (od 1)
def kosaraju(g):
    n = len(g.adjacency_list)
    sys.setrecursionlimit(max(1000, 2 * n + 100))
    d = [-1] * n
    f = [-1] * n
    t = [0]
    order = []
    for v in range(n):
        if d[v] == -1:
            dfs_visit(v, g, d, f, t, order)

    gt = transpose(g)
    comp = [-1] * n
    nr = 0
    # malejące czasy f = wierzchołki zdejmowane ze stosu
    for v in reversed(order):
        if comp[v] == -1:
            nr += 1
            comp[v] = nr
            components_r(nr, v, gt, comp)
    return comp


def is_strongly_connected(g):
    return max(kosaraju(g)) == 1


def components_lists(comp):
    result = []
    for _ in range(max(comp)):
        result.append([])
    for v in range(len(comp)):
        result[comp[v] - 1].append(v + 1)
    return result


def print_components(comp):
    components = components_lists(comp)
    for i in range(len(components)):
        print(f"Składowa {i + 1}: {components[i]}")
    if len(components) == 1:
        print("Digraf jest silnie spójny.")
    else:
        print(f"Digraf nie jest silnie spójny (składowych: {len(components)}).")


# losuje digraf G(n, p), wypisuje go i jego silnie spójne składowe
# np. python -m zestaw_4.zadanie_2 7 0.3
def main():
    g = read_random_digraph()
    draw_digraph(g)
    print("Lista sąsiedztwa:")
    print_adjacency_list(g)
    print()
    print_components(kosaraju(g))
    plt.show()


if __name__ == "__main__":
    main()
