def main() -> int:
    n = int(input())
    p = list(map(int, input().split()))

    s, profit = 0, 0
    for i in range(n):
        if s and i == n - 1:
            profit += p[i]
            break
        if not s and i == n - 1:
            break
        if not s and p[i + 1] > p[i]:
            s = 1
            profit -= p[i]
        if s and p[i + 1] < p[i]:
            s = 0
            profit += p[i]

    print(profit)
    return 0


if __name__ == '__main__':
    main()
