# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

def rooms_required(arr):
    arrival = [arr[i][0] for i in range(len(arr))]
    departure = [arr[i][1] for i in range(len(arr))]
    arrival.sort()
    departure.sort()
    n = len(arrival)
    i = j = 0
    mxr = 0
    rooms = 0
    while i < n and j < n:
        if arrival[i] <= departure[j]:
            i+=1
            rooms += 1
            if mxr < rooms :
                mxr = rooms
        else:
            j+=1
            rooms -= 1
    print(mxr)

if __name__ == "__main__":
    arr = [(900, 910), (940, 1200), (950, 1120), (1100, 1130), (1500, 1900), (1800, 2000)]
    rooms_required(arr)
