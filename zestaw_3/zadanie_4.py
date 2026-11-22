from zestaw_3.graf_wazony import read_random_weighted_graph
from zestaw_3.zadanie_3 import distance_matrix
from zestaw_3.graf_wazony import print_weighted_graph, read_random_weighted_graph
from zestaw_3.zadanie_3 import distance_matrix, print_matrix

# centrum: najmniejsza suma odległości; minimax: najmniejsza odległość do najdalszego
# przy remisie wybieramy wierzchołek o najmniejszym numerze
# zwraca (centrum, suma, centrum minimax, odległość od najdalszego), numeracja od 0
def centers(d):
    sums = [sum(row) for row in d]
    farthest = [max(row) for row in d]
    c = sums.index(min(sums))
    cm = farthest.index(min(farthest))
    return c, sums[c], cm, farthest[cm]


def print_centers(d):
    c, total, cm, dist = centers(d)
    print(f"Centrum = {c + 1} (suma odleglosci: {total})")
    print(f"Centrum minimax = {cm + 1} (odleglosc od najdalszego: {dist})")




# np. python -m zestaw_3.zadanie_4 12 19
def main():
    g, w = read_random_weighted_graph()
    print("Graf (sąsiad(waga)):")
    print_weighted_graph(g, w)
    d = distance_matrix(g, w)
    print("\nMacierz odległości:")
    print_matrix(d)
    print()
    print_centers(d)


if __name__ == "__main__":
    main()
