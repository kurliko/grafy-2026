import sys

import matplotlib.pyplot as plt

from zestaw_1.graph import Graph
from zestaw_1.wypisywanie import print_adjacency_list
from zestaw_1.zadanie_2 import draw_graph

def parse_sequence(words):
    sequence = []
    for word in words:
        number = int(word)
        if number < 0:
            raise ValueError(f"{number} nie jest liczbą naturalną")
        sequence.append(number)
    return sequence


# ciąg stopni -> graf, w którym wierzchołek v ma stopień sequence[v]
# zwraca None, jeśli ciąg nie jest graficzny 
def graph_from_degree_sequence(sequence):
    n = len(sequence)

    odd = 0
    for degree in sequence:
        if degree % 2 == 1:
            odd = odd + 1
    if odd % 2 == 1:
        return None

    adjacency_list = []
    for _ in range(n):
        adjacency_list.append([])

    pairs = []
    for v in range(n):
        pairs.append([sequence[v], v])
    pairs.sort(reverse=True)

    while True:
        all_zero = True
        for pair in pairs:
            if pair[0] != 0:
                all_zero = False
        if all_zero:
            for neighbors in adjacency_list:
                neighbors.sort()
            return Graph(adjacency_list)

        if pairs[0][0] >= n:
            return None
        for pair in pairs:
            if pair[0] < 0:
                return None

        degree = pairs[0][0]
        u = pairs[0][1]
        for i in range(1, degree + 1):
            pairs[i][0] = pairs[i][0] - 1
            v = pairs[i][1]
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        pairs[0][0] = 0
        pairs.sort(reverse=True)


# sprawdza czy ciąg jest graficzny, jeśli jest to wypisuje i rysuje zbudowany graf
def main():
    if len(sys.argv) < 2:
        sys.exit("Podaj ciąg liczb naturalnych, np. 4 2 2 3 2 1 4 2 2 2 2.")
    try:
        sequence = parse_sequence(sys.argv[1:])
    except ValueError as error:
        sys.exit(str(error))

    g = graph_from_degree_sequence(sequence)
    if g is None:
        print("Ciąg nie jest graficzny.")
        return

    print("Ciąg jest graficzny.")
    print("Lista sąsiedztwa:")
    print_adjacency_list(g)
    draw_graph(g)
    plt.show()


if __name__ == "__main__":
    main()
