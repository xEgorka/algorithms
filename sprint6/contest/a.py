def main():
    x = list(map(int, input().split()))
    n, m = x[0], x[1]
    adj = [[] for _ in range(n)]
    for _ in range(m):
        x = list(map(int, input().split()))
        u, v = x[0], x[1]
        adj[u - 1].append(v)
    [print(*[len(x), *sorted(x)]) if x else print(0) for x in adj]


if __name__ == '__main__':
    main()
