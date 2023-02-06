def catalan(n: int) -> int:
    if n <= 1:
        return 1
    sum = 0
    for i in range(n):
        sum += catalan(i) * catalan(n - i - 1)
    return sum


# def binomial_coefficient(n: int, k: int) -> int:
#     if k > n - k:
#         k = n - k
#     res = 1
#     for i in range(k):
#         res = res * (n - i)
#         res = res / (i + 1)
#     return res


# def catalan(n: int) -> int:
#     c = binomial_coefficient(2 * n, n)
#     return int(c / (n + 1))


def main() -> int:
    print(catalan(int(input())))
    return 0


if __name__ == '__main__':
    main()
