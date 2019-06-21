# Problem 90
import random
def RandomExcept(n,l):
    r = random.randint(0,n-1)
    while r in l:
        r = random.randint(0,n-1)
    return r

if __name__ == "__main__":
    print RandomExcept(5,[0,3,4])