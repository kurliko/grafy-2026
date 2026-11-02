import matplotlib.pyplot as plt

from zestaw_1.wczytywanie import read_graph
from zestaw_1.zadanie_2 import draw_graph


# wczytuje graf, wypisuje go w trzech kodowaniach i pokazuje w oknie
# np. python -m zestaw_1.zadanie_1 lista "[[1],[0]]"
# albo python -m zestaw_1.zadanie_1 macierz zestaw_1/dane/macierz.txt
# kodowanie: macierz, incydencja albo lista
def main():
    g = read_graph()

    # ten sam graf w trzech kodowaniach
    print("Lista sąsiedztwa:")
    for u in range(len(g.adjacency_list)):
        print(f"{u}: {g.adjacency_list[u]}")
    print("Macierz sąsiedztwa:")
    for row in g.to_adjacency_matrix():
        print(row)
    print("Macierz incydencji:")
    for row in g.to_incidence_matrix():
        print(row)

    draw_graph(g)
    plt.show()


if __name__ == "__main__":
    main()
