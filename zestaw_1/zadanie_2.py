import math

import matplotlib.pyplot as plt

from zestaw_1.wczytywanie import read_graph


# liczy współrzędne n wierzchołków równomiernie na okręgu
def circle_positions(n):
    positions = []
    for i in range(n):
        # pełny okrąg dzielimy na n równych kątów
        angle = 2 * math.pi * i / n
        # kąt -> współrzędne (x, y)
        positions.append((math.cos(angle), math.sin(angle)))
    return positions


# rysuje graf g: krawędzie jako odcinki, wierzchołki jako kółka z numerem
def draw_graph(g):
    positions = circle_positions(len(g.adjacency_list))
    fig, ax = plt.subplots()

    for u in range(len(g.adjacency_list)):
        for v in g.adjacency_list[u]:
            # u < v: każda krawędź raz
            if u < v:
                # odcinek między pozycjami sąsiadów
                x_u, y_u = positions[u]
                x_v, y_v = positions[v]
                ax.plot([x_u, x_v], [y_u, y_v], color="black", zorder=1)

    for i in range(len(positions)):
        x, y = positions[i]
        ax.scatter(x, y, s=500, color="white", edgecolors="black", zorder=2)
        ax.text(x, y, str(i), ha="center", va="center", zorder=3)

    ax.set_aspect("equal")
    ax.margins(0.15)
    ax.axis("off")
    return ax


# wczytuje graf i pokazuje go w oknie
# np. python -m zestaw_1.zadanie_2 lista "[[1],[0]]"
# kodowanie: macierz, incydencja albo lista
def main():
    g = read_graph()
    draw_graph(g)
    plt.show()


if __name__ == "__main__":
    main()
