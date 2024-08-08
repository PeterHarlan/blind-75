def length_of_longest_substring_solution(string: str) -> int:
    # Goal: Find the length of the longest substring without repeating charaters

    # Learning Outcome: Figure out how to use two pointers
    # Using right pointer as explortory
    # When char in hashset data structure already exists, increment left pointer
    # Basically, understand when to move the left and right pointers

    # We need to return the count of the longest substring
    # - when there is a repeated character, we need to rest max_char count
    # - therefore, we need to store max_continuous_length
    #
    # Walk through some examples
    # string = "abcabcbb" output is 3 ("abc")
    # string = "bbbbb" output is 1 ("b")
    # string = "pwwkew" output is 3 ("wke")

    # Potentially generate all permutations of the sub strings O(n^3)
    # Maybe there is a better way to do this...
    # Doing some brainstorming, I think we may be able to use sliding pointers
    # How about pointers? Perhaps we explore the soliding window technique?
    # start_pointer, end_pointer.
    # Maintain a window of characters that expand and contracts as we process the string
    # Need a way to track unique characters, we can use a set (ensures all chars in set is unique)
    # Move end_pointer to explore new characters
    # If duplicate character is found, reset duplicate and bump up start_pointer. Continue from left until duplicate is removed

    # Two loops for sliding pointer
    # 1. outer loop for the right pointer (exploritory)
    # 2. inner loop for the left pointer (e.g. while loop)
    # while there is a repeat char at left pointer
    #   remove char at left pointer when shifting left pointer
    #   increment left pointer
    # charset add right pointer
    # calculate and update max size.
    # note calculation of size with an array causes u to add +1 to len

    # Brainstorm
    # 1 2 3 4 5 6 7 8
    # a b c a b c b b
    # s
    # e
    # max 3
    # substring = cbb

    chart_set = set()
    left_pointer = 0
    max_length = 0

    for right_pointer in range(len(string)):
        while string[right_pointer] in chart_set:
            chart_set.remove(string[left_pointer])
            left_pointer += 1
        chart_set.add(string[right_pointer])
        max_length = max(max_length, right_pointer - left_pointer + 1)
    return max_length


def length_of_longest_substring(string: str) -> int:
    # Practice solution here
    pass


if __name__ == "__main__":
    # input_string = "bbbbb"
    input_string = "abcabcbb"  # abc, expected out is 3
    print(f"length of string {len(input_string)}")
    # count = length_of_longest_substring_solution(input_string)
    count = length_of_longest_substring(input_string)
    print(count)
