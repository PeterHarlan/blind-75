from typing import List


class Solution:

    # Goal: find the largest area of water
    # return the max area size.
    # We know that the max height will have to be either left or right
    # min_height = min(height[left], height[right])
    # area = width * min_height
    #
    # We can do a brute forced approach see brute_force()
    # We know the run time of this is O(n^2)

    def brute_force(self, height: List[int]) -> int:
        max_area = 0
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                print(l, r)
                area = (r - l) * min(height[l], height[r])
                max_area = max(max_area, area)
        return max_area

    # Lets try the sliding window strategy
    # We need two pointers, left and right pointer
    # We know we need to store the max_area
    # Lets initialize two pointers, one at the left side and one at the right side
    # left_pointer will be 0 and right_pointer will be at the end len(height) - 1
    # Increment left_pointer and decrement right_pointer
    # exit condition, when left_pointer => right_pointer
    # How do we know when to increment left_pointer or decrement right_pointer?
    # Basically, decrement or increment the smaller value at pointer
    #   - When the value at left_pointer < value at right_pointer, increment left_pointer
    #   - else, decrement right_pointer

    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        left_pointer, right_pointer = 0, len(height) - 1

        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            min_height = min(height[left_pointer], height[right_pointer])
            area = width * min_height
            max_area = max(max_area, area)
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return max_area


if __name__ == "__main__":
    s = Solution()
    height_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    max_area = s.maxArea(height_list)
    # max_area = s.brute_force(height_list)
    print(max_area)
