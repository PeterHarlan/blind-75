from typing import List


def binary_search2(array: List[int], target: int):
    left_pointer, right_pointer = 0, len(array) - 1

    while left_pointer <= right_pointer:
        # // floor division
        mid_pointer = (left_pointer + right_pointer) // 2
        if array[mid_pointer] == target:
            return mid_pointer
        elif array[mid_pointer] < target:
            left_pointer = mid_pointer + 1
        else:
            right_pointer = mid_pointer - 1

    return -1  # Target not found


def binary_search(array: List[int], target: int):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (right + left) // 2
        if array[mid] == target:
            return mid
        elif array[left] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Example usage:
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
target = 15

index = binary_search(sorted_array, target)
if index != -1:
    print(f"Element found at index {index}.")
else:
    print("Element not found in the array.")
