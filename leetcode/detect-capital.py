# https://leetcode.com/problems/detect-capital

# Lower the string and compare to the string


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.lower() or word == word.upper() or word.istitle()


def main() -> int:
    word = 'FlaG'
    print(Solution().detectCapitalUse(word))
    return 0


if __name__ == '__main__':
    main()
