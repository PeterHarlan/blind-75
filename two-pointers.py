# 1. Two-Pointer Technique: Finding a Pair with a Sum in a Sorted Array
# **Problem**: Given a sorted array, find if there exist two numbers that sum up to a target value.
# Lesson: Cheking for an exit condition based on the examing the numbers at the pair of index
def test_pair_with_sum():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 10
    out = find_pair_with_sum(arr, target)
    print(out)
    if out != (1, 9):
        raise "Error with find_par_with_sum()"


def find_pair_with_sum(arr, target):
    # Pointers start at the left and the right
    # Does not use set data structure
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None


# 2. Binary Search
# **Problem**: Implement binary search on a sorted array.
# Lesson: Searching through an array


def test_binary_search():
    arr = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    out = binary_search(arr, target)
    if out != 3:
        raise "Error finding binary index"


def binary_search(arr, target):
    # Learn to use left and right pointers
    # left start at 0 and right is len()-1
    # Also use the mid pointer
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# 3. Palindrome Checking
# **Problem**: Check if a string is a palindrome.
# Lesson: String manipulation based on pointers


def test_is_palindrome():
    s = "racecar"
    s = "ww"
    out = is_palindrome(s)
    print(out)
    if not out:
        raise "Error checking palindrome"


def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# 4. Dutch National Flag Problem: 3-Way Partitioning
# **Problem**: Given an array of 0s, 1s, and 2s, sort the array.
# Lesson: Using pointers as partitioning. Note the while loop use of mid pointer.
# Walking three pointers, low and mid in a positive direction and high in a
# negative direction.


def test_sort_colors():
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    print(nums)
    answer_list = [0, 0, 1, 1, 2, 2]
    for i in range(len(nums)):
        if nums[i] != answer_list[i]:
            raise f"test_sort_colors error: {nums[i]} does not equal {answer_list[i]}"


def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# 5. Sliding Window: Maximum Sum of a Subarray of Length K
# **Problem**: Find the maximum sum of a subarray of length `k`.
# Lesson: A sliding window algorithm with the use of index and offset.


def test_max_sum_subarray():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 3
    out = max_sum_subarray(arr, k)
    print(out)
    if out != 24:
        raise "Error max sum subarray"


def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum


# 6. Interval Merging
# **Problem**: Merge overlapping intervals
# Lesson: Use one pointer for end of the previous interval and another for the start of the next
# for each interval and adjust them to check if they overlap or to merge them.


def test_merge_intervals():
    intervals = [[1, 3], [8, 10], [2, 6], [15, 18]]
    out = merge_intervals(intervals)
    expected_list = [[1, 6], [8, 10], [15, 18]]
    print(out)
    for i in range(len(out)):
        for j in range(len(out[i])):
            if expected_list[i][j] != out[i][j]:
                raise "Merge intervals errors"


def merge_intervals(intervals):
    if not intervals:
        return []
    print(intervals)
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    print(intervals)

    for current in intervals[1:]:
        last_merged = merged[-1]
        print(current, last_merged)
        if current[0] <= last_merged[1]:
            # Overlapping intervals, merge them
            last_merged[1] = max(last_merged[1], current[1])
            print(last_merged)
        else:
            # No overlap, add current interval
            merged.append(current)

    return merged


# These examples cover various common uses of the left and right pointer technique. Each example demonstrates how to efficiently solve different types of problems using this approach.


def main():
    # test_pair_with_sum()
    # test_binary_search()
    test_is_palindrome()
    # test_sort_colors()
    # test_max_sum_subarray()
    # test_merge_intervals()


if __name__ == "__main__":
    main()
