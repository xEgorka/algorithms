def get_hash(a: int, m: int, s: str) -> None:
    if len(s) == 0:
        print(0)
        return

    h = ord(s[0]) % m
    if len(s) == 1:
        print(h)
        return

    for n in range(len(s) - 1):
        h = (h * a + ord(s[n + 1])) % m
    print(h)
    return


def main() -> int:
    get_hash(int(input()), int(input()), str(input()))
    return 0


if __name__ == '__main__':
    main()
