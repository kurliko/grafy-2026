import matplotlib.pyplot as plt

from zestaw_1.wczytywanie import read_graph
from zestaw_1.zadanie_2 import draw_graph


def components(g):
    n = len(g.adjacency_list)
    nr = 0
    # -1: wierzchołek nieodwiedzony
    comp = [-1] * n
    for v in range(n):
        if comp[v] == -1:
            nr = nr + 1
            comp[v] = nr
            components_r(nr, v, g, comp)
    return comp


# przechodzi w głąb
def components_r(nr, v, g, comp):
    for u in g.adjacency_list[v]:
        if comp[u] == -1:
            comp[u] = nr
            components_r(nr, u, g, comp)



def largest_component(comp):
    count = max(comp)
    sizes = [0] * (count + 1)
    for nr in comp:
        sizes[nr] = sizes[nr] + 1
    best = 1
    for nr in range(1, count + 1):
        if sizes[nr] > sizes[best]:
            best = nr
    return best


def print_components(comp):
    for nr in range(1, max(comp) + 1):
        text = f"{nr})"
        for v in range(len(comp)):
            if comp[v] == nr:
                text = text + f" {v + 1}"
        print(text)


# wczytuje graf, wypisuje jego spójne składowe i rysuje go
def main():
    g = read_graph()
    if len(g.adjacency_list) == 0:
        print("Graf nie ma wierzchołków.")
        return
    comp = components(g)
    print_components(comp)
    print(f"Największa składowa ma numer {largest_component(comp)}.")
    draw_graph(g)
    plt.show()


if __name__ == "__main__":
    main()
