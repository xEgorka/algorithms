# https://leetcode.com/problems/merge-intervals

from typing import List, Optional


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        ans.append(intervals[0])
        for i in range(1, len(intervals)):
            prev_start, prev_end = ans[-1][0], ans[-1][1]
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            if prev_end < curr_start:
                ans.append([curr_start, curr_end])
            elif prev_end == curr_start or prev_end < curr_end:
                ans[-1] = [prev_start, curr_end]
        return ans


def main() -> int:
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(Solution().merge(intervals))
    return 0


if __name__ == '__main__':
    main()
