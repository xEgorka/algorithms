def main() -> int:
    s, t, hs, ht = str(input()), str(input()), {}, {}
    for letter in s:
        if letter not in hs:
            hs[letter] = 0
        hs[letter] += 1
    for letter in t:
        if letter not in ht:
            ht[letter] = 0
        ht[letter] += 1
    print('YES') if list(hs.values()) == list(ht.values()) else print('NO')
    return 0


if __name__ == '__main__':
    main()
