# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def seperate_negative(arr):
    np = 0
    for i in range(len(arr)):
        if arr[i] <= 0:
            arr.insert(np, arr.pop(i))
            np+=1
    return arr[np:]
def find_min(arr):
    arr = seperate_negative(arr)
    n = len(arr)
    for i in range(n):
        index = abs(arr[i])-1
        if index < n and arr[index] > 0:
            arr[index] *= -1
    print(arr)
    for i in range(n):
        if arr[i] > 0:
            return i+1
    return n+1
if __name__ == "__main__":
    arr = [3, 4, -1, 1]
    print(find_min(arr))