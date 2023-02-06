class Queue:
    def __init__(self, n):
        self.queue, self.max_n = [None] * n, n
        self.head, self.tail, self.size = 0, 0, 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size < self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1

    def pop(self):
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


def bfs(s, adj, color, planned, distance):
    planned.push(s)
    color[s - 1] = 'gray'
    distance[s - 1] = 0
    while not planned.is_empty():
        u = planned.pop()
        for v in adj[u - 1]:
            if color[v - 1] == 'white':
                distance[v - 1] = distance[u - 1] + 1
                color[v - 1] = 'gray'
                planned.push(v)
        color[u - 1] = 'black'


def main():
    x = list(map(int, input().split()))
    n, m = x[0], x[1]
    adj = [[] for _ in range(n)]
    for _ in range(m):
        x = list(map(int, input().split()))
        u, v = x[0], x[1]
        adj[u - 1].append(v)
        adj[v - 1].append(u)
    s = int(input())
    color, planned = ['white' for _ in range(n)], Queue(n)
    distance = [None for _ in range(n)]
    bfs(s, adj, color, planned, distance)
    print(max(distance))


if __name__ == '__main__':
    main()
