# https://contest.yandex.ru/contest/25069/problems/D/
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


def bfs(s, adj, color, planned):
    planned.push(s)
    color[s] = 1
    while not planned.is_empty():
        u = planned.pop()
        for v in adj[u]:
            if color[v] == 0:
                color[v] = 1
                planned.push(v)
        color[u] = 2
        print(u + 1, end=' ')


def main():
    x = list(map(int, input().split()))
    n, m = x[0], x[1]
    adj = [[] for _ in range(n)]
    for _ in range(m):
        x = list(map(int, input().split()))
        u, v = x[0] - 1, x[1] - 1
        adj[u].append(v)
        adj[v].append(u)
    s, adj = int(input()) - 1, [sorted(adj[i]) for i in range(n)]
    color, planned = [0] * n, Queue(n)
    bfs(s, adj, color, planned)


if __name__ == '__main__':
    main()
