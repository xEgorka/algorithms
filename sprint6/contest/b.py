def main():
    x = list(map(int, input().split()))
    n, m = x[0], x[1]
    A = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        x = list(map(int, input().split()))
        u, v = x[0], x[1]
        A[u - 1][v - 1] = 1
    [print(*A[i]) for i in range(n)]


if __name__ == '__main__':
    main()
