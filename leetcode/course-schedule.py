# https://leetcode.com/problems/course-schedule

from typing import List, Optional


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        def dfs(i):
            if not graph[i]:
                return False
            if i in visited:
                return True
            visited.add(i)
            for j in graph[i]:
                if dfs(j):
                    return True

            visited.remove(i)
            return False

        for i in range(numCourses):
            visited = set()
            if dfs(i):
                return False
            graph[i] = []
        return True


def main() -> int:
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(Solution().canFinish(numCourses, prerequisites))
    return 0


if __name__ == '__main__':
    main()
