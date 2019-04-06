import random

def mcPi(n):
    i = 0

    for p in range (n):
        x = random.random() 
        y = random.random()

        if (x**2 + y**2 <= 1.0): i+=1
    return (4.0*float(i)/n)

if __name__ == "__main__":
    print '%.3f'%mcPi(100)