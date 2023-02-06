def main() -> int:
    s, t = input(), input()
    n = min(len(s), len(t))
    j, err = 0, 0
    for i in range(n):
        if j == len(t):
            print('FAIL')
            return
        if s[i] != t[j]:
            err += 1
            if err > 1:
                print('FAIL')
                return
            if i < len(s) - 1 and s[i + 1] == t[j]:
                j -= 1
            if j < len(t) - 1 and s[i] == t[j + 1]:
                j += 1
        j += 1
    print('OK')
    return 0


if __name__ == '__main__':
    main()
