from typing import List

# results
# Base case
# recurrance relation


def permutation(nums: List[int]):
    result = []
    if len(nums) == 1:
        return [nums[:]]

    for _ in range(len(nums)):
        n = nums.pop()
        perm_list = permutation(nums)
        for perm in perm_list:
            perm.append(n)

        # Add multiple values to an array
        result.extend(perm_list)
        nums.append(n)
    return result


num = [
    1,
    2,
    3,
]
out = permutation(num)
print(out)
print(len(out))
