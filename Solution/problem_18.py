# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.


from collections import deque

def max_values(arr, k):
    if k == len(arr):
        return list(max(arr))
    mxv = []
    dq = deque()
    for i in range(k):
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
    mxv.append(arr[dq[0]])

    for i in range(k, len(arr)):
        while dq and dq[0] <= i-k:
            dq.popleft()
        
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)

        mxv.append(arr[dq[0]])
    
    return mxv

if __name__ == "__main__":
    arr = [10, 5, 2, 7, 8, 7]
    print(max_values(arr, 4))