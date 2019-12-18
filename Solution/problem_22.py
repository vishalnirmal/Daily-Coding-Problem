# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

def getOrignalString(s, string):
    j = 0
    arr = []
    for i in range(len(string)):
        if string[j:i+1] in s:
            arr.append(string[j:i+1])
            s.remove(string[j:i+1])
            j = i+1
    return arr

if __name__ == "__main__":
    print(getOrignalString(['bed', 'bath', 'bedbath', 'and', 'beyond'], "bedbathandbeyond"))