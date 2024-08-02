from typing import List


class Solution:

    # [2, 4, 4] # Case 1: If the nums[mid] <= nums[right]
    #  l  m  r
    # We know that the smallest number will be on the left portion
    # this means we need to adjust right pointer to be at mid
    # [2, 4, 4]
    #  l  r
    # return array[left]

    # [2, 4, 6, 1, 2] Case 2: If nums [mid] > nums[right]
    #  l     m     r
    # We know that smallest number will be on the right side
    # of the array since the mid is bigger than the right.
    # Therefore, we need to adjust the left pointer to be next
    # to the mid pointer.

    # [2, 4, 6, 1, 2]
    #           l  r
    # return array[left]
    def findMin2(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]


if __name__ == "__main__":
    s = Solution()
    nums = [6, 8, 10, 12, 32]
    # nums = [3, 4, 5, 1, 2]
    out = s.findMin(nums)
    print(out)
