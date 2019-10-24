# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def checkSum(arr, k):
    temp = {}
    for i in arr:
        if temp.get(i):
            return True
        else:
            temp[k-i] = i
    return False

if __name__ == "__main__":
    import random
    arr = [10, 15, 3, 7]
    k = 17
    print(checkSum(arr, k))