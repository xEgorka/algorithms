def dsf(s, adj, color, traverse):
    stack = [s]
    while len(stack):
        v = stack.pop()
        if color[v - 1] == 'white':
            color[v - 1] = 'gray'
            stack.append(v)
            [stack.append(w) for w in adj[v - 1] if color[w - 1] == 'white']
            traverse.append(v)
        elif color[v - 1] == 'gray':
            color[v - 1] = 'black'


def main():
    x = list(map(int, input().split()))
    n, m = x[0], x[1]
    adj = [[] for _ in range(n)]
    for _ in range(m):
        x = list(map(int, input().split()))
        u, v = x[0], x[1]
        adj[u - 1].append(v)
        adj[v - 1].append(u)
    s, adj = int(input()), [sorted(adj[i], reverse=True) for i in range(n)]
    color, traverse = ['white' for _ in range(len(adj))], []
    dsf(s, adj, color, traverse)
    print(*traverse)


if __name__ == '__main__':
    main()
