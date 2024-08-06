def SubArraySum(arr):
    length = len(arr)
    temp, result = 0, 0
    # Pick starting point
    for i in range(0, length):
        # Pick ending point
        temp = 0
        for j in range(i, length):
            temp += arr[j]
            print(temp)
            result += temp
        print("\n")
    return result


def subArraySum(arr):
    n = len(arr)
    result = 0
    for i in range(0, n):
        result += arr[i] * (i + 1) * (n - i)

    # return all subarray sum
    return result


# Driver code
arr = [1, 2, 3]
print("Sum of SubArray :", SubArraySum(arr))
print("Sum of SubArray :", subArraySum(arr))
