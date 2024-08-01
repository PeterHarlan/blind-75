from typing import List


class Solution:

    # Find
    # Union j
    def countComponents(self, node_count: int, edges: List[List[int]]) -> int:

        # Node id is array index and value at index is node_parent
        root_node_list = [i for i in range(node_count)]

        def merge_node_sets(first_node: int, second_node: int) -> None:
            first_node = find_root_node(first_node)
            second_node = find_root_node(second_node)
            if first_node != second_node:
                root_node_list[first_node] = second_node

        def find_root_node(node: int) -> int:
            while node != root_node_list[node]:
                root_node_list[node] = root_node_list[
                    root_node_list[node]
                ]  # path compression
                node = root_node_list[node]
            return node

        for edge in edges:
            node_1, node_2 = edge
            merge_node_sets(node_1, node_2)
        print(root_node_list)
        return len({find_root_node(nodes) for nodes in root_node_list})


if __name__ == "__main__":
    s = Solution()
    number_nodes = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    count = s.countComponents(number_nodes, edges)
    print(count)
