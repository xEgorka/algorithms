def main() -> int:
    x = list(map(int, input().split()))
    n, k = x[0], x[1]
    if n == 0 or n == 1:
        print(1)
        return 0
    i = 2
    f1, f2 = 1, 1
    while i <= n:
        fi = f1 + f2
        f2 = f1
        f1 = fi % 10**k
        i += 1
    print(f1)
    return 0


if __name__ == '__main__':
    main()
