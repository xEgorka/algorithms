def dsf(s, adj, visited, time, entry, leave):
    stack = [s]
    while len(stack):
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            entry[v - 1] = time
            time += 1
            stack.append(v)
            [stack.append(w) for w in adj[v - 1] if w not in visited]
        elif not leave[v - 1]:
            visited.add(v)
            leave[v - 1] = time
            time += 1


def main():
    x = list(map(int, input().split()))
    n, m = x[0], x[1]
    adj = [[] for _ in range(n)]
    for _ in range(m):
        x = list(map(int, input().split()))
        u, v = x[0], x[1]
        adj[u - 1].append(v)
    s, adj = 1, [sorted(adj[i], reverse=True) for i in range(n)]
    visited, time, entry, leave = set(), 0, [None] * n, [None] * n
    dsf(s, adj, visited, time, entry, leave)
    [print(entry[i], leave[i]) for i in range(n)]


if __name__ == '__main__':
    main()
