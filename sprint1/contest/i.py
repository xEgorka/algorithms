def is_power_of_four(number: int) -> bool:
    n, x, power_of_four = 0, 1, []
    while x <= 10000:
        x = 4 ** n
        power_of_four.append(x)
        n += 1
    return True if number in power_of_four else False


def main() -> int:
    print(is_power_of_four(int(input())))
    return 0


if __name__ == '__main__':
    main()
