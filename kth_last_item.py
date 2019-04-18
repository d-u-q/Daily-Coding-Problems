def removeK(k, l):
    del l[-k]
    return l

if __name__ == "__main__":
    print removeK(2, [5,4,3,2,1])