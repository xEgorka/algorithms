# https://leetcode.com/problems/reverse-words-in-a-string-iii

# Split by space, iterate the list and reverse each of the words


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return ' '.join(words)


def main() -> int:
    s = "Let's take LeetCode contest"
    print(Solution().reverseWords(s))
    return 0


if __name__ == '__main__':
    main()
