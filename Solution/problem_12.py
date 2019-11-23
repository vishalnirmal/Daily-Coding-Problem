# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

def unique_ways(n, X):
    temp = [0 for i in range(n+1)]
    temp[0] = 1
    for i in range(1, n+1):
        for j in X:
            if i-j >= 0:
                temp[i] += temp[i-j]
    return temp[-1]
if __name__ == "__main__":
     n = 6
     X = [1, 3, 5]
     print(unique_ways(n, X))