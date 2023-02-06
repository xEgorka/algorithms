def get_longest_uniq_substr(s: str) -> None:
    l, cur_max, hash = 0, 0, {}
    for r in range(len(s)):
        if s[r] in hash:
            l = max(l, hash[s[r]] + 1)
        hash[s[r]] = r
        cur_max = max(cur_max, r - l + 1)
    print(cur_max)


def main() -> int:
    get_longest_uniq_substr(str(input()))
    return 0


if __name__ == '__main__':
    main()
