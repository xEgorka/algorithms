def get_longest_word(s):
    word, longest_word = '', ''
    s.strip()
    for i in range(len(s)):
        if s[i] == ' ':
            word = ''
        else:
            word = word + s[i]
            if len(word) > len(longest_word):
                longest_word = word
    print(longest_word)
    print(len(longest_word))


def main():
    _ = input()
    get_longest_word(input().strip())


if __name__ == '__main__':
    main()
