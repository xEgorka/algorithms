import re


def is_palindrome(s: str) -> bool:
    s = re.sub('[^a-z0-9]', '', s.lower())
    print(s == s[::-1])


def main() -> int:
    is_palindrome(input().strip())
    return 0


if __name__ == '__main__':
    main()
