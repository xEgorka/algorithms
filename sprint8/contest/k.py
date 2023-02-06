def main() -> int:
    a, b = input(), input()
    hash = {'b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z'}
    s, t = '', ''
    for x in a:
        if x in hash:
            s += x
    for x in b:
        if x in hash:
            t += x
    if s < t:
        print(-1)
    elif s == t:
        print(0)
    else:
        print(1)
    return 0


if __name__ == '__main__':
    main()
