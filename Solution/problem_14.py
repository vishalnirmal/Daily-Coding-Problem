# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
import random
def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
def estimate_pi():
    center = (0.5, 0.5)
    count = 0
    n = 100000000
    for i in range(n):
        x, y = random.random(), random.random()
        
        if dist(center, (x, y)) <= 0.5:
            count+=1
    
    print(4*count/n)

if __name__ == "__main__":
    estimate_pi()

