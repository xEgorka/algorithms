# https://leetcode.com/problems/student-attendance-record-i

class Solution:
    def checkRecord(self, s: str) -> bool:
        L, A = 0, 0
        for i in range(len(s)):
            if s[i : i + 3] == 'LLL':
                return False
            if s[i] == 'A':
                A += 1
                if A > 1:
                    return False
        return True


def main() -> int:
    # s = 'PPALLP'
    s = 'PPALLL'
    print(Solution().checkRecord(s))
    return 0


if __name__ == '__main__':
    main()
