def multExcept(ln):
    rn = []
    tot = 1
    for x in ln:
        tot = tot * x
    for i, y in enumerate(ln):
        rn.append(tot/ln[i])
    return rn

def multExceptNoDiv(ln):
    rn = []    
    for i,x in enumerate(ln):
        tot = 1
        for j,y in enumerate(ln):
            if i == j: tot = tot*1
            else: tot = tot * ln[j]
        rn.append(tot)
    return rn


if __name__ == "__main__":
    print(multExcept([1,2,3,4,5]))
    print(multExceptNoDiv([1,2,3,4,5]))
    print(multExcept([3,2,1]))
    print(multExceptNoDiv([3,2,1]))