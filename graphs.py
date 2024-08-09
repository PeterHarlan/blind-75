from typing import List, Dict
from collections import deque

# Graph Problems and Implementations


# 1. **Finding Connected Components (DFS)**
# **Context:** Social network analysis to find separate groups of friends.
# Lesson: Iterating through everything because the graphs can be disconnected.
# Also address the edge case of cycles. Make sure we are checking for diagonal
# connectivity. Tricky part is ensuring that we guard on bound checks before
# visiting the node. Optimize dfs only when the current cell is '1'.
# - Edge cases
#   - Check Diagonal neighbors
#   - Cycles
#   - Disconnected graphs
def test_finding_connected_components():
    matrix = [
        [0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0],
    ]
    count = finding_connected_components(matrix)
    print(count)
    if count != 2:
        raise "Error finding connected components"


def finding_connected_components(matrix: List[List[int]]):
    visited = set()
    count = 0
    rows = len(matrix)
    columns = len(matrix[0])
    queue = deque()

    neighbor_list = [
        [1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1],
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
    ]

    def dfs():
        # If already visited, exit and return
        while queue:
            # Note: Stack.pop() or Stack.leftpop()
            origin_r, origin_c = queue.pop()
            visited.add((origin_r, origin_c))

            for offset_r, offset_c in neighbor_list:
                row, column = origin_r + offset_r, origin_c + offset_c
                if (
                    0 <= row < rows
                    and 0 <= column < columns
                    and (row, column) not in visited
                    and matrix[row][column] == 1
                ):
                    visited.add((row, column))
                    queue.append((row, column))

    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == 1 and (row, column) not in visited:
                queue.append((row, column))
                dfs()
                count += 1
    return count


matrix_path = [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]]


def path_exists_bfs(matrix, start, end):
    visited = [False] * len(matrix)
    queue = [start]
    visited[start] = True
    while queue:
        current = queue.pop(0)
        if current == end:
            return True
        for i in range(len(matrix)):
            if matrix[current][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)
    return False


# 2. **Finding All Paths Between Two Vertices (DFS)**
# **Context:** Transportation network to find all possible routes between cities.
# Lesson:
# - Edge Case
#   - Cycle
#   - Current/node does not exist in graph
def test_find_all_paths():
    graph_paths = {0: [1, 2], 1: [2], 2: [0, 3, 4], 3: []}
    out = find_all_paths(graph_paths, 0, 3)
    print(out)


def find_all_paths(
    graph: Dict[int, List[int]], start: int, end: int
) -> List[List[int]]:
    paths = []
    path = set()

    def all_paths_dfs(current: int):
        path.add(current)
        if current == end:
            paths.append(list(path))
        else:
            for neighbor in graph.get(current, []):  # Default that node does not exist
                if neighbor not in path:  # Avoid cycles
                    all_paths_dfs(neighbor)
        print(path, current)
        path.remove(current)

    all_paths_dfs(start)
    return paths


# 3. **Shortest Path in an Unweighted Graph (BFS)**
# **Context:** Finding the shortest route on a city map.
def test_bfs_shortest_path():
    graph_shortest = {0: [1, 2, 5, 0], 1: [2], 2: [0, 3], 3: []}
    out = bfs_shortest_path(graph_shortest, 0, 0)
    print(out)


def bfs_shortest_path(graph: Dict[int, List[int]], start: int, end: int):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        # Edge case of edge does not exist
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                print(neighbor)
                # Edge case that path may be None
                queue.append((neighbor, path + [neighbor]))
    return None


def main():
    # test_finding_connected_components()
    # test_find_all_paths()
    test_bfs_shortest_path()


if __name__ == "__main__":
    main()
