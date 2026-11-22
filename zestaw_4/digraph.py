import random
import sys

import matplotlib.pyplot as plt

from zestaw_1.wczytywanie import list_from_one_based, read_data
from zestaw_1.zadanie_2 import circle_positions


class Digraph:
    """Graf skierowany o wierzchołkach 0..n-1; adjacency_list[u] = wierzchołki, do których prowadzi łuk z u."""

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    # macierz sąsiedztwa (matrix[u][v] == 1: łuk u -> v) -> lista
    @staticmethod
    def from_adjacency_matrix(matrix):
        n = len(matrix)
        adjacency_list = []
        for _ in range(n):
            adjacency_list.append([])
        for u in range(n):
            for v in range(n):
                if matrix[u][v] == 1:
                    adjacency_list[u].append(v)
        return Digraph(adjacency_list)

    # lista -> macierz sąsiedztwa
    def to_adjacency_matrix(self):
        n = len(self.adjacency_list)
        matrix = []
        for _ in range(n):
            matrix.append([0] * n)
        for u in range(n):
            for v in self.adjacency_list[u]:
                matrix[u][v] = 1
        return matrix

    # macierz incydencji (-1: początek łuku, 1: koniec łuku) -> lista
    @staticmethod
    def from_incidence_matrix(matrix):
        n = len(matrix)
        m = len(matrix[0]) if n > 0 else 0
        adjacency_list = []
        for _ in range(n):
            adjacency_list.append([])
        for j in range(m):
            u = None
            v = None
            for i in range(n):
                if matrix[i][j] == -1:
                    u = i
                elif matrix[i][j] == 1:
                    v = i
            adjacency_list[u].append(v)
        for neighbors in adjacency_list:
            neighbors.sort()
        return Digraph(adjacency_list)

    # lista -> macierz incydencji; łuki uporządkowane po początku, potem po końcu
    def to_incidence_matrix(self):
        n = len(self.adjacency_list)
        edges = []
        for u in range(n):
            for v in sorted(self.adjacency_list[u]):
                edges.append((u, v))
        matrix = []
        for _ in range(n):
            matrix.append([0] * len(edges))
        for j in range(len(edges)):
            u, v = edges[j]
            matrix[u][j] = -1
            matrix[v][j] = 1
        return matrix

    def edges(self):
        edges = []
        for u in range(len(self.adjacency_list)):
            for v in self.adjacency_list[u]:
                edges.append((u, v))
        return edges


# G(n, p): każdy łuk (u, v), u != v, osobno z prawdopodobieństwem p
def random_digraph(n, p):
    if n < 1:
        raise ValueError("n musi być dodatnie")
    if not 0 <= p <= 1:
        raise ValueError("p musi być od 0 do 1")
    adjacency_list = []
    for u in range(n):
        neighbors = []
        for v in range(n):
            if u != v and random.random() < p:
                neighbors.append(v)
        adjacency_list.append(neighbors)
    return Digraph(adjacency_list)


# wypisuje listę sąsiedztwa z numeracją od 1
def print_adjacency_list(g):
    for u in range(len(g.adjacency_list)):
        neighbors = []
        for v in g.adjacency_list[u]:
            neighbors.append(v + 1)
        print(f"{u + 1}: {neighbors}")


# lista sąsiedztwa z wagami: v(waga); w[u][v] == None oznacza brak łuku
def print_weighted_adjacency_list(g, w):
    for u in range(len(g.adjacency_list)):
        neighbors = []
        for v in g.adjacency_list[u]:
            neighbors.append(f"{v + 1}({w[u][v]})")
        print(f"{u + 1}: {', '.join(neighbors)}")


# rysuje digraf na okręgu; łuki zakrzywione, żeby u -> v i v -> u się nie nakładały
def draw_digraph(g, w=None):
    n = len(g.adjacency_list)
    positions = circle_positions(n)
    fig, ax = plt.subplots(figsize=(7, 7))
    rad = 0.15

    for u, v in g.edges():
        x_u, y_u = positions[u]
        x_v, y_v = positions[v]
        ax.annotate("", xy=(x_v, y_v), xytext=(x_u, y_u),
                    arrowprops=dict(arrowstyle="-|>", color="black", shrinkA=13,
                                    shrinkB=13, connectionstyle=f"arc3,rad={rad}"),
                    zorder=1)
        if w is not None:
            # środek krzywej Béziera arc3 leży w połowie odcinka przesunięty o 0.5 * rad * (dy, -dx)
            dx = x_v - x_u
            dy = y_v - y_u
            label_x = (x_u + x_v) / 2 + 0.5 * rad * dy
            label_y = (y_u + y_v) / 2 - 0.5 * rad * dx
            ax.text(label_x, label_y, str(w[u][v]), ha="center", va="center", fontsize=8,
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.5), zorder=3)

    for i in range(n):
        x, y = positions[i]
        ax.scatter(x, y, s=500, color="white", edgecolors="black", zorder=2)
        ax.text(x, y, str(i + 1), ha="center", va="center", zorder=4)

    ax.set_aspect("equal")
    ax.margins(0.15)
    ax.axis("off")
    return ax


# n i p z wiersza poleceń -> losowy digraf; extra = liczba dodatkowych argumentów opcjonalnych
def read_random_digraph(extra=0):
    if not 3 <= len(sys.argv) <= 3 + extra:
        sys.exit("Podaj n (liczba wierzchołków) i p (prawdopodobieństwo łuku, od 0 do 1).")
    try:
        return random_digraph(int(sys.argv[1]), float(sys.argv[2]))
    except ValueError as error:
        sys.exit(str(error))


# wierzchołek startowy s (numeracja od 1) z argumentu o indeksie index; domyślnie 1
def read_start(index, n):
    if len(sys.argv) <= index:
        return 0
    try:
        s = int(sys.argv[index]) - 1
    except ValueError:
        sys.exit("s musi być liczbą całkowitą.")
    if not 0 <= s < n:
        sys.exit(f"s musi być od 1 do {n}.")
    return s


# digraf zakodowany w terminalu: kodowanie (macierz, incydencja, lista) + dane
def digraph_from_encoding(encoding, source):
    data = read_data(encoding, source)
    if encoding == "lista":
        data = list_from_one_based(data)
    if encoding == "macierz":
        return Digraph.from_adjacency_matrix(data)
    if encoding == "incydencja":
        return Digraph.from_incidence_matrix(data)
    return Digraph(data)
