def counting_sort(arr, k):
    counted_values = [0] * k
    for value in arr:
        counted_values[value] += 1
    arr = []
    for i in range(k):
        arr += [i] * counted_values[i]
    return arr


def main() -> int:
    k = 3
    n = int(input())
    if n == 0:
        return 0
    arr = list(map(int, input().split()))
    arr = counting_sort(arr, k)
    print(*arr)
    return 0


if __name__ == '__main__':
    main()
