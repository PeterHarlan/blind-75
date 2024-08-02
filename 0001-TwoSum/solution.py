from typing import List


class Solution:

    def two_sum(self, nums: List[int], target: int) -> List[int]:
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


if __name__ == "__main__":
    s = Solution()
