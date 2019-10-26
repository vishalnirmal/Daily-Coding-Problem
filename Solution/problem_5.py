# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
def car(pair):
    def temp(a, b):
        return a
    return pair(temp)
def cdr(pair):
    def temp(a, b):
        return b
    return pair(temp)
if __name__ == "__main__":
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))