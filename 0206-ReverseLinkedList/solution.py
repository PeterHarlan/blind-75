from typing import Optional, List


class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def list_to_linked_list(head: List[int]) -> Optional[ListNode]:
    if not head:
        return None

    # Create the head of the linked lista
    linked_list_head = ListNode(head[0])
    current_node = linked_list_head

    # Iterate through the rest of the list and create nodes
    for value in head[1:]:
        current_node.next = ListNode(value)
        current_node = current_node.next

    return linked_list_head


def print_linked_list(node: Optional[ListNode]):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


class Solution:

    def reverse_list(self, head: ListNode):
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            print_linked_list(curr)
        return prev


if __name__ == "__main__":
    s = Solution()
    head = [1, 2, 3, 4, 5]
    linked_list = list_to_linked_list(head)
    print_linked_list(linked_list)
    it = s.reverse_list(linked_list)
    print_linked_list(it)
