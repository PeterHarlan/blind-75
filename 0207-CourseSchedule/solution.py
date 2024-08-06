from typing import List, Set


class Solution:

    # Generate a map of course numbers to array of preq {0: [1, 2], 1:[2]}
    # DFS, if preq, return true, else, explore neighbors
    # 1. cycles
    # 2. disconnected

    # Exploring neighbors
    # if cycle, return false
    # else, dfs
    # O(e+v)
    def solution(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursePreMap = {i: [] for i in range(numCourses)}
        for course, preq in prerequisites:
            coursePreMap[course].append(preq)

        # Edge Cases (cycles and disconnected)
        # 1. Cycles = Set
        # add to set
        # remove from set
        visited_set = set()

        # 2. Disconnected Graph. Use DFs to iterate through all the course
        # If the pre list is empty, return True,
        # otherwise, return False.
        def dfs(course):
            # 1. base case
            # 2. for all neighbors

            # Base case, return when there is a cycle
            if course in visited_set:
                return False

            # Optimize: There are no more courese left - base case
            if coursePreMap[course] == []:
                return True

            # Cycles
            visited_set.add(course)
            # For all the neighbors
            for pre in coursePreMap[course]:
                if not dfs(pre):
                    return False
            visited_set.remove(course)
            # Remove all elements rather than pop them 1-by-1
            coursePreMap[course] = []
            return True

        # Disconnected = iterate through all course
        for course in range(numCourse):
            if not dfs(course):
                return False
        return True


if __name__ == "__main__":
    prerequisites = [[1, 0], [0, 1]]
    numCourse = 2
    s = Solution()
    solution = s.solution(numCourse, prerequisites)
    print(solution)
