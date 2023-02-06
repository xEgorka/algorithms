def get_hash(a: int, m: int, s: str) -> None:
    if len(s) == 0:
        print(0)
        return

    h = ord(s[0]) % m
    if len(s) == 1:
        print(h)
        return

    h_s = {}
    h_a = {}
    for n in range(len(s) - 1):
        h_a[n] = a ** n
        h_s[n] = h
        h = (h * a + ord(s[n + 1])) % m
    # print(h)
    print(h_s)
    # print(h_a)
    return


def main() -> int:
    a, m, s, t = int(input()), int(input()), str(input()), int(input())
    subs = []
    for _ in range(t):
        subs.append(tuple(map(int, input().split())))
    # get_hash(a, m, s[subs[0][0]-1:subs[0][1]])
    # get_hash(a, m, s[subs[1][0]-1:subs[1][1]]) # 1 5
    # get_hash(a, m, s[subs[2][0]-1:subs[2][1]]) # 2 3
    # get_hash(a, m, 'bc')
    get_hash(a, m, s)
    # print(subs)
    return 0


if __name__ == '__main__':
    main()
