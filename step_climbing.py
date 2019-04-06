def fibCounter(s):
    if s <= 1:
        return 1
    return fibCounter(s-2) + fibCounter(s-1)

def multiFib(s, wtc):
    if s<=1: return 1
    elif s==2: return 2
    else:
        r = 0
        for i in wtc:
            r += multiFib(s-i,wtc)
        return r

def climbCounter(s, wtc):
    return fibCounter(s), multiFib(s, wtc)    

if __name__ == "__main__":
    print climbCounter(4,[1,2,3])