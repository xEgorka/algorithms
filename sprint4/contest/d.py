# https://contest.yandex.ru/contest/23991/problems/D/


def main() -> int:
    n, h = int(input()), set()
    for _ in range(n):
        s = input()
        if s not in h:
            h.add(s)
            print(s)
    return 0


if __name__ == '__main__':
    main()
