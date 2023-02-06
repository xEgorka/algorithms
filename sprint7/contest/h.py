def main() -> int:
    n, m = list(map(int, input().split()))
    A = []
    [A.append(list(map(int, list(input())))) for _ in range(n)]
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not i and not j:
                dp[(n - 1) - i][j] = A[(n - 1) - i][j]
            elif not i:
                dp[(n - 1) - i][j] = A[(n - 1) - i][j] + dp[(n - 1) - i][j - 1]
            elif not j:
                dp[(n - 1) - i][j] = A[(n - 1) - i][j] + dp[(n - 1) - (i - 1)][j]
            else:
                dp[(n - 1) - i][j] = A[(n - 1) - i][j] + max(
                    dp[(n - 1) - i][j - 1], dp[(n - 1) - (i - 1)][j]
                )
    print(dp[0][m - 1])
    return 0


if __name__ == '__main__':
    main()
