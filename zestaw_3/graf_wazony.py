import random
import sys

import matplotlib.pyplot as plt

from zestaw_1.graph import Graph
from zestaw_1.zadanie_2 import circle_positions
from zestaw_1.zadanie_3 import random_gnl

INF = float("inf")


# BFS od wierzchołka 0: czy da się dojść do wszystkich wierzchołków
def is_connected(g):
    n = len(g.adjacency_list)
    if n == 0:
        return True
    visited = [False] * n
    visited[0] = True
    queue = [0]
    while queue:
        u = queue.pop()
        for v in g.adjacency_list[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    return all(visited)


# losuje G(n, l) (z zestawu 1) tak długo, aż graf jest spójny
def random_connected_graph(n, l, max_tries=100000):
    if n < 1:
        raise ValueError("n musi być dodatnie")
    if l < n - 1:
        raise ValueError(f"spójny graf o {n} wierzchołkach ma co najmniej {n - 1} krawędzi")
    for _ in range(max_tries):
        g = random_gnl(n, l)
        if is_connected(g):
            return g
    raise ValueError("nie udało się wylosować spójnego grafu, podaj większe l")


# każdej krawędzi losowa waga 1..10; w[u][v] == w[v][u], None = brak krawędzi
def random_weights(g, low=1, high=10):
    n = len(g.adjacency_list)
    w = []
    for _ in range(n):
        w.append([None] * n)
    for u in range(n):
        for v in g.adjacency_list[u]:
            if u < v:
                w[u][v] = random.randint(low, high)
                w[v][u] = w[u][v]
    return w


# zadanie 1: spójny graf losowy z wagami
def random_weighted_graph(n, l):
    g = random_connected_graph(n, l)
    return g, random_weights(g)


def edge_list(g, w):
    edges = []
    for u in range(len(g.adjacency_list)):
        for v in g.adjacency_list[u]:
            if u < v:
                edges.append((u, v, w[u][v]))
    return edges


# wypisuje graf: lista sąsiedztwa z wagami, numeracja od 1
def print_weighted_graph(g, w):
    for u in range(len(g.adjacency_list)):
        neighbors = []
        for v in g.adjacency_list[u]:
            neighbors.append(f"{v + 1}({w[u][v]})")
        print(f"{u + 1}: {', '.join(neighbors)}")


# rysuje graf na okręgu z wagami; krawędzie z mst_edges (u, v, waga) na niebiesko
def draw_weighted_graph(g, w, mst_edges=()):
    n = len(g.adjacency_list)
    positions = circle_positions(n)
    in_tree = set()
    for u, v, _ in mst_edges:
        in_tree.add((min(u, v), max(u, v)))
    fig, ax = plt.subplots(figsize=(7, 7))

    for u, v, weight in edge_list(g, w):
        x_u, y_u = positions[u]
        x_v, y_v = positions[v]
        if (u, v) in in_tree:
            color, width = "blue", 3
        elif in_tree:
            color, width = "lightgray", 1
        else:
            color, width = "black", 1
        ax.plot([x_u, x_v], [y_u, y_v], color=color, linewidth=width, zorder=1)
        ax.text((x_u + x_v) / 2, (y_u + y_v) / 2, str(weight), ha="center",
                va="center", fontsize=8, color=color if color != "lightgray" else "gray",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.5), zorder=3)

    for i in range(n):
        x, y = positions[i]
        ax.scatter(x, y, s=500, color="white", edgecolors="black", zorder=2)
        ax.text(x, y, str(i + 1), ha="center", va="center", zorder=4)

    ax.set_aspect("equal")
    ax.margins(0.15)
    ax.axis("off")
    return ax


# wczytuje n i l z wiersza poleceń i losuje graf z wagami
def read_random_weighted_graph(extra=0):
    usage = "Podaj n (liczba wierzchołków) i l (liczba krawędzi)"
    if not 3 <= len(sys.argv) <= 3 + extra:
        sys.exit(usage + ".")
    try:
        n = int(sys.argv[1])
        l = int(sys.argv[2])
        return random_weighted_graph(n, l)
    except ValueError as error:
        sys.exit(str(error))
