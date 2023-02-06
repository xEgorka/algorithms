def is_subseq(s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
            continue
        j += 1
    return True if i == len(s) else False


def main() -> int:
    s, t = input(), input()
    print(is_subseq(s, t))
    return 0


if __name__ == '__main__':
    main()
