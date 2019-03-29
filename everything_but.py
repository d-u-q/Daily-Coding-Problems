def multExcept(ln):
    rn = []
    tot = 1
    for x in ln:
        tot = tot * x
    for i in enumerate(ln): rn.append(tot/ln[i[0]])
    return rn

def multExceptNoDiv(ln):
    rn = []    
    for i in enumerate(ln):
        tot = 1
        for j in enumerate(ln):
            if i[0] == j[0]: tot = tot*1
            else: tot = tot * j[1]
        rn.append(tot)
    return rn


if __name__ == "__main__":
    print(multExcept([1,2,3,4,5]))
    print(multExceptNoDiv([1,2,3,4,5]))
    print(multExcept([3,2,1]))
    print(multExceptNoDiv([3,2,1]))