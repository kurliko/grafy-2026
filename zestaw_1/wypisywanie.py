# wypisuje listę sąsiedztwa z numeracją od 1, po jednym wierzchołku w linii
# w programie wierzchołki mają numery od 0, więc przy wypisywaniu dodajemy 1
def print_adjacency_list(g):
    for u in range(len(g.adjacency_list)):
        neighbors = []
        for v in g.adjacency_list[u]:
            neighbors.append(v + 1)
        print(f"{u + 1}: {neighbors}")
