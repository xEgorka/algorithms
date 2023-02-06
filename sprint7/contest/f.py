def main() -> int:
    n, k = list(map(int, input().split()))
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        cur_sum = 0
        for j in range(1, k + 1):
            if i < 3:
                cur_sum = 1
                break
            else:
                cur_sum += dp[i - j]
        dp[i] = cur_sum % 1000000007
    print(dp[n])
    return 0


if __name__ == '__main__':
    main()
