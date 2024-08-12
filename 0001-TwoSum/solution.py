from typing import List

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


class Solution:

    def two_sum_map(self, nums: List[int], target: int) -> List[int]:
        # Key is the complement value and the value is the index
        comp_to_index_map = {}
        for index, number in enumerate(nums):
            # Calculate complement value
            complement = target - number
            if complement in comp_to_index_map:
                stored_index = comp_to_index_map[complement]
                return [index, stored_index]
            else:
                comp_to_index_map[number] = index

    def two_sums_pointers(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [left, right]
            elif sum < target:
                left += 1
            else:
                right -= 1


if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    # out = s.two_sum_map(nums, target)
    out = s.two_sums_pointers(nums, target)
    print(out)
