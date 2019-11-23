# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

def find_sum(arr):
    prev = 0
    largest = 0
    for i in arr:
        prev, largest = largest, max(prev+i, largest)
    return largest

if __name__ == "__main__":
    arr = [5, 1, 1, 5]
    find_sum(arr)