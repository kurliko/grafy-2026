import sys

import matplotlib.pyplot as plt

from zestaw_1.wypisywanie import print_adjacency_list
from zestaw_1.zadanie_2 import draw_graph
from zestaw_2.zadanie_1 import graph_from_degree_sequence
from zestaw_2.zadanie_2 import randomize


def random_regular_graph(n, k):
    if not 0 <= k < n:
        raise ValueError("musi być 0 <= k < n")
    if k % 2 == 1 and n % 2 == 1:
        raise ValueError("n * k musi być parzyste")
    g = graph_from_degree_sequence([k] * n)
    randomize(g, 100)
    return g


# losuje graf k-regularny, wypisuje go i rysuje
def main():
    if len(sys.argv) != 3:
        sys.exit("Podaj 2 argumenty: liczbę wierzchołków n i stopień k")
    try:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
        g = random_regular_graph(n, k)
    except ValueError as error:
        sys.exit(str(error))

    print("Lista sąsiedztwa:")
    print_adjacency_list(g)
    draw_graph(g)
    plt.show()


if __name__ == "__main__":
    main()
