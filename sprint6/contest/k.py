class Graph:
    def __init__(self, n):
        self.n = n
        self.A = [[0] * n for _ in range(n)]

    def get_min_dist_not_visited_vertex(self, dist, visited):
        cur_min, cur_min_vertex = float('inf'), None
        for v in range(self.n):
            if not visited[v] and dist[v] < cur_min:
                cur_min = dist[v]
                cur_min_vertex = v
        return cur_min_vertex

    def relax(self, dist, u, v):
        if dist[v] > dist[u] + self.A[u][v]:
            dist[v] = dist[u] + self.A[u][v]

    def print_shortest_dist(self, dist):
        [print(x if x != float('inf') else -1, end=' ') for x in dist]
        print()

    def Dijkstra(self, s):
        dist = [float('inf')] * self.n
        dist[s] = 0
        visited = [False] * self.n
        for _ in range(self.n):
            u = self.get_min_dist_not_visited_vertex(dist, visited)
            if u is not None:
                visited[u] = True
                [self.relax(dist, u, v) for v in range(self.n) if self.A[u][v]]
        self.print_shortest_dist(dist)


def main():
    x = list(map(int, input().split()))
    n, m = x[0], x[1]
    if not m:
        for i in range(n):
            [print(0 if i == j else -1, end=' ') for j in range(n)]
            print()
        return

    G = Graph(n)
    for _ in range(m):
        x = list(map(int, input().split()))
        u, v, w = x[0] - 1, x[1] - 1, x[2]
        G.A[u][v] = min(G.A[u][v], w) if G.A[u][v] else w
        G.A[v][u] = min(G.A[v][u], w) if G.A[v][u] else w
    [G.Dijkstra(s) for s in range(n)]


if __name__ == '__main__':
    main()
