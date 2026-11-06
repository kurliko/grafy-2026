class Graph:
    """Graf prosty o wierzchołkach 0..n-1, trzymany jako lista sąsiedztwa."""


    def __init__(self, adjacency_list):
       
        self.adjacency_list = adjacency_list

    # macierz sąsiedztwa -> lista
    @staticmethod
    def from_adjacency_matrix(matrix):
        n = len(matrix)
        adjacency_list = []
        for _ in range(n):
            adjacency_list.append([])
        for u in range(n):
            for v in range(n):
                if matrix[u][v] == 1:
                    adjacency_list[u].append(v)
        return Graph(adjacency_list)

    # lista -> macierz sąsiedztwa
    def to_adjacency_matrix(self):
        n = len(self.adjacency_list)
        matrix = []
        for _ in range(n):
            matrix.append([0] * n)
        for u in range(n):
            for v in self.adjacency_list[u]:
                matrix[u][v] = 1
        return matrix

    # macierz incydencji -> lista
    @staticmethod
    def from_incidence_matrix(matrix):
        n = len(matrix)
        m = len(matrix[0]) if n > 0 else 0
        adjacency_list = []
        for _ in range(n):
            adjacency_list.append([])
        for j in range(m):
            ends = []
            for i in range(n):
                if matrix[i][j] == 1:
                    ends.append(i)
            u = ends[0]
            v = ends[1]
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        for neighbors in adjacency_list:
            neighbors.sort()
        return Graph(adjacency_list)

    # lista -> macierz incydencji
    def to_incidence_matrix(self):
        n = len(self.adjacency_list)
        edges = []
        for u in range(n):
            for v in self.adjacency_list[u]:
                if u < v:
                    edges.append((u, v))
        matrix = []
        for _ in range(n):
            matrix.append([0] * len(edges))
        j = 0
        for edge in edges:
            u = edge[0]
            v = edge[1]
            matrix[u][j] = 1
            matrix[v][j] = 1
            j = j + 1
        return matrix
