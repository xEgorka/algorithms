def main() -> int:
    s, words = input(), []
    while True:
        x = s.find(' ')
        if x == -1:
            words.append(s)
            break
        w = s[0:x]
        words.append(w)
        s = s[x + 1 :]
    while len(words):
        print(words.pop(), end=' ')
    return 0


if __name__ == '__main__':
    main()
