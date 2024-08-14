from typing import List

# Prefix and Suffix Products:
# The concept of prefix and suffix products allows you to calculate
# the product of elements in an array efficiently. By separately
# calculating products of elements before and after the current index,
# you can avoid direct multiplication for each element.

# Avoiding Division:
# The problem can typically be solved using division, but this solution
# showcases how to achieve the same result without it, which can be
# important in scenarios where division by zero might occur or when you
# want to avoid floating-point inaccuracies.

# In-Place Modification:
# Modifying an existing list (res) instead of creating new lists for
# intermediate calculations helps to reduce space complexity,
# making the solution more efficient.

# Single Pass Technique:
# Using two passes through the list (one for prefix products and one
# for suffix products) is a powerful technique that allows you to
# build up results in a structured way, reducing the need for nested
# loops and achieving linear time complexity.

# Iterating Backwards:
# Understanding how to iterate backwards through a list can be beneficial,
# especially when you need to process elements relative to their positions
# in the original order. This is often useful for tasks involving cumulative
# calculations.

# Complexity Analysis:
# Analyzing time and space complexity is crucial for evaluating the
# efficiency of an algorithm. This solution operates in O(n) time
# complexity and O(1) additional space complexity (excluding the output),
# which is optimal for this problem.

# Code Readability and Structure:
# Breaking down the solution into clear steps (initialization, prefix
# calculation, suffix calculation, and return) enhances code readability
# and maintainability. Clear structure is important for understanding
# and debugging complex algorithms.


class Solution:

    # This is designed to compute all the products of the elements in the numput of nums
    # except for the element at each index. The return result list should be returned

    def productExceptSelfSolution(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # Does not matter what we default this array to, we are grabbing from nums
        res = [1 for _ in nums]

        # Building prefix product
        # Store the previously calculated prefix product
        # Update the prefix for the next loop
        pre = 1
        for i in range(length):
            res[i] = pre
            pre *= nums[i]

        # Build the suffix product
        # Update the result with the previously calculated suffix product
        # Update the suffix for the next loop
        suffix = 1
        for i in range(length - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_list = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            num_list[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            num_list[i] *= post
            post *= nums[i]
        return num_list


if __name__ == "__main__":
    input = [1, 2, 3, 4]
    output = [24, 12, 8, 6]
    s = Solution()
    out = s.productExceptSelf(input)
    print(out)
    print(output == out)
