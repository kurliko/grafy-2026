from zestaw_3.graf_wazony import print_weighted_graph, read_random_weighted_graph, draw_weighted_graph
from zestaw_3.zadanie_2 import dijkstra
import matplotlib.pyplot as plt

# wiersz s macierzy = wynik Dijkstry ze startem w s
def distance_matrix(g, w):
    d = []
    for s in range(len(g.adjacency_list)):
        ds, _ = dijkstra(g, w, s)
        d.append(ds)
    return d


def print_matrix(d):
    width = len(str(max(max(row) for row in d)))
    for row in d:
        print(" ".join(f"{x:>{width}}" for x in row))


# np. python -m zestaw_3.zadanie_3 12 19
def main():
    g, w = read_random_weighted_graph()
    print("Graf (sąsiad(waga)):")
    print_weighted_graph(g, w)
    draw_weighted_graph(g,w)
    print("\nMacierz odległości:")
    print_matrix(distance_matrix(g, w))
    plt.show()


if __name__ == "__main__":
    main()