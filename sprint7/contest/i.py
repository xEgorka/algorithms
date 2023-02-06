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

    route = ''
    i, j = 0, m - 1
    while True:
        if i == n - 1 and not j:
            print(route[::-1])
            break
        elif i == n - 1:
            route += 'R'
            j -= 1
        elif not j:
            route += 'U'
            i += 1
        elif dp[i + 1][j] > dp[i][j - 1]:
            route += 'U'
            i += 1
        else:
            route += 'R'
            j -= 1
    return 0


if __name__ == '__main__':
    main()
