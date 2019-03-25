def addToK(ln,k):   # find if any 2 numbers in ln sum to k
    ld = [0]        # list of differences
    found = False
    for x in ln:
        if x in ld:
            found = True
        ld.append(k-x)
    return found

if __name__ == '__main__':
    print(addToK([10,15,3,7], 17))