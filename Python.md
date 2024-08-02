# Python Notes

## Sliding Pointers

The sliding pointer technique, also known as the sliding window technique, is a common method used in algorithm design to solve problems related to arrays, lists, or strings. It efficiently finds solutions by maintaining a subset of the data that "slides" through the dataset, adjusting its size and position as needed.

1. Initialize Pointers: Start with two pointers (start and end). These pointers represent the current window of data being considered.

1. Expand the Window: Move the end pointer to expand the window and include new elements from the dataset (exploratory pointer). This might involve performing operations or checks on the new element added to the window.

1. Shrink the Window: Once the window meets certain conditions or constraints (e.g. exceeding a size limit or finding a duplicate), increment the start pointer to shrink the window. Continue until entry condition is no longer met

1. Update Results: During the expansion and contraction of the window, update the results or evaluation metric based on the current state of the window. This could involve keeping track of maximum/minimum values, sums, or other relevant metrics.

```bash
# Calculating length usign pointers requres + 1 to account for offset
length = max(max_continuous_length, second_pointer - first_pointer + 1)

# Sliding window outline
# - two pointers (start_pointer, end_pointer)
# - loop of end_pointer from 0 to end, incrementing end_pointer
# - increment start_pointer as need when special condition is met
# - process calculation on elements in window
def length_of_longest_substring(string: str):
    chart_set = set()
    start_pointer = 0
    max_length = 0

    # Explore new chars using end_pointer
    for end_pointer in range(len(string)):
        # Update start pointer as needed
        while string[end_pointer] in chart_set:
            chart_set.remove(string[start_pointer])
            start_pointer += 1
        chart_set.add(string[end_pointer])
        # Evaluate the items in the window
        max_length = max(max_length, end_pointer- start_pointer + 1)
    return max_length
```

## Iterating through loops

```python
# for each element in list
for i in current_list:

# by index
for i in range(current_list):

# by offseet index
for i in range(offset, current_list):

# by index and element
for index, elenum in enumerate(current_list):
```

## Strings Slices

```python
string = "hello world"
start_pointer = 0
end_pointer = 1

# This will print only "h". Include everything up to the end_pointer
substring = string[start_pointer:end_pointer]
```

## String Iteration

```python
# Generate all permutation of a string O(n^3)
def generate_all_permutations(string: str)
    string_length = len(string)
    for i in range(string_length):
        for j in range (i+1, string_length+1):
            substring = ""
            for k in range(i, j):
                substring += string[k]
            print(substring)
```

## Set

```python
# Turn string into a set
string = "pwke"
print(set(look_up)) # Outputs {'p', 'w', 'k', 'e'}
```

## Map

```python
map_obj = {"hi": "bye"}
print(len(map_obj)) # Returns 1
print(map_obj.keys()) # Returns dict_keys["hi"]

# Convert Keys to list of keys
key_list = list(map_obj.keys()) # ["hi"]
```

## Common Troubleshoot
1. Check the scope of the return statement

### Array

```python
my_list = [0] * size

my_list = [i for i in range(10)]
```