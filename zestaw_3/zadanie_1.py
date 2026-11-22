import matplotlib.pyplot as plt

from zestaw_3.graf_wazony import (draw_weighted_graph, print_weighted_graph,
                                  read_random_weighted_graph)


# losuje spójny graf z wagami 1..10, wypisuje go i rysuje
# np. python -m zestaw_3.zadanie_1 12 19
def main():
    g, w = read_random_weighted_graph()
    print("Lista sąsiedztwa (sąsiad(waga)):")
    print_weighted_graph(g, w)
    draw_weighted_graph(g, w)
    plt.show()


if __name__ == "__main__":
    main()
