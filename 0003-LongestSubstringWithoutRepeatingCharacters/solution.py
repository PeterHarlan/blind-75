def length_of_longest_substring(string: str) -> int:
    # Find the length of the longest substring without repeating charaters
    # 

    # We need to return the count of the longest substring
    # - when there is a repeated character, we need to rest max_char count
    # - therefore, we need to store max_continuous_length
    # 
    # Walk through some examples
    # string = "abcabcbb" output is 3 ("abc")
    # string = "bbbbb" output is 1 ("b")
    # string = "pwwkew" output is 3 ("wke")

    # Potentially generate all permutations of the sub strings O(n^3)
    # Maybe there is a better way to do this
    # How about pointers? Perhaps we explore the soliding window technique?
    # start_pointer, end_pointer.
    # Maintain a window of characters that expand and contracts as we process the string
    # Need a way to track unique characters, we can use a set (ensures all chars in set is unique)
    # Move end_pointer to explore new characters
    # If duplicate character is found, reset duplicate and bump up start_pointer. Continue from left until duplicate is removed

    # Brainstorm
    # 1 2 3 4 5 6 7 8
    # a b c a b c b b
    # s
    # e
    # max 3
    # substring = cbb

    chart_set = set()
    start_pointer = 0
    max_length = 0

    for end_pointer in range(len(string)):
        while string[end_pointer] in chart_set:
            chart_set.remove(string[start_pointer])
            start_pointer += 1
        chart_set.add(string[end_pointer])
        max_length = max(max_length, end_pointer- start_pointer + 1)
    return max_length




if __name__ == "__main__":
    input_string = "bbbbb"
    print(f"length of string {len(input_string)}")
    count = length_of_longest_substring(input_string)
    print(count)

