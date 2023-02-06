def fib(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def main() -> int:
    print(fib(int(input())))
    return 0


if __name__ == '__main__':
    main()
