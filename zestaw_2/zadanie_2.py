import random
import sys

import matplotlib.pyplot as plt

from zestaw_1.wypisywanie import print_adjacency_list
from zestaw_1.zadanie_2 import draw_graph
from zestaw_2.zadanie_1 import graph_from_degree_sequence, parse_sequence



def edge_list(g):
    edges = []
    for u in range(len(g.adjacency_list)):
        for v in g.adjacency_list[u]:
            if u < v:
                edges.append((u, v))
    return edges



def add_edge(g, u, v):
    g.adjacency_list[u].append(v)
    g.adjacency_list[v].append(u)
    g.adjacency_list[u].sort()
    g.adjacency_list[v].sort()



def remove_edge(g, u, v):
    g.adjacency_list[u].remove(v)
    g.adjacency_list[v].remove(u)



def randomize(g, times):
    done = 0
    attempts = 0
    while done < times and attempts < 100 * times:
        attempts = attempts + 1
        edges = edge_list(g)
        if len(edges) < 2:
            break

        a, b = random.choice(edges)
        c, d = random.choice(edges)
        if random.random() < 0.5:
            c, d = d, c

        if a == c or a == d or b == c or b == d:
            continue
        if d in g.adjacency_list[a] or c in g.adjacency_list[b]:
            continue

        remove_edge(g, a, b)
        remove_edge(g, c, d)
        add_edge(g, a, d)
        add_edge(g, b, c)
        done = done + 1
    return done


# buduje graf z ciągu, randomizuje go, wypisuje przed i po, rysuje wynik
def main():
    if len(sys.argv) < 3:
        sys.exit("Podaj liczbę randomizacji i ciąg graficzny, np. 10 4 2 2 3 2 1 4 2 2 2 2.")
    try:
        times = int(sys.argv[1])
        sequence = parse_sequence(sys.argv[2:])
    except ValueError as error:
        sys.exit(str(error))
    if times < 0:
        sys.exit("Liczba randomizacji nie może być ujemna.")

    g = graph_from_degree_sequence(sequence)
    if g is None:
        sys.exit("Ciąg nie jest graficzny.")

    print("Przed randomizacją:")
    print_adjacency_list(g)
    done = randomize(g, times)
    print(f"Po {done} randomizacjach:")
    print_adjacency_list(g)
    if done < times:
        print(f"Wykonano tylko {done} z {times} zamian, bo nie znaleziono więcej dozwolonych zamian.")
    draw_graph(g)
    plt.show()


if __name__ == "__main__":
    main()
