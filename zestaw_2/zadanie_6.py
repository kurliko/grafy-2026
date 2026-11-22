import matplotlib.pyplot as plt

from zestaw_1.wczytywanie import read_graph
from zestaw_1.zadanie_2 import draw_graph
from zestaw_2.zadanie_4 import format_path


def hamilton_cycle(g):
    n = len(g.adjacency_list)
    if n < 3:
        return None
    visited = [False] * n
    stack = [0]
    visited[0] = True
    if hamilton_r(g, stack, visited):
        return stack + [0]
    return None

# przechodzenie w głąb
def hamilton_r(g, stack, visited):
    last = stack[-1]
    if len(stack) == len(g.adjacency_list):
        return stack[0] in g.adjacency_list[last]

    for v in g.adjacency_list[last]:
        if not visited[v]:
            visited[v] = True
            stack.append(v)
            if hamilton_r(g, stack, visited):
                return True
            # zdejmujemy ze stosu
            stack.pop()
            visited[v] = False
    return False


# wczytuje graf, sprawdza, czy jest hamiltonowski, i rysuje go
def main():
    g = read_graph()
    cycle = hamilton_cycle(g)
    if cycle is None:
        print("Graf nie jest hamiltonowski.")
    else:
        print("Graf jest hamiltonowski.")
        print(f"Cykl Hamiltona: {format_path(cycle)}")
    draw_graph(g)
    plt.show()


if __name__ == "__main__":
    main()
