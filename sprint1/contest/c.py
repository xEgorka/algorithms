def get_neighbours(A, row, col):
    neigh = []
    if row - 1 >= 0:
        neigh.append(A[row - 1][col])
    if row + 1 <= len(A) - 1:
        neigh.append(A[row + 1][col])
    if col - 1 >= 0:
        neigh.append(A[row][col - 1])
    if col + 1 <= len(A[0]) - 1:
        neigh.append(A[row][col + 1])
    neigh.sort()
    print(*neigh)


def main():
    n, _, A = int(input()), int(input()), []
    [A.append(list(map(int, input().strip().split()))) for _ in range(n)]
    get_neighbours(A, int(input()), int(input()))


if __name__ == '__main__':
    main()
