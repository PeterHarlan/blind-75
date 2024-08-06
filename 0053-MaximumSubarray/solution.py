from typing import List


class Solution:
    # Max sub array, consider using prefix and postfix
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = prev = nums[0]
        for i in range(1, len(nums)):
            num = nums[i] or None
            curr = max(prev, 0) + num
            res = max(res, curr)
            prev = curr
        return res


if __name__ == "__main__":
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    res = s.maxSubArray(array)
    print("\n")
    print(res)
