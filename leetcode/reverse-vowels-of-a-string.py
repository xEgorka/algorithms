# https://leetcode.com/problems/reverse-vowels-of-a-string

# Simple two pointers. Filter vowels using hash


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        left, right = 0, len(s) - 1
        s = list(s)
        while left <= right:
            if not s[left].lower() in vowels:
                left += 1
                continue
            if not s[right].lower() in vowels:
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)


def main() -> int:
    s = "hello"
    print(Solution().reverseVowels(s))
    return 0


if __name__ == '__main__':
    main()
