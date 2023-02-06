def dsf(s, adj, visited, comp_cnt, comp):
    stack = [s]
    comp.append(set())
    while len(stack):
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            stack.append(v)
            [stack.append(w) for w in adj[v - 1] if w not in visited]
        else:
            comp[comp_cnt - 1].add(v)


def main():
    x = list(map(int, input().split()))
    n, m = x[0], x[1]
    if not m:
        print(n)
        [print(i + 1) for i in range(n)]
        return
    adj = [[] for i in range(n)]
    for _ in range(m):
        x = list(map(int, input().split()))
        u, v = x[0], x[1]
        adj[u - 1].append(v)
        adj[v - 1].append(u)
    visited, comp_cnt, comp = set(), 0, []
    for s in range(1, n + 1):
        if s not in visited:
            comp_cnt += 1
            dsf(s, adj, visited, comp_cnt, comp)
    print(comp_cnt)
    [print(*sorted(c)) for c in comp]


if __name__ == '__main__':
    main()
