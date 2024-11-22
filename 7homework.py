class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, source):
        # Шаг 1: Инициализация расстояний
        distance = [float('inf')] * self.V
        distance[source] = 0

        # Шаг 2: Расслабление рёбер
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

        # Шаг 3: Проверка на наличие отрицательных циклов
        for u, v, weight in self.edges:
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                print("Граф содержит отрицательный цикл")
                return None

        return distance

if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, -2)
    g.add_edge(2, 3, 2)
    g.add_edge(1, 3, 3)
    g.add_edge(0, 2, 4)


    source_vertex = int(input("Выберите вершину: "))
    distances = g.bellman_ford(source_vertex)

    if distances is not None:
        print("Расстояния от вершины", source_vertex)
        for i in range(len(distances)):
            print(f"До вершины {i}: {distances[i]}")