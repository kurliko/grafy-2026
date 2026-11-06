import json
import sys

from zestaw_1.graph import Graph


# plik z macierzą -> lista wierszy
def read_matrix_file(path):
    matrix = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            if line.strip():
                row = []
                for word in line.split():
                    row.append(int(word))
                matrix.append(row)
    return matrix


# plik z listą sąsiedztwa -> lista list
def read_list_file(path):
    adjacency_list = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue
            words = line.split()
            vertex = words[0]
            expected = f"{len(adjacency_list)}."
            if vertex != expected:
                raise ValueError(f"w pliku {path} oczekiwano numeru {expected}, a jest {vertex} (numeracja od 0)")
            neighbors = []
            for word in words[1:]:
                neighbors.append(int(word))
            adjacency_list.append(neighbors)
    return adjacency_list


def read_data(encoding, source):
    if source.startswith("["):
        return json.loads(source)
    if encoding == "lista":
        return read_list_file(source)
    return read_matrix_file(source)


# argumenty z terminala -> Graph
def read_graph():
    if len(sys.argv) != 3:
        sys.exit("Podaj dwa argumenty: kodowanie (macierz, incydencja albo lista) oraz graf w cudzysłowie lub ścieżkę do pliku .txt.")

    encoding = sys.argv[1]
    # graf w cudzysłowie, np. "[[0,1],[1,0]]", albo ścieżka do pliku .txt
    source = sys.argv[2]
    if encoding not in ["macierz", "incydencja", "lista"]:
        sys.exit("Kodowanie musi być macierz, incydencja albo lista.")

    try:
        data = read_data(encoding, source)
    except (OSError, ValueError) as error:
        sys.exit(str(error))

    # macierz: konwersja na listę; lista: bez konwersji
    if encoding == "macierz":
        return Graph.from_adjacency_matrix(data)
    if encoding == "incydencja":
        return Graph.from_incidence_matrix(data)
    return Graph(data)
