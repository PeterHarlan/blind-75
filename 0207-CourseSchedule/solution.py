from typing import List


class Solution:
    # Goal of this problem is to understand
    # dfs(), cycles, disconnected graphs, and adjacency.

    # [[1,0]]
    # course 1 -> 0 == true
    # [[1,0],[0,1]]
    # course 1 -> 0 and 0 -> 1 == false

    # Clearifying questions
    # Does num course increment with course ids, starting with 0? --> yes

    # From the example, we see a cycle, that reminds me of two edge cases with graphs
    # 1. cycles => need hashset to check if current is visited => return False
    # 2. disconnected graphs => do it for each node, perhaps dfs()???, lets brainstorm some more

    # What if we created an adjacency map such that course id is mapped to an array of preqs?
    # Such that a map of course numbers to array of preq {0: [1, 2], 1:[2]}

    # Outline of the algorithm
    # create adjacency map
    # key = course id and value is array of preq

    # dfs
    #   base case
    #       if already in cycle, return False
    #       if no dependencies, return True
    #
    #   cycle_set.add(node)
    #   check neighbors
    #   for preq in map[course]:
    #       if(not dfs(preq)):
    #           return False
    #   cycle_set.remove(node)
    #   map[course] = []
    #   return True
    #
    # disconnected graph
    # for course in range(numCourses):
    #   if(not dfs(course)):
    #       return False
    # return True

    # Run sanity check
    # cycles - yes
    # disconnected - yes
    # Runtime O(e+v)

    def solution(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Init adjacency list
        # 1). Key[course_id] = []
        coursePreMap = {i: [] for i in range(numCourses)}
        # 2). Fill list with preq through appending
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
