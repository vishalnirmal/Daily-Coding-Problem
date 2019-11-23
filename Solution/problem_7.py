# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

def fibo(n):
    # 1 -> 2
    # 2 -> 3
    # 3 -> 5
    a = 1
    b = 2
    c = 1
    if n == 0:
        return 1
    if n == 1:
        return 2
    for i in range(n-1):
        c = a + b
        a = b
        b = c
    return c
def find_ways(string):
    length = 0
    prod = 1
    ts = ""
    for i in range(len(string)-1):
        if int(string[i]+string[i+1]) < 27 and int(string[i]+string[i+1]) > 10:
            length+=1
        else:
            prod *= fibo(length)
            length = 0
        if i == len(string)-2:
            prod *= fibo(length)
    print(prod)
if __name__ == "__main__":
    find_ways('10114111')