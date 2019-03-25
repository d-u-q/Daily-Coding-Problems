times = 0

def add_pers(n):
    global times
    total = 0    
    if (n % 10 == n):
        t = times
        times = 0
        return t
    while n:
        total += n%10
        n /= 10
    times+=1
    return(add_pers(total))


if __name__ == "__main__":
    for x in (10, 19, 9876, 199):
        print(x, add_pers(x))