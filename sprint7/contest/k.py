def main() -> int:
    n = int(input())
    a = list(map(int, list(input().split())))
    m = int(input())
    b = list(map(int, list(input().split())))
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    if dp[n][m]:
        print(dp[n][m])
    else:
        print(0)
        return

    answer1, answer2 = [], []
    i, j = n, m
    while i and j:
        if a[i - 1] == b[j - 1]:
            answer1.append(i)
            answer2.append(j)
            i -= 1
            j -= 1
        elif dp[i - 1][j] == dp[i][j]:
            i -= 1
        else:
            j -= 1
    answer1.reverse()
    answer2.reverse()
    print(*answer1)
    print(*answer2)
    return 0


if __name__ == '__main__':
    main()
