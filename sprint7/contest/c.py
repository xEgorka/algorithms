def main() -> int:
    M, n = int(input()), int(input())
    pile, profit = [], 0
    [pile.append(list(map(int, input().split()))) for _ in range(n)]
    pile = sorted(pile, reverse=True)
    for i in range(n):
        if M - pile[i][1] > 0:
            M -= pile[i][1]
            profit += pile[i][0] * pile[i][1]
        else:
            profit += M * pile[i][0]
            break
    print(profit)
    return 0


if __name__ == '__main__':
    main()
