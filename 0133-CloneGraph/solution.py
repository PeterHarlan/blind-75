from datastructures.Node import Node
from typing import Dict
from collections import deque


class Solution:

    # Deep copy of the graph, return the graph clone
    # We make a note that the graph is not directed
    # Can be solved with DFS or BFS
    # Need to make sure we are not recloning already clone nodes
    def cloneGraph(self, node: Node | None) -> Node:

        visited_nodes = {}

        def dfs_recursive(node: Node):
            if node in visited_nodes:
                return visited_nodes[node]
            copy = Node(node.val)
            visited_nodes[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs_recursive(nei))
            return copy

        return dfs_recursive(node) if node else None

    def bfs_recursive(node: Node | None):
        if not node:
            return None

        # Dictionary to map original nodes to their clones
        old_to_new_node_map = {}

        def bfs_recursion(node: Node) -> Node:
            if node in old_to_new_node_map:
                return old_to_new_node_map[node]

            # Clone the node
            copy = Node(node.val)
            old_to_new_node_map[node] = copy

            # Recursively clone all the neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(bfs_recursion(neighbor))

            return copy

        # Start the DFS cloning process
        return bfs_recursion(node)

    # Same structure as bfs
    # Uses staack instead of queue
    # Be sure to guard for None

    def iterative_dfs(node: Node | None):
        if not node:
            return None

        old_to_new_map: Dict[Node, Node] = {}

        stack = [node]
        old_to_new_map[node] = Node(node.val)

        while stack:
            current = stack.pop()

            for neighbor in current.neighbors:
                if neighbor not in old_to_new_map:
                    old_to_new_map[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                old_to_new_map[current].neighbors.append(old_to_new_map[neighbor])

        return old_to_new_map[node]

    def iterative_bfs(node: Node | None):
        if not node:
            return None

        old_to_new_map: Dict[Node, Node] = {}

        queue = deque([node])
        old_to_new_map[node] = Node(node.val)

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor not in old_to_new_map:
                    old_to_new_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                old_to_new_map[current].neighbors.append(old_to_new_map[neighbor])

        return old_to_new_map[node]


if __name__ == "__main__":
    s = Solution()
