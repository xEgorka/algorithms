def top_sort(s, adj, clr, ord):
    stack = [s]
    while len(stack):
        v = stack.pop()
        if clr[v - 1] == 'white':
            clr[v - 1] = 'gray'
            stack.append(v)
            [stack.append(w) for w in adj[v - 1] if clr[w - 1] == 'white']
        elif clr[v - 1] == 'gray':
            clr[v - 1] = 'black'
            ord.append(v)


def main():
    x = list(map(int, input().split()))
    n, m = x[0], x[1]
    adj = [None] * n
    for _ in range(m):
        x = list(map(int, input().split()))
        u, v = x[0], x[1]
        adj[u - 1] = [] if not adj[u - 1] else adj[u - 1]
        adj[u - 1].append(v)
        adj = [sorted(adj[i]) if adj[i] else [] for i in range(n)]
        clr, ord = ['white' for _ in range(len(adj))], []
        [top_sort(i + 1, adj, clr, ord) for i in range(n) if clr[i] == 'white']
        ord.reverse()
        print(*ord)


if __name__ == '__main__':
    main()
