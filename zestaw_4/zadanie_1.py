import sys

import matplotlib.pyplot as plt

from zestaw_4.digraph import (Digraph, digraph_from_encoding, draw_digraph,
                              print_adjacency_list, random_digraph)


# dwa tryby:
#   losowy digraf G(n, p):   python -m zestaw_4.zadanie_1 gnp 7 0.3
#   digraf w kodowaniu:      python -m zestaw_4.zadanie_1 lista "[[2,3],[1],[]]"
#                            python -m zestaw_4.zadanie_1 macierz zestaw_4/dane/macierz.txt
# kodowanie: macierz, incydencja albo lista (numeracja od 1 w liście)
# program wypisuje digraf w trzech kodowaniach i rysuje go w oknie
def main():
    usage = "Podaj: gnp n p, albo kodowanie (macierz, incydencja, lista) i dane."
    if len(sys.argv) < 3:
        sys.exit(usage)
    try:
        if sys.argv[1] == "gnp":
            if len(sys.argv) != 4:
                sys.exit(usage)
            g = random_digraph(int(sys.argv[2]), float(sys.argv[3]))
        else:
            if len(sys.argv) != 3 or sys.argv[1] not in ["macierz", "incydencja", "lista"]:
                sys.exit(usage)
            g = digraph_from_encoding(sys.argv[1], sys.argv[2])
    except (OSError, ValueError, TypeError) as error:
        sys.exit(f"Błąd danych: {error}")

    print("Lista sąsiedztwa:")
    print_adjacency_list(g)
    print("Macierz sąsiedztwa:")
    for row in g.to_adjacency_matrix():
        print(row)
    print("Macierz incydencji:")
    for row in g.to_incidence_matrix():
        print(row)

    draw_digraph(g)
    plt.show()


if __name__ == "__main__":
    main()
