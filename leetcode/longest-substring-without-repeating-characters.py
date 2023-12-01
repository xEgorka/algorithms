# https://leetcode.com/problems/longest-substring-without-repeating-characters

# Use two pointers and hash. If right in hash, move left and take
# repeats into account. Update max each step


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, cur_max, hash = 0, 0, {}

        for right in range(len(s)):

            if s[right] in hash:
                left = max(left, hash[s[right]] + 1)

            hash[s[right]] = right
            cur_max = max(cur_max, right - left + 1)

        return cur_max


def main() -> int:
    print(Solution().lengthOfLongestSubstring('abacaba'))
    return 0


if __name__ == '__main__':
    main()
