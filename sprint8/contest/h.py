from typing import List


def search(p: str, text: str) -> List[int]:
    result = []
    s = p + '#' + text
    π = [0] * len(p)
    π_prev = 0
    for i in range(1, len(s)):
        k = π_prev
        while k and s[k] != s[i]:
            k = π[k - 1]
        if s[k] == s[i]:
            k += 1
        if i < len(p):
            π[i] = k
        π_prev = k
        if k == len(p):
            result.append(i - 2 * len(p))
    return result


def replace(s: str, t: str, text: str, position: List[int]) -> None:
    if not len(position):
        print(text)
        return
    i, j = 0, 0
    text_new = ''
    while i < len(text):
        if i == position[j]:
            text_new += t
            if j + 1 < len(position):
                j += 1
            i += len(s)
        else:
            text_new += text[i]
            i += 1
    print(text_new)


def main() -> int:
    text, s, t = input(), input(), input()
    replace(s, t, text, search(s, text))
    return 0


if __name__ == '__main__':
    main()
