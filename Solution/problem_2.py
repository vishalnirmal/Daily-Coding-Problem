# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

def modify_array(arr):
    n = len(arr)
    left = list([1]*n)
    right = list([1]*n)
    lprod = 1
    rprod = 1
    for i in range(len(arr)):
        left[i] = lprod
        right[n-i-1] = rprod
        rprod *= arr[n-i-1]
        lprod *= arr[i]
    for i in range(len(arr)):
        arr[i] = left[i]*right[i]
    return arr
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(modify_array(arr))