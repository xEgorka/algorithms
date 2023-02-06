def to_binary(number: int) -> str:
    if number == 0 or number == 1:
        return str(number)
    binary = ''
    while number > 0:
        binary = binary + str(number % 2)
        number = number // 2
    return binary[::-1]


def main() -> int:
    print(to_binary(int(input().strip())))
    return 0


if __name__ == '__main__':
    main()
