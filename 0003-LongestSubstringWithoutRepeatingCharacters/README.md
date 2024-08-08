# Longest Substring Without Repeating Characters
[Problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Useful info
- `s` consists of English letters, digits, symbols, and spaces
- there can be multiple substrings of the same maximum length

## Thought process
### Brute Force
- Start with each character and expand the substring until a repeat character is found. For example, for "abcabcbb":
    - "a" (length 1)
    - "ab" (length 2)
    - "abc" (length 3) 
    - "abca" → repetition found, Remember max length of 3.
- Move to the next starting character and repeat.
    - "b", "bc", "bca", "bcab", max is 3...
- Complexity: This approach is O(n²) because it requires multiple checks for each substring.

### Edge Cases
- Empty string (i.e. ""), return 0
- For single char, return 1
- Str of same repeated char (e.g. "bbbbb"), return 1
- Multiple sub strings with same length (i.e. "bacab" should return 3 -> "bac" and "cab")