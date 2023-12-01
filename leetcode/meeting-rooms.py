# https://leetcode.com/problems/meeting-rooms

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals)):
            if i > 0 and intervals[i][0] < intervals[i-1][1]:
                return False
        return True


def main() -> int:
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(Solution().canAttendMeetings(intervals))
    return 0


if __name__ == '__main__':
    main()
