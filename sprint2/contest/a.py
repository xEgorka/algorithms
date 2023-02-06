def main() -> int:
    n, m, matrix = int(input()), int(input()), []
    [matrix.append(list(map(int, input().split()))) for i in range(n)]
    [print(*[matrix[i][j] for i in range(n)]) for j in range(m)]
    return 0


if __name__ == '__main__':
    main()
